import os
import subprocess
import time
import threading
from PyQt5.QtCore import QObject, pyqtSignal

class Player(QObject):
    stopped = pyqtSignal()
    def __init__(self, directory):
        super().__init__()
        self.playing = False
        self.process = None
        self.directory = directory
        self.videos = self.get_videos()

    def get_videos(self):
        # List all files in the directory and filter out non-video files
        return [f for f in os.listdir(self.directory) if f.endswith(('.mp4', '.avi', '.mkv', '.VOB'))]
    
    def play_video(self, video_name):
        if video_name in self.videos:
            video_path = os.path.join(self.directory, video_name)
            try:
                wmplayer_path = r"C:\Program Files\Windows Media Player\wmplayer.exe"
                vlc_path = r"C:\Program Files\VideoLAN\VLC\vlc.exe"
                #self.process = subprocess.Popen(['start', video_path], shell=True)
                if video_path.endswith('.VOB'):
                    self.process = subprocess.Popen([vlc_path, video_path], shell=True)
                else:
                    self.process = subprocess.Popen([wmplayer_path, video_path], shell=True)
                self.playing = True
                threading.Thread(target=self.monitor_process).start()
            except subprocess.CalledProcessError as e:
                print(f"Error playing video: {e}")
        else:
            print(f"Video '{video_name}' not found in directory.")

    def monitor_process(self):
        while self.process.poll() is None:
            time.sleep(1)
        self.playing = False
        self.stopped.emit()

    def stop_video(self):
        if self.process and self.process.poll() is None:
            self.process.terminate()
            self.process.wait()
            self.playing = False

    def update_video(self, video_name):
        if self.playing:
            self.stop_video()
        self.play_video(video_name)


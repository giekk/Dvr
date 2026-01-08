import os
import csv
from file_video import AVI, MP4, MKV, VOB

class Database:
    def __init__(self, directory):
        self.directory = directory

    @property
    def get_directory(self):
        return self._directory

    def save_videos_to_csv(self, directory, csv_file):
        # List all files in the directory and filter out non-video files
        videos = [f for f in os.listdir(directory) if f.endswith(('.mp4', '.avi', '.mkv', '.VOB'))]
    
        # Write the list of videos to a CSV file
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Video Name"])  # Write the header
            for video in videos:
                writer.writerow([video])
    
    def load_videos_from_csv(self, csv_file):
        # Read the list of videos from a CSV file
        videos =[]
        with open(csv_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                video = row[0]
                if video.endswith(('.mp4')):
                    videos.append(MP4(video))
                elif video.endswith(('.avi')):
                    videos.append(AVI(video))
                elif video.endswith(('.mkv')):
                    videos.append(MKV(video))
                elif video.endswith(('.VOB')):
                    videos.append(VOB(video))
        return videos
    
    def load_libraries_from_csv(self, csv_file):
        # Read the list of libraries from a CSV file
        libraries = []
        with open(csv_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                libraries.append(row[0])
        return libraries
        
    def add_library_to_csv(self, library, csv_file):
        # Add a library to the CSV file
        with open(csv_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([library])
            
    
    


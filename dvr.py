from file_video import AVI, MP4, MKV
from database import Database

class DVR(Database):
    def __init__(self, directory):
        super().__init__(directory)
        self.videos = []
        self.libraries = []
        self.save_videos_to_csv(directory, "db/database.csv")
        self.videos = self.load_videos_from_csv("db/database.csv")
        self.libraries = self.load_libraries_from_csv("db/libraries.csv")

        if self.videos != []:
            print("Database successfully loaded.")
        else:
            print("No video found in the database.")

        if self.libraries != []:
            print("Libraries successfully loaded.")
        else:
            print("No library found in the database.")
import os
import subprocess

class MP4toMP3Converter:
    def __init__(self, target_directory):
        self.target_directory = target_directory

    def convert_mp4_to_mp3(self):
        # Iterate through all files in the target directory
        for file in os.listdir(self.target_directory):
            # Check if the file has a .mp4 extension
            if file.endswith('.mp4'):
                # Create the output file name by replacing the .mp4 extension with .mp3
                output_file = os.path.join(self.target_directory, file.replace('.mp4', '.mp3'))

                # Create the ffmpeg command
                cmd = f'ffmpeg -i "{os.path.join(self.target_directory, file)}" -vn -acodec libmp3lame -q:a 4 "{output_file}"'

                # Execute the ffmpeg command
                subprocess.run(cmd, shell=True, check=True)

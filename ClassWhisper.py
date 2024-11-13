import os
import subprocess
import whisper
from whisper.utils import get_writer

xosdirectory_name = "xos"
xossaved = "./txtalgo/"

class AudioTranscription:
    if os.path.exists(xosdirectory_name):
        print("exist")
    else:
        try:
            os.makedirs(xosdirectory_name)
            print("creating")
        except Exception as e:
            print("this failed")
            print("Error:", e)

    def __init__(self):
        self.dir_path = os.path.expanduser(xossaved)
        self.files = os.listdir(self.dir_path)
        self.num_files = len(self.files)
        self.new_dir_name = "xos_main"

        self.txt_dir = "txt"
        self.tsv_dir = "tsv"
        self.other_dir = "other"

        self.setup_directories()
        self.process_files()


    def setup_directories(self):
        if self.new_dir_name.endswith(".mp3"):
            self.new_dir_name = self.new_dir_name[:-4]

        if not os.path.exists(os.path.join(self.new_dir_name)):
            os.makedirs(os.path.join(self.new_dir_name))
            print("Main Directory created successfully!")
        else:
            print("Directory already exists.")

        for sub_dir in [self.txt_dir, self.tsv_dir, self.other_dir]:
            if not os.path.exists(os.path.join(self.new_dir_name, sub_dir)):
                os.makedirs(os.path.join(self.new_dir_name, sub_dir))
            else:
                print(f"Directory {sub_dir} already exists.")

    def process_files(self):
        for i in range(self.num_files):
            file_name = self.dir_path + self.files[i]
            model = whisper.load_model("base")
            audio = file_name
            result = model.transcribe(audio)

            for ext in ["txt", "tsv", "json", "srt", "vtt"]:
                writer = get_writer(ext, f"{self.new_dir_name}/{self.get_subdir(ext)}")
                writer(result, audio)

    def get_subdir(self, ext):
        if ext == "txt":
            return self.txt_dir
        elif ext == "tsv":
            return self.tsv_dir
        else:
            return self.other_dir

    def txt_files(self):
        dir_txt_path = f"./{self.new_dir_name}/txt/"
        txt_files = [
            filename
            for filename in os.listdir(dir_txt_path)
            if os.path.isfile(os.path.join(dir_txt_path, filename))
        ]

        for txt_file in txt_files:
                file_path = os.path.join(dir_txt_path, txt_file)
                with open(file_path, 'a') as file:
                    file.write("\nEnd of Line. Thank you.")

        return txt_files
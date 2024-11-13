from ClassGPT import ChatGPT
import os
from ClassWhisper import AudioTranscription
from ClassSox import SoxProcessor
from ClassDirbuilder import Dirbuilder
from ClassDirbuilder import create_empty_file
from ClassTextProcessor import TextProcessor
from MP4toMP3Converter import MP4toMP3Converter



if __name__ == "__main__":
    target_directory = './targetdirectory'
    converter = MP4toMP3Converter(target_directory)
    converter.convert_mp4_to_mp3()

if __name__ == "__main__":
    target_directory = "./targetdirectory"
    output_directory = "./txtalgo"
    processor = SoxProcessor(target_directory, output_directory)
    processor.process_files()

#Build Directory Structure

if __name__ == "__main__":
    create_empty_file("xos.txt")

    file_processor = Dirbuilder("xos.txt")
    file_processor.process_file()

    #load new directory name for use in other areas of the program
    new_directory = file_processor.dir_name
    print(f"New directory name: {new_directory}") # Print the name of the new directory
    os.remove("xos.txt") # Delete the xos.txt file


#Run Whisper process

if __name__ == "__main__":
    transcriber = AudioTranscription()
    txt_files = transcriber.txt_files()
    #print(txt_files)

#Run summary process

#Process files to change length and remove words


#Pass files to be summarized
if __name__ == "__main__":
    processor = TextProcessor()
    processor.process_files()
    directory = "./xos_main/txt/"
    api_key = os.getenv("OPENAI_API_KEY")
    chat_gpt = ChatGPT(directory, api_key)  # Pass the API key as a positional argument
    chat_gpt.generate_text(directory)  # Pass the directory as a positional argument
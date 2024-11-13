import openai
import os
import datetime



class ChatGPT:
    def __init__(self, directory, api_key):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.directory = directory
        self.api_key = api_key


    def generate_text(self, directory):





    # Iterate through all files in the specified directory
        for filename in os.listdir(self.directory):
            # Check if the file has a .txt extension
            if filename.endswith(".txt"):
                # Create the full file path by joining the directory path and filename
                file_path = os.path.join(self.directory, filename)
                #print(file_path)


            with open(self.directory+filename, 'r') as file:
                filename = file.read()

            completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                    messages=[{"role": "system", "content": "You are a text summarizer and consolidation expert."},
                        {"role": "user", "content": "Summarize the conversation into 10 bullet points."},
                        {"role": "user", "content": filename}], temperature=0.7, max_tokens=1024, n=1,
                    # only generate one response
                    stop=None,  # don't stop generation based on any special tokens
                    top_p=1,  # set top_p to 1 for a balance between diversity and quality
                )


            #print(completion.choices[0].message.content)

            current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3]
            extracted_filename = os.path.basename(file_path)
            myFile = (current_time+"_sum"+"_"+extracted_filename)
            print(myFile)

            #Previous
            # os.makedirs("./summaries", exist_ok=True)
            # try:
            #     with open("./summaries/" + myFile, "w") as f:
            #         f.write(completion.choices[0].message.content.strip())  # Access 'content' instead of 'text'
            # except FileNotFoundError:
            #     print("The 'summaries' directory does not exist")

            os.makedirs("./summaries", exist_ok=True)

            # Remove the ".txt" extension from myFile
            subdir_name = os.path.splitext(myFile)[0]

            # Create a sub-directory inside the 'summaries' directory
            os.makedirs(os.path.join("./summaries", subdir_name), exist_ok=True)

            try:
                with open(os.path.join("./summaries",subdir_name, myFile), "w") as f:
                    f.write(completion.choices[0].message.content.strip())  # Access 'content' instead of 'text'
            except FileNotFoundError:
                print("The 'summaries' directory does not exist")
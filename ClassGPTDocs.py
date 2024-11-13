import os
import math
import openai
import time
import datetime

class GPTDocs:

    def __init__(self, api_key):
        api_key = os.getenv("OPENAI_API_KEY")

    def list_txt_files(self, path):
        all_files = os.listdir(path)
        txt_files = [file for file in all_files if file.endswith('.txt')]
        return txt_files

    def split_text_equally(self, text, num_parts):
        chars_per_part = len(text) // num_parts
        parts = [text[i:i + chars_per_part] for i in range(0, len(text), chars_per_part)]
        return parts

    # Replace with the path to your file
    #file_path = './docsbox/txt/Fraction Plans 1_3-1_6.txt'

    def generate_text(self, file_path):
        # Check if the file exists
        if os.path.exists(file_path):
            # Read the file
            with open(file_path, 'r') as file:
                content = file.read()

            # Check if the content has more than 6000 characters
            if len(content) > 6000:
                # Calculate the number of variables based on the content length
                num_variables = math.ceil(len(content) / 6000)

                # Split the content as equally as possible
                content_parts = self.split_text_equally(content, num_variables)

                # Assign the split content to a list of variables
                variables = [None] * num_variables
                for i in range(num_variables):
                    variables[i] = content_parts[i] + " Part of a Series" #This tells the AI the content is over
                    #print(content_parts[0])

                collect_responses = []

                # Print the variables
                for i, var in enumerate(variables, 1):
                    #print({i - 1})
                    series_count = i - 1
                    #print(series_count)
                    #print(f"Variable {i} (array position {i - 1}):\n{var}\n")
                    #print(f"Variable {i}:\n{var}\n")
                    filename = var

                    # Make a request to the API
                    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                        messages=[{"role": "system", "content": "You are a Forensic Accountant. This content is part series. "},
                            {"role": "user", "content": "Summarize these lesson plans into 1-3 paragraphs. Ignore references "
                                                        "to holidays and events. Please focus on academics."},
                            {"role": "user", "content": filename}], temperature=0.7, max_tokens=1024, n=1, stop=None,
                                                              top_p=1, )

                    # Extract the generated response
                    print(series_count)
                    response = completion.choices[0].message.content
                    #print(completion.choices[0].message.content)
                    collect_responses.append(response)
                    #print(f"Response for variable {i} (array position {series_count}):\n{response}\n")

                #print("All responses:\n", collect_responses)
                #time.sleep(10)
                output_string = ""

                for element in collect_responses:
                    output_string += str(element) + " "

                time.sleep(10)

                #print(output_string)
                completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
                    {"role": "system", "content": "You are a Forensic Accountant. This content is part series. "}, {
                        "role": "user", "content": "Provide feedback on the summary for this lesson plan. Please ignore "
                                                   "mentions of Holidays."
                                                   "Format to 10 "
                                                   "Bullet Points."}, {"role": "user", "content": output_string}], temperature=0.7,
                                                          max_tokens=1024, n=1, stop=None, top_p=1, )
                # Extract the generated response
                time.sleep(10)
                response = completion.choices[0].message.content
                #print(f"Response for variable {i} (filename {filename}):\n{response}\n")
                #print(response)
                current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3]
                extracted_filename = os.path.basename(file_path)
                myFile = (current_time + "_sum" + "_" + extracted_filename)
                print(myFile)
                os.makedirs("./summaries", exist_ok=True)

                # Remove the ".txt" extension from myFile
                subdir_name = os.path.splitext(myFile)[0]

                # Create a sub-directory inside the 'summaries' directory
                os.makedirs(os.path.join("./summaries", subdir_name), exist_ok=True)

                try:
                    with open(os.path.join("./summaries", subdir_name, myFile), "w") as f:
                        f.write(completion.choices[0].message.content.strip())  # Access 'content' instead of 'text'
                except FileNotFoundError:
                    print("The 'summaries' directory does not exist")


            else:
                print("The file has less than 6000 characters.")
                filename = os.path.basename(file_path)

                print(filename)

                # Make a request to the API
                completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
                    {"role": "system", "content": "You are a Forensic Accountant. This content is part series. "}, {
                        "role": "user", "content": "Provide feedback on the summary for this lesson plan. Please ignore "
                                                   "mentions of Holidays."
                                                   "Format to 10 "
                                                   "Bullet Points."},
                    {"role": "user", "content": filename}], temperature=0.7, max_tokens=1024, n=1, stop=None, top_p=1, )
                time.sleep(5)
                response = completion.choices[0].message.content
                # print(f"Response for variable {i} (filename {filename}):\n{response}\n")
                #print(response)
                #begin saving summaries

                current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3]
                extracted_filename = os.path.basename(file_path)
                myFile = (current_time + "_sum" + "_" + extracted_filename)
                print(myFile)
                os.makedirs("./summaries", exist_ok=True)

                # Remove the ".txt" extension from myFile
                subdir_name = os.path.splitext(myFile)[0]

                # Create a sub-directory inside the 'summaries' directory
                os.makedirs(os.path.join("./summaries", subdir_name), exist_ok=True)

                try:
                    with open(os.path.join("./summaries", subdir_name, myFile), "w") as f:
                        f.write(completion.choices[0].message.content.strip())  # Access 'content' instead of 'text'
                except FileNotFoundError:
                    print("The 'summaries' directory does not exist")




        else:
            print("File not found.")

api_key = os.getenv("OPENAI_API_KEY")

api_key = os.getenv("OPENAI_API_KEY")

chat_gptdocs = GPTDocs(api_key=api_key)  # Create an instance and pass the API key

txt_file_list = chat_gptdocs.list_txt_files("./docsbox/txt/")

for file_name in txt_file_list:
    file_path = os.path.join("./docsbox/txt/", file_name)
    chat_gptdocs.generate_text(file_path)
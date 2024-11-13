import os
import csv
import glob
import openai
import datetime
import random
import shutil


class Trends:

    def __init__(self, input_file, api_key):
        self.input_file = input_file
        self.api_key = api_key
        #self.directory = directory


    def read_csv(self):
        with open(self.input_file, 'r', newline='') as infile:
            reader = csv.DictReader(infile)
            data = [row for row in reader]
        return data

    def split_and_save_csv(self):
        data = self.read_csv()
        file_size = os.path.getsize(self.input_file)

        if file_size > 6000:
            total_files = int(file_size / 6000) + 1
            return self.save_split_files(data, total_files)
        else:
            # print("File contents:")
            # print(data)
            csv_string = self.csv_data_to_string(data)
            prompt = f"Review this data, and identify the top 10 trends in the data. Do not repeat statements.\n\n{csv_string}"
            messages = [{"role": "system", "content": "You are a Data Analyst."}, {"role": "user", "content": prompt}, ]

            response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=1024, n=1,
                                                    stop=None, temperature=0.7, )

            result = response.choices[0].message['content'].strip()

            # Get the current date and time
            now = datetime.datetime.now()

            # Generate a random hexadecimal number between 1000 and 3000
            random_hex = hex(random.randint(1000, 3000))[2:]



            # Create the directory and file name
            dir_and_file_name = './summaries/' + now.strftime("%Y%m%d%H%M%S") + random_hex + '_trend_results'


            # Ensure the directory exists
            os.makedirs(dir_and_file_name, exist_ok=True)


            # Open the file in the directory
            with open(dir_and_file_name + '/' + dir_and_file_name.split('/')[-1] + '.txt', 'a') as small_results_file:
                small_results_file.write(result + "\n")

            # Print the result
            print(result)

    def save_split_files(self, data, total_files):
        os.makedirs("./docsbox/trends/split/", exist_ok=True)

        chunk_size = len(data) // total_files
        for i in range(total_files):
            start = i * chunk_size
            end = (i + 1) * chunk_size if i < total_files - 1 else len(data)

            chunk_data = data[start:end]
            output_file = f'./docsbox/trends/split/split_{i + 1}.csv'

            with open(output_file, 'w', newline='') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=chunk_data[0].keys())
                writer.writeheader()
                writer.writerows(chunk_data)

        return self.read_and_print_csv_files()

    def read_and_print_csv_files(self):
        input_dir = './docsbox/trends/split/'
        csv_files = glob.glob(os.path.join(input_dir, '*.csv'))
        csv_strings = {}

        for i, file in enumerate(csv_files):
            with open(file, 'r', newline='') as infile:
                reader = csv.DictReader(infile)
                data = [row for row in reader]
                csv_string = self.csv_data_to_string(data)
                # print(f"Contents of {file}:")
                # print(csv_string)
                csv_strings[f'csv_file_{i + 1}'] = csv_string

        return csv_strings

    def csv_data_to_string(self, csv_data):
        headers = list(csv_data[0].keys())
        header_str = ','.join(headers)
        data_rows = [','.join([str(row[header]) for header in headers]) for row in csv_data]
        data_str = '\n'.join(data_rows)
        csv_string = f"{header_str}\n{data_str}"
        return csv_string

    def analyze(self):
        #self.directory="./docsbox/trends/split/"
        csv_strings = self.split_and_save_csv()
        if csv_strings:
            self.api_key = os.getenv("OPENAI_API_KEY")

            # Get the current date and time
            current_datetime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

            # Generate a random hexadecimal number between 1000 and 3000
            random_hex = hex(random.randint(1000, 3000))

            # Create a new directory under "./summaries"
            dir_name = f"./summaries/{current_datetime}_{random_hex}"
            os.makedirs(dir_name, exist_ok=True)

            # Create a new file under the new directory
            self.file_path = f"{dir_name}/trend_results.txt"

            with open(self.file_path, "a") as results_file:
                for key, value in csv_strings.items():
                    # Send each key:value pair into the completion block and print the result
                    prompt = f"Review this data, and identify the top 10 trends in the data. The Grade column " \
                             f"contains "\
                                                              "Grades A+, A, A-, B+, B, B-, C+, C, C-, F. Your goal "\
                                                              "is to product a list of trends. A negative trend is a "\
                                                              "high number of Grades categorized between B- and F. " \
                             "Please list upto 5 students who need support based on their grades. Students are " \
                             "identified using the User_ID column, FirstName column, and LastName column.  Do " \
                                                              "not repeat statements.\n\n{key}: {value}"
                    messages = [{"role": "system", "content": "You are a Data Analyst. Your goal is to help students "
                                                              "improve by informing their teachers and parents."},
                        {"role": "user", "content": prompt}, ]

                    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=1024,
                        n=1, stop=None, temperature=0.7, )

                    result = response.choices[0].message['content'].strip()

                    # Save the result to the file
                    results_file.write(f"{key}:\n{result}\n\n")

            print(self.file_path)
            #return self.file_path
            folder_path = os.path.dirname(self.file_path)
            print(folder_path)

            new_folder_path = os.path.join(folder_path, "combo")

            # Check if the folder already exists
            if not os.path.exists(new_folder_path):
                # Create the new folder
                os.makedirs(new_folder_path)
                print("Folder 'combo' created successfully.")
            else:
                print("Folder 'combo' already exists.")

            new_file_name = os.path.basename(self.file_path)

            # Construct the destination file path in the new folder
            destination_path = os.path.join(new_folder_path, new_file_name)

            # Copy the file to the new folder
            shutil.copy2(self.file_path, destination_path)
            print("File copied successfully.")

            final_prompt_file = destination_path
            print("Final prompt file path:", final_prompt_file)

            # Read the contents of the copied file
            with open(final_prompt_file, "r") as file:
                file_content = file.read()

            # Construct the prompt using the file content
            prompt = f"Review this data, and identify the top 10 trends in the data. Do not repeat statements." \
            "Please list up to 5 students who need support based on their grades. Students are identified using the " \
                     "User_ID, FirstName, and LastName."\
                     f"\n\
            n{file_content}"

            messages = [{"role": "system", "content": ""},  # Empty system message to start a new API session
                {"role": "user", "content": prompt}]

            # Make sure to replace 'your_api_key' with your actual API key
            self.api_key = os.getenv("OPENAI_API_KEY")
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=1024, n=1,
                stop=None, temperature=0.7)

            result = response.choices[0].message['content'].strip()

            print("Result:", result)

            # current_directory = os.path.dirname(final_prompt_file)
            #
            # print("Directory:", current_directory)
            #
            # new_file_path = os.path.join(current_directory, "final_results.txt")
            #
            # with open(new_file_path, 'a') as f:
            #     print("Result:", result, file=f)



if __name__ == "__main__":
    # Replace these values with your actual file, api_key and directory
    input_file = "./docsbox/trends/listresults_2023-05-09_12-17-21_1f01.csv"
    api_key = os.getenv("OPENAI_API_KEY")
    #directory = "./docsbox/trends/split/"

    trends = Trends(input_file, api_key)
    result_file_path = trends.analyze()





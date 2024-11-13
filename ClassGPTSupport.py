import openai
import os
import datetime
import csv
import random
import time
class ChatGPTSupport:
    def __init__(self, directory, api_key):
        api_key = os.getenv("OPENAI_API_KEY")
        self.directory = directory
        self.api_key = api_key
        self.output_file = ""

    def generate_text(self):
        results = []  # Add an array to store results

        # Iterate through all files in the specified directory
        for filename in os.listdir(self.directory):
            # Check if the file has a .csv extension
            if filename.endswith(".csv"):
                # Create the full file path by joining the directory path and filename
                file_path = os.path.join(self.directory, filename)

                with open(file_path, 'r') as file:
                    csv_data = file.read()

                completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a Data Scientist."},
                        {"role": "user", "content": "Given the following data, list each student with their "
                                     "UserID, CourseTitle, the number of incomplete items (Incomplete = True), "
                                     "and the number of late items (Late = True). "
                                     "Output the results in bullet points, and format the student's name as lastname, firstname. "
                                     "Please ensure you only include unique student records. "
                                     "For example:"
                                     "\n- Doe, John | UserID: 1 | CourseTitle: Math | Incomplete Items: 2 | Late Items: 1"},
                        {"role": "user", "content": csv_data}
                    ],
                    temperature=0.7,
                    max_tokens=1024,
                    n=1,
                    stop=None,
                    top_p=1,
                )

                results.append(completion.choices[0].message.content.strip())  # Append result to the array

        # Print results when the loop is complete
        #print(results)
        self.save_results_to_file(results)

    # def save_results_to_file(self, results):
    #     output_file = "./docsbox/txt/results1.txt"
    #     os.makedirs(os.path.dirname(output_file), exist_ok=True)
    #
    #     with open(output_file, "w") as f:
    #         for result in results:
    #             f.write(result + "\n")

    def save_results_to_file(self, results):
        random_hex = hex(random.randint(0x1000, 0x4000))[2:]
        self.output_file = f"./docsbox/csv/temp/results_{random_hex}.txt"
        os.makedirs(os.path.dirname(self.output_file), exist_ok=True)

        with open(self.output_file, "w") as f:
            for result in results:
                f.write(result + "\n")

    def process_results_file(self):

        self.results = []
        with open(self.output_file, "r") as f:
            results_text = f.read()

        # Use the contents of results1.txt as input for a second completion prompt
        completion2 = openai.ChatCompletion.create\
            (model="gpt-3.5-turbo", messages=[{"role": "system", "content": "You are a Data Scientist."},
               {
                   "role": "user",
                   "content": "Summarize the following student data into two paragraphs that highlight the students who need the most help:"},
               {"role": "user", "content": results_text+"\n\nSummary"}], temperature=0.7, max_tokens=1024, n=1,
             stop=None,
                                                        top_p=1, )

        self.results.append(completion2.choices[0].message.content.strip())  # Append result to the array

        # Print results when the loop is complete
        print(self.results)

        filename = f"missingwrk_{random.randint(1000, 4000)}{time.strftime('%H%M%S')}.txt"
        filepath = f"./summaries/csv_results/{filename}"
        with open(filepath, "w") as file:
            file.write("\n".join(self.results))



if __name__ == "__main__":
    directory = "./docsbox/support/file_split/"
    api_key = os.getenv("OPENAI_API_KEY")
    chatgpt_grades = ChatGPTSupport(directory, api_key)
    chatgpt_grades.generate_text()
    chatgpt_grades.process_results_file()
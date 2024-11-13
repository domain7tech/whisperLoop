import openai
import os
import datetime

class ChatGPTCalc:
    def __init__(self, api_key):
        self.api_key = os.getenv("OPENAI_API_KEY")

    def generate_text(self, directory):
        combined_results = ""

        # Iterate through all files in the specified directory
        for filename in os.listdir(directory):
            # Check if the file has a .txt extension
            if filename.endswith(".txt"):
                # Create the full file path by joining the directory path and filename
                file_path = os.path.join(directory, filename)

                with open(file_path, 'r') as file:
                    file_content = file.read()

                if len(file_content) > 6000:
                    chunk_size = 6000
                    content_chunks = [file_content[i:i + chunk_size] for i in range(0, len(file_content), chunk_size)]
                else:
                    content_chunks = [file_content]

                for chunk in content_chunks:
                    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "You are a data analysis expert specialized in summarizing statistical information and identifying trends."},
                            {"role": "user", "content": "Provide a summary of the dataset, including key statistics and trendlines."},
                            {"role": "user", "content": chunk}
                        ],
                        temperature=0.7,
                        max_tokens=1024,
                        n=1,
                        stop=None,
                        top_p=1,
                    )

                    combined_results += completion.choices[0].message['content'].strip() + "\n"

        final_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a data analysis expert specialized in summarizing statistical information and identifying trends."},
                {"role": "user", "content": "Provide a summary of the dataset, including key statistics and "
                                            "trends. The data is academic in nature. Use up to 10 bullet points in "
                                            "the response. "},
                {"role": "user", "content": combined_results}
            ],
            temperature=0.7,
            max_tokens=1024,
            n=1,
            stop=None,
            top_p=1,
        )

        print(final_completion.choices[0].message['content'].strip())

if __name__ == "__main__":
    directory = './docsbox/csv/calc/final/'
    chat_gpt_calc = ChatGPTCalc(api_key=os.getenv("OPENAI_API_KEY"))
    chat_gpt_calc.generate_text(directory)

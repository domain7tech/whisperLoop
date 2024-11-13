import os
import datetime
import csv
import random


def save_results_to_file(results):
    random_hex = hex(random.randint(0x1000, 0x4000))[2:]
    output_file = f"./summaries/csv/results_{random_hex}.txt"
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "w") as f:
        for result in results:
            f.write(result + "\n")

results = ["1", "2", "3"]
save_results_to_file(results)
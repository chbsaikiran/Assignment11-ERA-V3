import csv

def csv_to_txt(csv_file_path, txt_file_path):
    try:
        with open(csv_file_path, 'r', encoding='utf-8') as csv_file, open(txt_file_path, 'w', encoding='utf-8') as txt_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if len(row) >= 2:  # Ensure the row has at least two columns
                    txt_file.write(row[0] + '\\n')  # Write the first cell
                    txt_file.write(row[1] + '\\n')  # Write the second cell
    except FileNotFoundError:
        print(f"Error: The file {csv_file_path} was not found.")
    except UnicodeDecodeError as e:
        print(f"Unicode error: {e}. Try using a different encoding like 'latin1'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
csv_file_path = 'train.csv'  # Replace with your .csv file path
txt_file_path = 'output.txt'  # Replace with your desired .txt file path
csv_to_txt(csv_file_path, txt_file_path)

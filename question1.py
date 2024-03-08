import csv
import json
from tkinter import Tk, Button, messagebox

# Function to clean up extra quote characters
def clean_data(data):
    return data.replace('"', '')

# Function to convert CSV to JSON
def csv_to_json(csv_file, json_file):
    sales_data = []

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            clean_row = {key: clean_data(value) for key, value in row.items()}
            sales_data.append(clean_row)

    with open(json_file, 'w') as file:
        json.dump(sales_data, file, indent=4)

# Main GUI class
class SalesApp:
    def __init__(self, master):
        self.master = master
        master.title("Sales Data Converter")
        master.geometry("300x100")

        self.quit_button = Button(master, text="Quit", command=self.quit)
        self.quit_button.pack()

    def quit(self):
        self.master.quit()
        messagebox.showinfo("Info", "All windows closed.")

# Main function
def main():
    # Define file paths
    csv_file = "/Users/rohithkoushal/Documents/College/Winter 2024 Wayne/Software Engineering/Code/Weekly Homework 8/SalesJan2009.csv"
    json_file = "/Users/rohithkoushal/Documents/College/Winter 2024 Wayne/Software Engineering/Code/Weekly Homework 8/transaction_data.json"

    # Convert CSV to JSON
    csv_to_json(csv_file, json_file)

    # Create GUI
    root = Tk()
    app = SalesApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

import sys
import easygui
import os
import pandas as pd
import yaml
from src.load_data import load_data

def check_dtypes(data):
    print(data.dtypes)


def analyze_1d(data, column):
    # Here you can add more detailed analysis for a single column
    print(data[column].describe())


def analyze_2d(data, column1, column2):
    # Here you can add more detailed analysis for two columns
    print(data[[column1, column2]].describe())


def analyze_md(data, columns):
    # Here you can add more detailed analysis for multiple columns
    print(data[columns].describe())



class GUI():
    def __init__(self):
        self.data_list = []
        self.data_names = []
        self.config = None
        self.data_of_interest = None
        self.data_of_interest_indx = None
        self.column_of_interest1d = None
        self.column_of_interest2d1 = None
        self.column_of_interest2d2 = None
        self.columns_of_interest_md = []

    def load_config(self):
        if os.path.exists("config.yml"):
            with open("config.yml", 'r') as ymlfile:
                cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
            self.config = cfg

    def load_data_from_config(self):
        if self.config is None:
            self.load_config()
        if self.config:
            for data in self.config.get('data', []):
                self.data_names.append(data['name'])
                self.data_list.append(load_data(data['path']))

    def load_data(self):
        print("What is the name of the data you want to load? (Alias)")
        name = input("Enter the name: ")
        self.data_names.append(name)
        self.data_list.append(load_data())
        if len(self.data_list) == 1:
            self.data_of_interest = name
            self.data_of_interest_indx = 0

    def save_data_by_name_type(self, data, fname):
        """
        If the file ends in csv than save it as csv
        Handles, csv, xlsx, json, parquet, hdf5
        """
        if fname.endswith('.csv'):
            data.to_csv(fname)
        elif fname.endswith('.xlsx'):
            data.to_excel(fname)
        elif fname.endswith('.json'):
            data.to_json(fname)
        elif fname.endswith('.parquet'):
            data.to_parquet(fname)
        elif fname.endswith('.h5'):
            data.to_hdf(fname)
        else:
            print("Unsupported file format.")

    def save_data(self):
        if len(self.data_list) == 0:
            print("No data loaded.")
        else:
            for i, data in enumerate(self.data_list):
                print(f"{i}: {self.data_names[i]}")
            data_number = int(input("Enter the data number: "))
            data = self.data_list[data_number]
            fname = easygui.filesavebox()
            self.save_data_by_name_type(data, fname)

    def select_data(self):
        """
        Prints data available with a number in front of them.
        User can select a data by entering the number.
        """
        if len(self.data_list) == 0:
            print("No data loaded.")
        else:
            for i, data_name in enumerate(self.data_names):
                print(f"{i}: {data_name}")
            data_number = int(input("Enter the data number: "))
            self.data_of_interest = data_name 
            self.data_of_interest_indx = data_number
    
    def check_dtypes(self):
        print("--- Data types ---")
        if len(self.data_list) == 0:
            print("No data loaded.")
        else:
            df = self.data_list[self.data_of_interest_indx]
            for col in df.columns:
                examples = df[col].head(5).values
                example_str = ", ".join([str(x) for x in examples])
                print(f"{col}: {df[col].dtype} \t {example_str}")

    def select_column(self):
        """
        Prints columns available with a number in front of them.
        User can select a column by entering the number.
        """
        if len(self.data_list) == 0:
            print("No data loaded.")
        else:
            df = self.data_list[self.data_of_interest_indx]
            for i, column in enumerate(df.columns):
                print(f"{i}: {column}")
            column_number = int(input("Enter the column number: "))
            return df.columns[column_number]
    
    def analyze_1d(self):
        if len(self.data_list) == 0:
            print("No data loaded.")
        else:
            self.column_of_interest1d = self.select_column()
            analyze_1d(self.data, self.column_of_interest1d)
    
    def main_menu(self):
        while True:
            print("\nOptions:")
            print("1: Load data")
            print("2: Check dtypes")
            print("3: Analyze 1D")
            print("4: Analyze 2D")
            print("5: Analyze MD")
            print("6: Save data")
            print("7: Quit")

            option = input("Enter option number: ")

            if option == '1':
                self.load_data()

            elif option == '2':
                self.check_dtypes()

            elif option == '3':
                self.analyze_1d()

            elif option == '4':
                self.analyze_2d()

            elif option == '5':
                self.analyze_md()

            elif option == '6':
                self.save_data()

            elif option == '7':
                print("Exiting the program.")
                sys.exit()

            else:
                print("Invalid option. Please enter a number between 1 and 7.")
        


            


def main():
    gui = GUI()
    gui.main_menu()

if __name__ == "__main__":
    main()

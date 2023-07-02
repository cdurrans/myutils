import pandas as pd
import easygui
import os

def load_data():
    file_path = easygui.fileopenbox()
    
    if file_path is None:
        print("No file selected.")
        return None

    _, file_extension = os.path.splitext(file_path)

    try:
        if file_extension == '.csv':
            data = pd.read_csv(file_path)
        elif file_extension == '.xlsx':
            data = pd.read_excel(file_path)
        elif file_extension == '.json':
            data = pd.read_json(file_path)
        elif file_extension == '.parquet':
            data = pd.read_parquet(file_path)
        elif file_extension == '.h5':
            data = pd.read_hdf(file_path)
        # You can add more file formats here
        else:
            print("Unsupported file format.")
            return None

        return data
    
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")
        return None

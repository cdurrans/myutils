import numpy as np
import pandas as pd
import re

def is_date(string):
    try:
        pd.to_datetime(string)
        return True
    except ValueError:
        return False

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def has_leading_zeroes(string):
    return re.match(r'^0\d+', string) is not None

def is_whole_number(value):
    try:
        num = float(value)
        return num.is_integer() or pd.isna(num)
    except ValueError:
        return False

def convert_dataframe(dataframe):
    for column in dataframe.columns:
        # Check if all the values in the column are dates
        if all(dataframe[column].apply(lambda x: is_date(str(x)))):
            dataframe[column] = pd.to_datetime(dataframe[column])
        # Check if all the values in the column are floats or integers
        elif all(dataframe[column].apply(lambda x: is_float(str(x)))):
            # Check for leading zeroes
            if any(dataframe[column].astype(str).apply(lambda x: has_leading_zeroes(x))):
                dataframe[column] = dataframe[column].astype(str)
            else:
                # Check if all the values in the column are whole numbers
                if all(dataframe[column].apply(lambda x: is_whole_number(str(x)))):
                    dataframe[column] = pd.to_numeric(dataframe[column]).astype("Int64")
                else:
                    dataframe[column] = pd.to_numeric(dataframe[column]).astype("Float64")
    return dataframe



def load_and_convert_dataframe(fname):
    dataframe = pd.read_csv(fname, dtype=str)
    converted_dataframe = convert_dataframe(dataframe)
    return converted_dataframe


def test_convert_dataframe():
    df = pd.DataFrame({'a': ['1', '2', '3']
                       , 'b': ['2018-01-01', '2018-01-02', '2018-01-03']
                       , 'c': ['1.1', '2.2', '3.3']
                       , 'd': [np.nan, '02', '03']
                       , 'e': ['1.0', '2.0', np.nan]})
    converted_df = convert_dataframe(df)
    assert converted_df['a'].dtype == 'Int64', "column a should be int but is:" + str(converted_df['a'].dtype)
    assert converted_df['b'].dtype == 'datetime64[ns]', "column b should be datetime but is:" + str(converted_df['b'].dtype)
    assert converted_df['c'].dtype == 'Float64', "column c should be float but is:" + str(converted_df['c'].dtype)
    assert converted_df['d'].dtype == 'object', "column d should be object but is:" + str(converted_df['d'].dtype)
    assert converted_df['e'].dtype == 'Int64', "column e should be int but is:" + str(converted_df['e'].dtype)







if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('fname', help='CSV file to load')
    args = parser.parse_args()
    converted_dataframe = load_and_convert_dataframe(args.fname)
    print(converted_dataframe)
    #test_convert_dataframe()





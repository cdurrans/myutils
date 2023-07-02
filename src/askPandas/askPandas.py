

import pandas as pd 

def most_frequent_values(df, column, n=10):
    """
    Question: find me the most frequent value in the column
    params:
        df: pandas dataframe
        column: string
        n: int
    return description: n most frequent values
    return type: 'pandas.core.series.Series'
    """
    return df[column].value_counts().head(n)



def least_frequent_values(df, column, n=10):
    """ 
    Question: find me the least frequent value in the column
    params: 
        df: pandas dataframe
        column: string
        n: int
    return description: n least frequent values
    return type: 'pandas.core.series.Series'
    """
    return df[column].value_counts().tail(n)


def filter_columns_null_percent(df, n=0.5):
    """
    Question: find me the columns with more than n% non-null values
    params:
        df: pandas dataframe
        n: float
    return description: dataframe with columns with more than n% non-null values
    return type: 'pandas.core.frame.DataFrame'
    """
    return df.loc[:, df.notnull().mean() > n].copy()

# what are the column names of this dataframe
def get_column_names(df):
    """
    Question: what are the column names of this dataframe
    params:
        df: pandas dataframe
    return description: column names of this dataframe
    return type: 'list'
    """
    return df.columns.tolist()


def get_unique_value_count(df, column):
    """
    Question: how many unique values are there in the column
    params:
        df: pandas dataframe
        column: string
    return description: number of unique values in the column
    return type: 'int'
    """
    return df[column].nunique()


def get_unique_values(df, column):
    """
    Question: what are the unique values in the column
    params:
        df: pandas dataframe
        column: string
    return description: unique values in the column
    return type: 'list'
    """
    return df[column].unique().tolist()


def get_values_percent_of_total(df, column):
    """
    Question: what values are in the column and what percent of the total do they make up
    params:
        df: pandas dataframe
        column: string
    return description: values in the column and what percent of the total they make up
    return type: pd.core.series.Series
    """
    return df[column].value_counts(normalize=True) * 100


def get_value_counts(df, column):
    """
    Question: what are the value counts for the column
    params:
        df: pandas dataframe
        column: string
    return description: value counts for the column
    return type: pd.core.series.Series
    """
    return df[column].value_counts()



def get_percentile(df, column, n=0.1):
    """
    Question: what is the nth percentile of the column
    params:
        df: pandas dataframe
        column: string
        n: float
    return description: nth percentile of the column
    return type: 
    """
    return df[column].quantile(n)



def filter_values_above(df, column, n):
    """
    Question: filter values above n
    params:
        df: pandas dataframe
        column: string
        n: float
    return description: dataframe with values above n
    return type: pd.core.frame.DataFrame
    """
    return df[df[column] > n].copy()


def filter_values_below(df, column, n):
    """
    Question: filter values below n
    params:
        df: pandas dataframe
        column: string
        n: float
    return description: dataframe with values below n
    return type: pd.core.frame.DataFrame
    """
    return df[df[column] < n].copy()



def filter_values_between(df, column, n1, n2):
    """
    Question: filter values between n1 and n2
    params:
        df: pandas dataframe
        column: string
        n1: float
        n2: float
    return description: dataframe with values between n1 and n2
    return type: pd.core.frame.DataFrame
    """
    return df[(df[column] > n1) & (df[column] < n2)].copy()


def above_vs_below_percentile_value_counts(df, columnOfInterest, columnNumeric, n):
    """
    Question: what are the value counts for columnOfInterest for values above and below the nth percentile of columnNumeric
    params:
        df: pandas dataframe
        columnOfInterest: string
        columnNumeric: string
        n: float
    return description: value counts for values
    return type: pd.core.series.Series, pd.core.series.Series
    """
    assert n > 0 and n < 1
    assert columnOfInterest in df.columns.tolist()
    assert columnNumeric in df.columns.tolist()
    assert df[columnNumeric].dtype.name in ['int64', 'float64', 'int32', 'float32', 'int', 'float', 'Int64', 'Float64', 'Int32', 'Float32', 'Int', 'Float']
    assert df[columnOfInterest].dtype.name in ['object', 'string', 'str']
    value = get_percentile(df, columnNumeric, n)
    below = filter_values_below(df, columnNumeric, value)
    above = filter_values_above(df, columnNumeric, value)
    return below[columnOfInterest].value_counts(), above[columnOfInterest].value_counts()


def get_null_values_boolean(df, column):
    """
    Question: Which values are null and which are not null
    params:
        df: pandas dataframe
        column: string
    return description: boolean series where True is null and False is not null
    return type: pd.core.series.Series
    """
    return df[column].isnull()
    
    
def null_vs_not_value_counts(df, columnWithNulls, columnOfInterest):
    """
    Question: what makes the null values different from the non-null values for this column
    params:
        df: pandas dataframe
        columnWithNulls: string
        columnOfInterest: string
    return description: value counts for null and non-null values
    return type: pd.core.series.Series, pd.core.series.Series
    """
    assert columnWithNulls in df.columns.tolist()
    assert columnOfInterest in df.columns.tolist()
    assert df[columnOfInterest].dtype.name in ['object', 'string', 'str']
    null_filter = get_null_values_boolean(df, columnWithNulls)
    nulls = df[null_filter][columnOfInterest].value_counts()
    not_nulls = df[~null_filter][columnOfInterest].value_counts()
    return nulls, not_nulls

import matplotlib.pyplot as plt
import seaborn as sns

# plot overlapping histograms for two series
def plot_two_histograms(seriesA, seriesB):
    """
    Question: how do the distributions of two series compare
    params:
        seriesA: pandas series
        seriesB: pandas series
    return description: plot of two histograms
    return type: matplotlib.axes._subplots.AxesSubplot
    """
    assert seriesA.dtype.name in ['int64', 'float64', 'int32', 'float32', 'int', 'float', 'Int64', 'Float64', 'Int32', 'Float32', 'Int', 'Float']
    assert seriesB.dtype.name in ['int64', 'float64', 'int32', 'float32', 'int', 'float', 'Int64', 'Float64', 'Int32', 'Float32', 'Int', 'Float']
    fig, ax = plt.subplots()
    sns.histplot(seriesA, ax=ax, label=f"First Series: {seriesA.name}")
    sns.histplot(seriesB, ax=ax, label=f"Second Series: {seriesB.name}")
    ax.legend()
    return ax


def plot_bar_chart(data, column, title=None, xlabel=None, ylabel=None):
    """
    Question: plot me a bar chart of values in the column
    params:
        data: pandas dataframe
        column: string
        title: string
        xlabel: string
        ylabel: string
    return description: bar chart of values in the column
    return type: matplotlib.axes._subplots.AxesSubplot
    """
    assert column in data.columns.tolist()
    assert data[column].dtype.name in ['object', 'string', 'str']
    fig, ax = plt.subplots()
    sns.countplot(data=data, x=column, ax=ax)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return ax


# plot value counts over time
def plot_value_counts_over_time(data, column, time_column, title=None, xlabel=None, ylabel=None):
    """
    Question: plot me a bar chart of values in the column over time
    params:
        data: pandas dataframe
        column: string
        time_column: string
        title: string
        xlabel: string
        ylabel: string
    return description: bar chart of values in the column over time
    return type: matplotlib.axes._subplots.AxesSubplot
    """
    assert column in data.columns.tolist()
    assert data[column].dtype.name in ['object', 'string', 'str']
    assert time_column in data.columns.tolist()
    assert data[time_column].dtype.name in ['datetime64[ns]', 'datetime64', 'datetime']
    fig, ax = plt.subplots()
    sns.countplot(data=data, x=column, hue=time_column, ax=ax)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return ax


def group_by_time_period(data, time_column, time_period="M"):
    """
    Question: group date by time period

    params:
        data: pandas dataframe
        time_column: string
        time_period: string
    """
    assert time_column in data.columns.tolist()
    assert data[time_column].dtype.name in ['datetime64[ns]', 'datetime64', 'datetime']
    return data[time_column].dt.to_period(time_period)


# group date by time period and plot value counts
def plot_value_counts_by_time_period(data, column, time_column, time_period, title=None, xlabel=None, ylabel=None):
    """
    Question: plot me a bar chart of values in the column over time
    params:
        data: pandas dataframe
        column: string
        time_column: string
        time_period: string
        title: string
        xlabel: string
        ylabel: string
    return description: bar chart of values in the column over time
    return type: matplotlib.axes._subplots.AxesSubplot
    """
    assert column in data.columns.tolist()
    assert data[column].dtype.name in ['object', 'string', 'str']
    assert time_column in data.columns.tolist()
    assert data[time_column].dtype.name in ['datetime64[ns]', 'datetime64', 'datetime']
    assert time_period in ['M', 'Y', 'D', 'W']
    fig, ax = plt.subplots()
    temp_column = f"new_{time_column}_temp"
    data[temp_column] = data[time_column].dt.to_period(time_period)
    col_cnt = f"{column}_cnt"
    gr = data.groupby(temp_column)[column].value_counts()
    gr.name = col_cnt
    gr = gr.reset_index()
    sns.countplot(data=gr, x=col_cnt, hue=gr.index, ax=ax)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return ax



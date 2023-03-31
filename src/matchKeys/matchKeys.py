import pandas as pd

def maybe_upsample(df1, df2):
    n = len(df1) - len(df2)
    if n > 0:
        # Randomly sample n rows from df2 and concatenate with df2
        df2 = pd.concat([df2.sample(n=n, replace=True), df2], ignore_index=True)
    elif n < 0:
        # Randomly sample n rows from df1 and concatenate with df1
        df1 = pd.concat([df1.sample(n=(n*-1), replace=True), df1], ignore_index=True)
    assert len(df1) == len(df2)
    return df1, df2

def find_matching_keys(df1, df2):
    mapping = {}
    #
    print("Length df1:", len(df1))
    print("Length df2:", len(df2))
    print("Ideally, df1 and df2 should have the same length.")
    df1, df2 = maybe_upsample(df1, df2)
    for col1 in df1.columns:
        for col2 in df2.columns:
            equal = (df1[col1].apply(lambda x: str(x).lstrip('0')) == df2[col2].apply(lambda x: str(x).lstrip('0')))
            if equal.any():
                mapping[col1] = dict()
                mapping[col1]["MatchName"] = col2
                mapping[col1]["NumberMatch"] = equal.sum()
                mapping[col1]["NumberPossible"] = len(equal)
                break
    # if there are no matches, return an empty dictionary
    return mapping



def test_find_matching_keys():
    # Create two sample dataframes
    df1 = pd.DataFrame({'AwesomeBankid': ['1', '2', '5', '0', '1', '2', '5', '0'],
                        'name': ['John', 'Jane', 'Joe', 'Jill', 'John', 'Jane', 'Joe', 'Jill'],
                        'RandomName': ['5000', '70000', '35', '60000', '5000', '70000', '35', '60000'],
                        'a4': ['0000XXYM', '0000AF2F', '0000AF2F', '0000FFF2', '0000XXYM', '0000AF2F', '0000AF2F', '0000FFF2']
                        })
    df2 = pd.DataFrame({'uid': ['0', '2', '5', '2'],
                        'x2': ['XXYM', 'AF2F', 'AF2F', 'FFF2'],
                        'gender': ['M', 'F', 'M', 'F'],
                        'Ugh': ['5000', '60000', '70000', '80000']})

    answer = find_matching_keys(df1, df2)
    print(answer)  


if __name__ == "__main__":
# Create two sample dataframes
    test_find_matching_keys()

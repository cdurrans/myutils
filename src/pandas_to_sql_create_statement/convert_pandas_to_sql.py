import pandas as pd
from sqlalchemy import create_engine, inspect

# Create a sample DataFrame
data = {
    "id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"],
    "age": [28, 34, 22],
    "is_member": [True, False, True],
    "join_date": ["2021-03-01", "2021-04-15", "2021-05-28"],
}

df = pd.DataFrame(data)

# Convert Pandas datatypes to PostgreSQL datatypes
def pandas_dtype_to_postgres(dtype):
    if pd.api.types.is_integer_dtype(dtype):
        return "integer"
    elif pd.api.types.is_float_dtype(dtype):
        return "float"
    elif pd.api.types.is_bool_dtype(dtype):
        return "boolean"
    elif pd.api.types.is_datetime64_any_dtype(dtype):
        return "timestamp"
    else:
        return "text"


# Generate CREATE TABLE statement for PostgreSQL
def generate_create_table_statement(df, table_name):
    create_table_template = "CREATE TABLE {table_name} (\n{columns});"
    column_template = "    {column_name} {column_type}"
    columns = []
    # Iterate over the columns in the DataFrame
    for column_name, dtype in df.dtypes.items():
        postgres_dtype = pandas_dtype_to_postgres(dtype)
        columns.append(column_template.format(column_name=column_name, column_type=postgres_dtype))
    #
    create_table_statement = create_table_template.format(
        table_name=table_name,
        columns=",\n".join(columns)
    )
    return create_table_statement



def test_generate_create_table_statement():
    table_name = "my_table"
    create_table_statement = generate_create_table_statement(df, table_name)
    print(create_table_statement)


if __name__ == "__main__":
    test_generate_create_table_statement()
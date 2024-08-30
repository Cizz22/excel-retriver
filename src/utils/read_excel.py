import os
import pandas as pd


def read_excel_data(file_path):
    # Load the Excel file and slice the dataframe from B8 onwards
    """
    Reads an Excel file and extracts the data from the rows starting from B8,
    up to the last row in the sheet.

    :param file_path: The path to the Excel file to be read.
    :type file_path: str
    :return: data.
    :rtype: pandas.DataFrame
    """
    df = pd.read_excel(file_path, sheet_name=0,
                       engine='openpyxl', header=None).iloc[1:, 1:]
    return df


def clean_input_data(data):

    result = []

    category = None
    for row in data.values:
        if pd.isna(row[0]):
            continue
        if row[2] == "Input":
            category = row[0]
            continue

        if row[0] == "Primary:":
            category = f"{category} {row[0]}" if category else row[0]
            continue

        if row[0] == "Secondary:":
            category = f"{category.split(' ')[0]} {category.split(' ')[1]} {row[0]}"
            continue

        result.append([
            row[0],
            category,
            row[1],
            "in"
        ])

    return result


# df = read_excel_data(
#     "/Users/user/programming/digital-twin/ExcelRetriver/dummy_data/input.xlsx")


# clean_input_data(df)


def read_excel_folder(folder_path):
    """
    Reads all Excel files in a folder and returns a list of their names.

    :param folder_path: The path to the folder containing the Excel files.
    :type folder_path: str
    :return: A list of Excel file names, or a message indicating that the directory was not found.
    :rtype: list or str
    """

    try:
        # List all files in the folder
        return [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    except FileNotFoundError:
        raise ValueError(f"Directory not found: {folder_path}")


def clean_output_data(data):
    # Filter rows based on the headers and keep relevant rows
    """
    Filters rows based on the headers and keeps relevant rows.

    Args:
        data (pandas.DataFrame): DataFrame containing data to be cleaned.

    Returns:
        list: List of lists containing the cleaned data, where each inner list
            contains the variable title, unit, and type of variable (in or out).
    """
    headers = {'INPUT VARIABLE DESCRIPTION', 'OUTPUT VARIABLE DESCRIPTION'}
    cleaned_data = []
    variable_type = 'in'

    for row in data.values:
        if isinstance(row[0], str):
            if row[0] in headers:
                if row[0] == 'OUTPUT VARIABLE DESCRIPTION':
                    variable_type = 'out'
                continue

            if variable_type == 'in':
                continue

            category, variable = get_category(row[0])
            cleaned_data.append([variable, category, row[1], variable_type])

    return cleaned_data


def get_category(data: str):

    splits = data.split(': ', 1)

    if len(splits) == 2:
        return splits[0], splits[1]
    else:
        return None, data


def get_output_data(data):
    """
    Extracts the output variables that appear after the 'OUTPUT VARIABLE DESCRIPTION' section.
    :param data: The sliced dataframe.
    :return: A list of output variables with their corresponding values.
    """
    output_data = {}
    capture_output = False

    for row in data.values:
        # Check if the current row contains 'OUTPUT VARIABLE DESCRIPTION'
        if isinstance(row[0], str) and row[0] == 'OUTPUT VARIABLE DESCRIPTION':
            capture_output = True
            continue  # Start capturing data after this line

        # Once capturing starts, append the output data
        if capture_output and isinstance(row[0], str):
            if pd.isna(row[2]):
                row[2] = 0
                
            output_data[row[0]] = row[2]

    return output_data

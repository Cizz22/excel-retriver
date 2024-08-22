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
                       engine='openpyxl', header=None).iloc[6:, 1:]
    return df


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


def clean_data(data):
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
            cleaned_data.append([row[0], row[1], variable_type])

    return cleaned_data


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
            output_data[row[0]] = row[2]

    return output_data


# data = read_excel_data('/Users/user/programming/digital-twin/ExcelRetriver/dummy_data/TFELINK.xlsm')

# output = get_output_data(data)

# print(output)
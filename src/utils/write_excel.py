import openpyxl

def map_variable_titles(sheet, target_column='B'):
    """
    Creates a dictionary mapping variable titles to their row numbers.
    :param sheet: The worksheet object.
    :param target_column: The column where the variable titles are located (default is 'B').
    :return: A dictionary where keys are variable titles and values are row numbers.
    """
    title_to_row = {}
    for row in range(1, sheet.max_row + 1):
        cell_value = sheet[f'{target_column}{row}'].value
        if isinstance(cell_value, str):
            title_to_row[cell_value] = row
    return title_to_row

def write_values_to_excel(file_path, variable_value_mapping, target_column='D'):
    """
    Writes values to the corresponding cells based on the variable titles.
    :param file_path: Path to the Excel file.
    :param variable_value_mapping: Dictionary mapping variable titles to the input values.
    :param target_column: The column where the input values should be written (default is 'D').
    """
    try:
        # Load the workbook and select the active sheet
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active

        # Map all variable titles to their respective rows
        title_to_row = map_variable_titles(sheet)

        # Write the values to the corresponding cells
        for variable_title, input_value in variable_value_mapping.items():
            if variable_title in title_to_row:
                row = title_to_row[variable_title]
                sheet[f'{target_column}{row}'] = input_value
            else:
                raise ValueError(f"Variable title '{variable_title}' not found in the sheet.")

        # Save the workbook
        workbook.save(file_path)
        print("All values have been written successfully.")

    except FileNotFoundError:
        raise FileNotFoundError(f"The file at '{file_path}' was not found. Please check the file path.")

    except PermissionError:
        raise PermissionError(f"Permission denied: Unable to write to '{file_path}'. Make sure the file is not open or in use.")

    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")

# Example usage:
variable_value_mapping = {
    'Variable 1': 'Value 1',
    'Variable 2': 'Value 2',
    'Variable 3': 'Value 3',
}

# try:
#     write_values_to_excel('./dummy_data/TFELINK.xlsx', variable_value_mapping)
# except Exception as e:
#     print(f"Error: {e}")

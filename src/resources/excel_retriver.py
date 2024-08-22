
import os
from flask_restful import Resource
from utils import parse_params, response, read_excel_folder
from config import EXCEL_FOLDER_PATH
from utils.read_excel import clean_data, get_output_data, read_excel_data
from utils.write_excel import write_values_to_excel
from flask_restful.reqparse import Argument


class ExcelsResource(Resource):
    """ Excels resource """

    def get(self):
        """Get All Excel File"""

        files = read_excel_folder(
            "/Users/user/programming/digital-twin/ExcelRetriver/dummy_data")

        print(files)
        return response(200, True, "Get All Excel File", {"excels": files})


class ExcelResource(Resource):
    """ Excel resource """

    def get(self, excel_name):
        """ Get excel variabels """
        excel_path = os.path.join(EXCEL_FOLDER_PATH, excel_name)

        data = read_excel_data(excel_path)
        cleaned_data = clean_data(data)

        return response(200, True, "Get excel variabels", [{"variabel": i[0], "unit": i[1], "type": i[2]} for i in cleaned_data])

    @parse_params(
        Argument("inputs", type=dict, required=True, location="json")
    )
    def post(self, excel_name, inputs):
        """ Post excel variabels """

        """Example Input"""
        # {
        #  'Variable 1': 'Value 1',
        #  'Variable 2': 'Value 2',
        #  'Variable 3': 'Value 3',
        #    }

        excel_path = os.path.join(EXCEL_FOLDER_PATH, excel_name)

        try:
            write_values_to_excel(excel_path, inputs)

            # Run Macro script (dummy using sleep 5 seconds)

            # Get Output
            output = get_output_data(read_excel_data(excel_path))

            return response(200, True, "Post excel variabels", output)

        except Exception as e:
            return response(500, False, "Error post excel", {"message": str(e)})

    pass

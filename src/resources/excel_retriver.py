
import os
from flask_restful import Resource
from utils import parse_params, response, read_excel_folder
from config import EXCEL_FOLDER_PATH
from utils.read_excel import clean_input_data,clean_output_data, get_output_data, read_excel_data
from utils.write_excel import write_values_to_excel
from flask_restful.reqparse import Argument


class ExcelsResource(Resource):
    """ Excels resource """

    def get(self):
        """Get All Excel File"""

        files = read_excel_folder("/Users/user/programming/digital-twin/ExcelRetriver/dummy_data")

        print(files)
        return response(200, True, "Get All Excel File", {"excels": files})


class ExcelResource(Resource):
    """ Excel resource """

    def get(self, excel_name):
        """ Get excel variabels """
        out_path = os.path.join("/Users/user/programming/digital-twin/ExcelRetriver/dummy_data", "output.xlsm")
        in_path = os.path.join("/Users/user/programming/digital-twin/ExcelRetriver/dummy_data", "input.xlsx")

        out = read_excel_data(out_path)
        inp = read_excel_data(in_path)
        input = clean_input_data(inp)
        output = clean_output_data(out)
        
        input.extend(output)

        return response(200, True, "Get excel variabels", [{"variabel": i[0],"category": i[1] ,"unit": i[2], "type": i[3]} for i in input])

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
            # write_values_to_excel(excel_path, inputs)

            # Run Macro script (dummy using sleep 5 seconds)

            # Get Output
            output = get_output_data(read_excel_data("/Users/user/programming/digital-twin/ExcelRetriver/dummy_data/output.xlsm"))

            return response(200, True, "Post excel variabels", output)

        except Exception as e:
            return response(500, False, "Error post excel", {"message": str(e)})

    pass

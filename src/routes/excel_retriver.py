"""
Defines the blueprint for the authentication
"""
from flask import Blueprint
from flask_restful import Api

from resources import ExcelsResource, ExcelResource

EXCEL_RETRIVER_BLUEPRINT = Blueprint("excel", __name__)

Api(EXCEL_RETRIVER_BLUEPRINT).add_resource(
    ExcelsResource, "/excels"
)

Api(EXCEL_RETRIVER_BLUEPRINT).add_resource(
    ExcelResource, "/excels/<excel_name>"
)

# Api(AUTHENTICATION_BLUEPRINT).add_resource(
#     SignupResource, "/sign-up"
# )

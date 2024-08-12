from fastapi import FastAPI
from milesianpy.calculations import no_variable_calculation
from milesianpy.parsers import basic_parser
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class Equation(BaseModel):
    equation: list


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def parse_user_input(equation: list):
    basic_parser_class = basic_parser.BasicParser

    basic_parser_class.check_decimals(equation)
    basic_parser_class.check_double_operators(equation)
    basic_parser_class.check_values(equation)
    basic_parser_class.check_if_empty_bracket(equation)


@app.post("/calculation/")
async def no_variable_calculate_value(user_input: Equation):
    no_variable_calculation_class = no_variable_calculation.NoVariableCalculation

    try:
        parse_user_input(user_input.equation)
        result = no_variable_calculation_class.no_variable_basic_calculation(user_input.equation)
        return result
    except Exception as e:
        return str(e)


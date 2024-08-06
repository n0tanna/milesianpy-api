from fastapi import FastAPI
from milesianpy.calculations import no_variable_calculation

app = FastAPI()


@app.get("/calculation/{equation}")
async def no_variable_calculate_value(equation: str):
    no_variable_calculation_class = no_variable_calculation.NoVariableCalculation
    result = no_variable_calculation_class.no_variable_basic_calculation(list(equation))
    return result


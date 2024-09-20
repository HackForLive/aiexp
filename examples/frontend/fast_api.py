from fastapi import FastAPI 
from pydantic import BaseModel

from calculator import calculate

class UserInput(BaseModel):
    operation: str
    x: int
    y: int

app = FastAPI()

@app.post("/calculate")
def operate(input: UserInput):
    result = calculate(operation=input.operation, x=input.x, y=input.y)
    return result

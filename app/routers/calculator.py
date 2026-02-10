from fastapi import APIRouter, HTTPException

from app.models.calculator import CalculateRequest, CalculateResponse
from app.services.calculator_service import calculate, parse

router = APIRouter()


@router.post("/calculate", response_model=CalculateResponse)
async def calculate_expression(request: CalculateRequest):
    try:
        tokens = parse(request.expression)
        result = calculate(tokens)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return CalculateResponse(
        expression=request.expression,
        result=result,
        parsed_tokens=tokens,
    )

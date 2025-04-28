from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os

from .generator import generate_erc20_contract

router = APIRouter()

GENERATED_DIR = "generated_contracts"
os.makedirs(GENERATED_DIR, exist_ok=True)

class ContractRequest(BaseModel):
    name: str
    symbol: str
    initial_supply: int

@router.post ("/composer/create")
def create_contract(request: ContractRequest):
    contract_code = generate_erc20_contract(
        request.name,
        request.symbol,
        request.initial_supply
    )

    file_path = os.path.join(GENERATED_DIR, f"{request.name}.sol")
    with open(file_path, "w") as f:
        f.write(contract_code)

    return {"message": "Contract generated successfully", "file_path": file_path}

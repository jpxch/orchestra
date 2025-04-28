def generate_erc20_contract(name: str, symbol: str, initial_supply: int) -> str:
    contract_template = f"""
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract {name} is ERC20 {{
    constructor() ERC20("{name}", "{symbol}") {{
        _mint(msg.sender, {initial_supply} * 10 **  decimals());
    }}
}}
"""

    return contract_template.strip()

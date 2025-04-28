def generate_erc20_contract(name: str, symbol: str, initial_supply: int, burnable: bool, pausable: bool, ownable: bool, mintable: bool) -> str:
    imports = [
        'import "@openzeppelin/contracts/token/ERC20/ERC20.sol";'
    ]
    inheritance = ["ERC20"]
    constructor_logic = [
        '_mint(msg.sender, initialSupply * 10 ** decimals());'
    ]

    if burnable:
        imports.append('import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol",')
        inheritance.append("ERC20Burnable")

    if pausable:
        imports.append('import "@openzeppelin/contracts/security/Pausable.sol";')
        inheritance.append("Pausable")
        constructor_logic.append('')

    if ownable:
        imports.append('import "@openzeppelin/contracts/access/Ownable.sol";')
        inheritance.append("Ownable")

    if mintable:
        constructor_logic.append('')

    contract_template = f"""
// SPDX-Lisence-Identifier: MIT
pragma solidity ^0.8.20;

{chr(10).join(imports)}

contract {name} is {" , ".join(inheritance)} {{

    constructor(uint256 initialSupply) ERC20("{name}", "{symbol}) {{
        {chr(10).join(constructor_logic)}
    }}

    {"function pause() public onlyOwner { _pause(); }" if pausable else ""}
    {"function unpause() public onlyOwner { _unpause(); }" if pausable else ""}
    {"function mint(address to, uint256 amount) public onlyOwner { _mint(to, amount); }" if mintable else ""}
}}
"""
    return contract_template.strip()

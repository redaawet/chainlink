// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract PocketToken is ERC20 {
    address private _owner;

    constructor() ERC20("PocketCashToken", "PCT") {
        _owner = msg.sender;
    }

    function mint(address account, uint256 amount) external {
        require(msg.sender == _owner, "Only owner can mint tokens");
        _mint(account, amount);
    }

    function burn(address account, uint256 amount) external {
        require(msg.sender == _owner, "Only owner can burn tokens");
        _burn(account, amount);
    }
}

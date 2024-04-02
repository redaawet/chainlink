from brownie import PocketToken, Wei, config
from scripts.helpful_scripts import get_account, get_contract, BLOCK_CONFIRMATIONS_FOR_VERIFICATION


def test_token_get_mint():
    # Arrange
    account = get_account(sk=1)
    price_feed = PocketToken[-1]
    # Act
    token_to_be_mint =  Wei("2 ether")
    balance_init = price_feed.balanceOf(account)
    price_feed.mint(account,token_to_be_mint,{"from": account})
    balance = price_feed.balanceOf(account)
    # Assert
    
    assert isinstance(balance, int)
    assert balance > 0
    assert balance == balance_init+token_to_be_mint
def test_burn():
    account = get_account(sk=1)
    price_feed = PocketToken[-1]
    balance = price_feed.balanceOf(account)
    tx = price_feed.burn(account, balance, {"from": account})
    tx.wait(BLOCK_CONFIRMATIONS_FOR_VERIFICATION)
    balance = price_feed.balanceOf(account)
    assert balance ==0

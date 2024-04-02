#!/usr/bin/python3
from brownie import PocketToken, config
from scripts.helpful_scripts import (
    BLOCK_CONFIRMATIONS_FOR_VERIFICATION,
    get_account,
    get_contract,
    is_verifiable_contract,
)


def deploy_pocket_token():
    account = get_account(sk=1)
    
    pocket_token = PocketToken.deploy(
            {"from": account},
        )
    
    if is_verifiable_contract():
        pocket_token.tx.wait(BLOCK_CONFIRMATIONS_FOR_VERIFICATION)
        PocketToken.publish_source(pocket_token)

    print(f"Token with name: {pocket_token.name()}, symbol: {pocket_token.symbol()}, decimals: {pocket_token.decimals()} and total supply: {pocket_token.totalSupply()} is created at address:{pocket_token.address}")
    return pocket_token


def main():
    deploy_pocket_token()

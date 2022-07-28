from brownie import (
    PoolProxy,
    config,
    accounts,
)

deployer = accounts.add(config["wallets"]["from_key"])

def main():
    PoolProxy.deploy(
        deployer.address,
        deployer.address,
        deployer.address,
        {"from": deployer}
    )


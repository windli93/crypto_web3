from web3 import Web3

if __name__ == '__main__':
    w3 = Web3()
    acct = w3.eth.account.create()
    private_key = acct.privateKey.hex()
    address = acct.address

    print(private_key)
    print(address)

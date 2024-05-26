import base64

from web3 import Web3

if __name__ == '__main__':
    message = "KuKu".encode()
    base64_msg = base64.b64encode(message)
    print(Web3.keccak(base64_msg).hex())
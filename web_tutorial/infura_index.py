import requests
import json


def main():
    INFURA_SECRET_KEY = '1087dd0fa0144dea8afb89667be1645d'

    url = f'https://mainnet.infura.io/v3/{INFURA_SECRET_KEY}'


    payload = {
        "jsonrpc": "2.0",
        "method": "eth_blockNumber",
        "params": [],
        "id": 1
    }

    headers = {'content-type': 'application/json'}

    response = requests.post(url, data=json.dumps(payload), headers=headers).json()

    print(response)

if __name__ == "__main__":
    main()

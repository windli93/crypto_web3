from binance.client import Client
import time

if __name__ == '__main__':
    binance_api_key = 'XjlpeieiKFsZRSI6fx6b2HaZnEKVw4G60ChlNHNXAGfuZ6ZCOorjtD3h0fDwawrD'
    binance_api_secret = 'vylvXIYqWe4tMoaTftSIb37wX3XGvF7sqqsxMAeTl9MCMv4RodwZ2PvPuWDtpPhq'
    # 实例化Binance
    client = Client(binance_api_key,
                    binance_api_secret)
    # spot表示现货 get_ticker_bookTicker获取最优挂单价格
    while True:
        try:
            info = client.get_account()
            print(info)
        except  Exception as e:
            print(e)
        print('Something went wrong. Error occured at %s. Wait for 1 hour.')
        time.sleep(3600)
        client = Client(binance_api_key, binance_api_secret)
        continue

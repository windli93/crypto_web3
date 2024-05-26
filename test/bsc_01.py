from pbinance import Binance
from pprint import pprint

if __name__ == '__main__':
    # 实例化Binance
    # 如果仅获取行情信息不需要key和secret，与账户交易相关的功能需要填写key和secret
    binance = Binance(
        key='XjlpeieiKFsZRSI6fx6b2HaZnEKVw4G60ChlNHNXAGfuZ6ZCOorjtD3h0fDwawrD',
        secret='vylvXIYqWe4tMoaTftSIb37wX3XGvF7sqqsxMAeTl9MCMv4RodwZ2PvPuWDtpPhq',
    )
    # spot表示现货 get_ticker_bookTicker获取最优挂单价格
    result = binance.spot.market.get_ticker_bookTicker(
        symbol='BTCUSDT'
    )
    pprint(result)

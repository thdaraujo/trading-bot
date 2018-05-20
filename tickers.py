# -*- coding: utf-8 -*-

import asyncio
import ccxt.async as ccxt


async def poll(tickers):
    i = 0
    kraken = ccxt.kraken()
    while True:
        symbol = tickers[i % len(tickers)]
        yield (symbol, await kraken.fetch_ticker(symbol))
        i += 1
        await asyncio.sleep(kraken.rateLimit / 1000)


async def main():
    tickers = [
      'BCH/BTC',
      'DASH/BTC',
      'ETC/BTC',
      'ETC/ETH',
      'ETH/BTC',
      'GNO/BTC',
      'GNO/ETH',
      'LTC/BTC',
      'REP/BTC',
      'REP/ETH',
      'XLM/BTC',
      'XMR/BTC',
      'XRP/BTC',
      'ZEC/BTC'
    ]

    async for (symbol, ticker) in poll(tickers):
        print(symbol, ticker['bid'])


asyncio.get_event_loop().run_until_complete(main())

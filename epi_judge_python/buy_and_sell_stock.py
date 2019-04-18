from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    minpx = float('inf')
    maxprofit = 0.0
    for px in prices:
        if px < minpx:
            minpx = px
        else:
            if px - minpx > maxprofit:
                maxprofit = px - minpx
    return maxprofit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))

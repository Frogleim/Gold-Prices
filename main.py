import time

from core import save_prices


def start_process():
    while True:
        res = save_prices.get_prices_api()
        print(res)
        save_prices.save_orders_data(res)
        time.sleep(10)


if __name__ == "__main__":
    start_process()
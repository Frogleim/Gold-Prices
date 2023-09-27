import time

from core import save_prices


def start_process():
    file_path = './core/keys/siranyan-1234fa5ac08f.json'

    while True:
        res = save_prices.get_prices_api()
        print(res)
        save_prices.save_orders_data(res, file_path)
        time.sleep(10)


if __name__ == "__main__":
    start_process()

import csv
import logging
import sys
import datetime


def csv_dict_reader():
    with open("data.csv") as f_obj:
        reader = csv.DictReader(f_obj, delimiter=',')
        for line in reader:
            yield line


def extract_trade_data(content):
    current_exchange = content["exchange"]
    (dt, mSecs) = content["time"].split(".")
    dt = datetime.datetime.strptime(dt, "%H:%M:%S")
    mseconds = datetime.timedelta(milliseconds=int(mSecs))
    trade_time = dt + mseconds
    return current_exchange, trade_time


def update_trade_table(trade_table, current_exchange, trade_time):
    if not trade_table.get(current_exchange):
        trade_table[current_exchange] = {trade_time: 1}
    else:
        timing = trade_table[current_exchange]
        for key, value in timing.items():
            delta = trade_time - key
            minute = datetime.timedelta(minutes=1)
            if delta.total_seconds() < 0:
                break
            if delta < minute:
                timing[key] += 1

        if trade_time not in timing:
            timing[trade_time] = 1


def main():
    logging.basicConfig(format='[%(asctime)s] %(levelname).1s %(message)s', level=logging.DEBUG, filename='tLog.log')
    trade_table = dict()
    try:
        for content in csv_dict_reader():
            current_exchange, trade_time = extract_trade_data(content)
            update_trade_table(trade_table, current_exchange, trade_time)
    except KeyError:
        logging.error("Broken content")

    logging.info("Result tradetable is {}".format(trade_table))
    exchange_names = list(trade_table.keys())
    exchange_names.sort()
    for exchange in exchange_names:
        max_val = max(trade_table[exchange].values())
        logging.info("The largest number of trade {} is equal {}".format(exchange, max_val))
        print(max_val)


if __name__ == "__main__":
    try:
        main()
    except:
        logging.exception(sys.exc_info()[0])

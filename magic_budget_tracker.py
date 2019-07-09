import json
import sys
import scrython
import pandas as pd
import argparse as ap


def file_load(budget_file, card_config):
    """
    this function loads the csv file and json config of cards.
    :param budget_file: (string) path to .csv file
    :param card_config: (string) path to .json config file
    :return:
    """
    data = pd.read_csv(budget_file)
    assert "Saving" in data.columns, f"{data.columns} missing column named Saving"

    total_savings = sum(data.Saving)

    with open(card_config) as f:
        card_file = json.load(f)

    return total_savings, card_file


def get_card_prices(card_file):
    """
    this function uses the scrython library to get prices from listed cards
    :param card_file:
    :return:
    """
    card_prices = {}
    for card in card_file:
        card_data = scrython.cards.Named(fuzzy=card)
        price = card_data.scryfallJson["prices"]["usd"]
        card_prices[card] = float(price)

    return card_prices


def total_value_calcs(card_prices, card_file):
    """
    this function takes card prices and the card quantities and returns a total value of each item
    :param card_prices:
    :param card_file:
    :return:
    """
    total_value_list = []
    for key, val in card_prices.items():
        quantity = card_file[key]["Quantity"]
        total = round(quantity * val, 2)
        total_value_list.append(total)

    return total_value_list


def goal_status(budget_file, card_config):
    """
    This returns how close to the total value of the cards in card_config based on savings in budget file
    :param budget_file: (string) path to .csv file
    :param card_config: (string) path to .json config file
    :return: print statement
    """

    total_savings, card_file = file_load(budget_file, card_config)
    card_prices = get_card_prices(card_file)
    total_value_list = total_value_calcs(card_prices, card_file)

    total_value = sum(total_value_list)

    percent = total_savings / total_value
    percent_pretty = "{0:.0f}%".format(percent * 100)

    return (
        f"You are {percent_pretty} of the way to your goal! Card Prices: {card_prices} "
        f"and Total Cost: ${round(total_value,2)} "
        f"and Total Saving: ${round(total_savings, 2)}"
    )


def initialize_parser():
    """ Initialize argparser
    """

    argparser = ap.ArgumentParser(
        description="""provide event dictionary for manual run"""
    )
    argparser.add_argument(
        "-budget_file",
        type=str,
        help="path to .csv with savings, needs a col named Saving",
    )
    argparser.add_argument(
        "-card_config",
        type=str,
        help="path to .json with config for card names and quantity",
    )

    return argparser


def main():
    p = initialize_parser()
    args = p.parse_args()

    file = args.budget_file
    config = args.card_config

    output = goal_status(budget_file=file, card_config=config)

    sys.stdout.write(output)


if __name__ == "__main__":
    main()

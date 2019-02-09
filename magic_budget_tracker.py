import pandas as pd
import json
import requests


def goal_status(budget_file, card_config):
    """
    This returns how close to the total value of the cards in card_config based on savings in budget file
    :param budget_file: (string) path to .csv file
    :param card_config: (string) path to .json config file
    :return: print statement
    """

    data = pd.read_csv(budget_file)




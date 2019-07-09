import magic_budget_tracker


def test_file_load():
    """
    this tests the functionality of file_load by checking the sum of savings and the json reader
    :return:
    """
    fake_data_path = "/Users/alex.knorr/PycharmProjects/magic_budget_tracker/tests/fake_csv.csv"
    fake_card_json = "/Users/alex.knorr/PycharmProjects/magic_budget_tracker/tests/fake_card_file.json"
    savings, card_file = magic_budget_tracker.file_load(fake_data_path, fake_card_json)

    assert savings == 20, f"Failed!, savings = {savings}, not 10!"
    assert type(card_file) is dict, f"Failed!, card_file is type {type(card_file)}, not dict!"


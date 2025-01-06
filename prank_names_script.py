# coding: utf-8
"""
This program generates random funny names inspired by Bart Simpson's prank
calls to Moe's Bar in The Simpsons.
It retrieves prank call names from SimpsonsWiki, processes them into first and
last name lists using dataframes,
and allows the user to generate new names by randomly selecting from the lists.
The user can continue generating names until they choose to quit.
"""

import random  # for retrieving a random value from a list
import sys #for exit
import requests  # for requesting a webpage
import pandas as pd  # for dataframes which manipulate tables
from requests import RequestException


def request_webpage(url):
    """
    This function is for requesting the content of a webpage at location url
    """
    try:
        response = requests.get(url, timeout=10)
        # Raise any exceptions
        response.raise_for_status()
        return response
    except RequestException as e:
        print(f"Error {e} during web page retrieval")
        return None


def process_tables(response):
    """
    This function processes the response document
    into two lists of first and last names
    """
    # Get the tables from the html document returned
    df = pd.read_html(response.content)
    # Unpack the dataframe to two first tables
    table1, table2, *tables = df
    del tables
    if not table1 or not table2:
        return None
    # Separate the name column from other episode data columns
    table1 = table1.iloc[1:, 1:2]
    table2 = table2.iloc[1:, 1:2]
    # Drop non-name rows
    table1 = table1.drop(28)
    table1 = table1.drop(32)
    table1 = table1.drop(34)
    table1 = table1.drop(13)
    table1 = table1.dropna(how="all")
    # Split first columns into two additional columns by space as delimiter,
    # with descriptors first and last names
    table1[["first", "last"]] = table1.iloc[:, 0].str.split(
        " ", n=1, expand=True
    )
    table2[["first", "last"]] = table2.iloc[:, 0].str.split(
        " ", n=1, expand=True
    )
    # Process the name columns into two lists of first and last names
    first_names = table1["first"].tolist() + table2["first"].tolist()
    last_names = table1["last"].tolist() + table2["last"].tolist()
    return first_names, last_names


def main():
    """The main process loop for generating names"""
    url = "https://simpsons.fandom.com/wiki/Bart%27s_prank_calls"
    response = request_webpage(url)

    if response is None:
        sys.exit()

    first_names, last_names = process_tables(response)

    if not first_names or last_names:
        sys.exit()

    print(
        "Welcome to generating amusing names in the style of prank calls "
        "made by Bart Simpson on the classic show The Simpsons!"
    )
    while True:
        user_input = str(
            input("Press Enter to generate a name or press q to exit:  ")
        )
        if user_input.lower() == "q":
            break
        new_first_name = random.choice(first_names)
        new_last_name = random.choice(last_names)
        print(f"{new_first_name} {new_last_name}")


if __name__ == "__main__":
    main()

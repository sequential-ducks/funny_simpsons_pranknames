# coding: utf-8
"""
This program generates random funny names inspired by Bart Simpson's prank
calls to Moe's Bar in The Simpsons.
It retrieves prank call names from SimpsonsWiki, processes them into first and
last name lists using dataframes,
and allows the user to generate new names by randomly selecting from the lists.
The user can continue generating names until they choose to quit.
No AI was used in the development.
"""

import random  # for retrieving a random value from a list
import sys  # for exit
from typing import Optional  # Optional type hint

import requests  # for requesting a webpage
import pandas as pd  # for dataframes which manipulate tables
from requests import Response  # Response type hint


def get_request(url: str) -> Optional[Response]:
    """
    Request the content of a webpage at location url

    :param
        url (str): The website address to make a get request to

    :return
        Server esponse if no errors occurred otherwise None

    ------------- Examples ----------------------

    Request is successful:
        >>> get_request("https://www.python.org/")
        <Response [200]>

    Incorrect url schema:
        >>> get_request('notanurl')
        Missing schema: include http or https

    Address is not found:
        >>> get_request('https://www.google.com/404')
        HTTP Error

    Website timeout:
        >>> get_request('https://10.255.255.1/')
        Timed out
    """

    try:
        response = requests.get(url, timeout=10)
        # Raise any exceptions
        response.raise_for_status()
    except requests.exceptions.ReadTimeout:
        print('Timed out')
        return None
    except requests.exceptions.MissingSchema:
        print('Missing schema: include http or https')
        return None
    except requests.exceptions.ConnectionError:
        print('Connection error')
        return None
    except requests.exceptions.HTTPError:
        print('HTTP Error')
        return None
    else:
        # Response is OK
        return response


def process_response_to_df_tables(r: requests.models.Response) \
                                                        -> (pd.DataFrame
                                                        | list[pd.DataFrame]
                                                        | None):
    """
    Extract html tables from a request into one pandas' dataframe

    :param r:
        Response object returned by a web request
    :return
        Dataframe object containing all tables of a html document, if page
        contains more than one it is a list of dataframe objects
    """

    try:
        assert type(r) == requests.models.Response
    except AssertionError:
        print("Invalid argument to function 'process_response_to_df_tables'")
        return None

    if not r.text.find('<table>'):
        print('Response contains no tables to process')
        return None

    df = pd.read_html(r.content)
    return df


def process_tables(table1 : pd.DataFrame, table2 : pd.DataFrame):
    """
    This function processes the response document
    into two lists of first and last names
    """

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
    table1[["first", "last"]] = table1.iloc[:, 0].str.split(" ", n=1,
        expand=True)
    table2[["first", "last"]] = table2.iloc[:, 0].str.split(" ", n=1,
        expand=True)
    # Process the name columns into two lists of first and last names
    first_names = table1["first"].tolist() + table2["first"].tolist()
    last_names = table1["last"].tolist() + table2["last"].tolist()
    return first_names, last_names


def random_combine_string_lists(a: Optional[list[str]] = None,
                                b: Optional[list[str]] = None) \
                                -> Optional[str]:
    """
    :param a:
    :param b:
    :return:
    """
    if a is None or b is None:
        return None

    ab_random_string = f'{random.choice(a)} {random.choice(b)}'
    return ab_random_string


def main():
    """The main process loop for generating names"""
    url = "https://simpsons.fandom.com/wiki/Bart%27s_prank_calls"
    response = get_request(url)

    if response is None:
        sys.exit()

    df = process_response_to_df_tables(response)
    table1 = df[0]
    table2 = df[1]
    list_of_first_names, list_of_last_names = process_tables(table1, table2)

    if not list_of_first_names or not list_of_last_names:
        sys.exit()

    print("\nWelcome to generating amusing names in the style of prank calls "
          "made by Bart Simpson on the classic show The Simpsons!")
    while True:
        user_input = str(
            input("\nPress Enter to generate a name or press q to exit:  "))
        if user_input.lower() == "q":
            return
        new_name = random_combine_string_lists(list_of_first_names,
                                               list_of_last_names)
        print(f'{new_name}')


if __name__ == "__main__":
    main()

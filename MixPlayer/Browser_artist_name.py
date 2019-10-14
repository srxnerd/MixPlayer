#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from inscriptis import get_text
import sys
import argparse

parser_get = argparse.ArgumentParser()
parser_get.add_argument("get_name", type=str, help=" get name artists with char")
args = parser_get.parse_args()


def Browser_artist():
    browser_artist_char = args.get_name
    url_radio_javan = "https://www.radiojavan.com/mp3s/browse/artists/"+browser_artist_char
    url_Browsers = requests.get(url_radio_javan).text
    soup = BeautifulSoup(url_Browsers, "lxml")
    data_Browser = soup.find_all("span", class_="artist")
    for item_browser in data_Browser:
        get_txt = get_text(str(item_browser))
        print(get_txt)

# def main():
    # Browser_artist():
# if __name__ == "__main__":
    # main()
import os
import requests
import urllib
import argparse
from dotenv import load_dotenv


def parse_command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument('long_url', help='Original link')
    args = parser.parse_args()
    long_url = args.long_url
    return long_url


def shorten_link(long_url, headers):
    long_url_data = {"long_url": long_url}
    response = requests.post(
        f'https://api-ssl.bitly.com/v4/shorten',
        headers=headers,
        json=long_url_data
    )
    response.raise_for_status()
    response_data = response.json()
    shorten_link = response_data.get('link')
    return shorten_link


def count_click(headers, bitlink):
    parts_of_bitlink = urllib.parse.urlsplit(bitlink)
    bitlink_for_response = f'{parts_of_bitlink.netloc}{parts_of_bitlink.path}'
    response = requests.get(
        f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink_for_response}'
        f'/clicks/summary', headers=headers
    )
    response.raise_for_status()
    response_data = response.json()
    total_clicks = response_data.get('total_clicks')
    return total_clicks


def check_link(headers, long_url):
    parts_of_bitlink = urllib.parse.urlsplit(long_url)
    bitlink_for_response = f'{parts_of_bitlink.netloc}{parts_of_bitlink.path}'
    response = requests.get(
        f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink_for_response}',
        headers=headers
    )
    return response.ok


if __name__ == '__main__':
    load_dotenv()
    token = os.getenv('GENERIC_ACCESS_TOKEN')
    authorization = {'Authorization': f'Bearer {token}'}
    long_url = parse_command_line()
    check = check_link(authorization, long_url)
    if check:
        try:
            clicks_count = count_click(authorization, long_url)
            print('Bitlinks clicks count : ', clicks_count)
        except requests.exceptions.HTTPError:
            print('Incorrect link inputed. Please restart script')
    else:
        try:
            bitlink = shorten_link(long_url, authorization)
            print('Bitlink : ', bitlink)
        except requests.exceptions.HTTPError:
            print('Incorrect link inputed. Please restart script')

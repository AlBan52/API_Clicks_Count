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
    payload = {'long_url': long_url}
    response = requests.post(
        f'https://api-ssl.bitly.com/v4/shorten',
        headers=headers,
        json=payload
    )
    response.raise_for_status()
    response_data = response.json()
    shorten_link = response_data.get('link')
    return shorten_link


def count_click(headers, raw_bitlink):
    parts_of_bitlink = urllib.parse.urlsplit(raw_bitlink)
    bitlink = f'{parts_of_bitlink.netloc}{parts_of_bitlink.path}'
    link = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    response = requests.get(link, headers=headers)
    response.raise_for_status()
    response_data = response.json()
    total_clicks = response_data.get('total_clicks')
    return total_clicks


def check_link(headers, long_url):
    parts_of_bitlink = urllib.parse.urlsplit(long_url)
    bitlink = f'{parts_of_bitlink.netloc}{parts_of_bitlink.path}'
    response = requests.get(
        f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}',
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
#   add the exception block for possible mistake of shorten link input
    else:
        try:
            raw_bitlink = shorten_link(long_url, authorization)
            print('Bitlink : ', raw_bitlink)
        except requests.exceptions.HTTPError:
            print('Incorrect link inputed. Please restart script')

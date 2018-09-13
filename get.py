#!/usr/bin/env nix-shell
#!nix-shell -i python -p python3 python3Packages.requests

"""
Kattis CLI plus :: get.py

Create new directory for a problem and download sample input file
"""

# TODO: use argparse
# TODO: use logging

from sys import argv
from os import path, mkdir, chdir

from requests import get  # to make GET request

prob_id = None

def print_usage():
    print(f"usage: {argv[0]!s} <problem_id>")
    print(f"example: {argv[0]!s} hello")

def main():
    global prob_id

    if len(argv) < 2:
        print_usage()
        exit()
    else:
        prob_id = argv[1]
        print(f"Problem ID: {prob_id!s}")

    url = f"https://open.kattis.com/problems/{prob_id!s}"
    if get(url).status_code != 200:
        print(f"Problem not exists on kattis website, please check again {url}")
        exit()

    # TODO: check if problemid is valid before create new directory
    if path.exists(prob_id):
        print("problem id : {prob_id} is already exists")
    else:
        mkdir(prob_id)
        print("created {prob_id!s}")

    chdir(prob_id)
    fetch_input()


def fetch_input():
    url = f"https://open.kattis.com/problems/{prob_id!s}/file/statement/samples.zip"
    print("downloading sample input...")
    print(url)
    download(url,"samples.zip")


def download(url, file_name):
    # get request
    response = get(url)
    if response.status_code == 200:
        # open in binary mode
        with open(file_name, "wb") as file:
            file.write(response.content)
    else:
        print(f"Warning {response.status_code!s}: downloading {url!s}")

    print("Done")

if __name__ == "__main__":
    main()

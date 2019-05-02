import argparse
import json

def get_arguments():
    # считывание консольных аргументов
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, nargs=1, help="input file path")
    parser.add_argument('--output', type=str, nargs=1, help="output file path")
    parser.add_argument('--seed', type=str, nargs=1, help="seed for random generation")
    parser.add_argument('--debug', type=str, nargs=1, help="developer mode")
    args = parser.parse_args()
    return args

cur_scen = "Beginning.sc"
HP = 20
MP = 100
ST = 50
while True:
    with open(cur_scen, 'r') as event:
        description, options = json.load(event)
        print("-"*10)
        print(description)
        print("-"*10)
        for option in options:
            print("-", option)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("what will you do?")
        while True:
            ans = input()
            try:
                cur_scen = options[ans]
                break
            except KeyError:
                print("invalid choice")


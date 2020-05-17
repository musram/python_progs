#!/home/msr/anaconda3/bin/python3

import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Say Hello')
    parser.add_argument('name', help='Name to great')
    args = parser.parse_args()

def main():
    args = get_args()
    print('Hello' + args.name + "!")


if __name__ == "__main__":
    main()



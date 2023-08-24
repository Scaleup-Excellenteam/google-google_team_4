import argparse
import re


def one_space(user_input):
    return re.sub(' +', ' ', user_input)


class CLI:
    def __init__(self):
        self.user_str = ""

    def print_user_input(self):
        print("\r" + self.user_str, end="", flush=True)

    def cli(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("input_text", nargs="*")

        args = parser.parse_args()
        self.user_str = " ".join(args.input_text)

        #print("Loading the files and preparing the system...")
        #load data

        print("The system is ready. Enter your text:")
        self.print_user_input()

        while True:
            user_input = input()
            user_one_space = one_space(user_input)

            # Calculate 5 best suggestions

            #print("Here are 5 suggestions")

            self.user_str += user_one_space
            self.print_user_input()

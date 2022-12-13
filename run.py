import os
import sys
import webbrowser
from datetime import date

length_of_arguments = len(sys.argv)
key_word = str(sys.argv[1])


def error():
    print('\033[1;31m' + 'Error.' + '\x1b[0m')
    sys.exit()


def success():
    print('\x1b[6;30;42m' + 'Files were created' + '\x1b[0m')
    sys.exit()


def new_day():
    today = date.today()
    d3 = today.strftime("%d/%m/%y")
    day = d3[0:2]

    input_dir = f"C:/Users/Dhava/Documents/AdventOfCode/Inputs/Day {day}"
    solution_dir = f"C:/Users/Dhava/Documents/AdventOfCode/Solutions/Day {day}"
    os.mkdir(input_dir)
    os.mkdir(solution_dir)

    file_name = f".\Solutions\Day {day}\Day{day}.py"
    input_sample_name = f".\Inputs\Day {day}\Day{day}SampleInput.txt"
    input_name = f".\Inputs\Day {day}\Day{day}Input.txt"

    code = open(file_name, "x")
    sample = open(input_sample_name, "x")
    input = open(input_name, "x")

    code.write(f'with open("{input_sample_name}", "r") as f:')
    code.write(f'\n\n')
    code.write(f'    input_file = f.read().strip().split("")')

    code.write(f'\n\n')
    code.write(f'def main():')

    code.write(f'\n\n')
    code.write(f'main()')

    success()


if key_word == "new":
    new_day()

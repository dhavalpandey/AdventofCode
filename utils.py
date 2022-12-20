import os
import sys
from datetime import date

length_of_arguments = len(sys.argv)
key_word = str(sys.argv[1])

today = date.today()
d3 = today.strftime("%d/%m/%y")


def error():
    print('\033[1;31m' + 'Error.' + '\x1b[0m')
    sys.exit()


def success():
    print('\x1b[6;30;42m' + 'Task executed correctly.' + '\x1b[0m')
    sys.exit()


def push(day=d3[0:2]):
    try:
        commit_message = 'Day ' + day + ' complete'

        os.system("git add .")
        os.system(f'git commit -m {day}')
        os.system("git push origin main")

        success()

    except:
        error()


def new_day(day=d3[0:2], lang="py"):
        dir = f"./{today.year}/Day {day}"
        os.mkdir(dir)

        solution1_name = f"./{today.year}/Day {day}/solutionA.{lang}"
        solution2_name = f"./{today.year}/Day {day}/solutionB.{lang}"
        sample_name = f"./{today.year}/Day {day}/sample.in"
        input_name = f"./{today.year}/Day {day}/input.in"

        solution1 = open(solution1_name, mode='x')
        solution2 = open(solution2_name, mode='x')
        sample = open(sample_name, mode='x')
        input = open(input_name, mode='x')

        template = open(f'./template.{lang}', mode='rt')
        template2 = open(f'./template.{lang}', mode='rt')

        solution1.write(template.read())
        solution2.write(template2.read())
        solution1.close()
        solution2.close()
        template.close()
        template2.close()
        sample.close()
        input.close()

        success()


if key_word == "new":
    if len(sys.argv) == 4:
        new_day(str(sys.argv[2]), str(sys.argv[3]))
    elif len(sys.argv) == 3:
        new_day(str(sys.argv[2]))
    else:
        new_day()
elif key_word == "push":
    if len(sys.argv) == 3:
        push(str(sys.argv[2]))
    else:
        push()


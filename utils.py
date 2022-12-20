import os
import sys
from datetime import date
import requests

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
    os.system("git add .")
    os.system(f'git commit -m "Day {day} complete"')
    os.system("git push origin main")

    success()


def fetch_input(day):
    url = f"https://adventofcode.com/2022/day/{day}/input"

    payload={}
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'cookie': '_ga=GA1.2.1526790196.1671441103; _gid=GA1.2.149920977.1671441103; session=53616c7465645f5fa021ae2350a194887c0731d96b9ab1f81e920c0bbe7c1b77e979f9e49c2105556fd5b66549a650edab23834a137f21049a8b85254d0dc163',
    'referer': 'https://adventofcode.com/2022/day/16',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text


def new_day(day=d3[0:2], lang="py"):
    dir = f"./{today.year}/Day{day}"
    os.mkdir(dir)

    solution1_name = f"./{today.year}/Day{day}/solutionA.{lang}"
    solution2_name = f"./{today.year}/Day{day}/solutionB.{lang}"
    sample_name = f"./{today.year}/Day{day}/sample.in"
    input_name = f"./{today.year}/Day{day}/input.in"

    solution1 = open(solution1_name, mode='x')
    solution2 = open(solution2_name, mode='x')
    sample = open(sample_name, mode='x')
    input = open(input_name, mode='x')

    template = open(f'./template.{lang}', mode='rt')
    template2 = open(f'./template.{lang}', mode='rt')

    solution1.write(template.read())
    solution2.write(template2.read())

    input_txt = fetch_input(day)
    input.write(input_txt)

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
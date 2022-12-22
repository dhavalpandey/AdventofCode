import os
import sys
from datetime import date

length_of_arguments = len(sys.argv)
today = date.today()
d3 = today.strftime("%d/%m/%y")


def compile(day=d3[0:2], files="AB"):
    os.chdir(f'./{today.year}/Day{day}/')

    if files == "A":
        os.system(f'python3 solutionA.py')
    elif files == "B":
        os.system(f'python3 solutionB.py')
    else:
        os.system(f'python3 solutionA.py')
        os.system(f'python3 solutionB.py')

if length_of_arguments == 3:
    compile(str(sys.argv[1]), str(sys.argv[2]))
elif length_of_arguments == 2:
    if str(sys.argv[1]) == "A":
        compile(d3[0:2], str(sys.argv[1]))
    elif str(sys.argv[1]) == "B":
        compile(d3[0:2], str(sys.argv[1]))
    else:
        compile(str(sys.argv[1]))
else:
    compile()

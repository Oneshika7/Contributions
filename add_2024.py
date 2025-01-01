import os
from datetime import datetime, timedelta
from random import randint
from subprocess import Popen

def run(commands):
    Popen(commands).wait()

def message(date):
    return date.strftime('Contribution: %Y-%m-%d %H:%M')

def contribute(date):
    with open('README.md', 'a') as file:
        file.write(message(date) + '\n\n')
    run(['git', 'add', '.'])
    run(['git', 'commit', '-m', '"%s"' % message(date),
         '--date', date.strftime('"%Y-%m-%d %H:%M:%S"')])

def main():
    frequency = 28 # roughly twice a week (2/7 = 28%)
    max_c = 2

    # Year 2024
    start_date = datetime(2024, 1, 1, 20, 0)
    days_in_2024 = 366

    for n in range(days_in_2024):
        day = start_date + timedelta(days=n)
        if randint(0, 100) < frequency:
            # 1 or 2 commits per active day
            for m in range(randint(1, max_c)):
                commit_time = day + timedelta(minutes=m)
                contribute(commit_time)

if __name__ == '__main__':
    main()

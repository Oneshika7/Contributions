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
    frequency = 57 # roughly 4 times a week (4/7 = 57%)
    max_c = 8

    start_date = datetime(2025, 1, 1, 20, 0)
    end_date = datetime.now().replace(hour=20, minute=0, second=0, microsecond=0)
    days_diff = (end_date - start_date).days

    if days_diff < 0:
        return

    for n in range(days_diff + 1):
        day = start_date + timedelta(days=n)
        if randint(0, 100) < frequency:
            # 1 to max_c commits per active day
            for m in range(randint(1, max_c)):
                commit_time = day + timedelta(minutes=m)
                contribute(commit_time)

if __name__ == '__main__':
    main()

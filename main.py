from datetime import timedelta, date
import os
import random as rd


def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)


def MakeCommits(dirs, dates):
    for directory in dirs:
        os.chdir(directory)
        os.system("git init")
        for cdate in daterange(dates[0], dates[1]):
            for i in xrange(rd.randint(0,9)):
                with open("readme.txt", "w") as f:
                    f.write(str(rd.randint(0,9)))
                os.system('git add readme.txt')
                os.system('git commit -m "piece" --date="' + cdate.isoformat() + 'T00:00:00+0300"')
        os.chdir("..")


def PushAll(dirs):
    for d in dirs:
        os.chdir(d)
        os.system("git remote add origin " + dirs[d])
        os.system("git push -u origin master")
        os.chdir("..")


def main(dirs, dates):
    MakeCommits(dirs, dates)
    PushAll(dirs)


if __name__ == "__main__":
    main({'github_auto_commiter':'https://github.com/alexbod/github-auto-committer.git'},
         (date(2017,2,23), date(2017,2,25)))

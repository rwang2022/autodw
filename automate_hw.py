# if you don't have these, just paste this command into terminal: 
# pip install pyperclip keyboard pause datetime getpass
import pyperclip, keyboard, pause, datetime, getpass
import subprocess, time, sys

# asdf = sys.argv[0]
# asdf = sys.argv[1]
# asdf = sys.argv[2]
# asdf = sys.argv[3]

# change these variables to suit yourself
gituser = "rwang2022"
last3first = "WangRya"
pd = 4
passwd = getpass.getpass("Please type your password here: ")

print("-" * 100)
print("to use this program first:")
print("\tsubmit the work to github as a repo (may be automated later)\n")
print("\tthen this program will take care of it")
print("-" * 100)

workNum = int(input("what is the work #? (e.g. work10, 10 is the work #)\n"))
dwName = (input("what is the dw name? (e.g. 10_list, list is the dw name)\n"))

own_repo = f"work{workNum}"
dw_repo = f"{workNum}_{dwName}"

# override the inputs (if repo names are unusual, e.g. for projects)
override = input(f"\ndo you want to override the values \nown_repo: {own_repo} \ndw_repo: {dw_repo}\n(y/n)\n").strip().lower()[0] == "y"
while override:
    own_repo = input("own_repo: ")
    dw_repo = input("dw_repo: ")
    override = input(f"\ndo you want to override the values \nown_repo: {own_repo} \ndw_repo: {dw_repo}\n(y/n)\n").strip().lower()[0] == "y"

print()
print(f"showing own_repo: {own_repo}")
print(f"showing dw_repo: {dw_repo}")

str1 = ""
str1 += (f"git clone git@github.com:{gituser}/{own_repo}; ")
str1 += (f"git clone git@github.com:mks65/{dw_repo}; ")
str1 += (f"cd {dw_repo}/{pd}; ")
str1 += (f"git submodule add -b main git@github.com:{gituser}/{own_repo} {last3first}; ")
str1 += (f"git pull; ")
str1 += (f"git commit -a -m \"added {last3first} submodule\" ; ")
str1 += (f"git push;")
# pyperclip.copy(str1)

print("-" * 100)
print(f"\nThe following commands has been saved to str1\n")
# print(f"(though if it has failed, you can simply copy it manually)\n")
print(f"\t{str1}\n")

# submitting the work to DW
# scheduling if user wants
if input("do u wanna schedule this submission? (y/n): \n(if 'y' then you will schedule a timer)\n(if 'n' then you will submit right now)\n").strip().lower()[0] == "y":
    # # this will let u schedule exactly when, but I think the "timer" one is more common/useful
    # print()
    # yr  = int(input("give me year  ('2021'): "))
    # mon = int(input("give me month ('1-12'): "))
    # day = int(input("give me day   ('1-31'): "))
    # hr  = int(input("give me hour  ('0-23'): "))
    # mnt = int(input("give me min   ('0-59'): "))
    # sec = int(input("give me sec   ('0-59'): "))
    # end_time = (datetime.datetime(yr, mon, day, hr, mnt, sec))
    
    print()
    hr  = int(input("give me hour from now ('0-23'): "))
    mnt = int(input("give me min  from now ('0-59'): "))
    sec = int(input("give me sec  from now ('0-59'): "))
    time_change = datetime.timedelta(hours=hr, minutes=mnt, seconds=sec)
    end_time = datetime.datetime.now() + time_change
    print()

    # https://stackoverflow.com/a/51037735 updating print statement??
    print(f"end_time: {end_time}")
    while datetime.datetime.now() != end_time:
        time_left = end_time - datetime.datetime.now()
        print(f"countdown: {time_left}\r", end="", flush=True)
        sys.stdout.flush()

# it is very important that shell=True (?)
# https://stackoverflow.com/a/19257995
subprocess.Popen("wsl.exe ssh 149.89.150.101", shell=True)
time.sleep(3)

cmd_list = \
    [
        passwd,   # enter pass exit
        str1,     # run commands
        "exit"    # exit wsl
        "exit"    # exit terminal
    ]

for cmd in cmd_list:
    time.sleep(3)
    keyboard.write(cmd)
    keyboard.send("enter")
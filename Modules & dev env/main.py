
# Modules
import os

cwd = os.getcwd()

print("Current working directory:", cwd)


def PWD():
    return os.getcwd()


os.chdir(f'{PWD()}/testFolder')
print("Current working directory:", PWD())


def ch_dir_safe(dir1):
    try:
        os.chdir(f'{PWD()}/{dir1}')
    except FileNotFoundError:
        print("FileNotFoundError: creating file")
        os.mkdir(f'{PWD()}/{dir1}')
        os.chdir(f'{PWD()}/{dir1}')
        print("File created and directory changed")


os.chdir('../')
ch_dir_safe('testFolder2')
os.chdir('../')
print("Files and dirs in", PWD(), ":")
print(os.listdir(PWD()))

# os.remove("file")  # Can only remove files, not directories
# os.rmdir("dir")  # Will remove directories

# Create 10 test file
ch_dir_safe('testFolder')
for _ in range(10):
    with open(f'file{_}.txt', 'w'):
        pass

for _ in range(3):
    try:  # Dirs may already exist
        os.mkdir(f'dir{_}')
    except FileExistsError:
        pass


os.remove('file0.txt')  # Will work
# os.remove('dir0')  # Will not work, because it is a directory
print(os.path.exists('dir0'))
os.rmdir('dir0')  # Will work
print(os.path.exists('dir0'))
# print(os.path.getsize('file1.txt'))  # Returns size in bytes
# os.rename('file9.txt', 'file10.txt')  # rename() works on directories and files
# os.rename('dir2', 'dir20')


import sys

# while True:
#     i = input()
#     print(i)
#     if i == 'q':
#         break
# print('Exit')
#
# for line in sys.stdin:
#     if 'q' == line.rstrip():
#         break
#     print(f'Input : {line}')
# print("Exit")


def my_print(output):
    sys.stdout.write(str(output)+'\n')


my_print(123)
print(123)
print(sys.modules)


import random

randomList = ['asd', (1, 'a'), 578, {'test': 123}]
print(random.randrange(0, 100, 10))  # int, step not needed
print(random.randint(0, 100))  # int
print(random.uniform(0, 100))  # float, range
print(random.choice(randomList))  # whatever, in given element
print(random.choice(randomList[1]))  # whatever, in list, in given element
print(random.random())  # float, 0 - 1


def roll_die(die_amount, dice_range):
    roll = []
    for _ in range(die_amount):
        roll.append(random.randint(1, dice_range))
    return roll


print(roll_die(random.randint(1, 3), random.randint(1, 100)))


import my_module as mm

pi_timed = mm.time_me(mm.estimate_pi)

print(pi_timed(100))
print(pi_timed(1000))
print(pi_timed(10000))

"""
This file integrates the text-to-speech module of Deep Speaking Avatar with rest of the project
"""
from watchdog.observers import Observer


##### Integration definitions
READLOCATION = "./files/in.txt"
WRITELOCATION = "./files/out.txt"



"""
Read input file and convert data to
right form.
"""
def read_file():
    f = open(READLOCATION, "r")
    lines = f.readlines()
    return lines


"""
Write sounddata to file for next module to use.
"""
def write_file(data):
    f = open(WRITELOCATION, "w")
    f.writelines(data)
    f.close()
    return


def parse_file(data):
    approvedCharacters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',' k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

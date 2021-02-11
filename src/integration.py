"""
This file integrates the text-to-speech module of Deep Speaking Avatar with rest of the project
"""
import string
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
    f = open(READLOCATION, "w")
    f.writelines(data)
    f.close()
    return


def parse_line(line):
    approvedCharacters = string.ascii_uppercase + string.ascii_lowercase + " " + "."
    returnString = ""
    for char in line:
        if char in approvedCharacters:
            returnString+=str(char)
    return returnString


def check_file():
    lines = read_file()
    print("Lines", lines)
    if (len(lines) < 1):
        return []
    parsed_lines = []
    for line in lines:
        parsed_lines.append(parse_line(line))

    ## Clear the file
##    write_file("")
    return parsed_lines

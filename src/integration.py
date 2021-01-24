"""
This file integrates the text-to-speech module of Deep Speaking Avatar with rest of the project
"""

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

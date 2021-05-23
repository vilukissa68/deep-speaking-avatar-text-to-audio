"""
This file integrates the text-to-speech module of Deep Speaking Avatar with rest of the project
"""
import string
import os.path
import re
import soundfile as sf


"""
Read input file and convert data to
right form.
"""
def read_file(read_location):
    f = open(read_location, "r")
    lines = f.readlines()
    return lines


"""
Write sounddata to file for next module to use.
"""
def write_file(data, write_location):
    f = open(write_location, "w")
    f.writelines(data)
    f.close()
    return

def write_soundfile(data, write_location, fs):
    # Prevent file overwriting
    index = 1
    while(os.path.isfile(write_location)):
        i = str(index)
        # Remove .wav
        write_location = write_location[:len(write_location) - 4]
        # Remove possible index number
        if(index > 1):
            write_location = write_location[:len(write_location) - len(i)]
        write_location = write_location + i + ".wav"
        index = index + 1
    sf.write(write_location, data, fs)
    return

def parse_line(line):
    approvedCharacters = string.ascii_uppercase + string.ascii_lowercase + " " + "." + "?" + "!" + "1" + "2" + "3" + "4" + "5" + "6" + "6" + "7" + "8" + "9" + "0"
    returnString = ""
    for char in line:
        if char in approvedCharacters:
            returnString+=str(char)
    return returnString.strip()


def check_file(read_location):
    lines = read_file(read_location)
    print("Lines", lines)
    if (len(lines) < 1):
        return []
    parsed_lines = []
    for line in lines:
        sentences = re.split(r'(.+?[.?,!])', line)
        for sentence in sentences:
            if sentence != "":
                parsed_lines.append(parse_line(sentence))
    ## Clear the file
    write_file("", read_location)
    return list(filter(bool, parsed_lines))

import re
import sys


def main():
    answer = []
    for line in sys.stdin:
        line = line.strip()
        if line == "D": break
        #if line == "0": answer.append(line)
        if re.match(r"0*((1(01*0)*1)*0*)*",  line).group(0):
            answer.append(line)

    for each in answer:
        print(each)


# start program
main()
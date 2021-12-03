import Part1
import Part2
import sys

def main():
    inFile = sys.argv[2]
    part = int(sys.argv[1])
    if part == 1:
        part1(inFile)
    elif part == 2:
        part2(inFile)
    else:
        part1(inFile)
        part2(inFile)

def part1(path):
    print("--== Part 1 ==--")
    cmds = Part1.getInput(path)
    endCoords = Part1.proccessCommands(cmds)
    #print(cmds)
    print(endCoords)
    result = endCoords[0] * endCoords[1]
    print(result)
    return result 

def part2(path):
    print("--== Part 2 ==--")
    cmds = Part1.getInput(path)
    endCoords = Part2.proccessCommands(cmds)
    print(endCoords)
    result = endCoords[0] * endCoords[1]
    print(result)
    return result

main()
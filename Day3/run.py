from typing import Match
import Part1
import Part2
import sys

def main():
    part = int(sys.argv[1])
    inFile = sys.argv[2]

    if part == 1:
        part1(inFile)
    elif part == 2:
        part2(inFile)
    else:
        part1(inFile)
        part2(inFile)

def part1(path):
    print("--== Part 1 ==--")
    data = Part1.getInput(path)
    gamma = Part1.getGammaRate(data)
    epsilon = Part1.getEpsilonRate(gamma)
    print(f"({gamma}, {epsilon})")
    power = int(gamma,2) * int(epsilon,2)
    print(power)
    return power

def part2(path):
    print("--== Part 2 ==--")
    data = Part1.getInput(path)
    o2 = Part2.getRating(data,Part2.Mode.HIGHER)
    co2 = Part2.getRating(data,Part2.Mode.LOWER)
    print(f"({o2}, {co2})")
    result = int(o2,2) * int(co2,2)
    print(result)
    return result

main()
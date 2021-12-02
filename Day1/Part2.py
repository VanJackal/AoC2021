import Part1

def main():
    depths = Part1.getInput("inputTest.txt")

    print(depths[0:3:])

    for i in range(len(depths[1:-1])):
        print(depths[i-1] + depths[i] + depths[i+1])

def main():
    depths = getInput("input.txt")

    prevDepth = depths[0]
    printDepthInfo(prevDepth,"N/A - no previous measurment")
    linecount = 0
    incCount = 0
    for depth in depths[1:]:
        print(f"{prevDepth} - {depth}")
        if depth > prevDepth:
            incCount += 1
            printDepthInfo(depth,"INCREASE")
        else:
            printDepthInfo(depth,"decrease")
        prevDepth = depth
        linecount+=1

    print(f"depth increased {incCount} times.")
    print(linecount)

def getInput(path):
    with open(path) as f:
        depthsSTR = f.readlines()
        depths = []
        for depth in depthsSTR:
            depths.append(int(depth.strip()))
    return depths

def printDepthInfo(depth,msg):
    print(f"{depth} ({msg})")
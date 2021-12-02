import Part1

def main(depths):
    rollingSums = []
    for i in range(1,len(depths)-1):
        print(depths[i-1:i+2])
        rollingSums.append(depths[i-1] + depths[i] + depths[i+1])
    
    Part1.main(rollingSums)

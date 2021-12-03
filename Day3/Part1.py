import math
def getInput(path):
    with open(path) as f:
        lines = f.readlines()
    
    data = []
    for line in lines:
        data.append(line.strip())
    return data

def getGammaRate(data):
    result = ""
    for i in range(len(data[0])):
        vals = [int(j[i]) for j in data]
        total = sum(vals)
        if total > len(data)/2:
            result += "1"
        else:
            result += "0"
    
    return result

def getEpsilonRate(gamma):
    gammaInt = int(gamma,2)
    epsilon = gammaInt ^ (2**len(gamma)-1)
    return bin(epsilon)[2:]

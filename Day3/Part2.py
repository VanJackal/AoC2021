class Mode:
    def HIGHER(l1,l2):
        return len(l1) >= len(l2)
    
    def LOWER(l1,l2):
        return len(l1) < len(l2)

def splitData(data,idx):
    zeros = []
    ones = []

    for i in data:
        if int(i[idx]) == 1:
            ones.append(i)
        else:
            zeros.append(i)
    return (zeros,ones)

def getRating(data, mode, idx = 0):
    if len(data) == 1:
        return data[0]

    zeros, ones = splitData(data,idx)
    
    if mode(ones,zeros):
        return getRating(ones, mode, idx+1)
    else:
        return getRating(zeros, mode, idx+1)

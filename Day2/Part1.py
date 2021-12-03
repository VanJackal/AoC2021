def getInput(path):
    with open(path) as f:
        lines = f.readlines()
    cmds = []
    for line in lines:
        cmd = line.split(" ")
        cmd[1] = int(cmd[1])
        cmds.append(cmd)
    
    return cmds

def proccessCommands(cmds):
    x = 0
    y = 0
    for cmd in cmds:
        dir, dist = cmd

        if dir == "forward":
            x += dist
        elif dir == "down":
            y += dist
        elif dir == "up":
            y -= dist
    
    return (x,y)
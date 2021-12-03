def proccessCommands(cmds):
    x = 0
    y = 0

    aim = 0
    for cmd in cmds:
        dir, dist = cmd

        if dir == "forward":
            x += dist
            y += dist * aim
        elif dir == "down":
            aim += dist
        elif dir == "up":
            aim -= dist
    
    return (x,y)
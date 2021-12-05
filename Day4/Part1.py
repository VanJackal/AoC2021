import Board

def getInput(path):
    with open(path) as f:
        calls = f.readline().strip().split(",")
        f.readline()
        boardData = f.readlines()
    boardsRaw = [[]]
    for data in boardData:
        if data == "\n":
            boardsRaw.append([])
        else:
            intData = []
            for i in data.split(" "):
                i = i.strip()
                if i:
                    intData.append(int(i))
            boardsRaw[-1].append(intData)
    
    boards = []
    for board in boardsRaw:
        boards.append(Board.Board(board))

    return (calls, boards)

def callToBoards(call, boards):
    for board in boards:
        board.call(call)

def checkBoards(boards):
    won = []
    for board in boards:
        if board.checkBoard():
            won.append(board)
    return won
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
    calls, boards = Part1.getInput(path)
    for call in calls:
        Part1.callToBoards(int(call),boards)
        board = Part1.checkBoards(boards)[0]
        if board:
            board.printBoard()
            uncallSum = board.getUncalledSum()
            result = uncallSum * int(call)
            print(f"({call}, {uncallSum})")
            print(result)
            return result
            
    

def part2(path):
    print("--== Part 2 ==--")
    calls, boards = Part1.getInput(path)
    for call in calls:
        Part1.callToBoards(int(call), boards)
        boardsWon = Part1.checkBoards(boards)
        for board in boardsWon:
            if board and len(boards) > 1:
                print(len(boards))
                board.printBoard()
                boards.remove(board)
            elif board:
                board.printBoard()
                uncallSum = board.getUncalledSum()
                result = uncallSum * int(call)
                print(f"({call}, {uncallSum})")
                print(result)
                return result


main()
import pygame
import ChessGame
import time

FPS = 60

PIECE_IMAGES = {
    "wK" : pygame.image.load(r"DataScience\Chess_AI\ChessPieceImages\WhiteKing.png"),
    "wQ" : pygame.image.load(r"DataScience\Chess_AI\ChessPieceImages\WhiteQueen.png"),
    "wR" : pygame.image.load(r"DataScience\Chess_AI\ChessPieceImages\WhiteRook.png"),
    "wN" : pygame.image.load(r"DataScience\Chess_AI\ChessPieceImages\WhiteKnight.png"),
    "wB" : pygame.image.load(r"DataScience\Chess_AI\ChessPieceImages\WhiteBishop.png"),
    "wP" : pygame.image.load(r"DataScience\Chess_AI\ChessPieceImages\WhitePawn.png"),

    "bK" : pygame.image.load(r"DataScience\Chess_AI\ChessPieceImages\BlackKing.png"),
    "bQ" : pygame.image.load(r"DataScience\Chess_AI\ChessPieceImages\BlackQueen.png"),
    "bR" : pygame.image.load(r"DataScience\Chess_AI\ChessPieceImages\BlackRook.png"),
    "bN" : pygame.image.load(r"DataScience\Chess_AI\ChessPieceImages\BlackKnight.png"),
    "bB" : pygame.image.load(r"DataScience\Chess_AI\ChessPieceImages\BlackBishop.png"),
    "bP" : pygame.image.load(r"DataScience\Chess_AI\ChessPieceImages\BlackPawn.png")
}

def DrawBoard (screen, flipped):
    screen.fill((0,0,0))
    lightSquare = (225, 220, 190)
    darkSquare = (155, 105, 50)
    windowHeight = screen.get_height()
    squareSize = windowHeight//8
    for row in range (8):
        for col in range (8):
            if ((row + col) % 2 == 0):
                pygame.draw.rect(screen, lightSquare, pygame.Rect((col * squareSize), (row * squareSize), squareSize, squareSize))
            else:
                pygame.draw.rect(screen, darkSquare, pygame.Rect((col * squareSize), (row * squareSize), squareSize, squareSize))

def DrawPieces (screen, board, flipped):
    DrawBoard(screen, flipped)
    windowHeight = screen.get_height()
    squareSize = windowHeight//8
    if (flipped == True):
        for row in range (8):
            for col in range (8):
                if (isinstance(board.board[row][col], ChessGame.King) == True):
                    if (board.board[row][col].color == True):
                        screen.blit(pygame.transform.smoothscale(PIECE_IMAGES["wK"], (squareSize, squareSize)), pygame.Rect(abs(col-7) * squareSize, abs(row-7) * squareSize, squareSize, squareSize))
                    else:
                        screen.blit(pygame.transform.smoothscale(PIECE_IMAGES["bK"], (squareSize, squareSize)), pygame.Rect(abs(col-7) * squareSize, abs(row-7) * squareSize, squareSize, squareSize))
                elif (isinstance(board.board[row][col], ChessGame.Queen) == True):
                    if (board.board[row][col].color == True):
                        screen.blit(pygame.transform.smoothscale(PIECE_IMAGES["wQ"], (squareSize, squareSize)), pygame.Rect(abs(col-7) * squareSize, abs(row-7) * squareSize, squareSize, squareSize))
                    else:
                        screen.blit(pygame.transform.smoothscale(PIECE_IMAGES["bQ"], (squareSize, squareSize)), pygame.Rect(abs(col-7) * squareSize, abs(row-7) * squareSize, squareSize, squareSize))
                elif (isinstance(board.board[row][col], ChessGame.Rook) == True):
                    if (board.board[row][col].color == True):
                        screen.blit(pygame.transform.smoothscale(PIECE_IMAGES["wR"], (squareSize, squareSize)), pygame.Rect(abs(col-7) * squareSize, abs(row-7) * squareSize, squareSize, squareSize))
                    else:
                        screen.blit(pygame.transform.smoothscale(PIECE_IMAGES["bR"], (squareSize, squareSize)), pygame.Rect(abs(col-7) * squareSize, abs(row-7) * squareSize, squareSize, squareSize))
                elif (isinstance(board.board[row][col], ChessGame.Knight) == True):
                    if (board.board[row][col].color == True):
                        screen.blit(pygame.transform.smoothscale(PIECE_IMAGES["wN"], (squareSize, squareSize)), pygame.Rect(abs(col-7) * squareSize, abs(row-7) * squareSize, squareSize, squareSize))
                    else:
                        screen.blit(pygame.transform.smoothscale(PIECE_IMAGES["bN"], (squareSize, squareSize)), pygame.Rect(abs(col-7) * squareSize, abs(row-7) * squareSize, squareSize, squareSize))
                elif (isinstance(board.board[row][col], ChessGame.Bishop) == True):
                    if (board.board[row][col].color == True):
                        screen.blit(pygame.transform.smoothscale(PIECE_IMAGES["wB"], (squareSize, squareSize)), pygame.Rect(abs(col-7) * squareSize, abs(row-7) * squareSize, squareSize, squareSize))
                    else:
                        screen.blit(pygame.transform.smoothscale(PIECE_IMAGES["bB"], (squareSize, squareSize)), pygame.Rect(abs(col-7) * squareSize, abs(row-7) * squareSize, squareSize, squareSize))
                elif (isinstance(board.board[row][col], ChessGame.Pawn) == True):
                    if (board.board[row][col].color == True):
                        screen.blit(pygame.transform.smoothscale(PIECE_IMAGES["wP"], (squareSize, squareSize)), pygame.Rect(abs(col-7) * squareSize, abs(row-7) * squareSize, squareSize, squareSize))
                    else:
                        screen.blit(pygame.transform.smoothscale(PIECE_IMAGES["bP"], (squareSize, squareSize)), pygame.Rect(abs(col-7) * squareSize, abs(row-7) * squareSize, squareSize, squareSize))
    else:
        for row in range (8):
            for col in range (8):
                if (isinstance(board.board[row][col], ChessGame.King) == True):
                    if (board.board[row][col].color == True):
                        screen.blit(pygame.transform.smoothscale(PIECE_IMAGES["wK"], (squareSize, squareSize)), pygame.Rect(col * squareSize, row * squareSize, squareSize, squareSize))
                    else:
                        screen.blit(pygame.transform.smoothscale(PIECE_IMAGES["bK"], (squareSize, squareSize)), pygame.Rect(col * squareSize, row * squareSize, squareSize, squareSize))
                elif (isinstance(board.board[row][col], ChessGame.Queen) == True):
                    if (board.board[row][col].color == True):
                        screen.blit(pygame.transform.smoothscale(PIECE_IMAGES["wQ"], (squareSize, squareSize)), pygame.Rect(col * squareSize, row * squareSize, squareSize, squareSize))
                    else:
                        screen.blit(pygame.transform.smoothscale(PIECE_IMAGES["bQ"], (squareSize, squareSize)), pygame.Rect(col * squareSize, row * squareSize, squareSize, squareSize))
                elif (isinstance(board.board[row][col], ChessGame.Rook) == True):
                    if (board.board[row][col].color == True):
                        screen.blit(pygame.transform.smoothscale(PIECE_IMAGES["wR"], (squareSize, squareSize)), pygame.Rect(col * squareSize, row * squareSize, squareSize, squareSize))
                    else:
                        screen.blit(pygame.transform.smoothscale(PIECE_IMAGES["bR"], (squareSize, squareSize)), pygame.Rect(col * squareSize, row * squareSize, squareSize, squareSize))
                elif (isinstance(board.board[row][col], ChessGame.Knight) == True):
                    if (board.board[row][col].color == True):
                        screen.blit(pygame.transform.smoothscale(PIECE_IMAGES["wN"], (squareSize, squareSize)), pygame.Rect(col * squareSize, row * squareSize, squareSize, squareSize))
                    else:
                        screen.blit(pygame.transform.smoothscale(PIECE_IMAGES["bN"], (squareSize, squareSize)), pygame.Rect(col * squareSize, row * squareSize, squareSize, squareSize))
                elif (isinstance(board.board[row][col], ChessGame.Bishop) == True):
                    if (board.board[row][col].color == True):
                        screen.blit(pygame.transform.smoothscale(PIECE_IMAGES["wB"], (squareSize, squareSize)), pygame.Rect(col * squareSize, row * squareSize, squareSize, squareSize))
                    else:
                        screen.blit(pygame.transform.smoothscale(PIECE_IMAGES["bB"], (squareSize, squareSize)), pygame.Rect(col * squareSize, row * squareSize, squareSize, squareSize))
                elif (isinstance(board.board[row][col], ChessGame.Pawn) == True):
                    if (board.board[row][col].color == True):
                        screen.blit(pygame.transform.smoothscale(PIECE_IMAGES["wP"], (squareSize, squareSize)), pygame.Rect(col * squareSize, row * squareSize, squareSize, squareSize))
                    else:
                        screen.blit(pygame.transform.smoothscale(PIECE_IMAGES["bP"], (squareSize, squareSize)), pygame.Rect(col * squareSize, row * squareSize, squareSize, squareSize))


def PossibleMoves (screen, board, flipped, pieceSelected):
    squareSize = screen.get_height() // 8
    if (pieceSelected != None):
        curY, curX = pieceSelected
    if (board.board[curY][curX] != 0):
        moves = board.board[curY][curX].MoveList()
        possibleCircles = pygame.Surface((screen.get_height(), screen.get_height()), pygame.SRCALPHA)
        possibleCircles
        for x in moves:
            takes = False
            targetY, targetX = x
            if (board.board[targetY][targetX] != 0 and board.board[targetY][targetX].color != board.board[curY][curX].color):
                takes = True
            if (flipped == True):
                if (takes == True):
                    pygame.draw.circle(possibleCircles, (255, 0, 0, 170), (abs(targetX-7) * squareSize + squareSize // 2, abs(targetY-7) * squareSize + squareSize //2), squareSize // 2, squareSize // 10)
                else:
                    pygame.draw.circle(possibleCircles, (160, 160, 160, 115), (abs(targetX-7) * squareSize + squareSize //2, abs(targetY-7) * squareSize + squareSize // 2), squareSize // 10)
            else:
                if (takes == True):
                    pygame.draw.circle(possibleCircles, (255, 0, 0, 170), (targetX * squareSize + squareSize // 2, targetY * squareSize + squareSize //2), squareSize // 2, squareSize // 10)
                else:
                    pygame.draw.circle(possibleCircles, (160, 160, 160, 115), (targetX * squareSize + squareSize //2, targetY * squareSize + squareSize // 2), squareSize // 10)
        screen.blit(possibleCircles, (0,0))


        
def main ():
    screen = pygame.display.set_mode((560,560), pygame.RESIZABLE)
    pygame.display.set_caption("Chess Game: ")
    
    board = ChessGame.Board()
    board.InitalizeBoard()

    clock = pygame.time.Clock()

    running = True
    flipped = False
    whiteToMove = True
    squareClicked = ()
    DrawPieces(screen, board, flipped)
    pygame.display.update()
    lastMove = []
    while (running == True):
        clock.tick(FPS)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                # Find the coordinates on the pygame window that the user clicked (x, y)
                col, row = pygame.mouse.get_pos() 
                col = col // (screen.get_height() // 8)
                row = row // (screen.get_height() // 8)
                if (flipped == True):
                    col = abs(col-7)
                    row = abs(row-7)
                
                if (len(lastMove) == 0 and (board.board[row][col] == 0 or board.board[row][col].color != whiteToMove)):
                    continue

                if (squareClicked == (row, col)):
                    squareClicked = ()
                    lastMove.clear()
                    DrawPieces(screen,board, flipped)
                    pygame.display.update()
                else:
                    # If the user clicks one of their pieces after they had selected another one of their pieces, 
                    # clear the move queue and then add that newly selected square to the move queue
                    if (squareClicked != () and board.board[row][col] != 0 and board.board[row][col].color == board.board[squareClicked[0]][squareClicked[1]].color):
                        lastMove.clear()
                        DrawPieces(screen, board, flipped)

                    squareClicked = (row, col)
                    # Generate the legal moves for the piece the user selected, draw on screen and add to move queue
                    if (len(lastMove) == 0):
                        PossibleMoves(screen, board, flipped, squareClicked)
                    
                    pygame.display.update()
                    lastMove.append(squareClicked)
                    
                    # If there are two moves in the move queue, try moving the piece from the first coordinate to the target/last coordinate
                    # in the move queue
                    if (len(lastMove) == 2):
                        # Won't move the piece/alter the board if the move was illegal
                        start_time = time.time()
                        # Was legal move keeps track if the move was legal, if move was legal, then it was completed and it 
                        # is the opposite color's turn to move
                        wasLegal = board.Move(lastMove[0], lastMove[1])
                        if (wasLegal == True):
                            whiteToMove = not whiteToMove
                        end_time = time.time()
                        for x in board.listOfMoves:
                            print (x + " ", end = " ")
                        print ()

                        print ("Calculated in " + str(end_time - start_time) + " seconds.")
                        # Clear the move queue and set the last clicked square to null/empty coordinates
                        lastMove.clear()
                        squareClicked = ()

                        # Get rid of the possible move circles 
                        DrawPieces (screen, board, flipped)
                        pygame.display.update()


if __name__ == "__main__":
    main()
    

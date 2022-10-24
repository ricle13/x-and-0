def conclusion(board):
    print(f'''
 {board[0]} | {board[1]} | {board[2]}
 --|---|--
 {board[3]} | {board[4]} | {board[5]}
 --|---|--
 {board[6]} | {board[7]} | {board[8]}''')

def check_win_line(board):
    win_line = ((0, 1, 2), (3, 4, 7), (6, 7, 8),
                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                (0, 4, 8), (2, 4, 6))
    
    for line in win_line:
        my_line = []
        for cord in line:
            my_line.append(board[cord])
        if my_line == ['X', 'X', 'X']:
            return True, 'X'
        if my_line == ['O', 'O', 'O']:
            return True, 'O'
    return False, None

    

def step(board, turn):
    check = ('0', '1', '2', '3', '4', '5', '6', '7', '8')
    while True:
        step = input(f'Ходит {turn}: ')
        if step in check:
            cord = int(step)
            if cord in board:
                break
            else:
                print('Клетка занята, попробуйте снова.')
        else:
            print('Ответ неверный попробуйте снова.')
    return cord

def x_o_step(board, x_step):
    if x_step == True:
        cord = step(board = board, turn = 'X')
        board[cord] = 'X'
    else:
        cord = step(board = board, turn = 'O')
        board[cord] = 'O'
    return board
            
def empy_board(): return [coard for coard in range(9)]



def main():
    print('Игра крестики нолики!')
    board = empy_board()
    x_step = True
    while True:
        conclusion(board)
        board = x_o_step(board, x_step)
        x_step = not x_step
        win, winer = check_win_line(board)
        if win == True:
            conclusion(board)
            print(f'---Выиграл {winer}!---')
            break
    again = input('Сыграть снова?(y/n): ')
    if again == 'y':
        main()
        

main()
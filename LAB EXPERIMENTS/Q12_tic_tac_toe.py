board = ["X", "O", "X", "O", "X", "O", "O", "X", " "]
def show():
    for i in range(0, 9, 3): print(" | ".join(board[i:i+3]))
show()
wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
winner = next((board[a] for a,b,c in wins if board[a] != " " and board[a] == board[b] == board[c]), None)
print("Winner:", winner if winner else "Draw" if " " not in board else "Game in progress")

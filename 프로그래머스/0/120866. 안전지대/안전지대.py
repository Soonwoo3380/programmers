def solution(board):

    mine_coord = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                mine_coord.append((i,j))

    dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

    result = []

    for coord in mine_coord:
        for k in range(9):
            nx = coord[0] + dx[k]
            ny = coord[1] + dy[k]

            if 0 <= nx < len(board) and 0 <= ny < len(board):
                result.append((nx, ny))

    result = list(set(result))
    return (len(board) * len(board)) - len(result)
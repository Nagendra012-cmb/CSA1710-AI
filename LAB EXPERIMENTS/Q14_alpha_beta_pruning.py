tree = [[3, 5], [6, 9]]
def alphabeta(node, depth, alpha, beta, maximizing):
    if depth == 0: return node
    if maximizing:
        value = float("-inf")
        for child in node:
            value = max(value, alphabeta(child, depth-1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta: break
        return value
    value = float("inf")
    for child in node:
        value = min(value, alphabeta(child, depth-1, alpha, beta, True))
        beta = min(beta, value)
        if alpha >= beta: break
    return value
print("Game tree:", tree)
print("Optimal value:", alphabeta(tree, 2, float("-inf"), float("inf"), True))

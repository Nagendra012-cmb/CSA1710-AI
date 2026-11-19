scores = [3, 5, 2, 9]
def minimax(values, maximizing):
    if len(values) == 1: return values[0]
    mid = len(values)//2
    results = [minimax(values[:mid], not maximizing), minimax(values[mid:], not maximizing)]
    return max(results) if maximizing else min(results)
print("Leaf utility values:", scores)
print("Best minimax value for MAX:", minimax(scores, True))

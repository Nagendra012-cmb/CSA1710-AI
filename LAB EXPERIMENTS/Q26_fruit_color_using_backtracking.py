domains = {"Apple":["Red","Green"], "Banana":["Yellow"], "Grapes":["Green","Purple"]}
assignment = {}
def backtrack(items):
    if not items: return True
    fruit = items[0]
    for color in domains[fruit]:
        assignment[fruit] = color
        if backtrack(items[1:]): return True
    assignment.pop(fruit, None)
    return False
backtrack(list(domains))
print("Fruit-color assignments:")
for fruit, color in assignment.items(): print(fruit, "->", color)

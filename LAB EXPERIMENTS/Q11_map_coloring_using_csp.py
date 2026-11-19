colors = ["Red", "Green", "Blue"]
graph = {"A":["B","C"], "B":["A","C","D"], "C":["A","B","D"], "D":["B","C"]}
assignment = {}
def safe(region, color):
    return all(assignment.get(n) != color for n in graph[region])
def solve():
    if len(assignment) == len(graph): return True
    region = next(r for r in graph if r not in assignment)
    for color in colors:
        if safe(region, color):
            assignment[region] = color
            if solve(): return True
            del assignment[region]
    return False
if solve():
    print("Map coloring solution:")
    for region, color in assignment.items(): print(f"{region} -> {color}")
else: print("No solution found")

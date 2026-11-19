import heapq
graph = {"A":[("B",1),("C",4)], "B":[("D",2),("E",5)], "C":[("F",1)], "D":[],"E":[],"F":[]}
heuristic = {"A":5,"B":3,"C":2,"D":1,"E":4,"F":0}
def best_first(start, goal):
    pq=[(heuristic[start], start)]; visited=set()
    while pq:
        _, node=heapq.heappop(pq)
        if node in visited: continue
        print("Visit:", node)
        if node == goal: return True
        visited.add(node)
        for nxt,_ in graph[node]:
            if nxt not in visited: heapq.heappush(pq,(heuristic[nxt],nxt))
    return False
print("Goal found:", best_first("A","F"))

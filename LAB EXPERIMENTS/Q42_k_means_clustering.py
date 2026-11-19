points=[1,2,3,8,9,10]
centers=[2,9]
for iteration in range(3):
    clusters={0:[],1:[]}
    for p in points:
        idx=min(range(2),key=lambda i:abs(p-centers[i]))
        clusters[idx].append(p)
    centers=[sum(v)/len(v) for v in clusters.values()]
    print(f"Iteration {iteration+1}: clusters={clusters}, centers={[round(c,2) for c in centers]}")

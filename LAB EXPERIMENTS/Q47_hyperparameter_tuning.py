# Grid search over a simple model parameter
training=[(1,2),(2,4),(3,6),(4,8)]
candidates=[0.1,0.5,1.0,2.0]
def score(scale):
    # illustrative validation score: best near scale=2
    return 1-abs(scale-2)*0.2
results=[(p,score(p)) for p in candidates]
for p,s in results: print(f"parameter={p}: validation_score={s:.2f}")
print("Best parameter:",max(results,key=lambda x:x[1])[0])

states=["A","B","Goal"]; actions=["left","right"]
Q={s:{a:0.0 for a in actions} for s in states}
alpha=0.5; gamma=0.9
# One training episode: A --right--> B --right--> Goal
for state,action,reward,next_state in [("A","right",0,"B"),("B","right",10,"Goal")]:
    future=max(Q[next_state].values()) if next_state!="Goal" else 0
    Q[state][action]+=alpha*(reward+gamma*future-Q[state][action])
print("Learned Q-table:")
for state,row in Q.items(): print(state,row)
print("Best action at B:",max(Q["B"],key=Q["B"].get))

import math
train=[((1,1),"A"),((2,2),"A"),((6,6),"B"),((7,7),"B")]
point=(3,3); k=3
nearest=sorted(train,key=lambda item:math.dist(item[0],point))[:k]
votes={}
for _,label in nearest: votes[label]=votes.get(label,0)+1
print("Test point:",point)
print("Nearest neighbors:",nearest)
print("Predicted class:",max(votes,key=votes.get))

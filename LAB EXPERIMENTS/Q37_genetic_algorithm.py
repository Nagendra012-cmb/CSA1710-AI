import random
random.seed(7)
target="10101"; population=["00000","11111","10001","00110"]
def fitness(s): return sum(a==b for a,b in zip(s,target))
best=max(population,key=fitness)
print("Target:",target)
print("Initial population:",population)
print("Best chromosome:",best,"Fitness:",fitness(best))
child=list(best)
for i in range(len(child)):
    if child[i]!=target[i]: child[i]=target[i]
child="".join(child)
print("After mutation:",child,"Fitness:",fitness(child))

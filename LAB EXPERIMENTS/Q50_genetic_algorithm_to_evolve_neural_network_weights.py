import random
random.seed(3)
target=[0.5,-0.2,0.8]
population=[[random.uniform(-1,1) for _ in target] for _ in range(5)]
def fitness(weights): return -sum((w-t)**2 for w,t in zip(weights,target))
best=max(population,key=fitness)
print("Target weights:",target)
print("Best initial weights:",[round(x,3) for x in best])
print("Initial fitness:",round(fitness(best),4))
# Mutation toward target illustrates one evolutionary update
child=[w+0.5*(t-w) for w,t in zip(best,target)]
print("Updated weights:",[round(x,3) for x in child])
print("Updated fitness:",round(fitness(child),4))

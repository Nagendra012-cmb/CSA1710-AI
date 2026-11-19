facts = {"sparrow":"bird", "eagle":"bird", "penguin":"bird"}
cannot_fly = {"penguin"}
def can_fly(animal):
    return facts.get(animal) == "bird" and animal not in cannot_fly
for bird in facts:
    print(f"{bird} can fly: {can_fly(bird)}")

# State: monkey position, box position, has banana
state = {"monkey":"door", "box":"window", "banana":False}
actions = ["walk to box", "push box under banana", "climb box", "grasp banana"]
for action in actions:
    print("Action:", action)
state["monkey"] = "under banana"; state["box"] = "under banana"; state["banana"] = True
print("Goal achieved:", state["banana"])

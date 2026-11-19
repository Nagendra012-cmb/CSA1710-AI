transition={"Sunny":{"Sunny":0.8,"Rainy":0.2},"Rainy":{"Sunny":0.4,"Rainy":0.6}}
state="Sunny"
print("Initial state:",state)
for day in range(1,6):
    # choose most likely next state for a deterministic demonstration
    state=max(transition[state],key=transition[state].get)
    print(f"Day {day}: {state}")

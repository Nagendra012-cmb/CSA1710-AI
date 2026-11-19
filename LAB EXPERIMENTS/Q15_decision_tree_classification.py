# A small rule-based decision tree for a study dataset
def predict(hours):
    if hours >= 5: return "Pass"
    if hours >= 3: return "Pass"
    return "Fail"
samples = [(1,"Fail"), (2,"Fail"), (4,"Pass"), (6,"Pass")]
print("Training samples:", samples)
for h in [2, 4, 6]:
    print(f"Study hours={h} -> Prediction={predict(h)}")

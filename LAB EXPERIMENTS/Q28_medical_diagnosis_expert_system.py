symptoms = {"fever","cough","body_pain"}
rules = [
    ({"fever","cough","body_pain"},"Flu-like illness"),
    ({"sneezing","runny_nose"},"Common cold")
]
diagnosis = [name for required,name in rules if required.issubset(symptoms)]
print("Observed symptoms:", sorted(symptoms))
print("Possible rule-based result:", diagnosis or ["No matching rule"])
print("This educational example is not a medical diagnosis.")

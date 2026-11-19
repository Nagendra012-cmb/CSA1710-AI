facts = {"rain"}
rules = [({"rain"},"wet_ground"), ({"wet_ground"},"slippery_road")]
changed = True
while changed:
    changed = False
    for premise, conclusion in rules:
        if premise.issubset(facts) and conclusion not in facts:
            facts.add(conclusion); changed = True
            print("Inferred:", conclusion)
print("Final facts:", sorted(facts))

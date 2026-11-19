rules = {"can_travel":["has_ticket","has_id"], "has_ticket":["ticket_paid"]}
facts = {"ticket_paid","has_id"}
def prove(goal):
    if goal in facts: return True
    if goal not in rules: return False
    return all(prove(item) for item in rules[goal])
goal = "can_travel"
print("Goal:", goal)
print("Proved:", prove(goal))

ratings={"A":{"Movie1":5,"Movie2":4},"B":{"Movie1":5,"Movie3":4},"C":{"Movie2":5,"Movie3":3}}
user="A"; target="Movie3"
similar_users=[u for u in ratings if u!=user and ratings[u].get("Movie1")==ratings[user].get("Movie1")]
scores=[ratings[u][target] for u in similar_users if target in ratings[u]]
print("User:",user)
print("Similar users:",similar_users)
print("Recommended item:",target if scores else "No recommendation")
if scores: print("Predicted rating:",round(sum(scores)/len(scores),2))

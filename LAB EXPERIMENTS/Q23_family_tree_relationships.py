parent = {("Ramesh","Suresh"), ("Ramesh","Lakshmi"), ("Suresh","Arjun"), ("Lakshmi","Meera")}
def children(person): return [child for p,child in parent if p == person]
def is_parent(a,b): return (a,b) in parent
print("Children of Ramesh:", sorted(children("Ramesh")))
print("Is Suresh parent of Arjun?", is_parent("Suresh","Arjun"))
print("Grandchildren of Ramesh:", sorted(c for child in children("Ramesh") for c in children(child)))

# Demonstrates face matching using simple feature vectors
known={"Person_A":[0.2,0.4,0.6],"Person_B":[0.8,0.3,0.1]}
probe=[0.22,0.39,0.58]
def distance(a,b): return sum((x-y)**2 for x,y in zip(a,b))**0.5
match=min(known,key=lambda name:distance(known[name],probe))
print("Probe feature vector:",probe)
print("Closest known identity:",match)
print("Distance:",round(distance(known[match],probe),4))
print("For real face recognition, use an authorized dataset and a pretrained model.")

# Linear decision boundary demonstration
training=[((1,1),"A"),((2,1),"A"),((5,5),"B"),((6,5),"B")]
def predict(point):
    # Boundary x+y=6; illustrative linear classifier
    return "A" if sum(point)<6 else "B"
print("Training points:",training)
for point in [(2,2),(5,4),(1,4)]:
    print(point,"=>",predict(point))

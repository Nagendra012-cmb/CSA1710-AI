# PCA for a 2D dataset using covariance and principal direction
data=[(2,1),(3,2),(4,3),(5,4)]
mx=sum(x for x,y in data)/len(data); my=sum(y for x,y in data)/len(data)
centered=[(x-mx,y-my) for x,y in data]
a=sum(x*x for x,y in centered)/len(data)
b=sum(x*y for x,y in centered)/len(data)
d=sum(y*y for x,y in centered)/len(data)
angle=0.5*__import__("math").atan2(2*b,a-d)
print("Mean:",(mx,my))
print("Covariance matrix:",((round(a,3),round(b,3)),(round(b,3),round(d,3))))
print("First principal component:",(round(__import__("math").cos(angle),3),round(__import__("math").sin(angle),3)))

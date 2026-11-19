# Simple least-squares linear regression
x=[1,2,3,4,5]; y=[2,4,5,4,5]
n=len(x); mx=sum(x)/n; my=sum(y)/n
m=sum((a-mx)*(b-my) for a,b in zip(x,y))/sum((a-mx)**2 for a in x)
c=my-m*mx
print("Slope:", round(m,3), "Intercept:", round(c,3))
print("Prediction for x=6:", round(m*6+c,3))

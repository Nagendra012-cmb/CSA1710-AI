positive={"good","great","excellent","happy","love"}
negative={"bad","poor","terrible","sad","hate"}
def sentiment(text):
    words=set(text.lower().split())
    score=len(words&positive)-len(words&negative)
    return "Positive" if score>0 else "Negative" if score<0 else "Neutral"
reviews=["The product is excellent and good","The service is poor and bad","The package arrived today"]
for review in reviews: print(review,"=>",sentiment(review))

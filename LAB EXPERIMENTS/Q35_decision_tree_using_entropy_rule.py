# A compact decision-tree rule example
def classify(weather):
    if weather == "Sunny": return "Play"
    if weather == "Rainy": return "Stay Inside"
    return "Play"
data=[("Sunny","Play"),("Rainy","Stay Inside"),("Cloudy","Play")]
print("Training examples:",data)
for weather in ["Sunny","Rainy","Cloudy"]:
    print(weather,"=>",classify(weather))

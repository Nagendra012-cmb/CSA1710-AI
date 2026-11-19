# Lightweight runnable demonstration; uses numeric image features
images=[("cat_1",[0.8,0.2]),("cat_2",[0.9,0.1]),("dog_1",[0.2,0.8]),("dog_2",[0.1,0.9])]
def classify(features):
    cat_center=(0.85,0.15); dog_center=(0.15,0.85)
    dist=lambda a,b:sum((x-y)**2 for x,y in zip(a,b))
    return "Cat" if dist(features,cat_center)<dist(features,dog_center) else "Dog"
sample=[0.75,0.25]
print("Training image feature samples:",len(images))
print("Test image features:",sample)
print("Predicted image class:",classify(sample))
print("For deep-learning training, install TensorFlow or PyTorch and use a labeled image dataset.")

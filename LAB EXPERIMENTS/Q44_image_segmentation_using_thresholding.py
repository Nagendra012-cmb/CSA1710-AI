# Segment a grayscale pixel matrix into foreground/background
image=[[20,35,180],[45,210,220],[15,170,30]]
threshold=128
mask=[[1 if pixel>=threshold else 0 for pixel in row] for row in image]
print("Grayscale image:")
for row in image: print(row)
print("Binary segmentation (1=foreground):")
for row in mask: print(row)

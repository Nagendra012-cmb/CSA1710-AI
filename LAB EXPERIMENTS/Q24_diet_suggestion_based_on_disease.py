diet = {
    "diabetes":["whole grains","green vegetables","low-sugar fruits"],
    "hypertension":["low-salt foods","fruits","vegetables"],
    "anemia":["spinach","beans","iron-rich foods"]
}
disease = "diabetes"
print("Selected condition:", disease)
print("General food suggestions:")
for food in diet[disease]: print("-", food)
print("Note: Follow advice from a qualified healthcare professional.")

planets = {
    "Mercury":{"order":1,"type":"Terrestrial"},
    "Venus":{"order":2,"type":"Terrestrial"},
    "Earth":{"order":3,"type":"Terrestrial"},
    "Mars":{"order":4,"type":"Terrestrial"},
    "Jupiter":{"order":5,"type":"Gas giant"}
}
for name, info in planets.items():
    print(f"{name}: position={info['order']}, type={info['type']}")
print("\nPlanet at position 3:", next(p for p,v in planets.items() if v["order"] == 3))

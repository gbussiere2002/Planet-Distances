from website import moon,moonmi,sun,sunmi,venus,venusmi,jupiter,jupitermi,mercury,mercurymi,saturn,saturnmi,mars,marsmi
from website import uranus,uranusmi,neptune,neptunemi

planet = input("Name a planet or moon to find out how far away it is: ")
if planet == "Moon":
    print("The Moon is currently",moon,"kilometers or",moonmi,"miles away from Earth!")
elif planet == "Sun":
    print("The Sun is currently", sun, "kilometers or", sunmi, "miles away from Earth!")
elif planet == "Venus":
    print("Venus is currently", venus, "kilometers or", venusmi, "miles away from Earth!")
elif planet == "Jupiter":
    print("Jupiter is currently", jupiter, "kilometers or", jupitermi, "miles away from Earth!")
elif planet == "Mercury":
    print("Mercury is currently", mercury, "kilometers or", mercurymi, "miles away from Earth!")
elif planet == "Saturn":
    print("Saturn is currently", saturn, "kilometers or", saturnmi, "miles away from Earth!")
elif planet == "Mars":
    print("Mars is currently", mars, "kilometers or", marsmi, "miles away from Earth!")
elif planet == "Uranus":
    print("Uranus is currently", uranus, "kilometers or", uranusmi, "miles away from Earth!")
elif planet == "Neptune":
    print("Neptune is currently", neptune, "kilometers or", neptunemi, "miles away from Earth!")
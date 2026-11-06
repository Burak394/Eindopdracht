wiskunde = 7.5
engels = 6.0
nederlands = 8.0

gemiddelde = (wiskunde + engels + nederlands) / 3

print("Wiskunde:", wiskunde)
print("Engels:", engels)
print("Nederlands:", nederlands)
print("Gemiddelde:", round(gemiddelde, 2))

if gemiddelde >= 5.5:
    print("Geslaagd!")
else:
    print("Gezakt!")
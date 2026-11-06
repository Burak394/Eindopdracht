
player_class = "Warrior"

match player_class:
    case "Warrior":
        health = 150
        damage = 20
    case "Mage":
        health = 80
        damage = 35
    case "Archer":
        health = 100
        damage = 25
    case "Rogue":
        health = 90
        damage = 30
    case _:
        print("Onbekende class gekozen!")
        health = 0
        damage = 0

if health > 0:
    print("Class:", player_class)
    print("Health:", health)
    print("Damage:", damage)

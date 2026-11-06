monster_health = 150
player_damage = 25
attack_count = 0

while monster_health > 0:
    monster_health -= player_damage
    attack_count += 1
    print(f"Monster health: {monster_health}")



print(f"Attack count: {attack_count}")
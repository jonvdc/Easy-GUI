heroes = {
    "MAT":
        {"name": "Materdon",
         "power": "flight",
         "strength": 5,
         "speed": 12},
    "ORA":
        {"name": "Orasy",
         "power": "x-ray vision",
         "strength": 2,
         "speed": 8}
}

for hero_id, hero_info in heroes.items():
    print(f"\nHero ID: {hero_id}")

    for key in hero_info:
        print(f"{key}: {hero_info[key]}")

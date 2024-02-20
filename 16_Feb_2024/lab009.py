#nested tuples

hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
awesome_team = (hero1, hero2)
print(awesome_team)

print(awesome_team[0])
print(awesome_team[0][0])
print(awesome_team[0][0][0])
print(awesome_team[0][1])

# Search in Tuple

# Search in Tuple
cities = ("London", "Paris", "Los Angeles", "Tokyo")
print("Paris" in cities)
print("Moscow" in cities)
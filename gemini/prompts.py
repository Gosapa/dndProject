def character_creation_prompt(name, origin, gender, plot):
    return f"""Please Create a character of the user!
Name: {name}
origin: {origin}
gender: {gender}
plot: {plot}
Please give random stats between 0~3 (game max is 20) for the character. The sum total of stats should be 10.
The type of stats are:
Strength
Dexterity
Vigor
Intelligence
Faith
Arcane
Please generate an according log under 50 character in on line, which is going to be used for saving the game. example: "User Created character 'Jake'"

Stats: {{'stats': Json with key = stat name (str), and value = stat value (int)}}
log = string"""
# nuskaityti tekstinį failą
with open("tekstas.txt", "r") as textfile:
    lines = textfile.readlines()

# suskaičiuoti ir atspausdinti kiek yra teksto eilučių
print(f"Lines: {len(lines)}")

# suskaičiuoti ir atspausdinti kiek yra žodžių kiekvienoje eilutėje
words_in_every_line = []
for number, line in enumerate(lines):
    words_count = len(line.split())
    words_in_every_line.append(words_count)
    print(f"{number}: zodziu: {words_count}")

# suskaičiuoti ir atspausdinti kiek yra didžiųjų raidžių kiekvienoje eilutėje
upper_in_every_line = []
upper_count = 0
for letter in line:
    if letter.isupper():
        upper_count + 1
upper_in_every_line.append(upper_count)
print(f"Upper letters:  {upper_count}")

# atspausdinti eilutę, kurioje yra daugiausia žodžių
print(lines[words_in_every_line.index(max(words_in_every_line))])

# atspausdinti eilutę, kurioje yra daugiausia didžiųjų raidžių
[print(lines[upper_in_every_line.index(max(upper_in_every_line))])]

# BONUS: suskaičiuoti ir atspausdinti, kiek tekste yra sakinių (sakinio techninis apibrėžimas laisvas)
text = "".join(lines)
sentences = 0
for character in text:
    if character == "." or character == "?" or character == "!":
        sentences += 1
print(f"sakiniu: {sentences}")
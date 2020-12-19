characters_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
characters_lower = "abcdefghijklmnopqrstuvwxyz"
flag = "Ypw'zj zwufpp hwu txadjkcq dtbtyu kqkwxrbvu! Mbz cjzg kv IAJBO{ndldie_al_aqk_jjrnsxee}. Xzi utj gnn olkd qgq ftk ykaqe uei mbz ocrt qi ynlu, etrm mff'n wij bf wlny mjcj :)."
counter1 = 1
counter2 = 27

for i, j in enumerate(flag):
    counter1 -= 1
    counter2 -= 1
    if j.islower():
        characters = characters_lower
    elif j.isupper():
        characters = characters_upper
    else:
        print(j, end='')
        continue
    if (i % 2) == 0:
        encoded_index = characters.index(j) + counter1
    else:
        encoded_index = characters.index(j) + counter2
    while encoded_index > len(characters) - 1:
        encoded_index -= len(characters)
    while encoded_index < 0:
        encoded_index += len(characters)
    print(characters[encoded_index], end='')
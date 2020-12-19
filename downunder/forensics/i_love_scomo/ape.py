data = open('ilovescomo.jpg.out').readlines()

binary = ''

for line in data:
    if (len(line) >= 2):
        print(line[-2])
        # print(ord(line[-2]))
        if ord(line[-2]) == 32:
            binary += '1'
        else:
            binary += "0"
    else:
        binary += '0'
# print(binary)
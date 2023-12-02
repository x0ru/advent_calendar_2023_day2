import csv

too_many = False
total = 0
max_green, max_red, max_blue = 0, 0, 0

with open('file.csv', 'r') as file:
    games = csv.reader(file)
    for game in games:
        first_split = ''.join(game).split(':')
        second_split = first_split[1].split(';')
        for i in second_split:
            print(second_split)
            each = i.split()
            for pos in range(len(each)):
                if each[pos] == 'green':
                    if int(each[pos - 1]) > max_green:
                        max_green = int(each[pos - 1])
                if each[pos] == 'red':
                    if int(each[pos - 1]) > max_red:
                        max_red = int(each[pos - 1])
                if each[pos] == 'blue':
                    if int(each[pos - 1]) > max_blue:
                        max_blue = int(each[pos - 1])

        total += max_red * max_blue * max_green
        max_green, max_red, max_blue = 0, 0, 0
        print(total)

    print(total)

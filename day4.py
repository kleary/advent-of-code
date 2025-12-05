file_path = "day4-data.txt"

def load_real_data():
    f = open(file_path, 'r')
    r = f.readlines()
    a = []
    for i in range(len(r)):
        r[i] = r[i][0:-1]
        a.append([])
        for j in range(len(r[i])):
            a[i].append(r[i][j])
    return a

def load_example_data():
    return [
        [".",".","@","@",".","@","@","@","@","."],
        ["@","@","@",".","@",".","@",".","@","@"],
        ["@","@","@","@","@",".","@",".","@","@"],
        ["@",".","@","@","@","@",".",".","@","."],
        ["@","@",".","@","@","@","@",".","@","@"],
        [".","@","@","@","@","@","@","@",".","@"],
        [".","@",".","@",".","@",".","@","@","@"],
        ["@",".","@","@","@",".","@","@","@","@"],
        [".","@","@","@","@","@","@","@","@","."],
        ["@",".","@",".","@","@","@",".","@","."]
    ]


def part_1():
    count = 0
    for y in range(len(rolls)):
        for x in range(len(rolls[y])):
            if rolls[y][x] != '@':
                continue
            if check_neighbors(x, y) < 4:
                count += 1
                #temp_rolls[y][x] = 'x'

    print(count)

def part_2():
    count = 0
    while True:
        sub_count = 0
        removal_indices = []
        for y in range(len(rolls)):
            for x in range(len(rolls[y])):
                if rolls[y][x] != '@':
                    continue
                if check_neighbors(x, y) < 4:
                    count += 1
                    sub_count += 1
                    removal_indices.append([y, x])
                    #temp_rolls[y][x] = 'x'
        for i in removal_indices:
            rolls[i[0]][i[1]] = '.'
        print(sub_count)
        if sub_count == 0: break
    print(count)

def check_neighbors(x, y):
    sum = 0
    if not (y - 1 < 0) and rolls[y-1][x] == '@': 
        sum += 1
        #print("y-1, x", y-1, x)
    if not (y - 1 < 0) and not (x - 1 < 0) and rolls[y-1][x-1] == '@':
        sum += 1
        #print("y-1, x-1", y-1, x-1)
    if not (x - 1 < 0) and rolls[y][x-1] == '@':
        sum += 1
        #print("y, x-1", y, x-1)
    if not (x - 1 < 0) and not (y + 1 > len(rolls)-1) and rolls[y+1][x-1] == '@':
        sum += 1
        #print("y+1, x-1", y+1, x-1)
    if not (y + 1 > len(rolls)-1) and rolls[y+1][x] == '@':
        sum += 1
        #print("y+1, x", y+1, x)
    if not (y + 1 > len(rolls)-1) and not (x + 1 > len(rolls[y])-1) and rolls[y+1][x+1] == '@':
        sum += 1
        #print("y+1, x+1", y+1, x+1)
    if not (x + 1 > len(rolls[y])-1) and rolls[y][x+1] == '@':
        sum += 1
        #print("y, x+1", y, x+1)
    if not (x + 1 > len(rolls[y])-1) and not (y - 1 < 0) and rolls[y-1][x+1] == '@':
        sum += 1
        #print("y-1, x+1", y-1, x+1)
    #print(sum, x, y, sum < 4)
    return sum

def print_rolls(r):
    for row in r:
        print(row)


rolls = load_real_data()
#rolls = load_example_data()
#print_rolls(rolls)
#part_1()
part_2()

file_path = "day3-data.txt"

def load_real_data():
    f = open(file_path, 'r')
    b = f.readlines()
    for i in range(len(b)):
        b[i] = b[i][0:-1]

    return b

def load_example_data():
    return [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111"
    ]

batteries = load_real_data()
#batteries = load_example_data()

def part_1():
    joltages = []
    for bank in batteries:
        leftmost_largest = 0
        lindex = 0
        rightmost_largest = 0
        rindex = 0
        for i in range(len(bank)):
            bat = int(bank[i])
            if bat > leftmost_largest and i != len(bank)-1:
                leftmost_largest = bat
                lindex = i
        for i in range(len(bank)-1, lindex, -1):
            bat = int(bank[i])
            if bat > rightmost_largest:
                rightmost_largest = bat
                rindex = i
        joltages.append(int(bank[lindex]+bank[rindex]))

        print(leftmost_largest, rightmost_largest, lindex, rindex, str(leftmost_largest)+str(rightmost_largest))
    print(joltages)
    sum = 0
    for j in joltages:
        sum += j

    print("Sum:", sum)
        
def part_2():
    joltages = []
    for bank in batteries:
        batteries_left = 12
        bank_string = ''
        lindex = 0
        while batteries_left > 0:
            leftmost_largest = 0
            for i in range(lindex, len(bank)-batteries_left+1, 1):
                bat = int(bank[i])
                if bat > leftmost_largest:
                    leftmost_largest = bat
                    lindex = i
            bank_string += bank[lindex]
            lindex+=1
            batteries_left-=1
        print(bank)
        print(bank_string)
        joltages.append(int(bank_string))
    sum = 0
    for j in joltages:
        sum += j
    print("Sum:", sum)


#part_1()
part_2()

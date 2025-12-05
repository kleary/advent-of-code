import math

file_path = "day1-data.txt"

def load_real_data():
    f = open(file_path, 'r')
    r = f.readlines()
    r = r[0:-1]
    for index in range(len(r)):
        r[index] = r[index][0:-1]
    return r
rotations = load_real_data()
#rotations = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
#rotations = ["R1000", "L1000", "L50", "R1", "L1", "L1", "R1", "R100", "R1"]



def part_1():
    pointer = 50
    zero_counter = 0
    for rotation in rotations:
        dir = rotation[0]
        amount = int(rotation[1:])
        match dir:
            case "L":
                new_pointer = (pointer - amount) % 100
                pointer = new_pointer
            case "R":
                new_pointer = (pointer + amount) % 100
                pointer = new_pointer
        if pointer == 0: zero_counter+= 1

    print(zero_counter)

def part_2():
    pointer = 50
    zero_counter = 0
    for rotation in rotations:
        dir = rotation[0]
        amount = int(rotation[1:])
        match dir:
            case "L":
                new_pointer = (pointer - amount) % 100
                for i in range(amount):
                    pointer -= 1
                    if pointer == 0: zero_counter += 1
                    if pointer < 0: pointer += 100
                pointer = new_pointer
            case "R":
                new_pointer = (pointer + amount) % 100
                for i in range(amount):
                    pointer += 1
                    if pointer >= 100: pointer -= 100
                    if pointer == 0: zero_counter += 1
                pointer = new_pointer

    print(zero_counter)

part_1()
part_2()

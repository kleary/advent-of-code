import re

file_path = "day5-data.txt"

def load_real_data():
    f = open(file_path, 'r')
    l = f.readlines()
    data = {
            "ranges": [],
            "ingredients": []
            }
    switch = False
    for d in l:
        if d == '\n':
            switch = True
            continue

        if switch:
            data["ingredients"].append(d[0:-1])
        else:
            data["ranges"].append(d[0:-1])

    return data

def load_example_data():
    return {
            "ranges": [
                "3-5",
                "10-14",
                "16-20",
                "13-13",
                "12-18",
                "16-19",
                "16-20"
                ],
            "ingredients": [
                "1",
                "5",
                "8",
                "11",
                "17",
                "32"
                ]
            }

def part_1():
    fresh_count = 0
    for i in data["ingredients"]:
        fresh = False
        for r in data["ranges"]:
            s = r.split("-")
            low = int(s[0])
            high = int(s[1])


            if int(i) >= low and int(i) <= high:
                fresh = True
                break

        if fresh:
            fresh_count += 1

    print("part1 sum:", fresh_count)


def part_2():
    ranges = combine_ranges(quicksort(data["ranges"]))
    #ranges = combine_ranges(data["ranges"], len(data["ranges"]))

    sum = 0
    #print(len(ranges))
    for r in ranges:
        s = r.split('-')
        l = int(s[0])
        h = int(s[1])
        #print("sum: ", sum, "range:", r, "add:", (h-l)+1)
        sum += (h - l)+1
    print("part2 sum:", sum)
    #if sum <= too_low:
    #    print("Too Low")
    #elif sum in wrong:
    #    print("Wrong")


def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = int(arr[len(arr) // 2].split('-')[0])
    left = [x for x in arr if int(x.split('-')[0]) < pivot]
    middle = [x for x in arr if int(x.split('-')[0]) == pivot]
    right = [x for x in arr if int(x.split('-')[0]) > pivot]

    return quicksort(left) + middle + quicksort(right)

def add_commas(rang):
    s = rang.split('-')
    l = re.sub(r'(?<=\d)(?=(\d{3})+(?!\d))', ',', s[0])
    h = re.sub(r'(?<=\d)(?=(\d{3})+(?!\d))', ',', s[1])
    return(l+' - '+h)

def combine_ranges(range_array, length=0):
    a = []
    skip = {}
    #print(range_array)
    #print(length)
    ranges_combined = False
    combine_counter = 0
    for r1 in range(len(range_array)):
        if r1 in skip: continue
        skip[r1] = True
        s1 = range_array[r1].split('-')
        l1 = int(s1[0])
        h1 = int(s1[1])
        low = l1
        high = h1
        for r2 in range(len(range_array)):
            if r2 in skip: continue
            s2 = range_array[r2].split('-')
            l2 = int(s2[0])
            h2 = int(s2[1])
            #print(l1, h1, l2, h2)
            if low <= l2 and high >= l2:
                if h2 > high:
                    high = h2
                    #print("combining ranges", add_commas(range_array[r1]), add_commas(range_array[r2]), "into", add_commas(str(low)+'-'+str(high)))
                #else:
                #    print("range", add_commas(range_array[r2]), "is encapsulated by", add_commas(range_array[r1]))
                ranges_combined = True
                combine_counter += 1
                skip[r2] = True
        a.append(str(low)+'-'+str(high))
    #if len(a) != length:
    if ranges_combined:
        #print("counter", combine_counter, "diff", length-combine_counter)
        #print("ranges combined...")
        a = combine_ranges(a, len(a))
    return a


too_low = 301950474217081
wrong = {
        332344479044515: True,
        352106978766431: True,
        377688395105290: True,
        378575113276846: True
        }
data = load_real_data()
#data = load_example_data()
part_1()
part_2()



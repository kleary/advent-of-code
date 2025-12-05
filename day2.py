file = "day2-data.txt"

def load_real_data():
    f = open(file, 'r')
    s = f.read()
    s = s[0:-1]
    return s.split(',')

def load_example_data():
    e = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    return e.split(',')

def check_repeating_pattern_p1(start, end):
    i = start
    invalid_ids = []
    while(i <= end):
        s = str(i)
        if len(s) % 2 != 0: 
            i+=1
            continue
        half = int(len(s)/2)
        if s[0:half] == s[half:]:
            invalid_ids.append(i)
        i+=1
    return invalid_ids

def check_repeating_pattern_p2(start, end):
    i = start
    invalid_ids = []
    while i <= end:
        s = str(i)
        half = int(len(s)/2)
        if half == 0:
            i+=1
            continue
        invalid = True
        for j in range(half):
            p = s[0:j+1]
            invalid = True
            for k in range(0, len(s), len(p)):
                invalid = invalid and p == s[k:k+len(p)]
                #print("iter:", p, s, k, s[k:k+len(p)], invalid)
            if invalid:
                break
        if invalid: 
            print("invalid", i)
            invalid_ids.append(i)
        i+=1
    return invalid_ids

#data = load_example_data()
data = load_real_data()

def sum(part1 = False):
    invalid = []
    for id_range in data:
        s = id_range.split('-')
        start_id = int(s[0])
        end_id = int(s[1])
        if part1:
            invalid.extend(check_repeating_pattern_p1(start_id, end_id))
        else:
            invalid.extend(check_repeating_pattern_p2(start_id, end_id))

    sum = 0
    for id in invalid:
        sum += id

    print(sum)

#print(check_repeating_pattern_p2(998, 1012))
#print(check_repeating_pattern_p2(222220, 222224))
#print(check_repeating_pattern_p2(446443, 446449))
#print(check_repeating_pattern_p2(1698522, 1698528))
#print(check_repeating_pattern_p2(565653, 565659))
#print(check_repeating_pattern_p2(513438518, 513569318))
#print(check_repeating_pattern_p2(4, 14))
sum()

#Too High: 27469417443
#Correct: 27469417404

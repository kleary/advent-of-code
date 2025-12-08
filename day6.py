import re
file_path="day6-data.txt"

def load_real_data():
    f = open(file_path, 'r')
    arr = f.readlines()
    data = {
            "length": 0,
            "operand1": [],
            "operand2": [],
            "operand3": [],
            "operand4": [],
            "operation": [],
            "raw": arr
            }
    data["operand1"] = re.split(r'\s+', arr[0])[0:-1]
    data["operand2"] = re.split(r'\s+', arr[1])[0:-1]
    data["operand3"] = re.split(r'\s+', arr[2])[0:-1]
    data["operand4"] = re.split(r'\s+', arr[3])[0:-1]
    data["operation"]= re.split(r'\s+', arr[4])[0:-1]

    data["length"] = len(data["operand1"])
    return data

def part_1():
    sum = 0
    for i in range(0, data["length"]):
        op1 = int(data["operand1"][i])
        op2 = int(data["operand2"][i])
        op3 = int(data["operand3"][i])
        op4 = int(data["operand4"][i])
        match data["operation"][i]:
            case '+':
                sum += (op1 + op2 + op3 + op4)
            case '*':
                sum += (op1 * op2 * op3 * op4)
    print("Part 1 Total:", sum)

def part_2():
    sum = 0
    cursor = 0        
    digit_cursor = 0
    num_array = data["raw"]
    num_array[0] = num_array[0][0:-1]
    num_array[1] = num_array[1][0:-1]
    num_array[2] = num_array[2][0:-1]
    num_array[3] = num_array[3][0:-1]
    col_a = ['']
    col_b = ['']
    col_c = ['']
    col_d = ['']
    while cursor < len(num_array[0]):

        a = re.match(r'\d', num_array[0][cursor])
        b = re.match(r'\d', num_array[1][cursor])
        c = re.match(r'\d', num_array[2][cursor])
        d = re.match(r'\d', num_array[3][cursor])
        if a or b or c or d:
            col_a[digit_cursor]+= num_array[0][cursor]
            col_b[digit_cursor]+= num_array[1][cursor]
            col_c[digit_cursor]+= num_array[2][cursor]
            col_d[digit_cursor]+= num_array[3][cursor]
        else:
            digit_cursor+=1
            col_a.append('')
            col_b.append('')
            col_c.append('')
            col_d.append('')
        cursor += 1

    total = 0
    for index in range(len(data["operation"])):
        operation = data["operation"][index]
        nums = []
        for i in range(len(col_a[index])-1, -1, -1):
            nums.append(int(col_a[index][i]+col_b[index][i]+col_c[index][i]+col_d[index][i]))

        match operation:
            case '*':
                result = nums[0]
                for i in range(1, len(nums)):
                    result *= nums[i]
                total += result

            case '+':
                for num in nums:
                    total += num
                
    print("Part 2 total:", total)


data = load_real_data()
part_1()
part_2()

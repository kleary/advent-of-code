file_path = "day7-data.txt"

def load_example_data():
    data = [
        [".",".",".",".",".",".",".","S",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","^",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".","^",".","^",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".","^",".","^",".","^",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".","^",".","^",".",".",".","^",".",".",".","."],
        [".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
        [".",".",".","^",".","^",".",".",".","^",".","^",".",".","."],
        [".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
        [".",".","^",".",".",".","^",".",".",".",".",".","^",".","."], [".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
        [".","^",".","^",".","^",".","^",".","^",".",".",".","^","."],
        [".",".",".",".",".",".",".",".",".",".",".",".",".",".","."]
    ]
    return data

def load_real_data():
    file = open(file_path, 'r')
    d = file.readlines()
    data = []
    for i in range(len(d)):
        data.append([])
        for j in range(len(d[i])-1):
            data[i].append(d[i][j])
    return data
        


def day_1():
    beam_tree = {"root": []}
    start_index = 0
    start_depth = 1
    for i in range(len(diagram[0])):
        if diagram[0][i] == 'S':
            start_index = i
            break
    recursive_beam(start_index, start_depth, beam_tree)
    print("day 1:", len(beam_tree.keys())-1)
    
def recursive_beam(start_index=0, depth=0, beam_tree={}):
    while diagram[depth][start_index] != '^' and depth < len(diagram)-1: 
        depth+=1

    if str(start_index)+','+str(depth) in beam_tree:
        return

    if depth == len(diagram)-1:
        return

    beam_tree[str(start_index)+','+str(depth)] = diagram[depth][start_index]
    recursive_beam(start_index-1, depth+1, beam_tree)
    recursive_beam(start_index+1, depth+1, beam_tree)

def day_2():
    start_index = 0
    start_depth = 1
    for i in range(len(diagram[0])):
        if diagram[0][i] == 'S':
            start_index = i
            break

    total = recursive_timeline(start_index, start_depth)
    print("day 2:", total)

def recursive_timeline(start_index, depth, cache={}):
    count = 0
    while diagram[depth][start_index] != '^' and depth < len(diagram)-1:
        depth+=1

    if depth == len(diagram)-1:
        return 1

    cache_key = str(start_index)+','+str(depth)
    if cache_key in cache:
        return cache[cache_key]

    count += recursive_timeline(start_index-1, depth)
    count += recursive_timeline(start_index+1, depth)
    cache[cache_key] = count
    return count


diagram = load_real_data()
#diagram = load_example_data()
#print(diagram)
day_1()
day_2()

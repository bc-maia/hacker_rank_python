def solve(string):
    base_list = set(string.split())
    new_list = list(map(str.capitalize, base_list))
    # print(*zip(base_list, new_list))
    for old, new in zip(base_list, new_list):
        string = string.replace(old, new)
    return string


print(solve("heLLo worlD    heLLo!"))
print(solve("1 2 2 3 4 5 6 7 8  9"))

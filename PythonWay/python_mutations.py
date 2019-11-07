def mutate_string(string, position, character):
    return string[:position] + character + string[(position + 1):]

def mutate_string_alt_2(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string

def mutate_string_alt_3(string, position, character):
    replaced = []
    for index, chara in enumerate(list(string)):
        if index == position:
            chara = character
        replaced.append(chara)
    return "".join(replaced)


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


"""
Strings aren't mutables, so for that it needs to become a mutable structure, like a list

SAMPLE INPUT "abracadabra"
SAMPLE OUTPUT "abrackdabra"
"""

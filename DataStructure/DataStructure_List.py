#!/home/maia/.pyenv/versions/3.7.4/bin/python3
# -*- coding: utf-8 -*-


def get_commands(counter):
    command_list = []
    for _ in range(counter):
        cmd, *params = input().split(" ")
        command_list.append((cmd, params))
    return command_list


def execute(commands):
    data = []
    for command in commands:
        cmd, *params = command
        params = list(*params)
        data = parse(cmd, params, data)


def parse(cmd, param_list, data: list) -> list:
    if param_list:
        params = [int(value) for value in param_list]
        if cmd == "insert":
            data.insert(params[0], params[1])
        if cmd == "append":
            data.append(params[0])
        if cmd == "remove":
            data.remove(params[0])
    else:
        if cmd == "print":
            print(data)
        if cmd == "sort":
            data.sort()
        if cmd == "pop":
            data.pop()
        if cmd == "reverse":
            data.reverse()
    return data


if __name__ == "__main__":
    counter = int(input("enter how many commands to input: "))
    commands = get_commands(counter)
    execute(commands)

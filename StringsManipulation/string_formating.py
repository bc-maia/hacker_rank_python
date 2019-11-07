def print_formatted(number) -> None:
    padding = len(bin(number)) - 1
    for n in range(1, number + 1):
        values = [
            str(n).rjust(padding - 1),
            oct(n)[2:].rjust(padding),
            hex(n)[2:].upper().rjust(padding),
            bin(n)[2:].rjust(padding),
        ]
        formatted = "".join(values)
        print(formatted)


if __name__ == "__main__":
    n = int(input())
    print_formatted(n)

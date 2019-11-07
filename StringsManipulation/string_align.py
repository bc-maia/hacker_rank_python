# TODO: Replace all ______ with rjust, ljust or center.
def build_logo(thickness, letter="H") -> str:

    # Top Cone
    for i in range(thickness):
        yield (
            f"{(letter * i).rjust(thickness - 1)}{letter}{(letter * i).ljust(thickness - 1)}"
        )

    # Top Pillars
    for i in range(thickness + 1):
        yield (
            f"{(letter * thickness).center(thickness * 2)}{(letter * thickness).center(thickness * 6)}"
        )

    # Middle Belt
    for i in range((thickness + 1) // 2):
        yield ((letter * thickness * 5).center(thickness * 6))

    # Bottom Pillars
    for i in range(thickness + 1):
        yield (
            f"{(letter * thickness).center(thickness * 2)}{(letter * thickness).center(thickness * 6)}"
        )

    # Bottom Cone
    for i in range(thickness):
        yield (
            (
                f"{(letter * (thickness - i - 1)).rjust(thickness)}{letter}{(letter * (thickness - i - 1)).ljust(thickness)}"
            ).rjust(thickness * 6)
        )


if __name__ == "__main__":
    thickness = int(input())  # This must be an odd number

    for line in build_logo(thickness):
        print(line)

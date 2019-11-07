def check_validators(string, validators):
    for vl in validators:
        checker = list(map(vl, string))
        if True in checker:
            print(True)
        else:
            print(False)


if __name__ == "__main__":
    s = input()
    validators = [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]
    check_validators(s, validators)

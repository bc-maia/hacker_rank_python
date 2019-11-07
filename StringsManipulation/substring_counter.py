def count_substring(string, substring):
    pos = string.find(substring)
    substr_counter = 0
    if pos == -1:
        return substr_counter
    else:
        substr_counter += 1
        substr_counter += count_substring(string[pos + 1 :], substring)
        return substr_counter


if __name__ == "__main__":
    print(count_substring("I am an Indian, by birth.", "Birth"))

def get_word_count(string):
    words = string.split()
    return len(words)

def count_chars(string):
    char_count = {}
    for char in string:
        if char.lower() in char_count:
            char_count[char.lower()] += 1
        else:
            char_count[char.lower()] = 1
    return char_count

def sort_on(items):
    return items["num"]

def sort_chars(chars):
    sorted_chars = []
    for char in chars:
        tmp_dict = {}
        tmp_dict["char"] = char
        tmp_dict["num"] = chars[char]
        sorted_chars.append(tmp_dict)
    sorted_chars.sort(reverse=True,key=sort_on)
    return sorted_chars
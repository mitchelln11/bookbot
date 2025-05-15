def get_num_words(text):
    words = text.split()
    return len(words)

def find_unique_chars(text):
    unique_chars = {}
    lower_letter = text.lower()
    for char in lower_letter:
        if char not in unique_chars:
            unique_chars[char] = 1
        else:
            unique_chars[char] += 1
    return unique_chars

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

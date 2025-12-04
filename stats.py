def get_num_words(text):
    list_of_words = text.split()
    return len(list_of_words)

def get_num_chars(text):
    num_char = {}
    for char in text:
        if char.lower() not in num_char:
            num_char[char.lower()] = 0
        num_char[char.lower()] += 1
    return num_char

def sort_on(items):
    return items['num']

def get_sorted_dict(num_char):
    list_of_dict = []
    for key in num_char:
        list_of_dict.append({'char': key, 'num': num_char[key]})
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict

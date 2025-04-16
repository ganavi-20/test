def remove_common_letters(name1, name2):
    name1 = list(name1.lower().replace(" ", ""))
    name2 = list(name2.lower().replace(" ", ""))
    
    for letter in name1[:]:
        if letter in name2:
            name1.remove(letter)
            name2.remove(letter)

    return len(name1) + len(name2)

def flames_result(count):
    flames = list("FLAMES")
    while len(flames) > 1:
        split_index = (count % len(flames)) - 1
        if split_index >= 0:
            right = flames[split_index + 1:]
            left = flames[:split_index]
            flames = right + left
        else:
            flames = flames[:len(flames)-1]
    return flames[0]

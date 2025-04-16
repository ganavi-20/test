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
def get_relationship(letter):
    return {
        'F': 'Friends',
        'L': 'Love',
        'A': 'Affection',
        'M': 'Marriage',
        'E': 'Enemies',
        'S': 'Siblings'
    }[letter]

name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

count = remove_common_letters(name1, name2)
result_letter = flames_result(count)
relationship = get_relationship(result_letter)

print(f"\nRelationship between {name1} and {name2}: {relationship}")

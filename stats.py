
def get_num_words(text):
    num_words = len(text.split())
    return num_words

def get_num_characters(text):
    characters = {}
    text = text.lower()
    for c in text:
        if c in characters:
            characters[c]+=1
        else:
            characters[c]=1
    return characters

def get_sorted_characters(character_dict):
    character_list = []

    for char, count in character_dict.items():
        character_count_dict = {char: count}
        character_list.append(character_count_dict)

    def sort_on(dict):
        char = list(dict.keys())[0]
        return dict[char]
    
    character_list.sort(reverse=True, key=sort_on)

    return character_list

    





    
# The word_count function takes a string and returns the number of words
def word_count(text):
    return len(text.split())
    

# The char_count function takes a string and returns each character found, as
# well as a count of each character.
def char_count(text):
    characters = {}
    for char in text.lower(): #converting to lowercase
        if char.isalpha() and char in "abcdefghijklmnopqrstuvwxyz":
            if char not in characters:
                characters[char] = 0
            characters[char] += 1
    return characters

 
# The print_sorted function prints a sorted list of the character count as 
# found with the char_count function.
def print_sorted(char_count):
    # This is the sort_on_count used to sort the list
    def sort_on_count(item):
        return item["count"]
    
    char_list = []

    #print(char_count)

    # Pulling key-value pairs
    for char, count in char_count.items():
        if not char.isalpha():
            continue
        temp_dict = {"char": char, "count": count}
        char_list.append(temp_dict)
    
    # Sorting the list
    char_list.sort(reverse=True, key=sort_on_count)
    
    return char_list
        
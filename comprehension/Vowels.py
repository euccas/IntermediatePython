# Starting with a vowel
# Make a function that accepts a list of names and returns a new list containing all names that start with a vowel. It should work like this:
#
# >>> names = ["Alice", "Bob", "Christy", "Jules", "elliot"]
# >>> vowel_names(names)
# ['Alice', 'elliot']
# >>> names = ["Scott", "Arthur", "Jan", "Elizabeth"]
# >>> vowel_names(names)
# ['Arthur', 'Elizabeth']

def get_vowel_names(names):
    vowel_names = []
    for name in names:
        if name[0].lower() in 'aeiou':
            vowel_names.append(name)

    return vowel_names

def get_vowel_names_2(names):
    return [
        name
        for name in names
        if name[0].lower() in 'aeiou'
    ]


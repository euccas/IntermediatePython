# Write a generator that accepts a string and repeatedly prompts the user for input using that string as the prompt text.
#
# Example:
#
# >>> list(stop_on(input_loop("Say a name: "), ""))
# Say a name: Trey
# Say a name: Diane
# Say a name: Guido
# Say a name:
# ['Trey', 'Diane', 'Guido']
# >>> list(stop_on(input_loop("Say a name: "), ""))
# Say a name: Trey
# Say a name: Diane
# Say a name: Guido
# Say a name:
# ['Trey', 'Diane', 'Guido']

def input_loop(prompt):
    while True:
        in_string = input(prompt)
        yield in_string
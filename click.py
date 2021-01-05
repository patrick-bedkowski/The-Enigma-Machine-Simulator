from string import ascii_uppercase

alphabet = [letter for letter in ascii_uppercase]
print(alphabet)

def shift(seq, n):
    return seq[n:] + seq[:n]

print(shift(alphabet, 1))
letter = 'A'
print(alphabet.index(letter))

next_letter = shift(alphabet, 1)[alphabet.index(letter)]
print(next_letter)
'''detected_values_keys = []

key = 'A'
value = 'B'
detected_values_keys.extend([key, value])

print(detected_values_keys)'''

'''dictionary = {'A': 'B'}

if "B" in dictionary.values():
    return "A"
elif "A" in dictionary.keys():
    return "B"'''

'''from enigma import format_to_dict

dict1 = 'AB'
dict2 = 'A B'
dict3 = 'AB,CD'
dict4 = 'A B, C D'

print(format_to_dict(dict1))
print(format_to_dict(dict2))
print(format_to_dict(dict3))
print(format_to_dict(dict4))'''
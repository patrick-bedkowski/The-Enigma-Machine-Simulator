from string import ascii_uppercase

alphabet = [letter for letter in ascii_uppercase]

def shift(seq, n):
    return seq[n:] + seq[:n]

letter = 'A'
reflector_alphabet = shift(alphabet, 3) 
reversed_a = reflector_alphabet[::-1]

def reflect_letter(index):
    return reflector_alphabet[index]

litera = reflect_letter(reversed_a.index(letter))
print(letter)
print(reflector_alphabet)
print(reversed_a)
print(litera)
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
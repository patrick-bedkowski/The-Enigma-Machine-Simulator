from string import ascii_lowercase

alphabet = [letter for letter in ascii_lowercase]

def shift(seq, n):
    return seq[n:]+seq[:n]

print(alphabet[1:]+alphabet[:1])
print(shift(alphabet, 1))

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
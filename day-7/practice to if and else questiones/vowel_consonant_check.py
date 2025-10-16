c = input('Enter a single character: ')

if len(c) == 1 and c.isalpha():
    vowels = 'aeiou'
    if c.lower() in vowels:
        print('Vowel')
    else:
        print('Consonant')
else:
    print('Not a valid single alphabet character')

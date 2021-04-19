
def generate_braille_code_dictionary(code_initializer, braille_code_initializer):

    legal_characters = 'abcdefghijklmnopqrstuvwxyz '

    code_initializer_complete = True
    for character in legal_characters:
        if character not in code_initializer:
            code_initializer_complete =False

    braille_list = list(map(''.join, zip(*[iter(braille_code_initializer)]*6))) 

    def identify_capital_code(braille_code):
        if braille_code == '000001':
            return False
        else:
            return True

    braille_list = list(filter(identify_capital_code, braille_list))

    characters_list = list(code_initializer)

    braille_dictionary = dict(zip(characters_list, braille_list))

    braille_dictionary['uppercase'] = '000001'

    if code_initializer_complete == True:
        return braille_dictionary
    else:
        return 'Not enough letters in code_initializer to map code.'


braille_code_initializer = '0000010111101100101000100000001111101010010101001001001010000000001100001110\
1010101001011110111000000011010010101010110100000001011010100110110011110001110000000010101\
0111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110'

code_initializer = "The quick brown fox jumps over the lazy dog".lower()

my_braille_dict = generate_braille_code_dictionary(code_initializer, braille_code_initializer)


def translate_to_braille (message):

    braille_translation = ''
    

    for character in message:
        if character.isupper():
            braille_character = my_braille_dict['uppercase'] + my_braille_dict[character.lower()]
        else:
            braille_character = my_braille_dict[character]
       
        braille_translation = braille_translation + braille_character
    
    return braille_translation
    
test_message = 'The quick brown fox jumps over the lazy Dog'    
test = translate_to_braille(test_message)
print(test)

assert test == '000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000000001100110101010110110', "Translated code does not match Braille Witness Code."
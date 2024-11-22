#module to encrypt/decrypt using the Caesar cipher

#encryption or decryption, 
#return True if encryption or False if decryption
def get_encrypt_or_decrypt():
    
    while True:
        user_input = input('Input E for Encryption or D for Decryption: ')   
        if user_input.upper() == 'E':
            encryption = True
            break
        elif user_input.upper() == 'D':
            encryption = False
            break
        else:
            print('invalid input')
    return encryption

#get the key from the user + validation
def get_key():
    
    while True:
        try:
            key = int(input('What is the Ceasar key: '))
            break
        except ValueError:
            print('That was no valid number.  Try again...')
    
    #change the key to be between -26 to 26
    key = key % 26
    
    return key

#encode one character 
def encode_char(char,key):

    #using the building function to get the unicode
    unicode = ord(char)

    #detect if it is a lower case letter:
    if 97 <= unicode <= 122:
        unicode = (unicode + key - 97)%26 + 97
        
    #detect if it is an upper case letter:
    if 65 <= unicode <= 90:
        unicode = (unicode + key - 65)%26 + 65
        
    return chr(unicode)

#main function of the module             
def caesar(input_text, key):

    #double check the key is between -26 to 26
    key = key % 26
    
    #initialiation
    output_text = ''
    
    for char in input_text:
       
       output_text = output_text + encode_char(char,key)

    return output_text
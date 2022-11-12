alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt or 'decode' to decrypt: \n")     #string
value = input("Enter the letters:  \n").lower()                                 #string
shift = int(input("Enter the shift number:  \n"))    

def caesar(direction, value, shift):
        def encrypt(text, shift_number):
            cipher_text = ""
            for letters in text:
                position = alphabet.index(letters)
                new_position = position + shift_number
                new_letter = alphabet[new_position]
                cipher_text = cipher_text + new_letter
            print(f"The encoded text is: {cipher_text}")
    
        def decrypt(cipher_text, shift_number):
            value = ""
            for letters in cipher_text:
                position = alphabet.index(letters)
                new_position = position - shift_number
                new_letter = alphabet[new_position]
                value = value + new_letter
            print(f"The decoded text is: {value}") 
            
        if direction == "encode":
            encrypt(text=value, shift_number=shift)
        elif direction == "decode":
            decrypt(cipher_text=value, shift_number=shift)
        else:
            print("Enter the correct direction")                     

caesar(direction=direction, value=value, shift=shift)

    
        
  
    





    

    
    
    

    




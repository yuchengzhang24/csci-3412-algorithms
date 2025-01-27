# **********************************************************************
# Name        :  Yucheng Zhang
# Class       :  CSC 3412 Section 002
# Assignment  :  HW 1a Setting Up Python Development Environment
# Due Date    :  11/22/2024
# **********************************************************************

#encodes original message using substitution cipher
def encode_message(input_message, n):
  #initialize empty string
  encoded_message = ""
  #loop through input message and convert letter to unicode 
  for char in input_message:
    #check if char is an alphabetic character
    if char.isalpha():
      #check if the char is uppercase and initialize base to 65 (unicode 'A')
      if char.isupper():
        base = 65
      else:
        #else, char is lowercase and initialize base to 97 (unicode 'a')
        base = 97
      #convert char to unicode integer 
      #normalize integer by subtracting by base 
      #shift converted integer by value of n 
      #divide my modulo 26 to account for wrap-around
      scaled = (ord(char) - base + n) % 26
      #add back to base unicode 
      scaled += base
      #convert unicode back to character and concatenate onto encoded_message string
      encoded_message += chr(scaled)
    #check if char is a digit
    elif char.isdigit():
      #shift digit by value of n and use modulo 10 to account for wrap-around
      scaled = (int(char) + n) % 10
      #convert back to character and concatenate onto encoded_message string
      encoded_message += str(scaled)
    #concatenate non-alphabetic and non-digit characters as is
    else:
      encoded_message += char
  return encoded_message
  
#decodes the encoded message back to the original message 
def decode_message(encoded_message, n):
  #reverses substitution cypher by calling encode_message method by the negative factor of n 
  return encode_message(encoded_message, -n)

def main():
  #prompt user for integer between 1-25
  n = int(input("Enter an integer value (1-25): "))
  if n < 1 or 25 < n:
    print("Invalid input.")
    return

  #prompt user for message to encode
  input_message = input("Enter a message: ")
  #encode the message
  encoded_message = encode_message(input_message, n)
  #decode the message
  decoded_message = decode_message(encoded_message, n)

  #print expected output
  print()
  print("Input Message: ", input_message)
  print("Shift(n): ", n)
  print("Encoded Message: ", encoded_message)
  print("Decoded message: ", decoded_message)
  print()

if __name__ == "__main__":
    main()
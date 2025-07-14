# logic
import string
import random

def generate_random_password(char_no, int_no, special_no): 
  try:  
    # error handling for negative numbers"
    if char_no < 0 or int_no < 0 or special_no < 0:
      raise ValueError("Character, integer, and special character counts must be non-negative.")  
    small_letters = string.ascii_lowercase
    capital_letters = string.ascii_uppercase
    numbers = string.digits
    special_character = string.punctuation
    #generating random characters
    letter = "".join(random.choices(small_letters + capital_letters, k=char_no))
    integer = "".join(random.choices(numbers,k=int_no))
    special = "".join(random.choices(special_character,k=special_no))
    #combining all the characters  
    return "".join(random.sample(letter + integer + special,len(letter + integer + special)))
  except ValueError as e:
     print("Error:", e)
#example usage
if __name__ == "__main__":
    try:
        char_no = int(input("enter the number of characters:"))
        int_no = int(input("enter the number of integers:"))
        special_no = int(input("enter the number of special characters:"))
        password = generate_random_password(char_no, int_no, special_no)
        print("generated password: ",password)
    except ValueError as e:
      print("Error:", e)
      
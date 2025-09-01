import random
import string

# indices = list(range(16))
# num_indices = 16
# random_index = random.sample(indices, num_indices)
# #print(random_index)

def uppercase_letter():
    """ returns uppercase of all letters in alphabets """
    return random.choice(string.ascii_uppercase)


def lowercase_letter():
    """ returns lowercase of all letters in alphabets """
    return random.choice(string.ascii_lowercase)

def spclcase_letter():
    """ returns all special characters """
    return random.choice(string.punctuation)

def num():
    """ returns all numbers from 0 to 9 """
    return random.choice(string.digits)

#spcl = spclcase_letter()
#print(spcl)

def password_generator(length=16):
    """ generates random string of 16 values containing atleast 1 uppercase, 1 lowercase, 
    1 spcl character, 1 number from 0 to 9"""

    if length < 16:
        raise ValueError("The length must always be 16")

    must_char = [uppercase_letter(), lowercase_letter(), spclcase_letter(), num()]

    remaining_len = length - len(must_char)
    all_char = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    random_chars = random.choices(all_char, k=remaining_len)

    password = must_char + random_chars

    random.shuffle(password)
    return "".join(password)

final_password = password_generator()
print(f"Your Password is:",final_password)




    
    

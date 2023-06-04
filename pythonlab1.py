#read string of 4 characters from user .convert every character in string to its next alphabet
def LetterChange(st):
    index=0
    new_word=""
    sample="abcdefghijklmnopqrstuvwxyz"
    if(len(st)==4):
        for i in st.lower():
            if i.islower():
                index=sample.index(i)+1
                new_word+=sample[index]
            else:
                new_word+=i
    return new_word.upper()

print(LetterChange(input("Enter 4 letter characters: ")))

'''
#using built in functions

def convert_to_next_alphabet(string):

    result = ""
    for chi in string:
        if chi.isalpha():
            if chi == 'z':

                result += 'a'
            elif chi == 'Z':

                result += 'A'
            else:

                result += chr(ord(chi) + 1)
        else:

            result += chi
    return result


# Read the input string from the user

input_string = input("Enter a string of 4 characters: ")


if len(input_string) != 4:

    print("Please enter a string with exactly 4 characters.")
else:

    converted_string = convert_to_next_alphabet(input_string)

    print("Converted string:", converted_string)


'''
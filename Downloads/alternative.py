#defined a function called alternate characters to apply to input_string
def alternate_characters(input_string):
    result = ""
    for i, char in enumerate(input_string): #used a for loop to iterate through characters in string and alternate between upper and lower case 
        if i % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
    return result

def alternate_words(input_string): #defined a function called alternate words to apply to input_string
    words = input_string.split() #used split() to separate input_string into individual words and alternate cases 
    result = ""
    for i, word in enumerate(words):
        if i % 2 == 0:
            result += word.lower()
        else:
            result += word.upper()
        result += " "
    return result.rstrip() 

input_string = "Here is an example" #entered input_string
output_string1 = alternate_characters(input_string)
print(f"{output_string1}") #printed input_string with alternate characters (output_string1)

output_string2 = alternate_words(input_string)
print(f"{output_string2}") #printed input_string with alternate words (output_string2)


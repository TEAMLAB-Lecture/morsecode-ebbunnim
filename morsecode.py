# -*- coding: utf8 -*-
import re

# Help Function - 수정하지 말 것
def get_morse_code_dict():
    morse_code = {
        "A": ".-", "N": "-.", "B": "-...", "O": "---", "C": "-.-.", "P": ".--.", "D": "-..", "Q": "--.-", "E": ".",
        "R": ".-.", "F": "..-.", "S": "...", "G": "--.", "T": "-", "H": "....", "U": "..-", "I": "..", "V": "...-",
        "K": "-.-", "X": "-..-", "J": ".---", "W": ".--", "L": ".-..", "Y": "-.--", "M": "--", "Z": "--.."
    }
    return morse_code


# Help Function - 수정하지 말 것
def get_help_message():
    message = "HELP - International Morse Code List\n"
    morse_code = get_morse_code_dict()

    counter = 0

    for key in sorted(morse_code):
        counter += 1
        message += "%s: %s\t" % (key, morse_code[key])
        if counter % 5 == 0:
            message += "\n"

    return message


def is_help_command(user_input):
    return user_input.lower() in ('h,help')


def is_validated_english_sentence(user_input):
    regex=re.compile("[0-9]|[\_\@\#\$\%\^\&\*\(\)\-\+\=\[\]\{\}\"\'\;\:\|\`\~]")
    mo=regex.search(user_input)
    if mo:
        return False
    regex=re.compile("[^.,!?]")
    if ''.join(regex.findall(user_input)).rstrip()=='':
        return False
    return True


def is_validated_morse_code(user_input):
    regex=re.compile("[^-.\s]")
    mo=regex.search(user_input)
    if mo:
        return False
    morse=user_input.split()
    morse_values=get_morse_code_dict().values()
    for mor in morse:
        if mor not in morse_values:
            return False
    return True


def get_cleaned_english_sentence(raw_english_sentence):
    regex=re.compile("[^.,!?\s]+")
    return ' '.join(regex.findall(raw_english_sentence))


def decoding_character(morse_character):
    morse_code_dict=get_morse_code_dict()
    for key,val in morse_code_dict.items():
        if morse_character==val:
            return key 


def encoding_character(english_character):
    morse_code_dict=get_morse_code_dict()
    return morse_code_dict.get(english_character)


def decoding_sentence(morse_sentence):
    morse_sentence=re.sub("\s\s","*",morse_sentence)
    res=morse_sentence.split('*')
    ans=''
    for r in res:
        tmp=r.split()
        for t in tmp:
            ans+=decoding_character(t)
        ans+=' '
    return ans[:-1]


def encoding_sentence(english_sentence):
    sentence=get_cleaned_english_sentence(english_sentence)
    ans=''
    for c in sentence:
        if c==' ':
            ans+=c
            continue
        ans+=encoding_character(c.upper())
        ans+=' '
    return ans[:-1]


def main():
    print("Morse Code Program!!")
    # ===Modify codes below=============
    while True:
        user_input=input("Input your message(H - Help, 0 - Exit): ")
        if user_input=='0':
            break
        elif is_help_command(user_input):
            print(get_help_message())
        elif is_validated_english_sentence(user_input):
            print(encoding_sentence(user_input))
        elif is_validated_morse_code(user_input):
            print(decoding_sentence(user_input))
        else:
            print("Wrong Input")

        
    # ==================================
    print("Good Bye")
    print("Morse Code Program Finished!!")

if __name__ == "__main__":
    main()

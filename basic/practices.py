def determine(text):
    text = text.strip().replace(' ','')
    text_palindrome = text[::-1]
    
    if text == text_palindrome:
        print("Is a palindrome")
    
    else:
        print("Not a palidrome")


def information():
    text = str(input("Write a word or a phrase: "))
    determine(text)


if __name__ == "__main__":
    information()




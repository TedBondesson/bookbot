def main():
    text = get_text(".gitignore/books/frankenstein.txt")
    num_words = get_num_words(text)
    letters = get_characters(text)
    print("Book report")
    print(f"{num_words} words found in the document")    
    for char in letters:
        print(f"the {char} character was found {letters[char]} times")   
       
    

def get_text(path):
    with open(path) as f: 
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_characters(text):
    letters = {}
    lower = text.lower()
    for i in range(len(lower)):
        character = lower[i]
        if character.isalpha(): 
            if character in letters:
                letters[character] = letters[character] + 1 
            else:
                letters[character] = 1 
    return letters 




main()

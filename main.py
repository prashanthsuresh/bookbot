with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def word_count(txt):
    return len(txt.split())

def character_counts(text):
    counts = {}
    text = text.lower()
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    for key, value in counts.items():
        if key.isalpha():    
            print(f"The '{key}' character was found {value} times.")

print (f"The document contains {word_count(file_contents)}  words.")  
print(character_counts(file_contents))

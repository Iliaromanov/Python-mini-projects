
text = input("Text: ")


def count_letters(text: str) -> int:
    letters = 0
    for char in text:
        if char.isalpha():
            letters += 1
    return letters
            

def count_words(text: str) -> int:
    words = 1
    for char in text:
        if char == " ":
            words += 1
    return words


def count_sentences(text: str) -> int:
    sentences = 0
    for char in text:
        if char in ".!?":
            sentences += 1
    return sentences


def calculate_grade(letters: int, words: int, sentences: int) -> str:
    # average number of letters per 100 words in the text
    L = round(letters / words * 100)
    # average number of sentences per 100 words in the text
    S = round(sentences / words * 100)
    
    # Coleman-Liau formula
    grade = round(0.0588 * L - 0.296 * S - 15.8)
    if grade < 0:
        return "Before Grade 1"
    elif grade < 16:
        return f"Grade {grade}"
    else:
        return "Grade 16+"
  

# Use above functions to calculate reading level of users text
grade = calculate_grade(count_letters(text), count_words(text), count_sentences(text))
print(grade)

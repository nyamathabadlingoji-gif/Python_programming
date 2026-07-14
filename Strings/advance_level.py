
# Capitalize the First Letter of Every Word (Without Using .title())


def capitalize_words(s):
    result = ""
    new_word = True

    for ch in s:
        if ch == " ":
            result += ch
            new_word = True
        elif new_word:
            if 'a' <= ch <= 'z':
                result += chr(ord(ch) - 32)
            else:
                result += ch
            new_word = False
        else:
            result += ch

    return result

text = "python programming language"
print(capitalize_words(text))


# Remove All Duplicate Words from a Sentence
def remove_duplicate_words(sentence):
    words = sentence.split()
    seen = []
    result = []
    for word in words:
        if word not in seen:
            seen.append(word)
            result.append(word)
    return " ".join(result)
text = "python is easy python is powerful"
print(remove_duplicate_words(text))

# Check Whether a String Contains Only Digits
def only_digits(S):
    for ch in s:
        if not('0' <= ch <= '9'):
            return False
        return True
print(only_digits("12333456"))
print(only_digits("123a"))


# Check Whether a String Contains Both Letters and Number
def remove_punctuation(s):
    punctuation = "!@#$%^&*#@!!!@#$%^&&&*"
    result = ""
    for ch in s:
        if ch not in punctuation:
            result += ch
        return result
    
text = "Hello,world ! welcome."
print(remove_punctuation(text))
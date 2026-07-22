"""
Q99. Vowel-Starting Words

Take a sentence as input. Split it into words and print how many words start
with a vowel.
"""

def count_vowels(sentence):
    vowels = "aeiouAEIOU"          # or        vowels = "aeiouAEIOU"
    count = 0
    words = sentence.split()
    for word in words:
        if word[0] in vowels:             #if word in vowels
            count += 1
    return count

sentence = "This is araveen Muttappa unagar "
print(count_vowels(sentence))
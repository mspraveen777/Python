"""
Q102. Longest Word

Take a sentence as input. Print the longest word in it.
"""
def longest_word(sentence):
    # longest = 0
    words = sentence.split()
    print(max(words,key=lambda x:len(x)))
    # for word in words:
    #     leng = len(word)
    #     if leng > longest:
    #         longest = leng
    #         long_word = word
    # print(long_word)
    
sentence = "This is Praveen From Bengaluru, I am coder"
longest_word(sentence)
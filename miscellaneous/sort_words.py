def sort_words(sentence):
    words = sentence.split()
    words = [ word.lower() + word for word in words]
    words.sort()
    words = [word[len(word)//2:] for word in words]
    return ' '.join(words)

sorted = sort_words('Blue green apple Admit bag of Salt')
print(sorted)
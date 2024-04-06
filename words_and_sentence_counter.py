def count_words(text):
    words = text.split()
    return len(words)

def count_sentences(text):
    sentences = text.split('.')
    return len(sentences)

if __name__ == "__main__":
    input_text = input("Enter a text: ")
    word_count = count_words(input_text)
    sentence_count = count_sentences(input_text)
    
    print("Number of words:", word_count)
    print("Number of sentences:", sentence_count)

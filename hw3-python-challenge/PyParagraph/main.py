# Analyze passages with simple metrics
# 2018-04-29

# Define a function that analyzes passages with simple metrics
def main(directory, file_name):

    """
    input: 
        directory - str, folder of the csv file
        file_name - str, name of the csv file including extension
    output:
        word_count - int, total number of words
        sentence_count - int, total number of sentences
        average_sentence_length - float, average length of each sentence
        average_letter_count - float, average length of each word
    """

    import os
    import re

    # Specify file path
    file_path = os.path.join(directory, file_name)

    # Read the paragraph into a string
    with open(file_path, 'r') as file_in:
        paragraph = file_in.read()

    # Read paragraph into a list of sentences
    lines = paragraph.split('\n')
    sentences_clean = []
    for line in lines:
        sentences_rough = line.strip().split('. ')
        for sentence in sentences_rough:
            if len(sentence) > 0:
                sentences_clean.append(sentence)

    # Read sentences into a list of words
    words_clean = []
    for sentence in sentences_clean:
        words_rough = sentence.strip().split(' ')
        for word_rough in words_rough:
            word_clean = word_rough.strip().strip('(),.!?;:{}[]><""/\\').lower()
            if len(word_clean) > 0:
                words_clean.append(word_clean)

    # Calculate total number of letters
    letters_total = 0
    for word in words_clean:
        letters_total += len(word)

    # Calculate metrics
    word_count = len(words_clean)
    sentence_count = len(sentences_clean)
    average_sentence_length = float(word_count) / sentence_count
    average_letter_count = float(letters_total) / word_count

    # Print results to terminal
    line1 = "Paragraph Analysis"
    line2 = "-" * 25
    line3 = f"Approximate Word Count: {word_count}"
    line4 = f"Approximate Sentence Count: {sentence_count}"
    line5 = f"Average Letter Count: {average_letter_count}"
    line6 = f"Average Sentence Length: {average_sentence_length}"
    results = [line1, line2, line3, line4, line5, line6]
    for line in results:
        print(line)

    # Write results to a text file
    output_file_path = file_name.split('.')[0] + '_output.txt'
    with open(output_file_path, 'w', newline = '') as file_out:
        for line in results:
            file_out.write(line + '\n')

    return sentences_clean, words_clean

# Analyze text file using the defined function
directory = 'raw_data'
file_name = 'paragraph_1.txt'
sentences1, words1 = main(directory, file_name)

# Analyze text file using the defined function
directory = 'raw_data'
file_name = 'paragraph_2.txt'
sentences2, words2 = main(directory, file_name)
vowels = 'aeiou'
while True:
    sentence = input("Enter a sentence (or type 'exit' to quit): ")
    if sentence.lower() == 'exit':
        break
    vowel_count = 0
    for letter in sentence.lower():
        if letter in vowels:
            vowel_count += 1
    print(f"Number of vowels in the sentence: {vowel_count}")
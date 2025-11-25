def count_each_word(sentence):
    count_word = {}
    for i in sentence:
        if i not in count_word:
            count_word[i] = 1

        else:
            count_word[i] += 1 
    return count_word

try:
    sentence = input("Enter your sentence : ").lower().split()

    word = count_each_word(sentence)
    print("Cout each word's : ",word)

except ValueError:
    print("Invalid Input, Please try again")
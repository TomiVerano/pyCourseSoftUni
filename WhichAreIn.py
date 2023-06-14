def sub_string_find():
    words_sentence = input().split(', ')
    words_sub_string = input().split(', ')
    result_string = []
    for word_sent in words_sentence:
        for word_sub in words_sub_string:
            if word_sent in word_sub:
                result_string.append(word_sent)
                break
    print(result_string)


sub_string_find()


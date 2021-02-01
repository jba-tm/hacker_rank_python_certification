def reverse_words_order_and_swap_cases(sentence):
    arr = sentence.split(' ')
    text = ' '.join(arr[::-1])
    return ''.join([i.lower() if i.isupper() else i.upper() for i in text])


if __name__ == '__main__':
    sentence = 'aWESOME is cODING ffadsfsd afds sdfa asdf adf'

    result = reverse_words_order_and_swap_cases(sentence)

    print(result)

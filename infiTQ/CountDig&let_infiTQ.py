'''
Write a python function which accepts a sentence and finds the number of letters and digits in the sentence.

It should return a list in which the first value should be letter count and second value should be digit count. Ignore the spaces or any other special character in the sentence.

Sample Input      Expected Output

Infosys 123      [7,3]

ABCEFG           [6,0]

'''
def count_digits_letters(sentence):
    dig=0
    let=0
    for i in sentence:
        if i.isdigit():
            dig+=1
        elif i.isalpha():
            let+=1

    result_list=list([let,dig])
    return result_list

sentence="Infosys Mysore 570027"
print(count_digits_letters(sentence))
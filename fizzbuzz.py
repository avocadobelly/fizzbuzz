#Write a program that prints the numbers from 1 to 100.
#If a number is a multiple of three, print "Fizz" instead of the number.
#If the number is a multiple of five print "Buzz" instead of the number.
#For numbers which are multiples of both three and five print "FizzBuzz" instead of the number.
#If a number is a multiple of 7, print "Bang" instead of the number.
# For numbers which are multiples of seven and three / five, append Bang to what you'd have printed anyway. (E.g. 3 * 7 = 21: "FizzBang").
#If a number is a multiple of 11, print "Bong" instead of the number. Do not print anything else in these cases. (E.g. 3 * 11 = 33: "Bong")
#If a number is a multiple of 13, print "Fezz" instead of the number.
# For multiples of most other numbers, the Fezz goes immediately in front of the first thing beginning with B, or at the end if there are none



i = 0

while i < 300:
    i = i + 1

    word = []

    if i % 3 == 0:
        word.append('fizz')
    if i % 5 == 0:
        word.append('buzz')
    if i % 7 == 0:
        word.append('bang')
    if i % 11 == 0:
        word = ['bong']
    if i % 13 == 0:
        added_fezz = False
        for k,j in enumerate(word):
            if j[0] == 'b':
                word.insert(k, 'fezz')
                added_fezz = True
                break
        if not added_fezz:
            word.append('fezz')
    if i % 17 == 0:
        #reverse the order the items in the array are printed
        reverse = []
        last = len(word)
        if word:
            for p in range (1, last + 1):
                reverse.append(word[-p])
        word = reverse
    if word:
        print(''.join(word))
    else:
        print(i)
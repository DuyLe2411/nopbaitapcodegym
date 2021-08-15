dictionary = {
            'time': 'Thời gian',
            'people': 'Con người',
            'road': 'Con đường',
            'school': 'Trường học',
            'family': 'Gia đình',
            'room': 'Căn phòng' 
           }
english_word = input("Nhập từ bạn cần dịch: ")


def translate(dictionary):
    global english_word
    for item in dictionary:
        if english_word == item:
           
            return item + " : " + dictionary[item]

translate_word = translate(dictionary)
if translate_word:
    print(translate_word)
else:
    print(english_word, " not in the dictionary")


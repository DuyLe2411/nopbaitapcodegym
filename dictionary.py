dictionary = {
            'time': 'Thời gian',
            'people': 'Con người',
            'road': 'Con đường',
            'school': 'Trường học',
            'family': 'Gia đình',
            'room': 'Căn phòng' 
           }
english_word = input("Nhập từ bạn cần dịch: ")
word = True

def translate(dictionary):
    global english_word
    for item in dictionary:
        if english_word == item:
            word = False
            return print(item + " : " + dictionary[item])
if word:
    translate(dictionary)
else:
    print(english_word + ' không có trong hệ thống' )



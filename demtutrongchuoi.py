message = '''This is a common message for people, message is private and circulate this with caution'''

def count_words(word):
    word = word.lower()
    mes = message.lower().split()
    num = mes.count(word)
    if word in mes:
        print(f"Số lần từ {word} trong chuỗi là: {num}" )
    else:
        print("Không có từ này")

word = input("Nhập từ bạn muốn tìm trong chuỗi: ")
count_words(word)
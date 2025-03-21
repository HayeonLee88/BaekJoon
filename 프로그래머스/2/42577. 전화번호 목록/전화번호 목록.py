'''
4:04~4:08
'''
def solution(phone_book):
    answer = True
    phone_book.sort()
    prev = phone_book[0]
    for i in range(1, len(phone_book)):
        if phone_book[i][:len(prev)] == prev:
            return False
        prev = phone_book[i]
    return answer
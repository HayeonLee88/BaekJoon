'''
4:59~
'''
def solution(numbers):
    answer = ''
    nums = [str(num) for num in numbers]
    nums.sort(reverse=True, key=lambda x: x*3)
    
    answer = ''.join(nums).lstrip('0')
    if answer == '':
        return '0'
    return answer
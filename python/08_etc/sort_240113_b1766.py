# 문제집 (gold 2, 48.816%)
# source : https://www.acmicpc.net/problem/1766
# keyword : 
# return : 

"""
1. 문제
- 

2. 입력 및 제한
- 

3. 로직
- 공백만 주어지는 경우도 고려
- (단어 - 암호키) % 26
    - a - y = 97 - 122 = -24 => 2(b) = 99
    - c - a = 99 - 97 = 2 => 2(b)
    - e - e = 0 => -1 + 97
"""

def solution(sentence, key):
    encrypted = ''
    for i in range(len(sentence)):
        if sentence[i] != ' ':
            encrypted_num = (ord(sentence[i]) - ord(key[i%len(key)]) - 1) % 26
            encrypted += chr(encrypted_num+ord("a"))
        else:
            encrypted += ' '
    return encrypted


def check(func, inputs, outputs):
    print(f"Check {func.__name__}")
    result = func(*inputs)
    print(result, True if result == outputs else False)
        

if __name__ == '__main__':
    test_cases = [(["nice day", "love"], "btgz oet")]
    for i, o in test_cases:
        check(solution, i, o)
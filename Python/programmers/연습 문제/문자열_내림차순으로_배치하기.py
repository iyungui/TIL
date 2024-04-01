# def solution(s):
#     answer = ''
#     data = []
#     for i in s:
#         data.append(int(ord(i)))
#     data.sort(reverse=True)
    
#     for i in data:
#         answer += chr(i)
    
#     return answer

def solution(s):
    return ''.join(sorted(s, reverse=True))

print(solution("Zbcdefg"))
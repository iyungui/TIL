# def solution(n, lost, reserve):
#     for i in reserve:
#         for j in lost:
#             if i not in lost and ((i - j) == 1 or (i - j) == -1):
#                 lost.remove(j)
#     answer = n - len(lost)
#     return answer

def solution(n, lost, reserve):
    # 여벌 체육복이 있으면서 도난당한 학생 처리
    set_reserve = set(reserve) - set(lost) 
    set_lost = set(lost) - set(reserve)
    for i in set_reserve:
        for j in set_lost:
            if (i - j) == 1 or (i - j) == -1:
                set_lost.remove(j)
    answer = n - len(set_lost)
    return answer
    
#     for r in set_reserve:
#         if r - 1 in set_lost:
#             set_lost.remove(r - 1)
#         elif r + 1 in set_lost:
#             set_lost.remove(r + 1)
    
#     answer = n - len(set_lost)
#     return answer



# for i in reserve:
#   for j in lost:
#       if i not in lost and ((i - j) == 1 or (i - j) == -1):
#           lost.remove(j)
# answer = n - len(lost)

# 최대한 많은 학생이 체육복을 가지고 있어야 함, 
# 즉, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost을 보고, 최대한 많은 학생이 체육복을 가지도록 해야함.
# 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve 에 있는 학생의 번호[i] && lost에 담긴 학생의 번호[j]의 차이가 1 일 경우, i번 학생이 j번 학생에게 체육복이 없는 학생에게 체육복을 빌려줄 수 있다.
# 그런데, reserve 에 있는 값이 lost에도 있을 수 있다. 만약, 그 경우에는 그 reserve 의 값은, 다른 사람에게 체육복을 못빌려준다. 

# 체육수업 가능한 학생 수 answer = 전체학생 n - len(lost)
# 주어진 예외조건(reserve에도 있고, lost에도 있는 경우) 를 고려하여,
# lost 의 길이를 최소화 해야함.

# for i in reserve:
#   for j in lost:
#       if i not in lost and ((i - j) == 1 or (i - j) == -1):
#           lost.remove(j)
# answer = n - len(lost)




# 주어진 조건 중, '중복되는 값은 없다' 라는 걸 보면, 집합(set) 사용을 고려해야 한다.
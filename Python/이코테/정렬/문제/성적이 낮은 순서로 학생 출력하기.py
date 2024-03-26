n = int(input())

# n 명의 학생 정보를 입력받아 리스트에 저장. 학생의 이름만 출력하면 되므로, 학생 정보를 (이름, 점수) 로 묶어서 입력 받고, 리스트에 append
data = []
for _ in range(n):
    input_data = input().split()
    data.append((input_data[0], int(input_data[1])))

# key 를 이용하여, 점수를 기준으로 정렬
data = sorted(data, key=lambda student: student[1])

# 정렬이 수행된 결과를 출력
for student in data:
    print(student[0], end=' ')

# 16번. 정사각형 형태의 지그재그 패턴으로 연속된 숫자 출력 프로그램

length = int(input("한 변의 길이(정수)를 입력하세요 : ")) # 한 변의 길이를 입력받아 정수 형태로 저장
list = [] # 지그재그 패턴의 숫자를 저장할 리스트
num = 1 # 각 열에 들어갈 변수 1로 초기화 (1~length*length)

for i in range(length): # 한 변의 길이만큼 length행 반복
    row = []  # 한 행을 저장할 리스트

    if i % 2 == 0: # 짝수 행일 경우 (0, 2, 4, ...행)
        for j in range(length): # 한 변의 길이만큼 length열 for문 (j는 0부터 length-1까지 하나씩 증가)
            row.append(num) # 현재 num (= 1)을 리스트 row에 추가
            num += 1 # 1만큼 증가 (오른쪽으로 이동한 숫자)
    else: # 홀수 행일 경우 (1, 3, 5, ...행)
        for j in range(length): # 한 변의 길이만큼 length열 for문 (짝수 행과 동일)
            row.append(num) # 현재 num (= 1)을 리스트 row에 추가
            num += 1 # 1만큼 증가 (오른쪽으로 이동한 숫자)
        row.reverse() # 숫자 리스트를 뒤집어서 반대 순서로 저장 (큰 수 -> 작은 수 순서)

    list.append(row) # 행을 전체 리스트인 list에 추가

# 출력
for row in list: # 리스트의 행만큼 반복
    for n in row: # 한 행의 열만큼 반복
        print("{:3}".format(n), end=" ")
         # 세 자리 수를 기준으로 오른쪽 정렬
         # end=" " 를 추가하여 각 열별 개행 대신 공백 추가
    print() # 한 행마다 개행 추가


# 17번. 풍차 모양으로 별 출력
# 1~5번째 줄
for i in range(5): # 0~4행 동안 반복
    for j_1 in range(i): # 0부터 i까지 반복 (0~4)
        print(" ",end="") # j_1번 동안 공백을 반복적으로 출력
    for j_2 in range(5-i): # 0부터 5-i까지 반복 (점점 감소) (5~1)
        print("*",end="") # j_2번 동안 *을 반복적으로 출력
    for j_3 in range(5-(i+1)): # 0부터 5-(i+1)까지 반복 (점점 감소) (4~0)
        print(" ",end="") # j_3번 동안 공백을 반복적으로 출력
    for j_4 in range(i+1): # 0부터 i+1까지 반복
        print("*",end="") # j_4번 동안 *을 반복적으로 출력 (1~5)
    print() # 각 행별 개행 추가

# 6~10번째 줄
for k in range(5): # 5~9행 동안 반복
    for l_1 in range(5-k): # 0부터 5-k까지 반복 (점점 감소) (5~1)
        print("*",end="") # l_1번 동안 *을 반복적으로 출력
    for l_2 in range(k): # 0부터 k까지 반복 (0~4)
        print(" ",end="") # l_2번 동안 공백을 반복적으로 출력
    for l_3 in range(k+1): # 0부터 k+1까지 반복 (1~5)
        print("*",end="") # l_3번 동안 *을 반복적으로 출력
    for l_4 in range(5-(k+1)): # 0부터 5-(k+1)까지 반복 (점점 감소) (4~0)
        print(" ",end="") # l_4번 동안 공백을 반복적으로 출력
    print() # 각 행별 개행 추가
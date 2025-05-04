# 11번. 문자열을 공백 기준으로 자르는 프로그램(중, 2점)
# Boolean, in, 문자열 내장함수(index), 문자열 슬라이싱
str1 = "Hello World!!" # str1에 문자열 저장

if " " in str1 : # str1에 공백이 있을 경우,
    print("공백이 들어있어, 문자열을 공백 기준으로 나눕니다.")

    # str1에서 공백의 위치를 찾아서 수동으로 문자열 슬라이싱 해줌
    space = str1.index(" ") # 문자열 str1에서 첫 번째 공백을 찾아 반환 -> space = 5
    split_str1 = str1[:space] # str1의 시작부터 space(= 5) 직전까지 잘라서 split_str1에 저장
    split_str2 = str1[space + 1:] # space 다음부터 끝까지 str1을 잘라서 split_str2에 저장
    print(split_str1) # 공백 기준 앞쪽 저장된 문자열 출력
    print(split_str2) # 공백 기준 뒤쪽 저장된 문자열 출력


# 13번. 숫자 2개, 연산자 1개를 계산 (중, 2점)
# input 함수, 비교 연산자, Boolean, 자료형 캐스팅, 문자열 형식화
# if문

num1 = input("정수 입력 > ") # 정수를 입력 받아서 변수 num1에 저장(string)
num2 = input("정수 입력 > ") # 정수를 입력 받아서 변수 num2에 저장(string)
op = input("+, - ,*, / 중 하나 입력 > ") # 연산자를 입력 받아서 변수 op에 저장
result = 0 # 계산 결과값을 저장할 변수 result 

if op == "+": # op가 문자열 "+"일 경우,
    result = int(num1) + int(num2) # num1, num2는 string이므로 int 함수로 형변환
if op == "-": # op가 문자열 "-"일 경우,
    result = int(num1) - int(num2) # num1, num2의 - 연산
if op == "*": # op가 문자열 "*"일 경우,
    result = int(num1) * int(num2) # num1, num2의 * 연산
if op == "/": # op가 문자열 "/"일 경우,
    result = int(num1) / int(num2) # num1, num2의 / 연산

print("{} {} {} = {}".format(num1, op, num2, result))
# format 함수를 이용해서 문자열 출력
# {} 안에 들어갈 변수를 순서대로 대입


# 14번. 13번 프로그램에서 연산자 입력의 예외처리가 추가된 프로그램 (중, 2점)
#input 함수, 멤버십 연산자(in), 비교 연산자, Boolean, 자료형 캐스팅, 문자열 형식화
#if문, else문

num1 = input("정수 입력 > ") # 정수를 입력 받아서 변수 num1에 저장(string)
num2 = input("정수 입력 > ") # 정수를 입력 받아서 변수 num2에 저장(string)
op = input("+, - ,*, / 중 하나 입력 > ") # 연산자를 입력 받아서 변수 op에 저장
result = 0 # 계산 결과값을 저장할 변수 result 

if  op in "+-*/": # in을 사용하여 op가 +, -, *, /일 때만 계산됨
    if op == "+": # op가 문자열 "+"일 경우,
        result = int(num1) + int(num2) # num1, num2는 string이므로 int 함수로 형변환
    if op == "-": # op가 문자열 "-"일 경우,
        result = int(num1) - int(num2) # num1, num2의 - 연산
    if op == "*": # op가 문자열 "*"일 경우,
        result = int(num1) * int(num2) # num1, num2의 * 연산
    if op == "/": # op가 문자열 "/"일 경우,
        result = int(num1) / int(num2) # num1, num2의 / 연산

    print("{} {} {} = {}".format(num1, op, num2, result))
else: # 입력받은 op가 예외일 경우
    print("+, -, *, / 이외의 문자를 입력했습니다.") # 예외 처리 문구 출력


# 17번. 윤년의 조건 (상, 5점)
    
while True:
    year = int(input("연도를 입력하세요(-1 입력 시 종료): ")) # 연도 입력(int로 저장)
    if year == -1: # 입력값이 -1일 경우 종료
        print("프로그램을 종료합니다.") # 종료 문구 출력
        break # 프로그램 break

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        # 연도가 4의 배수이고, 100의 배수는 아니라면, 또는 400의 배수일 경우
        print(f"{year}년도는 윤년입니다.") # 윤년 연도 출력
    else: # 윤년이 아닐 경우
        # 다음 윤년 찾기
        year_1 = year + 1 # 현재 year의 다음 연도 설정
        while not ((year_1 % 4 == 0 and year_1 % 100 != 0) or (year_1 % 400 == 0)):
            # 윤년의 조건에 부합하지 않을 동안
            year_1 += 1 # 연도에 +1
        print(f"{year}년도는 윤년이 아닙니다. 다음 윤년은 {year_1}입니다.") # 윤년 연도 출력


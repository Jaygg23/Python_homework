# 16번. 문자열에서 특정 문자 찾기 프로그램  (상, 5점)

def find_char(string, char): # 입력된 문자 위치 확인
    position = string.find(char)
    
    if position == -1: # 문자가 없을 경우 -1
        print(f"입력하신 '{string}' 에서 첫 번째 '{char}'는 -1번째 위치에 있습니다.")
    else: # 문자가 있을 경우
        print(f"입력하신 '{string}' 에서 첫 번째 '{char}'는 {position} 번째 위치에 있습니다.")

# 테스트
for i in range(5): # 5번 반복
    str = input("문자열을 입력하세요 : ")
    chr = input("문자를 입력하세요 : ")
    find_char(str,chr)


# 17번. 문자열 비교 프로그램 (상, 5점)

def compare_str(str1, str2): # 문자열 비교 
    # 모두 소문자로 변환
    if str1.lower() == str2.lower(): # 같을 경우
        print("두 문자열은 같습니다.")
    else: # 다를 경우
        print("두 문자열은 다릅니다.")

# 테스트
for i in range(2): # 2번 반복
    str1 = input("문자열 1을 입력하세요 : ")
    str2 = input("문자열 2를 입력하세요 : ")
    compare_str(str1, str2)
    print("\n")

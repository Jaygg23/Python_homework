# 11번. 숫자를 받아 2를 더해주는 함수를 구현한 프로그램 (중, 2점)
def plus_2(num): # 숫자 2를 더해주는 함수
    # 지역 변수
    num = num + 2 # 지역변수 num에 2를 더함
    return num # 2를 더한 값 반환

## main
num = 4 # num 값을 4로 저장
print(num) # 초기 num 값 출력
num = plus_2(num) # 2를 더한 결과를 다시 num에 저장
print(num) # 연산 후의 num 값 출력


# 12번. 가변 키워드 매개변수를 이용하여 정보를 함수로부터 입력받고 출력하는 예제 (중, 2점)
user_settings = {} # 전역 딕셔너리

def set_preferences(username, **kwargs): # 사용자 설정 정보를 저장하는 함수
    if not kwargs: # kwargs가 없을 경우
        print(f"[{username}] 설정 정보가 없습니다.") # 정보 없음 메시지 출력
        return # 함수 종료

    user_settings[username] = kwargs # 사용자 이름 : key, 딕셔너리: value
    print(f"[{username}] 설정이 저장되었습니다.") # 정보 저장 메시지 출력

set_preferences("lee") # lee의 정보를 전달 (정보 없음)
set_preferences("kim", language="Korean", theme="Dark", notifications=True) # kim의 정보를 딕셔너리 형태로 전달
print(user_settings) # user_settings 딕셔너리 출력

# 13번. 기본 매개변수의 특성에 유의하여, 결과의 출력과 동일하도록 아래 코드의 빈칸을 채워 프로그램을 실행하세요. (중, 2점)
def add_item(item, item_list=[]): # item 항목을 추가하는 함수
    item_list.append(item) # 리스트에 item 추가
    return item_list # 리스트 반환

result1 = add_item("apple") # 리스트에 apple 추가
print("result1:", result1) # 리스트 출력

result2 = add_item("banana") # 리스트에 banana 추가
print("result2:", result2) # 리스트 출력 (apple, banana 출력)

result3 = add_item("cherry", []) # 새로운 리스트에 cherry 추가 
print("result3:", result3) # 리스트 출력

# 17번. 장애물을 피해 달리는 사람 (상, 5점)

# course 리스트
course = ["start", 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0,
          1, 0, 0, 3, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0,
          3, 0, 0, 1, 0, "end"]

road_symbols = { # 길, 장애물 기호 딕셔너리
    "start": ">", "end": "|", # 출발, 끝 지점
    0: "_", 1: "」", 2: "▤", 3: "▒" # 번호에 따른 길 및 장애물의 상태
}

player_symbols = { # 달리는 사람 기호 딕셔너리
    "start": "ዽ", "end": "ዽ", # 출발, 끝에서의 사람 모습
    0: "ጿ", 1: "ኈ", 2: "ቼ", 3: "⤠" # 번호에 따른 사람 모습
}

# 길 출력 함수
def print_road(course, idx):
    road = "" # 길 초기화
    for i in range(idx + 1, min(idx + 4, len(course))): # 현재의 다음 칸부터, 최대 3칸 or course 끝까지 반복
        if course[i] == "end": # 끝 지점일 경우
            road += "|" # 기호 | 추가
            break # 종료
        road += road_symbols[course[i]] # course 번호에 맞는 기호 추가
    return road # 길 상태 반환

# 사람 모습 출력 함수
def print_player(course, idx):
    symbol = player_symbols[course[idx]] # course 번호에 맞는 사람 캐릭터 반환
    return symbol # 사람 모습 반환

# 메인 루프
for i in range(len(course)): # course의 길이만큼 반복
    back = "" # 지난 길 초기화
    for j in range(i): # 현재의 이전까지 반복
        back += road_symbols[course[j]] # 해당 위치의 길 추가
    
    player = print_player(course, i) # 현재 위치에서의 사람 모습
    front = print_road(course, i) # 앞으로 갈 길 (3칸)
    print(back + player + front) # 지난 길, 현재, 앞으로 갈 길 모두 출력

    if course[i] == "end": # course가 끝 지점일 경우
        break # 종료
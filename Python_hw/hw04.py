#17. 자판기 프로그램 만들기 (최상, 10점)

vending_machine = { # 자판기 딕셔너리
    "Cold": { # 차가운 음료
        "콜라": {"가격": 1500, "재고": [True, True, True, True]}, # 콜라 : 1500원, 4개
        "환타": {"가격": 1000, "재고": []}, # 환타 : 1000원, 0개
        "사이다": {"가격": 1300, "재고": [True]}, # 사이다 : 1300원, 1개
        "캔커피": {"가격": 1000, "재고": [True, True]} # 캔커피 : 1000원, 2개
    },
    "Hot": { # 뜨거운 음료
        "율무차": {"가격": 500, "재고": [True, True, True]}, # 율무차 : 500원, 3개
        "핫초코": {"가격": 800, "재고": [True, True]} # 핫초코 : 800원, 2개
    }
}

def buying(money=0, choice=None, output=None): # 자판기의 현재 상태를 출력하는 함수
    print("\n========================== 자판기 ==========================") # 자판기 시작
    for temp in ["Cold", "Hot"]: # Cold, Hot 음료 출력
        drink = list(vending_machine[temp].keys()) # temp의 음료를 리스트에 저장
        if temp == "Cold": # temp가 Cold일 경우
            for item in drink: # drink의 item (콜라, 환타, 사이다, 캔커피 순서)
                print(f"{item}[{temp}]", end="     ") # 이름[temp] 형태로 item의 이름 출력
            print() # 개행 추가
            for item in drink: # drink의 item (콜라, 환타, 사이다, 캔커피 순서)
                print(f"  {vending_machine[temp][item]['가격']}원  ", end="      ") # 해당 음료의 가격 출력
            print() # 개행 추가
            for item in drink: # drink의 item (콜라, 환타, 사이다, 캔커피 순서)
                price = vending_machine[temp][item]["가격"] # 각 음료의 가격 저장
                stock = vending_machine[temp][item]["재고"] # 각 음료의 재고 저장
                if not stock: # 재고가 0개일 경우
                    print("[ Sold out ]", end="  ") # Sold out으로 출력
                elif money >= price: # 투입한 금액이 가격 이상일 경우
                    print("[   Buy   ]", end="  ") # 구매 가능한 음료만 Buy 출력
                else: # 투입한 금액이 음료를 구매하기에 부족할 경우
                    print("[    ㅁ    ]", end="  ") # 투입 금액으로 구매하지 못하는 음료는 ㅁ 으로 표기
            print() # 개행 추가
        else: # temp가 Hot일 경우
            for item in drink: # drink의 item (율무차, 핫초코 순서)
                print(f"{item}[{temp}]", end="   ") # 이름[temp] 형태로 item의 이름 출력
            print() # 개행 추가
            for item in drink: # drink의 item (율무차, 핫초코 순서)
                print(f"  {vending_machine[temp][item]['가격']}원", end="      ") # 해당 음료의 가격 출력
            print() # 개행 추가
            for item in drink: # drink의 item (율무차, 핫초코 순서)
                price = vending_machine[temp][item]["가격"] # 각 음료의 가격 저장
                stock = vending_machine[temp][item]["재고"] # 각 음료의 재고 저장
                if not stock: # 재고가 0개일 경우
                    print("[ Sold out ]", end="  ") # Sold out으로 출력
                elif money >= price: # 투입한 금액이 가격 이상일 경우
                    print("[   Buy   ]", end="  ") # 구매 가능한 음료만 Buy 출력
                else: # 투입한 금액이 음료를 구매하기에 부족할 경우
                    print("[    ㅁ    ]", end="  ") # 투입 금액으로 구매하지 못하는 음료는 ㅁ 으로 표기
            print() # 개행 추가
    if output: # 음료 구매에 성공한 경우
        print(f"========================[ {output} ]========================") # 구매한 음료의 이름 표기
    else: # 음료 구매에 실패한 경우
        print(f"========================[          ]========================") # 공백으로 음료 표기

buying() # 자판기 초기 상태 출력

money = int(input("돈 투입 > ")) # 유저의 돈 투입
buying(money) # 투입된 금액으로 자판기 음료 구매 상태 출력

choice = input("음료 선택 > ") # 유저의 음료 선택

output = "" # 구매에 성공하여 출력된 음료 이름 or 공백
change = 0 # 잔돈 초기화
found = False # 유저가 선택한 음료가 자판기에 있는지 여부

for temp in vending_machine: # 자판기 음료 전체
    for item in vending_machine[temp]: # temp에 맞는 자판기 음료
        if item == choice: # 유저가 선택한 음료가 있을 경우
            found = True # 음료가 있음 경우 True로 상태 변경
            price = vending_machine[temp][item]["가격"] # 해당 음료의 가격을 price에 저장
            stock = vending_machine[temp][item]["재고"] # 해당 음료의 재고를 stock에 저장
            
            if stock and money >= price: # 재고가 있고, 투입 금액이 가격 이상일 경우
                stock.pop(0)  # 재고 리스트에서 True 하나를 제거
                change = money - price # 잔돈 = 유저가 투입한 금액에서 가격을 뺀 값
                output = item # 구매 성공한 음료의 이름을 현재 item으로 저장
            else: # 재고가 없거나, 투입 금액이 가격 미만일 경우
                change = money # 잔돈은 유저가 투입한 금액 그대로 저장
            break # 내부 반복 종료
    if found: # 선택한 음료를 찾을 경우
        break # 외부 반복 종료

if not found: # 유저가 선택한 음료가 자판기에 없을 경우
    print(f"{choice} 음료가 자판기에 존재하지 않습니다.") # 오류 문구 출력
    output = "" # 구매 실패 : 공백으로 표기
    change = money # 잔돈은 유저가 투입한 금액 그대로 표기

buying(0, choice, output) # 구매 성공 or 실패 이후의 자판기 상태 출력 
print(f"잔돈 : {change}") # 잔돈 출력

print("\n<자판기 재고>") # 자판기 재고 출력
for temp in vending_machine: # 자판기 음료의 temp 동안
    for item in vending_machine[temp]: # 자판기 음료의 temp의 item 동안
        print(f"{item} {len(vending_machine[temp][item]['재고'])}") # 각 음료의 이름과 재고 출력

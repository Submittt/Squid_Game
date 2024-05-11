import random

# 게임 스타터
def game_starter(information) :
    input_value = input(information)
    if input_value == "" :
        return True

# 플레이어 명단 정렬
def player_info_sorting (players) :
    print("참가자 명단: ")
    x = 0  
    for key,value in players.items() :
        # print문의 기본적인 end = enter => end = \t으로 지정하여 줄바꿈을 탭으로 변경
        if key > 9 :
            print(f"{key}번: {value}" , end = "\t")  
        else :
            # 참가자 번호가 한자리 수일 때 정렬시 칸 밀림 => " n번" 스페이스바로 간격 조정
            print(f" {key}번: {value}" , end = "\t")
        x = x + 1
        # 출력이 1번 실행될 때마다 x의 값을 1 증가 => x의 값이 5가 되면 "" (enter)를 통해 줄바꿈
        if x == 5:
            print("")
            x = 0
            # 줄바꿈 시 x를 0으로 초기화

# 게임 정보 프린팅
def game_info(players) :
    player_info_sorting(players)
    print("\n총 상금: %s 원" %(format(len(players) * 10000000, ",")))
    print(f"\n참가자 수 : {len(players)}명")

# 주사위 게임
def dice_game(players) :
    if game_starter("\n\n첫번째 게임 (주사위 게임) 실행 | (엔터)") == True :
        random_dice = random.randrange(2,7)
        print(f"\n주사위 게임 숫자: {random_dice}")
        # players = dict({key: value for key, value in players.items() if key % random_dice != 0})
    
        for key in list(players.keys()) :
            if key % random_dice == 0 :
                del(players[key])

        player_info_sorting(players)

# 소수 판별기
def prime(number) :
    for i in range(2, number) :
        if number % i  == 0 :
            return False
    return True 
    # 2, 파라미터 number 의 범위를 기준으로 합성수 or 소수인지 판별
    # 2 부터 number까지 판별하여 하나라도 나머지 값이 0일 때, 소수가 아님 => False 산출
    # 2 부터 number까지 판별하여 모두 나머지 값이 0이 아닐 때, 소수임 => True 산출    

# 프라임 게임
def prime_game(players) :
    if game_starter("\n\n두번째 게임 (프라임 게임) 실행 | (엔터)") == True :
        choice_value = int(input("\n1번(소수 탈락) 또는 2번(합성수 탈락)을 선택하세요 : "))
        
        # 입력값이 1 또는 2가 아님 => while문으로 루프
        while choice_value > 2 :
            print("메뉴에서 다시 고르세요.")
            choice_value = int(input("1번(소수 탈락) 또는 2번(합성수 탈락)을 선택하세요 : "))
        
        # 입력 값이 1 또는 2 => 소수 판별기를 통해 참가자 번호(key값)를 True, False 판별
        if choice_value == 1 or choice_value == 2 :
            for i in list(players.keys()) :
                prime_result = prime(i)

                # 판별된 boolean 값과 입력값이 조건식과 모두 일치 => 참가자 번호를 딕셔너리에서 삭제
                if prime_result == True and choice_value == 1 :
                    del(players[i])
                elif prime_result == False and choice_value == 2 :
                    del(players[i])

        player_info_sorting(players)

# 제비뽑기 게임
def last_game(players) :
    if game_starter("\n\n마지막 게임 실행 (제비뽑기) | (엔터)") == True :
        last_gamers = list(players.keys())
        game_result = random.choice(last_gamers)
        print(f"\n최종 우승자: {players[game_result]}")

# 오징어게임 메인 함수    
def main() :
    game_info(dictionary)
    dice_game(dictionary)
    prime_game(dictionary)
    last_game(dictionary)

if __name__ == '__main__' :
# if __name__ == 'main__' => 임포트된 파일끼리 충돌을 방지하기 위한 구문

    players_names = [
                "정지희","황지호","성은주","김유진","김소은",
                "김도현","윤수호","김태환","안산음","강혜정",
                "김예은","홍시우","이예진","신선영","염가영",
                "박재호","송수연","김선재","양수빈","황인선",
                "박소현","신준서","강건희","송수연","최도원",
                "김학진","김성민","박천호","이상윤","김준호",
                "김예린","조수빈","윤여은","김학진","정도형",
                "김민지","이현아","정의손","박준규","김단아",
                "박승보","김종훈","남춘성","최성용","김태간"
    ]

    users = (len(players_names))
    random_number = random.sample(range(1,users+1),users)

    # 딕셔너리 생성 구문
    dictionary = {}
    for i in range(0, users) :
        dictionary[random_number[i]] = players_names[i] 
    # dictionary = dict(zip(random_number , players_names))

    # 딕셔너리를 순서대로 정렬
    dictionary = dict(sorted(dictionary.items()))

    main()
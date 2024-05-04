import random

class info() :
    def __init__(self) -> None:
        pass

class diceGame() :
    def __init__(self) -> None:
        pass

class primeGame() :
    def __init__(self) -> None:
        pass

class lastGame() :
    def __init__(self) -> None:
        pass    

def player_info_sorting (players) :
    print("참가자 명단: ")
    x = 0
    for key,value in players.items() :
        if key > 9 :
            print("%s번: %s" %(key,value) , end = "\t")
        else :
            print(" %s번: %s" %(key,value) , end = "\t")
        x = x + 1
        if x == 5:
            print("")
            x = 0

def game_info(players) :
    player_info_sorting(players)
    print("\n총 상금: %s 원" %(format(total_price, ",")))
    print("\n참가자 수 : %s명" %(users))

def dice_game(players) :
    game_starter = input("\n\n첫번째 게임 (주사위 게임) 실행 | (엔터)")
    if game_starter == "" :
        random_dice = random.randrange(2,7)
        print("\n주사위 게임 숫자: %s " %(random_dice))
        # players = dict({key: value for key, value in players.items() if key % random_dice != 0})
    
        for key in list(players.keys()) :
            if key % random_dice == 0 :
                del(players[key])

        player_info_sorting(players)

def prime(number) :
    for i in range(2, number) :
        if number % i  == 0 :
            return False
    return True 

def prime_game(players) :
    game_starter = input("\n\n두번째 게임 (프라임 게임) 실행 | (엔터)")
    if game_starter == "" :
        prime_value = int(input("\n1번(소수 탈락) 또는 2번(합성수 탈락)을 선택하세요 : "))
        if prime_value == 1 or prime_value == 2 :
            for i in list(players.keys()) :
                prime_result = prime(i)
                if prime_result == True and prime_value == 1 :
                    del(players[i])
                if prime_result == False and prime_value == 2 :
                    del(players[i])
        while prime_value > 2 :
            print("메뉴에서 다시 고르세요.")
            prime_value = int(input("1번(소수 탈락) 또는 2번(합성수 탈락)을 선택하세요 : "))

        player_info_sorting(players)

def last_game(players) :
    game_starter = input("\n\n마지막 게임 실행 (제비뽑기) | (엔터)")
    if game_starter == "" :
        last_game = list(players.keys())
        result_game = random.choice(last_game)
        print("\n최종 우승자: %s "  %(players[result_game]))

    
def main() :
    game_info(dictionary)
    dice_game(dictionary)
    prime_game(dictionary)
    last_game(dictionary)

if __name__ == '__main__' :
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
    total_price = users*10000000
    random_number = random.sample(range(1,users+1),users)
    dictionary = dict(zip(random_number , players_names))

    main()
    

    







    






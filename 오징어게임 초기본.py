import random



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

total_price = users*100000

random_number = random.sample(range(1,users+1),users)

random_pick = []

for i in range(1, 46):
        number = str(random_number[i-1])
        a = players_names[i-1] + ":" + number
        random_pick.append(a)


def is_prime(number) :
    if number <= 1 :
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def game_info() :
    print("Player of this game : \n %s" %(", ".join(random_pick)))
    print("Total number of people : %s" %(users))
    print("Total price of this Game : %s Won" %(total_price))


def dice_game() :
    dice_result = random.randrange(2,7)
    for i in range(users):
            i * dice_result        


game_info()
dice_game()


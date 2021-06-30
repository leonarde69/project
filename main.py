#고려하는 각인은  총 3가지이고 등급에 따라 목표를 유효 각인 66/77/97로 설정한다.
#확률이 낮을 때(45퍼 이하)는 디버프 각인을 선택한다.
#디버프 각인이라도 3이 넘지 않게 한다.
#확률은 75에서 시작하고 성공하면 -10 실패하면 +10된다 (MAX=75, MIN=15)
#사용자가 초기화를 원하거나 모든 각인의 세공 횟수를 사용하면 프로그램을 종료한다.
#한 각인 세공 횟수를 모두 소모하면 그 다음 세공에 해당 각인을 고려하지 않는다.
#사용자에게 성공/실패 여부와 스톤의 등급을 입력받는다.
#성공 확률이 높은 각인을 추천한다.

#디버프 각인이라도 3이 넘지 않게 한다.
#한 각인의 세공 횟수를 모두 소모하면 그 다음 세공에 해당 각인을 고려하지 않는다.

global ability1
ability1 = 0
global ability2
ability2 = 0
global debuff
debuff = 0
ability = 0
ability1_suc = 0
ability2_suc = 0
debuff_suc = 0
chance = NULL
recommend = 
grade_str = input("어빌리티 스톤의 등급은? (1.희귀 2.영웅 3.전설 4.유물")
if grade_str == "희귀" :
    ability1 += 7
    ability2 += 7
    debuff += 7
elif grade_str == "영웅" :
    ability1 += 8
    ability2 += 8
    debuff += 8
elif grade_str == "전설" :
    ability1 += 9
    ability2 += 9
    debuff += 9
elif grade_str == "유물" :
    ability1 += 10
    ability2 += 10
    debuff += 10

success = 75

while(debuff > 0) and (ability1 > 0) and (ability2 > 0) :
    #각인1: 성공개수 횟수 
    #각인2: 성공개수 횟수 
    #디버프: 성공개수 횟수
    #추천하는 각인
    #성공했습니까?(예/아니오)
    print("각인1 : %d회성공  %d" % (ability1_suc, ability1))
    print("각인2 : %d회성공  %d" % (ability2_suc, ability2))
    print("디버프 : %d회성공  %d" % (debuff_suc, debuff_suc))
    print("추천하는각인 : %s" % (recommend))
    chance = input("성공했습니까?(예/아니오)")
    if chance == "예" :
        if success >25:
            success -=10
            if recommend == "각인1" :
                ability1_suc += 1
            elif recommend == "각인2" :
                ability2_suc += 1
            else :
                debuff_suc += 1
    elif chance == "아니오" :
        if success < 75:
            success +=10



def trial() :
    if success < 45 :
        if debuff > 0 :
            recommend = "디버프"
        else :
            if ability1 > ability2 :
                recommend = "각인1"
            else :
                recommend = "각인2"
    else :
        if ability1 > ability2 :
            recommend = "각인2"
        else :
            recommend = "각인1"
    print("추천하는각인 : %s" % (recommend))

def convin_lotto():
    global lotto_total
    global extra_total
    global want_lotto_1
    global want_lotto_2
    if lotto_total + extra_total < want_lotto_1 + 2*want_lotto_2:
        print("낸 금액보다 복권 값이 더 비쌉니다.")
    elif want_lotto_2 != 0:
        change_lotto_2 = min(want_lotto_2,lotto_total // 2)
        change_lotto_1 = min(want_lotto_1, lotto_total - 2*change_lotto_2)
        if lotto_total %2 != 0 and 2*want_lotto_2 > lotto_total and want_lotto_1 == 0:
            print("교환 기능으로 복권를 교환할 수 없습니다.\n현금으로 바꾼 뒤 그냥 결제로 이용해주세요 \n------------------------------------\
\n교환을 이용할 수 없는 이유는 \n당첨금 총합이 홀수이고 교환하려는 로또가 2천원이기 때문입니다.\n------------------------------------")
            print("만약 로또 당첨금 중에 1000원짜리 당첨금이 있다면, \n그 복권만 현금으로 교환해주세요,\n추가 금액은 ",extra_total+1," 천원이 됩니다(",extra_total," 천원 + 1 천원 ). 따라서 ")
            lotto_total -= 1
            extra_total += 1
            convin_lotto()
        elif extra_total == 0:
            if 2*change_lotto_2 + change_lotto_1 < lotto_total:
                #당첨금 일부는 현금, 당첨금 일부는 복권으로 교환하려는 손님임
                print(lotto_total-(change_lotto_1+2*change_lotto_2),"천원은 \'현금\'으로 교환, \n교환 \n1천원짜리 복권 :",change_lotto_1,"개\n2천원짜리 복권 :",change_lotto_2,"개",)
            elif 2*change_lotto_2 + change_lotto_1 == lotto_total:
                print("교환 \n1천원짜리 복권 :",change_lotto_1,"개\n2천원짜리 복권 :",change_lotto_2,"개")#
        else: #추가 금액이 있는 손님
            remain_1 = want_lotto_1 - change_lotto_1
            remain_2 = want_lotto_2 - change_lotto_2
            if change_lotto_1 + 2*change_lotto_2 < lotto_total:
                print("교환할 로또 가격이 당첨금보다 작다, 추가금액을 낼 이유가 없다. 추가금액을 돌려드리자 그리고")
                extra_total = 0
                convin_lotto()
            elif want_lotto_1 + 2*want_lotto_2 < lotto_total + extra_total:
                remain = (lotto_total + extra_total) - (want_lotto_1 + 2 * want_lotto_2)
                extra_total -= remain
                convin_lotto()
                print("\n",remain,"천원 거슬러 드리기")
            else:
                print("교환 \n1천원짜리 복권 :",change_lotto_1,"개\n2천원짜리 복권 :",change_lotto_2,"개\n\n\
구매 \n1천원짜리 복권 :",remain_1,"개\n2천원짜리 복권 :",remain_2,"개")
    else:   #2천원이 0개 -> 싹 다 천원으로 교환
        print("교환기능으로 1천원짜리", lotto_total,"개, 구매 기능으로",extra_total,"개 구매하시면 됩니다.")

while 1:
    print("############# 스피또 가격 구하기 ##############")
    lotto_total = int(input("당첨금 총액(천원 단위)\n"))
    extra_total = int(input("추가 금액 없다면 0 입력 (천원 단위)\n"))
    want_lotto_1 = int(input("1천원짜리 몇 개?\n"))
    want_lotto_2 = int(input("2천원짜리 몇 개?\n"))
    print("-"*10)
    convin_lotto()
    print("\n\n")

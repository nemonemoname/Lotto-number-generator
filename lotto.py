import random

times = 0


# 숫자 생성
def make_number():
    return sorted([random.randrange(1, 46) for _ in range(6)])


# 번호 5개 출력
while times != 5:
    number = make_number()
    if len(set(number)) < 6:  # 번호중에 같은것이 있는가?
        number = make_number()
    else:
        print(times+1, ":", number)
        times += 1

import random


# 로또 번호를 생성해 주는 함수
def lotto_set(num):
    # 원하는 로또 게임 수 만큼 반복 (0, 1, 2 ... num-1)
    for i in range(num):
        # 로또 번호를 저장할 빈 집합 생성
        # 집합의 데이터는 중복되지 않고 순서가 없다.
        result = set()
        # 집합의 원소의 개수가 6개가 될 때까지 반복
        while len(result) < 6:
            # 집합에 1~45까지의 숫자 중 하나를 랜덤하게 추가
            # 집합은 중복된 숫자를 허용하지 않기 때문에,
            # 집합에 있는 숫자가 입력되는 경우 len(result)는 증가되지 않는다.
            result.add(random.randrange(1, 46))
            # 집합은 정렬되지 않기 때문에 리스트 형식으로 변경
            res = list(result)
            # res 데이터 정렬
            res.sort()

        # res 출력
        print(res)


# 함수 호출
lotto_set(5)
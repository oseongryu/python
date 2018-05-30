try:
    raise Exception('인덱스 오류!')
except Exception as e:
    print(e)
    print(type(e))
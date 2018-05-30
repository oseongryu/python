# pairs = [
#     ('time', 8),
#     ('the', 15),
#     ('turbo', 1),
#     ('time', 9),
#     ('time', 10),
#     ('time', 11),
# ]
#
#
# # 단어와 빈도수의 쌍으로 이루어진 튜플을 받아, 빈도수를 리턴합니다.
# def get_freq(pair):
#     count  = 0;
#     for key, val in pairs:
#         if key == pair:
#             count += 1;
#             # print('{0}, {1}'.format(key, val))
#
#     return count
#
#
# # print("총계 :" + str(get_freq('time')))
#
# print("총계 :" + str(get_freq(input("Key 값을 입력하세요 : "))))



pairs = [
    ('time', 8),
    ('the', 15),
    ('turbo', 1),
]

# 단어와 빈도수의 쌍으로 이루어진 튜플을 받아, 빈도수를 리턴합니다.
def get_freq(pair):
    return_val = "";
    for key, val in pairs:
        if key == pair:
            return_val = val;
    return return_val

print("총계 :" + str(get_freq(input("Key 값을 입력하세요 : "))))

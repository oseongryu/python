score = int(input("총점입력"))

# if score >= 90:
#     print("수")
# else:
#     if 80 <= score < 90 :
#         print("우")
#     else:
#         if 70 <= score < 80:
#             print("미")
#         else:
#             if 60 <= score < 70:
#                 print("양")
#             else:
#                 print("가")


if score >= 90:
    print("수")
elif 80 <= score < 90 :
    print("우")
elif 70 <= score < 80:
    print("미")
elif 60 <= score < 70:
    print("양")
else:
    print("가")
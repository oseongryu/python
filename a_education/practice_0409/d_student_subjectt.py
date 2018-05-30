import operator
student_count = int(input("학생수를 입력하십시오:"))

student_list = []
for count in range(student_count):
    print(count + 1, end='')
    student_score_comma = input("번째 학생의 이름과 과목별 점수를 입력하십시오(,로 구분):")
    student_score_list = student_score_comma.split(",")
    student_list += [student_score_list]
# print(student_list)

s_sum = 0
sum_list = ['과목합계', 0, 0, 0]  # 과목합계 초기화
avg_list = ['과목평균', 0, 0, 0]  # 과목평균 초기화

# print(len(sum_list))
# print(len(avg_list))
for s_list in student_list:
    s_sum = 0  # 한 학생의 합계 초기화
    for count in range(1, len(s_list)):
        s_sum += float(s_list[count])  # 한 학생의 합계 계산
    s_list.insert(len(s_list)+1,s_sum)  # 합계를 리스트에 추가
    s_avg = s_sum / (len(s_list)-2)  # 평균을 계산
    s_list.insert(len(s_list)+2,s_avg)  # 평균을 리스트에 추가


    for count in range(1, len(s_list)-2):
        sum_list[count] += float(s_list[count])
        avg_list[count] += float(s_list[count])/student_count

print(student_list)
print(sum_list)
print(avg_list)

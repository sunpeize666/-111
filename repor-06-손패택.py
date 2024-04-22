'''
反复输入3个科目的成绩,
并写出输出总分和平均分的程序。 
当三门课的分数均为0分时，
程序输出迄今为止的处理人员，
并退出程序。
 [执行结果]第1位学生:总分000分，
 平均分00分 第2位学生:总分000分，
 平均分00分
'''
cnt=0

while True:
    scorel=int(input("첫 번째 점수 입력: "))
    score2=int(input("두 번째 점수 입력: "))
    score3=int(input("세 번째 점수 입력: "))

    if(scorel==0 and score2==0 and score3==0):
        break

    total=scorel+score2+score3
    avg=total/3
    cnt=cnt+1
    print(cnt,"첫번째 학생: 총점",total,"점, 평균%.1f"%avg,"점")
print("총",cnt,"명 성적 처리")
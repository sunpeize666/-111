'''
洪吉童的本薪为300万韩元。
这个月拿到了30万韩元的津贴,
并缴纳了总额的20%。 
请制定洪吉童这个月工资领取额的程序。
'''
본봉 = 3000000
수당 =  300000
세금 = 본봉*12 * 0.2
수령액 = 본봉 + 수당 - 세금

print(f"수령액 = {수령액}")
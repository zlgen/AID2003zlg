"""
    增强运算符(累计运算符)
        +=  -=  *=  幂运算**=  /=   //=   %=
""" 
data01 = 5
print(data01 + 2)  # 没有修改data01
print(data01)  # 5

data02 = 5
data02 = data02 + 2  # 运算过后给自身赋值
print(data02)  # 7

data03 = 5
data03 += 2  # 建议 累加
print(data03)  # 7

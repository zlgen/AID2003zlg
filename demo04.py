"""
    核心数据类型
         空类型    整形int    浮点型float   字符串str
         None      10         1.2         "我是"
"""
# 1.  None 空类型
# 需求：必须在本行创建变量,但是又不能关联数据
# 解决：通过None为创建变量的数据占位置
name = None
# ....
name = "庆帝"
# 需求：只为解除变量与数据的关联
# 解决：让变量指向None
name = None

# 2. 整形int :整数
# 十进制：每位用十种状态计数，逢十进一，写法是0~9。0   1    2      3      4 .... 9
number01 = 10
# 二进制：每位用二种状态计数，逢二进一，写法是01。0    1    10    11     100 ...
number02 = 0b10
print(number02)  # 以十进制打印：2
# 八进制：每位用八种状态计数，逢八进一，写法是0～7。0    1   2    ....      7 10 11
number03 = 0o10
print(number03)  # 以十进制打印：8
# 十六进制：每位用十六种状态计数，逢十六进一，写法是0～9 a ~ f。0    1   2    .... 9  a  b
number04 = 0x10
print(number04)  # 以十进制打印：16

# 3. 浮点型float：小数
number05 = 12.34
# print(type(number05))# <class 'float'>
# 科学计数法    e 代表 乘以10
number06 = 1234e-3
print(number06)
print(0.00000000000000000001)  # 1e-20

# 4. 字符串str:文字
message = "我是qtx"

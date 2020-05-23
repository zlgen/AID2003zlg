"""
    类型转换
             整形int    浮点型float   字符串str
               10         1.2         "我是"
        语法：
            类型名称(待转换数据)
    练习:exercise05
"""
# input返回的结果,一定是字符串str类型
# 不能与数进行数学运算
# 需求：根据今年年龄，计算明年年龄.
age = int(input("请输入年龄："))
print("明年你" + str(age + 1) + "岁啦")

# 字符串str  --> 数值(整数int  小数float)
number01 = int("18")
number02 = float("1.25")

# 数值(整数int  小数float)  --> 字符串str
s01 = str(100)
s02 = str(1.234)

# 整数int --> 小数float
f1 = float(100)
print(f1)
# 小数float --> 整数int
i1 = int(1.999)
print(i1)  # 1  截断删除

# 小心
# 等待转换的数据格式必须符合需要转换的类型
# int("1.5")  错误
# int("文字")  错误

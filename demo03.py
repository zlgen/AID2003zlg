"""
    变量
        程序运行在哪里？  -->   内存
        程序在处理什么？  -->   数据
        价值：在内存中操作数据
        语法：
            名称 = 数据
            名称1,名称2 = 数据1,数据2
            名称1 = 名称2 = 数据1
    练习:exercise03/04
"""
# 命名必须做到：望文生义
class_name = "2003"

person_name01, person_name02 = "庆帝", "范闲"

person_name03 = person_name04 = "师傅"

del person_name03, class_name

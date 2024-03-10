import random


# 获取用户输入的最小和最大数值
aaa = int(input("请输入最小（十进制）数："))
aab = int(input("请输入最大（十进制）数："))

# 设置默认答题数量，并获取用户输入
aac = 40  # 默认答题数量为40
user_input_aac = input("请输入答题数量（默认40）：")
if user_input_aac.isdigit():
    aac = int(user_input_aac)

# 设置题目总数
for i in range(aac):
    # 生成随机数
    dnc = random.randint(aaa, aab)
    
    # 显示二进制数（去掉前缀）
    print(bin(dnc)[2:])
    
    # 获取用户输入的答案，并进行循环直到得到有效的整数输入
    while True:
        try:
            abc = input("请输入你认为的十进制答案：")
            abc = int(abc)
            break
        except ValueError:
            print("输入的内容不能转换为十进制整数，请重新输入。")

    # 判断并给出反馈
    if abc == dnc:
        print("正确")
    else:
        print("错误")
print("感谢使用")
# 当前版本的代码会在完成所有题目后添加了一句言论
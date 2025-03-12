import random

def guess_number_game():
    # 生成一个1到100之间的随机数
    target_number = random.randint(1, 100)
    # 记录猜测次数
    guess_count = 0
    # 记录用户输入的历史
    guess_history = []
    
    print("欢迎来到猜数字游戏！")
    print("我已经生成了一个1到100之间的数字，请开始猜测吧！")
    
    while True:
        # 获取用户输入
        user_input = input("请输入你的猜测（输入'q'退出游戏）：")
        
        # 判断用户是否选择退出
        if user_input.lower() == 'q':
            print("你选择退出游戏，游戏结束！")
            break
        
        # 检查输入是否为有效数字
        if not user_input.isdigit():
            print("请输入一个有效的数字！")
            continue
        
        # 转换用户输入为整数
        guess = int(user_input)
        
        # 检查输入是否在1到100之间
        if guess < 1 or guess > 100:
            print("请输入1到100之间的数字！")
            continue
        
        # 增加猜测次数
        guess_count += 1
        # 记录用户输入
        guess_history.append(guess)
        
        # 判断猜测结果
        if guess < target_number:
            print("太小了！再试一次吧。")
        elif guess > target_number:
            print("太大了！再试一次吧。")
        else:
            print(f"恭喜你，第{guess_count}次就答对了！")
            print(f"你总共猜了{guess_count}次，猜测历史为：{guess_history}")
            break

# 运行游戏
if __name__ == "__main__":
    guess_number_game()

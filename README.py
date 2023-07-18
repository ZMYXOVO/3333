import time

def pomodoro_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        print(f"\r剩余时间：{seconds//60}分钟 {seconds%60}秒", end="")
        time.sleep(1)
        seconds -= 1
    print("\n时间到！")

def main():
    print("欢迎使用专注时钟！")
    while True:
        try:
            minutes = int(input("请输入要设定的专注时间（分钟）："))
            break
        except ValueError:
            print("输入无效，请重新输入！")
    
    pomodoro_timer(minutes)

if __name__ == "__main__":
    main()

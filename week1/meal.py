#题目要求的24小时制
def main():
    t = convert(input("What time is it? ").strip())
    if 7 <= t <=8 :
        print("breakfast time")
    elif 12 <= t <=13 :
        print("lunch time")
    elif 18 <= t <= 19 :
        print("dinner time")

def convert(time):
    x , y = time.split(":")
    x , y = float(x) , float(y)
    x += y/60
    return x 
if __name__ == "__main__":
    main()

"""
功能更强的12小时制convert函数参考
def convert(time):
    original = time                                     保留原始字符串
    time = time.replace("a.m.", "").replace("p.m.", "") 去除time里面的am和pm 
    hours, minutes = map(int, time.split(":"))          转换数据类型 map批量应用函数
    if "p.m." in original and hours != 12:
        hours += 12
    if "a.m." in original and hours == 12:
        hours = 0
    return hours + minutes / 60


"""

#初始代码(通过样例)
def main() :
    # 原始代码：exp = input("Expression: ").strip().split()
    x , y , z =  input("Expression: ").strip().split()
    
    ans = 0 
    match y :
        case "+" : ans = float(x) + float(z) 
        case "-" : ans = float(x) - float(z)
        case "*" : ans = float(x) * float(z)
        case "/" : ans = float(x) / float(z)
    print(round(ans,1))

main()



"""
用来借鉴学习的方法

x, y, z = input("Expression: ").split()

x, z = int(x), int(z)
ans = eval(f"{x} {y} {z}")

print(f"{ans:.1f}")

"""
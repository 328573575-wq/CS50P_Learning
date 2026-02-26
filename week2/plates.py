def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    #长度2-6 开头两个是字母 数字不能在中间第一个数字不能为0 不能用标点符号
    if (v_len(s) and v_begin(s) and v_num(s) and v_alnum(s)) :
        return True
    return False
    
#判断长度合法
def v_len( s ) :
    if len(s) < 2 or len(s) > 6 :
        return False
    return True
#判断开头合法
def v_begin( s ) :
    if s[0:2].isalpha() :
        return True
    return False
#判断数字合法
def v_num( s ) :
    first = True 
    for i in s :
        if i.isdigit() and first :
            if i == "0" :
                return False
            first = False
        if i.isalpha() and not first :
            return False
    return True
#判断字符合法
def v_alnum( s ) : 
   return True if s.isalnum() else False

main()
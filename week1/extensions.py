#创建一个字典
types = {
    "gif" : "image/gif", 
    "jpg" : "image/jpeg",
    "jpeg" : "image/jpeg",
    "png" : "image/png",
    "pdf" : "application/pdf",
    "txt" : "text/plain",
    "zip" : "application/zip"
}
def main() :
    #获得文件后缀
    suf = input("File name: ").strip().lower().split(".")[-1]
    #转换并打印
    print(types.get(suf,"application/octet-stream"))

main()
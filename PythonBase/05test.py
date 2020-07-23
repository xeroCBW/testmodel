
# 递归使用
def printfme(str,i):

    if(i>0):
        print(str[i - 1])
        i-=1
    else:
        return
    printfme(str,i)

printfme('123',3)
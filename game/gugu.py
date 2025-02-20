

#구구단 만들어서 첫번쨰 인자 시작값 2단 2x1 ~ 2x9단  두번재 인자 개수 값으로4이벽시 2~5단까지

import sys
args= sys.argv

aa , bb = int(args[1][:-1]), int(args[2])
print(aa,type(aa),bb,type(bb))
def gugu(a,b):
    for i in range(a,a+b):
        print(f"==={i}단===")
        for j in range(1,10):
            print(f"{i}x{j}={i*j}")
   
gugu(aa,bb)

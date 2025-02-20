import sys
import requests as req
url ="https://finance.naver.com/sise/sise_market_sum.naver"
web = req.get(url)
html = web.text

#인자 받기 위함
args = sys.argv

def samsung(jong):
   
    f1 = html.find('삼성전자')
    return(f'{jong}:'+html[f1:f1 + 100][19:50].replace('<td class="number">',"").replace('</td>',"").replace('\n',"")+"원")

#내부

if __name__ == '__main__':
     print(args[1])
     print(sam(args[1]))
#if 조건 직접 호출 할떄 함수 실행 되서 나가고 직접호출 안하면 만들어놓은채 안나가게 만듬


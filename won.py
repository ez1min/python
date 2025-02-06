
import requests
import json
url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=qk0p0bggBwBY0NWKqAxuQ85q15uy6EJZ&searchdate=&data=AP01'
res = requests.get(url).text
#print(res)
data = json.loads(res)
print(type(data))
result = data[-1]['deal_bas_r'] # 젤 마지막줄에 있어서 -1넣음
print(result,type(result))
res2 = result.replace(",","").replace(".","")
print(res2,type(res2))
exc = int(res2)/10
dollor = int(input("원화로 계산할 달러를 입력하세요."))
res = dollor * exc
print(f"1달러는 {exc:,}원 이므로 \n {dollor}달러는 {res}원 입니다")
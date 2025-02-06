bag=['호박', '감자','소주', '맥주','피자']
test1 = input('추가할 물건')
test2 = input('어느 물품 뒤에?')
위치 = (bag.index(test2))+1
bag.insert(위치,test1)
print(bag)

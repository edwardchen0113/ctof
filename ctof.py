c = input('請輸入攝氏溫度：')
c = float(c)
f = c * 9 / 5 + 32
print('華氏溫度為：', f) 
if c >= 23 :
 if c <= 28 :
     print('今天氣溫適中！')
if c < 23:
 if c >= 16:	
    print("今天有點冷！最好加個薄外套！") 
if c < 16 :
 if c >= 0 :
     print('冷氣團來了！該穿厚衣了！！')	
if c >28 :
	input("氣溫適合去游泳！")
produsts = []
while True:
    name = input('請輸入商品名稱:')
    if name == 'q' :
        break
    price = input('請輸入商品價格:')
    price = int(price)
    p = []
    produsts.append([name,price])
print(produsts)

for p in produst:
	print(p[0],'的價格是',p[1])

with open('produsts.csv','w',encoding ='utf-8')as f:
	f.write('商品，價格\n')
	for p in produsts:
		f.write(p[0] + ',' + str(p[1]) + '\n')
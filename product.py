products = []
while True:
    name = input('輸入商品名稱: ')
    if name == 'q':
        break
    price = input('輸入商品價格: ')
    #p =[]
    #p.append(name)
    #p.append(price)
    p = [name, price]
    products.append(p) #products.append([name, price])
print(products)

for p in products:
    print(p[0], '的價格是', p[1])

#寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:  #打開檔案
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')  #寫入檔案，寫入csv檔用,和換行做區隔


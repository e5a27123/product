import os #operating system

main()

def main():
    filename = 'products.csv'
    if os.path.isfile(filename):  #檢查檔案是否存在(絕對路徑or相對路徑檔)
        print('找到檔案!')
        products = read_file(filename)
    else:
        print('找不到檔案!')
        
    products = user_input(products)
    print_products(products)
    write_file(filename, products)

def read_file(filename):
    products = []
    with open(filename, 'r', encoding = 'utf-8') as f:
            for line in f:
                if '商品,價格' in line:
                    continue
                name, price = line.strip().split(',')    #strip去除頭尾空格及換行符號
                                                         #aplit字串切割,以逗點當切割標準
                products.append([name, price])
    return products

#使用者輸入
def user_input(products):
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
    return products

#印出所有商品
def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename,products):
    with open(filename, 'w', encoding = 'utf-8') as f:  #打開檔案
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')  #寫入檔案，寫入csv檔用,和換行做區隔

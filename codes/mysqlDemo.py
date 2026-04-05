import pymysql

def displayAll():
    cur.execute('Select * from product')
    print("\nProduct Details:\n")
    for row in cur.fetchall():
        print(f'Id = {row[0]} Name = {row[1]} Quantity = {row[2]} Price= {row[3]} Maf Date = {row[4]} \n')

def addNewProduct():
    pid = int(input('Enter product Id: '))
    pname = input('Enter product name: ')
    qty = int(input('Enter product quantity: '))
    price = float(input('Enter product price: '))
    mfdate = input("Enter date(yyyy-mm-dd) : ")
    cur.execute('Insert into Product values(%s,%s,%s,%s,%s)', (pid,pname,qty,price,mfdate) )
    conn.commit()

def deleteProductById(pid):
    cur.execute('Delete from product where pid = %s', pid)
    conn.commit()
    return True    
    
def updateProductById(pid,qty,price):
    cur.execute('update product set qty = %s , price = %s where pid = %s', (qty,price,pid,))
    conn.commit()
    return True

def displayById(pid):
    cur.execute('Select * from product where pid = %s', pid)
    row = cur.fetchone()
    print(f'Id = {row[0]} Name = {row[1]} Quantity = {row[2]} Price= {row[3]} Maf Date = {row[4]} \n')
    
try:
    conn = pymysql.connect(host = 'localhost', port = 3306, user = 'root', passwd='bda123', db = 'bdalab')
    if conn != None:
        print('Connection done')
    else:
        print('Connection not done')
except Exception as e:
    print(e)

try:
    if conn != None:
        cur  = conn.cursor()
        choice = 0 
        while choice != 6:
            choice =int(input('''*****************************
1. Add new product
2. Delete product
3. Update product
4. Display all product
5. Search product by Id
6. Exit 
*****************************
Enter your choice: '''
)) 
            match choice:
                case 1:
                    addNewProduct()
                    print('Product Added Successfully')
                case 2:
                    pid = int(input('Enter id of the product: '))
                    status = deleteProductById(pid)
                    if status != False:
                        print('Product deleted successfully')
                    else:
                        print(f'Product with Product id {pid} is not available')
                case 3:
                    pid = int(input('Enter id of the product: '))
                    qty = int(input('Enter new quantity of the product: '))
                    price = float(input('Enter new price of the product: '))
                    status = updateProductById(pid,qty,price)
                    if status != False:
                        print('Product details updated successfully')
                    else:
                        print(f'Product with Product id {pid} is not available') 
                    pass
                case 4:
                    displayAll()
                    pass
                case 5:
                    pid = int(input('Enter id of the product: '))
                    displayById(pid)
                    
                    pass
                case 6:
                    print('\nExiting....')
                    break
                case others:
                    print("Wrong choice")
    else:
        print('fail')

except Exception as e:
    print(e)
finally:
    if conn != None :
        cur.close()  
        conn.close()
        
        
        
        
        
        
        
        
        
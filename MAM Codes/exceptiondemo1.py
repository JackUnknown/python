def divide(x,y):
    try:
        ans=x/y
        return ans
    except ZeroDivisionError as e:
        print(e)
        raise e   #rethrow exception
        

d={'a':12,'b':3}
for i in range(3):
    try:
        #print(d['x'])
        x=int(input("enter number"))
        y=int(input("enter number"))
        ans=divide(x,y)
        print("Division : ",ans)
        break
    except ZeroDivisionError as e:
        print("denomenator cannot be zero")
        print(e)
    except (ValueError,KeyError) as e:
        print(e)
    #except:
    except Exception as e:  #generalized exception
        print(e)
        print("error occured")
    finally:
        print("in finally block")
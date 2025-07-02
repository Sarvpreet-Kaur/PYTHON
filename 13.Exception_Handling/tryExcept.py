# try()
def divide(x, y):
    try:
        # Floor Division : Gives only Fractional Part as Answer
        result = x // y
        print("Yeah ! Your answer is :", result)
    except ZeroDivisionError:
        print("\nSorry ! You are dividing by zero ")
    else:
        print(result)
        print("Executed when there is no error raise")
    finally:
        print("This will always get executed whether there is an error or not")
#try will execute
divide(3, 2)
#except will execute
divide(3,0)
class abc:

    def val_num(self):
        try:
            a = int(input("Enter number \n"))
        except Exception as e:
            print(e)
            print("number only")
        else:
            print(a)
        finally:
            print("This will always get printed")

obj = abc()
obj.val_num()


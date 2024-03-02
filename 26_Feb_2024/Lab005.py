class russia:

    def __init__(self):
        self.name = "name"

    def publiq_var(self):
        print("Public")

    def _protected_var(self):
        print("protected")

    def __private_var(self):
        print("private")


obj = russia()

obj.publiq_var()


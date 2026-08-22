# super keyword 

class parentclass:
    def parent_method(self):
        print("this is parent method 1")

class childclass(parentclass):
    def parent_method(self):
        print('tom')
        super().parent_method()
    
    def child_method(self):
        print("this is child method 2")
        super().parent_method()

child_object = childclass()
child_object.child_method()
child_object.parent_method()
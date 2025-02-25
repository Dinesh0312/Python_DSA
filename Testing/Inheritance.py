class A:
    def fetaure1(self):
        print("Feature 1 is working")

class B(A): # Single Inheritance
    def fetaure2(self):
        print("Feature 2 is working")

class C(B): # Multilevel Inheritance
    def fetaure3(self):
        print("Feature 3 is working")

class X:
    def extra_feature(self):
        print("extra_feature is working")

class result(A,X): # Multiple Inheritance
    def final_result(self):
        print("final_result is working")

a1 = A()

a1.fetaure1()

b1 = B()

b1.fetaure1()
b1.fetaure2()

c1 = C()


c1.fetaure1()
c1.fetaure2()
c1.fetaure3()


f1 = result()

f1.fetaure1()
f1.extra_feature()
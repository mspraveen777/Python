"""
Diamond problem
"""


class A:
    def hello(self):
        print("Hello from A")


class B(A):
    # def hello(self):
    #     print("Hello from B")
    pass


class C(A):
    # def hello(self):
    #     print("Hello from C")
    pass


class D(B, C):
    pass


d = D()
d.hello()  # It will go on priority

print(D.__mro__)  # To check the priority

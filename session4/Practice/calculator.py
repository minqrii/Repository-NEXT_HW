class Calculator:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.result = 0
    def add(self, num):
        global result
        self.result += num
        return self.result
    def sub(self, num):
        global result
        self.result -= num
        return self.result
    def mul(self, num):
        global result
        self.result *= num
        return self.result
    def div(self, num):
        global result
        self.result /= num
        return self.result
        if num == 0:
            return None
        print("0으로 나눌 수 없습니다")

cal1 = Calculator("김민규", 25)
cal2 = Calculator("김준현", 24)

print(cal1.add(3))
print(cal1.add(3))
print(cal1.add(3))
print(cal1.mul(3))
print(cal1.mul(3))
print(cal1.div(3))

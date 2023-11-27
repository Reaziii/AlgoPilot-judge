
class Hello():
    static_value = 100

    def connect(self,num):
        Hello.static_value = num



a = Hello()

b = Hello()

b.connect(10)

c = Hello()


print(c.static_value)

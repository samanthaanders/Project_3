class my_class:
    def __init__(self, text, num):
        self.text = text
        self.num = num
    def __str__(self):
        return f"{self.text}"
    def test_function(self):
        for x in range(self.num):
            print(self.text)
    def get_name(self):
        return(self)




object = my_class("hi", 2)
object.test_function()
print(object.get_name())
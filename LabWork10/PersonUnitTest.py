import unittest

class Person:
    def __init__(self, name, age):
        self.__name = name #__ - закрытые переменные
        self.__age = age

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getAge(self):
        return self.__age

    def setAge(self, age):
        if age >= 0: # что возраст не отрицательный
            self.__age = age
        else:
            raise ValueError("Возраст не может быть отрицательным!")

# UnitTest
class TestPerson(unittest.TestCase):
    def testPerson(self):
        p = Person("Мия", 19)
        self.assertEqual(p.getName(), "Мия")
        self.assertEqual(p.getAge(), 19)

        p.setName("Рома")
        self.assertEqual(p.getName(), "Рома")

        p.setAge(20)
        self.assertEqual(p.getAge(), 20)

        #Ожидание ошибки!!!
        with self.assertRaises(ValueError):
            p.setAge(-10)

if __name__ == '__main__':
    unittest.main()
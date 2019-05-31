

from Public_method import table
import unittest

class case(unittest.TestCase):
    def test1(self):
        table.write(self,0,'chen')
        table.write(self,1,'yong')
        table.write(self,2,'yan')

    def test2(self):
        k1 = table.read(self,0)
        k2 = table.read(self,1)
        k3 = table.read(self,2)
        print(k1[0],k2[0],k3[0])



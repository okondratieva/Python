#from unittest import TestCase, main
from polynomial import Polynomial
import unittest
import xmlrunner
class Test_test1(unittest.TestCase):

    def setup_method(self):

        self.p1=Polynomial([1, 2, 3])
        self.p2=Polynomial([4, 5])
        self.p3=Polynomial([-1])
        self.p4=Polynomial([3, 0, 7])
        self.p5=Polynomial([3.5, 4,2,0])
        self.p6=Polynomial([0,1,6,8])
        self.p7=Polynomial([0,0,0,0,1,6,8])
        self.p8=Polynomial([0])
        self.p9=Polynomial([0,0,0,0,-1,6,0,8])
       
    def test_bag(self):
	self.setup_method()	
	assert self.p1==Polynomial([1,2,3])

 '''   def test_print(self):
        self.setup_method()
        print(Polynomial([0,0]))
        print(self.p1)
        print(self.p2)
        print(self.p3)
        print(self.p4)
        print(self.p5)
        print(Polynomial([1,-1,1,-1,0,0,-8]))
        print(Polynomial([0,0,0,0,1,6,-8]))
        print(self.p9+Polynomial([0,0,3,0]))
        print(Polynomial([-7,-8,0,3,1,-4, 0]))
        print(Polynomial([-7,-8,0,3,1,-4, 1]))
        print(Polynomial([-7,-8,0,3,1,-4, -1]))
'''

    def test_copy(self):
        self.setup_method()
        m1=self.p7
        print(m1 is self.p7)
        m1=m1*(-1)
        assert m1==(-1)*self.p7
        assert(m1+self.p7)==Polynomial([0,0])
       

    def test_eq(self):#method __eq__
        self.setup_method()

        assert not self.p2==self.p1
        assert self.p6==self.p7
        assert Polynomial([0,0])==self.p8
        assert self.p1==Polynomial([1,2,3])
        assert self.p5==Polynomial([3.5, 4, 2, 0])

    def test_neq(self):#method __ne__
        self.setup_method()
        tmp=Polynomial([1,3,3])
        assert self.p1!=tmp

    def test_add(self):#method __add__ 
        self.setup_method()
        n1=self.p2+self.p3
        n2=self.p1+self.p2
        n5=self.p1+self.p5

        n3=self.p2+4
        n4=self.p5+1.5
        n6=self.p9+Polynomial([0,0,3,0])

        assert n1==Polynomial([4,4])
        assert n2==Polynomial([1,6,8])
        assert n3==Polynomial([4,9])
        assert n4==Polynomial([3.5, 4, 2, 1.5])
        assert n5==Polynomial([3.5, 5, 4, 3])
        assert n6==Polynomial([0,-1,6,3,8])

    def test_sub(self): #method __sub__
        self.setup_method()

        n1=self.p1-self.p2
        n2=self.p4-self.p1
        n3=self.p1-self.p3
        n4=self.p2-self.p1
        n5=self.p5-self.p1
        n6=self.p2-(-2)

        assert n1==Polynomial([1, -2, -2])
        assert n2==Polynomial([2, -2, 4])
        assert n3==Polynomial([1, 2, 4])
        assert n4==Polynomial([-1, 2, 2])
        assert n5==Polynomial([3.5, 3, 0, -3])
        assert n6==Polynomial([4,7])

    def test_mul(self):#method __mul__ 
        self.setup_method()

        n1=self.p1*(5)
        n2=self.p5*(-2)
        n3=self.p1*self.p2

        assert n1==Polynomial([5,10,15])
        assert n2==Polynomial([-7,-8,-4, 0])
        assert n3==Polynomial([4,13,22,15])

    def test_neg(self):#Exceptions
        self.setup_method()
        s="str"      
        with self.assertRaises(TypeError):
            self.p3==-1
            self.p3!=s
            m1=Polynomial(1)
            m2=self.p1+s
            m3=self.p1-s
            m4=self.p1*s
            m5=Polynomial(['a'])
    
    def test_reverse(self):
        self.setup_method()
        n1=1+self.p1 #___radd
        n2=3-self.p2 #__rsub__
        n3=2*self.p4 #__rmul__
        assert n1==Polynomial([1,2,4])
        assert n2==Polynomial([-4, -2])
        assert n3==Polynomial([6,0,14])

        

if __name__ == '__main__':
	xmlrunner.XMLTestRunner(output='result').run(unittest.TestLoader().loadTestsFromTestCase(Test_test1))
	#with open("result.xml", 'wb') as output:
	#	unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output))
  #main()

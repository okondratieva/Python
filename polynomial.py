class Polynomial(object):
    def __init__(self, coeffs):
        self.coeffs = coeffs
        self.n=len(coeffs)-1

    def __str__(self):
        s=''
        for i in range(self.n):
            if self.coeffs[i]!=0:
                s=s+str(self.coeffs[i])+'*x^' + str(self.n-i)+'+'
        if self.coeffs[self.n]!=0:
                s=s+str(self.coeffs[self.n])
        else:
            s=s[:-1]
        return s
    def __add__(self, p):
       if (type(p) is not int) and (type(p) is not float):
            if self.n > p.n:
                c1=[0]*(self.n-p.n)+p.coeffs
                c2=self.coeffs
            else:
                c1=[0]*(p.n-self.n)+self.coeffs
                c2=p.coeffs
            new=[i+j for i, j in zip(c1,c2)]
       else:
            new=self.coeffs
            new[self.n]=new[self.n]+p
       return Polynomial(new)


    def __sub__(self, p):
      if (type(p) is not int) and (type(p) is not float):
        if self.n >= p.n:
            c1=[0]*(self.n-p.n)+p.coeffs
            c2=self.coeffs
        else:
            c1=p.coeffs
            c2=[0]*(p.n-self.n)+self.coeffs

        new=[j-i for i, j in zip(c1,c2)]
      else:
         new=self.coeffs
         new[self.n]=new[self.n]-p
      return Polynomial(new)

    def __mul__(self, p):
        if (type(p) is  int) or (type(p) is float):
            new=[p*i for i in self.coeffs]
        else:
            new=[0]*(self.n+p.n+1) 
            for i in range(self.n+1):
                for j in range(p.n+1):
                    new[i+j]=new[i+j]+self.coeffs[i]*p.coeffs[j]
        return Polynomial(new)

    def __eq__(self, p):
       if self.n!=p.n:
           return False
       return self.coeffs==p.coeffs

    def __ne__(self, p):
       return not(self==p)


     
       

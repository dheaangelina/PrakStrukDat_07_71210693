class PrefixConverter:
    def __init__(self):
        self.stackList = ['?']
    
    def push(self, data):
        self.stackList.append(data)

    def peek(self):
        if self.stackList:
            return self.stackList[-1]
        else:
            return "Isi Stack Kosong"
    
    def pop(self):
        if self.stackList:
            data = self.stackList.pop(-1)
            return data
        else:
            return "Isi Stack Kosong"
    
    def cekValidExpression(self, expression):
        if "(" and ")" in expression:
            return False
        elif expression >= 'a' and expression <= 'z':
            return False
        elif expression >= 'A' and expression <= 'Z':
            return False
        else:
            return True

    def infixToPrefix(self, expression):
        if self.cekValidExpression(expression) == True:
            return "Expresi Prefix-nya Adalah : "
        else:
            return "Expresi Infix yang anda masukkan tidak valid !!"

if __name__ == '__main__':
    expresi1 = PrefixConverter()
    print(expresi1.infixToPrefix("1+2+3*4/2-1"))
    print(expresi1.infixToPrefix("A * (B + C) / D"))
    print(expresi1.infixToPrefix("(1+2)*3"))
    print(expresi1.infixToPrefix("20 * 3 - 10 + 289"))
    print(expresi1.infixToPrefix("100 * 30 / 600 - 30 + 100 * 777"))


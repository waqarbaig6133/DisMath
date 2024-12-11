import re

class derivative:
    def __init__(self, inputs):
        self.inputs = inputs
    def poly(self):
        def normal_der(self):
            if 'x' not in self.inputs:
                print(0)
            else:
                new_func = [x for x in re.split(r'[()]', self.inputs) if x != '']        
                for x in new_func:
                    if 'x' not in x and x not in ['+', '-']:
                        new_func.remove(x)
                        new_func.pop()
                    else:
                        if x not in ['+','-']:
                            if '^' in x:
                                new_func[new_func.index(x)] = f"{str(int(x[:x.index('x')])*int(x[x.index('^')+1:]))}x^{int(x[x.index('^')+1:])-1}"
                            else:
                                new_func[new_func.index(x)] = f"{int(x[:x.index('x')])}"
                for x in new_func[2:]:
                    if x not in ['+','-']:
                        if 'x' in x:
                            if int(x[:x.index('x')]) < 0 and new_func[new_func.index(x)-1] == '+':
                                new_func.remove(new_func[new_func.index(x)-1])
                        else:
                            if int(x) < 0 and new_func[new_func.index(x)-1] == '+':
                                new_func.remove(new_func[new_func.index(x)-1])
                print(''.join(new_func))
derivative('[(2x^2)+(6x)]*[').poly()
                        































'''

import re

class derivative:
    def __init__(self, inputs):
        self.inputs = inputs
    def poly(self):
        if 'x' not in self.inputs:
            print(0)
        else:
            new_func = [x for x in re.split(r'[()]', self.inputs) if x != '']        
            for x in new_func:
                if 'x' not in x and x not in ['+', '-']:
                    new_func.remove(x)
                    new_func.pop()
                else:
                    if x not in ['+','-']:
                        coefficient = int(x[:x.index('x')])
                        if '^' in x:
                            exponent = int(x[x.index('^')+1:])
                            new_func[new_func.index(x)] = f"{str(coefficient*exponent)}x^{exponent-1}"
                        else:
                            new_func[new_func.index(x)] = f"{coefficient}"
            for x in new_func[2:]:
                if x not in ['+','-']:
                    if 'x' in x:
                        a = int(x[:x.index('x')])
                        b =new_func[new_func.index(x)-1]
                        if a < 0 and b == '+':
                            new_func.remove(new_func[new_func.index(x)-1])
                    else:
                        if int(x) < 0 and b == '+':
                            new_func.remove(new_func[new_func.index(x)-1])
                        
            print(''.join(new_func))
    def log(self):
        
derivative('(5x)-(3)').poly()



'''

'''
Sources:
https://docs.python.org/3/library/re.html
https://www.geeksforgeeks.org/python-split-multiple-characters-from-string/

'''





'''
Sources:
https://docs.python.org/3/library/re.html
https://www.geeksforgeeks.org/python-split-multiple-characters-from-string/



def poly(self):
        if 'x' not in self.inputs:
            print(0)
        else:
            new_func = [x for x in re.split(r'[()]', self.inputs) if x != '']        
            for x in new_func:
                if 'x' not in x and x not in ['+', '-']:
                    new_func.remove(x)
                    new_func.pop()
                else:
                    if x not in ['+','-']:
                        if '^' in x:
                            new_func[new_func.index(x)] = f"{str(int(x[:x.index('x')])*int(x[x.index('^')+1:]))}x^{int(x[x.index('^')+1:])-1}"
                        else:
                            new_func[new_func.index(x)] = f"{int(x[:x.index('x')])}"
            for x in new_func[2:]:
                if x not in ['+','-']:
                    if 'x' in x:
                        if int(x[:x.index('x')]) < 0 and new_func[new_func.index(x)-1] == '+':
                            new_func.remove(new_func[new_func.index(x)-1])
                    else:
                        if int(x) < 0 and new_func[new_func.index(x)-1] == '+':
                            new_func.remove(new_func[new_func.index(x)-1])
                        
            print(''.join(new_func))
'''

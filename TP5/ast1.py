class Circuit:
    def __init__(self, Linput, Loutput, Lassign):
        self.Linput = Linput
        self.Loutput = Loutput
        self.Lassign = Lassign
    def __str__(self):
        return(str([str(inp) for inp in self.Linput]) +str([str(out) for out in self.Loutput])+str([str(ass) for ass in self.Lassign]))

    def accept(visitor):
        visitor.visit_circuit(self)


class Identifier:
    def __init__(self):
        self.id = id
    def __str(self):
        return(str(self.id))
"""class Declaration:
    def __init__(self,)"""

class Input:
    def __init__(self,id):
        self.id1 = id
    def __str__(self):
        return("input" + str(self.id1))
    def accept(self, visitor):
        visitor.visit_input(self)

class Output:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return ("output" + str(self.name))
    def accept(self, visitor):
        visitor.visit_output(self)
        
class Assignment:
    def __init__(self,gauche,droiteop):
        self.gauche = gauche
        self.droiteop = droiteop
    def __str__(self):
        return(str(self.gauche) + "=" + str(self.droiteop))
    def accept(self, visitor):
        visitor.visit_assignment(self)
        

class Operation:
    def __init__(self,inputL1,inputL2,op):
        self.input1 = inputL1
        self.input2 = inputL2
        self.op =op
    def __str__(self):
        return (str(self.input1) + str(self.op) + str(self.input2) )
    def accept(self, visitor):
        visitor.visit_operation(self)
        

a = "a"
b = "b"
Input1 = Input(a)
Input2 = Input(b)

Output1 = Output("sum")
Output2 = Output("carry")

Operation1 = Operation("a","b","XOR")
Operation2 = Operation("a","b","AND")

Assignment1 = Assignment("sum",Operation1)
Assignment2 = Assignment("carry",Operation2)

Linput1 = [Input1,Input2]
Loutput1 = [Output1,Output2]
Lassignment = [Assignment1,Assignment2]

Circuit1 = Circuit(Linput1, Loutput1, Lassignment)
print(Circuit1)



print("============TEST PRETTY PRINTER=========\n")
from visiter import *
#Visitor().pp(Circuit1)
PrettyPrinter().visit_input(Input1)
#SemanticAnalyser()

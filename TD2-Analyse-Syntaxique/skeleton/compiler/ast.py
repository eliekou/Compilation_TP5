class If_stat:

    def __init__(self,cond,body,Else):
        self.cond = cond 
        self.body = body
        self.Else = Else

    def __str__(self):
        return("if (" + str(self.cond ) + "){" +str(self.body)+ "} " + str(self.Else))


#class Expression:

class Identifier:
    def __init__(self,id):
        self.id = id
    def __str(self):
        return(str(self.id))

class Assignment:

    def __init__(self,identifier,expression):
        self.identifier = identifier
        self.expression = expression

    def __str__(self):
        return(str(self.identifier) + " = " + str(self.expression ))


class Equality:

    def __init__(self,cond1,cond2):
        self.cond1 = cond1
        self.cond2 = cond2
    def __str__(self):
        return(str(self.cond1) + "==" + str(self.cond2))


class Mulop:

    def __init__(self,id1,id2,op):
        self.id1 = id1
        self.id2 = id2
        self.op = op

class Program:

    def __init__(self,condition = None,statement= None):
        self.condition = condition
        self.statement = statement
    def __str__(self):
        return(str(self.condition) + str(self.statement))

    
a =9
b = 10

Id1 = Identifier(a)
Id2 = Identifier(b)
X = Identifier(2)
Y = Identifier(3)

Eq1 = Equality(Id1,Id2)

Ass1 = Assignment(X,Y)


If1 = If_stat(Eq1, Ass1, None)


print(If1)
#Créer l'AST en mémoire grace au parseur
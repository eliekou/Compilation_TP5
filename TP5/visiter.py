class Visitor:
    def visit_circuit(self, circuit):
        for inp in circuit.Linput:
            inp.accept(self)
        for output in circuit.Loutput:
            output.accept(self)
        for assign in circuit.Lassign:
            assign.accept(self)
        
    def visit_output(self, output):
        pass

    def visit_input(self, input):
        pass

    def visit_operation(self, operation):
        pass

    def visit_assignment(self, assignment):
        assignment.droiteop.accept(self)


class PrettyPrinter(Visitor):
    def visit_input(self, input):
        print(input.id1)

    def visit_output(self, output):
        print(output.id1)

    def visit_operation(self, operation):
        print(f"{operation.gauche} {operation.op} {operation.droite}")

    def visit_assignment(self, assignment):
        print



class PrintVisitor:
    def pp(self,prog):
        print(self.visitProgram(prog,[]))
    



    def visitProgram(self,prog,args): 
        name= ([str(inp) for inp in prog.Linput])

        return name

class SemanticAnalyser:
    def __init__(self):
        self.DICT_INPUT =[]
        self.DICT_OUTPUT = []
        self.DICT_ASSIGNMENT = []

    def visitProgram(self,prog,args):

        for obs in prog.Linput:

            if obs in DICT_INPUT:
                raise "ERROR at #{obs} : duplicate identifier input '#{obs}'"
            if obs in DICT_OUTPUT:
                raise "ERROR at #{obs} : wrong identifier and duplicate identifier output '#{obs}'"
            if obs in DICT_ASSIGNMENT:
                raise "ERROR at #{obs} : wrong identifier and duplicate identifier assignment '#{obs}'"
            else:
                self.DICT_{args}.append(obs)


        for obs in prog.Loutput:

            if obs in DICT_INPUT:
                raise "ERROR at #{obs} : wrong identifier and duplicate identifier input '#{obs}'"
            if obs in DICT_OUTPUT:
                raise "ERROR at #{obs} : duplicate identifier output '#{obs}'"
            if obs in DICT_ASSIGNMENT:
                raise "ERROR at #{obs} : wrong identifier and duplicate identifier assignment '#{obs}'"
            else:
                self.DICT_{args}.append(obs)


        
        for obs in prog.Lassignment:

            if obs in DICT_INPUT:
                raise "ERROR at #{obs} : wrong identifier and duplicate identifier input '#{obs}'"
            if obs in DICT_OUTPUT:
                raise "ERROR at #{obs} : wrong identifier and duplicate identifier output '#{obs}'"
            if obs in DICT_ASSIGNMENT:
                raise "ERROR at #{obs} : duplicate identifier assignment '#{obs}'"
            else:
                self.DICT_{args}.append(obs) 
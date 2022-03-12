
class LogicGate():
    def __init__(self, n):
        self.label = n
        self.output = None
    
    def getLabel(self):
        return self.label
    
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):
    def __init__(self, n):
        super().__init__(n)
        self.pinA = None # How are we going to define these if nothing is passed to the constructor??
        self.pinB = None

    def setPinA(self):
        return int(input("Enter pin A input for gate " + self.getLabel() + "---> "))

    def setPinB(self):
        return int(input("Enter pin B input for gate " + self.getLabel() + "---> "))

    def setNextPin(self, source): # How does this work if source is the Connector instance itself? It doesn't have a value of 0 or 1?
        if self.pinA is None:
            self.pinA = source
        else:
            if self.pinB is None:
                self.pinB = source
            else:
                raise RuntimeError("Error: no empty pins") 
    
    def getPinA(self):
        if self.pinA is None:
            return self.setPinA()
        else:
            return self.pinA.getFrom().getOutput() # self.pinA needs to be a Connector object for this to work..? 
            # Yes, Gate.setNextPin() explicitly does this which takes in a Connector object as the source
            # Then, Connector.getFrom() returns a Gate object from which you can get its output
    
    def getPinB(self):
        if self.pinB is None:
            return self.setPinB()
        else:
            return self.pinB.getFrom().getOutput()


class UnaryGate(LogicGate):
    def __init__(self, n):
        super().__init__(n)
        self.pin = None

    def setPin(self):
        self.pin = int(input("Enter pin input for gate " + self.getLabel()+ "---> "))

    def setNextPin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            raise RuntimeError("Error: no empty pin")

    def getPin(self):
        if self.pin is None:
            return self.setPin()
        else:
            return self.pin.getFrom().getOutput()


class Connector():
    def __init__(self, fgate, tgate):
        self.fromGate = fgate
        self.toGate = tgate
        tgate.setNextPin(self) # Why not self.toGate.setNextPin(self)?

    def getFrom(self):
        return self.fromGate
    
    def getTo(self):
        return self.toGate


class OrGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)
    
    def performGateLogic(self):
        self.pinA = self.getPinA()
        self.pinB = self.getPinB()
        if self.pinA == 1 or self.pinB == 1:
            return 1
        return 0


class AndGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)
      
    def performGateLogic(self):
        self.pinA = self.getPinA()
        self.pinB = self.getPinB()
        if self.pinA == 1 and self.pinB == 1:
            return 1
        return 0


class NotGate(UnaryGate):
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        if self.getPin() == 0:
            return 1
        return 0


class NandGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 0
        return 1


class NorGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 0
        return 1

def main(): 
   g1 = NorGate("G1")
   g2 = NandGate("G2")
   g3 = OrGate("G3")
   g4 = NotGate("G4")
   c1 = Connector(g1,g3)
   c2 = Connector(g2,g3)
   c3 = Connector(g3,g4)
   print(g4.getOutput())
    

if __name__ == '__main__':
    main()
import connective_statements as cs

def bitToBool(bit):
    if int(bit):
        return True
    return False

class ass0:
    def __init__(self):
        self.string = 'p=>q if and only if ¬ q => ¬ p'
    def claim_func(self,p,q):
        return cs.iff(cs.imp(not q, not p), cs.imp(p,q))
    def claim(self,binary):
        return self.claim_func(bitToBool(binary[0]),bitToBool(binary[1]))

class ass1_1:
    def __init__(self):
        self.string = '¬ (p => q)'

    def claim_func(self, p , q):
        return not (cs.imp( p, q))
    def claim(self,binary):
        return self.claim_func(bitToBool(binary[0]),bitToBool(binary[1]))

class ass128_1:
    def __init__(self):
        self.string = "a'b + a'b'c'd' + abcd'"

    def claim_func(self,a,b,c,d):
        return (not(a) and b) or (not(a) and not(b) and not(c) and not(d)) or (a and b and c and not(d))

    def claim(self,binary):
        return self.claim_func(bitToBool(binary[0]),bitToBool(binary[1]),bitToBool(binary[2]),bitToBool(binary[3]))

class ass1_3:
    def __init__(self):
        self.string = '(P => q) => (p => q) iff p => P'

    def claim_func(self,P,p,q):
        return cs.iff( cs.imp( cs.imp(P,q), cs.imp(p,q)), cs.imp(p,P))

    def claim(self,binary):
        return self.claim_func(bitToBool(binary[0]),bitToBool(binary[1]),bitToBool(binary[2]))

class ass1_3_1:
    def __init__(self):
        self.string = '(p => P => q) => (p=>q)'

    def claim_func(self,P,p,q):
        return cs.imp(cs.imp(cs.imp(p,P), q),cs.imp(p,q))

    def claim(self,binary):
        return self.claim_func(bitToBool(binary[0]),bitToBool(binary[1]),bitToBool(binary[2]))

class ass1_3_2:
    def __init__(self):
        self.strings = ['p => P','P => q','p => q','(P => q) => (p=>q)','(p => P) => ((P => q) => (p=>q))']

    def claim_func(self,p,P,q):
        p1 = cs.imp(p,P)
        p2 = cs.imp(P,q)
        p3 = cs.imp(p,q)
        p4 = cs.imp(p2,p3)
        p5 = cs.imp(p1,p4)
        return [p1,p2,p3,p4,p5]

    def claim(self,binary):
        return self.claim_func(bitToBool(binary[0]),bitToBool(binary[1]),bitToBool(binary[2]))

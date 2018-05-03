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

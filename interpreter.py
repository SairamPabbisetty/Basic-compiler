class Interpreter :
    def __init__(self, tree) :
        self.tree = tree

    def readINT(self, value) :
        return int(value)
    
    def readFLOAT(self, value) :
        return float(value)

    def computeBin(self, left, op, right) :
        left_type = left.type
        right_type = right.type

        left = getattr(self, f"read{left_type}")(left.value)
        right = getattr(self, f"read{right_type}")(right.value)

        if op.type == "+" :
            return left + right

    def interpret(self) :
        left_node = self.tree[0]
        operator = self.tree[1]
        right_node = self.tree[2]

        return self.computeBin(left_node, operator, right_node)
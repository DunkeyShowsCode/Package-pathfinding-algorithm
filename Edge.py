# Keeps track of all the edges connecting the vertices (address)
# @pram - from_node: the departure address
# @parm - to_node: the arrival address
# @parm - weight: the miles between from_node and to_node
class Edge():
    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight

    def __str__(self):
        # -> {self.weight}
        return f"{self.from_node} -> {self.to_node}"

import math
class polyhedron():
    
    def Surface(Edges): 
             thisEdges = 1
             Tetrahedron = 8 * math.sqrt(3) / 3 * [Edges]
     
             Hexahedron = 8 * [Edges]
    
             Octahedron = 4 * math.sqrt(3) * [Edges]
    
             Dodecahedron = 3 * math.sqrt(25 + 10 * math.sqrt(5)) * [Edges]
    
             Icosahedron = [30 * math.sqrt(3) - 10 * math.sqrt(15)] * [Edges]

    def Volume(Radius):
             thisRadius = 1
             Tetrahedron = 8 * math.sqrt(3) * [Radius]/27

             Hexahedron = 8 * math.sqrt(3) * [Radius]/9

             Octahedron = (4/3) * [Radius]

             Dodecahedron = [15 + 7 * math.sqrt(5)]/4 * [Radius]

             Tetrahedron = math.sqrt[25 + 10 * math.sqrt(5)]/4 * [Radius]

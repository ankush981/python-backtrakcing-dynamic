# Given an undirected graph, find out if it has a Hamiltonian cycle and print it

class HamiltonianProblem:
    def __init__(self, adjacency_matrix):
        self.num_vertices = len(adjacency_matrix)
        self.hamiltonian_path = [None] * self.num_vertices
        self.adjacency_matrix = adjacency_matrix
    
    def hamiltonian_cycle(self):
        # Add first vertex to the path
        self.hamiltonian_path[0] = 0 # note that the names of the vertices in the algorithm are 0, 1, 2 ... while in the diagram it was a, b, c ...

        if not self.find_feasible_solution(1):
            print("No feasible solution")
            return
        
        self.show_hamiltonian_path()
    
    # position is position in the Hamiltonian array we are keeping
    def find_feasible_solution(self, position):
        # check whether we are at the last node, and if so, does it connect to the first node
        if (position == self.num_vertices):
            last_element = self.hamiltonian_path[position - 1]
            first_element = self.hamiltonian_path[0]

            if(self.adjacency_matrix[last_element][first_element] == 1):
                return True
            
            return False
        
        # compare the current vertex with all other vertices except the first
        for vertex_index in range(1, self.num_vertices):
            if self.is_feasible(vertex_index, position):
                # add the vertex_index to the Hamiltonian path
                self.hamiltonian_path[position] = vertex_index
                if self.find_feasible_solution(position + 1):
                    return True
                
                # "Backtrack" because the for-loop will pick the next vertex to compare
        return False
    
    # vertex_num is the current vertex in the graph that we're checking against
    # while vertex_index is just an iterator across all vertices
    def is_feasible(self, vertex_index, vertex_num):
        # first check: is the current vertex connected to the last vertex in the Hamiltonian path?
        last_vertex = self.hamiltonian_path[vertex_num - 1]
        if self.adjacency_matrix[last_vertex][vertex_index] == 0:
            return False

        # second check: have we already added the given node?
        for i in range(vertex_num):
            if self.hamiltonian_path[i] == vertex_index:
                return False

        return True
    
    def show_hamiltonian_path(self):
        print("Cycle: ")
        print(self.hamiltonian_path, '->', self.hamiltonian_path[0])

if __name__ == "__main__":
    adjacency_matrix = [
        [0, 1, 1, 0, 0, 1],
        [1, 0, 0, 1, 0, 1],
        [1, 0, 0, 1, 1, 1],
        [0, 1, 1, 0, 1, 1],
        [0, 0, 1, 1, 0, 0],
        [1, 1, 1, 1, 0, 0]
    ]

    problem = HamiltonianProblem(adjacency_matrix)
    problem.hamiltonian_cycle()




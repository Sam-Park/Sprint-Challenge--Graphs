"""
Simple graph implementation compatible with BokehGraph class.
"""


class Vertex:
    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component

    def __repr__(self):
        return 'Vertex: ' + self.label


class Graph:
    """Trying to make this Graph class work..."""
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        if vertex in self.vertices:
            raise Exception('Error! That vertex already exists')
        if not set(edges).issubset(self.vertices):
            raise Exception('Error, cannot have edge to vertex that does not exist')
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Verticies to connect not in graph')
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def dfs(self, start, target=None):
        stack = [start]
        visited = set()

        while stack:
            print("stack", stack)
            current = stack.pop()
            if current == target:
                break
            visited.add(current)
            stack.extend(self.vertices[current] - visited)

        return visited
    ###########################
    #########lecture Code#######
    ###########################

    """def dfs_recursive(self, start, visited=None, target=None):
        visited = visited or set()
        visited.append(start)
        for vertex in self.vertices[start]:
            if vertex not in visited:
                self.dfs_recursive(vertex, visited=visited)
        return visited"""
    #### Inner method recursion ####

    def dfs_recursive(self, start, target=None):
        def dfs_helper(vertex, visited):
            visited.add(vertex)
            for neighbor in self.vertices[vertex]:
                if neighbor not in visited:
                    dfs_helper(neighbor, visited)
            return visited
        return dfs_helper(start, set())
    ###########################
    #########Sprint Code#######
    ###########################
    """def graph_rec(self, start, target=None):
        x = set()
        x.append(start)
        for v in self.vertices[start]:
            graph_rec(v)
        return x"""

    def find_components(self):
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            if vertex not in visited:
                reachable = self.dfs(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component

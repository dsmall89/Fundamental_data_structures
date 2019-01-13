from collections import defaultdict
class graph(object):
    def __init__(self, connections, directed = False):
        self.graph = defaultdict(set)
        self.directed = directed
        self.add_Connections(connections)

    def add_Connections(self,connections):
        for start_node, end_node in connections:
            self.add(start_node, end_node)

    def add(self, start_node,end_node):
        self.graph[start_node].add(end_node)
        if not self.directed:
            self.graph[end_node].add(start_node)


    def is_Connected(self,start_node,end_node):

        return start in self.graph and node in self.graph[start_node]
# Determines a path between two nodes,
#takes a self.graph and the start_node and end_node nodes as args.
    def find_Path(self, start_node, end_node, path= []):
        path = path + [start_node_node]

        if start_node == end_node :
            return path

        if not self.graph.has_key(start_node):
            return none

        for node in self.graph[start_node]:
            if node not in path:
                newpath = self.find_Path( start_node, end_node, path)

                if newpath:
                    #returns a  list of nodes comprising the path.
                    return newpath
        #if no path are return None !
        return None

    def find_All_paths(self, start_node, end_node, path= []):
        path = path + [start_node]

        if start_node == end_node:
            return [path]

        if not self.graph.has_key(start_node):
            return []
        paths = []

        for node in self.graph[start_node]:
            if node not in path :
                newpaths = self.find_All_paths(start_node, end_node, path)

                for newpath in newpaths:
                    paths.append_node(newpath)
        return paths

    def find_Shortest_path(self,start_node, end_node , path=[]):
        path = path + [start_node]

        if start_node == end_node:

            return path

        if not self.graph.has_key(start_node):
            return None
        shortest = None
        for node in self.graph[start_node]:
            if node not in path:
                newpath = self.find_Shortest_path( self.node, end_node, path)

                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest= newpath
        return shortest

def main():
    connections = [('A', 'B'), ('B', 'C'), ('B', 'D'),
               ('C', 'D'), ('E', 'F'), ('F', 'C')]
    a_graph = graph(connections, directed = True)
    print(a_graph.graph),
    print("\n")

main()

import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, v, w):
        if v not in self.adj:
            self.adj[v] = []
        if w not in self.adj:
            self.adj[w] = []

        if w not in self.adj[v]:
            self.adj[v].append(w)
        if v not in self.adj[w]: 
            self.adj[w].append(v)

    def is_eulerian(self):
        odd = 0
        for v in self.adj:
            if len(self.adj[v]) % 2 != 0:
                odd += 1

        if odd > 2:
            return 0  
        elif odd == 2:
            return 1 
        else:
            return 2  

    def print_result(self):
        res = self.is_eulerian()
        if res == 0:
            return "Não é Euleriano"
        elif res == 1:
            return "Semi-Euleriano"
        else:
            return "É Euleriano"

    def draw_graph(self, filename):
        G = nx.Graph()
        for v, neighbors in self.adj.items():
            for w in neighbors:
                G.add_edge(v, w)

        plt.figure(figsize=(8, 8))
        nx.draw(G, with_labels=True, node_color='skyblue', edge_color='gray', node_size=3000, font_size=15, font_weight='bold')
        plt.title(f"Grafo: {filename}", fontsize=20)
        plt.savefig(f"{filename}.png")
        plt.close()
        print(f"Imagem do grafo salva como {filename}.png")

def read_graph_from_file(filename):
    g = Graph()
    with open(filename, 'r') as file:
        lines = file.readlines()

    edges = []
    for line in lines:
        if line.strip():  
            v, w = map(int, line.split())
            edges.append((v, w))

    for u, v in edges:
        g.add_edge(u, v)

    return g

def main():
    filenames = ['Email-Enron.txt', 'grafo1.txt', 'grafo2.txt', 'grafo3.txt', 'grafo4.txt']

    for filename in filenames:
        g = read_graph_from_file(filename)
        print(f"Resultado para {filename}: {g.print_result()}")
        g.draw_graph(filename.split('.')[0]) 

if __name__ == "__main__":
    main()

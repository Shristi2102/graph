from multipledispatch import dispatch
nodes = []
graph = []
node_count = 0
def add_node(v):
    global node_count
    if v in nodes:
        print(v, "already present")
    else:
        node_count = node_count + 1
        nodes.append(v)
        for i in graph:
            i.append(0)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)

def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j], end = " ")
        print()

# for undirected and unweighted graph

@dispatch(str, str)
def add_edge(v1, v2):
    if v1 not in nodes:
        print(v1, "node not present")

    elif v2 not in nodes:
        print(v2, "node not present")

    else:
        list1 = nodes.index(v1)
        list2 = nodes.index(v2)
        graph[list1][list2] = 1
        graph[list2][list1] = 1

# for directed and weighted graph

@dispatch(str, str, int)
def add_edge(v1, v2, cost):
    if v1 not in nodes:
        print(v1, "node not present")

    elif v2 not in nodes:
        print(v2, "node not present")

    else:
        list1 = nodes.index(v1)
        list2 = nodes.index(v2)
        graph[list1][list2] = cost

add_node("A")
add_node("B")
add_node("C")
add_edge("A", "B")
print_graph()
add_edge("A", "B", 5)

print(node_count)
print_graph()

import json
import numpy as np
from tabulate import tabulate


def read_file(filename):
    file = open(filename)
    paths = json.load(file)
    file.close()

    vertices = []
    for i in paths:
        if i[0] not in vertices:
            vertices.append(i[0])
        elif i[1] not in vertices:
            vertices.append(i[1])
    vertices.sort()

    return paths, vertices


def dijkstra(paths, vertices, source_vertex):
    finalised = []
    distance = {}
    left = vertices.copy()
    for i in vertices:
        if i == source_vertex:
            distance[i] = [None, 0]
        else:
            distance[i] = [None, np.inf]
    while len(finalised) != len(vertices):
        chosen = min(left, key=lambda x: distance[x][1])
        left.remove(chosen)
        finalised.append(chosen)
        for i in paths:
            if i[0] == chosen:
                if (distance[chosen][1] + i[2]) < distance[i[1]][1]:
                    distance[i[1]] = [chosen, distance[chosen][1] + i[2]]

    return distance


def print_table(distance: dict):
    table = np.empty([3, len(distance)], dtype=object)
    for i, vertex in enumerate(distance.keys()):
        table[0, i] = vertex
        table[1, i] = distance[vertex][1]
        table[2, i] = distance[vertex][0]
    table = tabulate(table, tablefmt="fancy_grid")
    print(table)


def main():
    filename = input("Enter the name of the file: ")
    source_vertex = input("Enter the source vertex: ")
    paths, vertices = read_file(filename)
    distance = dijkstra(paths, vertices, source_vertex)
    print_table(distance)


if __name__ == "__main__":
    main()

import sys

def eulerian_cycle(edge_dict):
    current_node = list(edge_dict.keys())[0]
    path = [current_node]
    while True:
        path.append(edge_dict[current_node][0])

        if len(edge_dict[current_node]) == 1:
            del edge_dict[current_node]
        else:
            edge_dict[current_node] = edge_dict[current_node][1:]

        if path[-1] in edge_dict:
            current_node = path[-1]
        else:
            break
    while len(edge_dict) > 0:
        for i in range(len(path)):
            if path[i] in edge_dict:
                current_node = path[i]
                cycle = [current_node]
                while True:
                    cycle.append(edge_dict[current_node][0])
                    if len(edge_dict[current_node]) == 1:
                        del edge_dict[current_node]
                    else:
                        edge_dict[current_node] = edge_dict[current_node][1:]

                    if cycle[-1] in edge_dict:
                        current_node = cycle[-1]
                    else:
                        break

                path = path[:i] + cycle + path[i+1:]
                break
    return path

if __name__ == '__main__':
    #filename = sys.stdin.read().strip()
    file_name = input("State file name: ").strip()
    with open(file_name, 'r') as input_data:
        from collections import OrderedDict
        edges = OrderedDict()
        for edge in [line.strip().split(' -> ') for line in input_data.readlines()]:
            if ',' in edge[1]:
                edges[int(edge[0])] = list(map(int,edge[1].split(',')))
            else:
                edges[int(edge[0])] = [int(edge[1])]
    #print edges
    path = eulerian_cycle(edges)
    # print('->'.join(list(map(str,path))))
    with open('answer_eulerian_cycle.txt', 'w') as output_data:
        output_data.write('->'.join(list(map(str,path))))
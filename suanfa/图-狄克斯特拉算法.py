

# 创建图（散列表存储）
def create_graph():
    graph = {}
    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2
    graph["a"] = {}
    graph["a"]["fin"] = 1
    graph["b"] = {}
    graph["b"]["a"] = 3
    graph["b"]["fin"] = 5
    graph["fin"] = {}
    return graph


# 创建散列表存储每一个节点的开销
def create_costs():
    costs = {}
    costs["a"] = 6
    costs["b"] = 2
    # 无穷大
    infinity = float("inf")
    costs["fin"] = infinity
    return costs


# 创建散列表存储父节点
def create_parents():
    parents = {}
    parents["a"] = "start"
    parents["b"] = "start"
    parents["fin"] = None
    return parents


# 在未处理的节点中找出开销最小的节点
def find_lowest_cost_node(costs, processed):
    if isinstance(costs, dict):
        lower_cost = float("inf")
        lower_cost_node = None
        for key in costs.keys():
            cost = costs[key]
            # 如果当前节点的开销更低且未处理过
            if cost < lower_cost and key not in processed:
                lower_cost = cost
                lower_cost_node = key
        return lower_cost_node


if __name__ == "__main__":
    # 用来记录已经处理过的节点
    processed = []
    graph = create_graph()
    costs = create_costs()
    parents = create_parents()
    # 找出开销最低的节点
    lower_cost_node = find_lowest_cost_node(costs, processed)
    while lower_cost_node is not None:
        cost = costs[lower_cost_node]
        neighbors = graph[lower_cost_node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = lower_cost_node
        processed.append(lower_cost_node)
        lower_cost_node = find_lowest_cost_node(costs, processed)

    print(costs)
    print(parents)

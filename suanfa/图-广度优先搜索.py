
# 创建图
def create_graph():
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []
    return graph


# 创建搜索队列
def create_search_queue():
    from collections import deque
    graph = create_graph()
    search_queue = deque()
    search_queue.extend(graph["you"])
    is_cheakd = []
    while search_queue:
        person = search_queue.popleft()
        # 检查此人是否满足要求
        if person_is_true(person) and (person not in is_cheakd):
            is_cheakd.append(person)
            print(person + " is True")
            return True
        else:
            search_queue.extend(graph[person])
    return False


# 检查是否满足要求
def person_is_true(name):
    return name[-1] == 'm'


if __name__ == "__main__":
    print(create_search_queue())
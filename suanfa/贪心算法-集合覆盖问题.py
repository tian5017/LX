'''
假设你办了个广播节目，要让全美50个州的听众都收听得到。为此，你需要决定在哪些广播台播出。在每个广播台播出都需要支付费用，因此你力图在尽可能少的广播台播出。
'''

def greedy_test():
    # 创建一个列表，其中包含要覆盖的州
    states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
    # 广播台覆盖清单
    stations = {}
    stations["kone"] = set(["id", "nv", "ut"])
    stations["ktwo"] = set(["wa", "id", "mt"])
    stations["kthree"] = set(["or", "nv", "ca"])
    stations["kfour"] = set(["nv", "ut"])
    stations["kfive"] = set(["ca", "az"])
    # 存储最终选择的广播台
    final_stations = set()
    while states_needed:
        # 迭代中存放覆盖最多州的广播台
        best_station = None
        # 迭代中存放覆盖最多州广播台所覆盖的州集合
        states_covered = set()
        for station, states_for_station in stations.items():
            # 计算交集
            coverred = states_needed & states_for_station
            if coverred is not None and len(coverred) > 0:
                if len(coverred) > len(states_covered):
                    best_station = station
                    states_covered = coverred
                # 将覆盖最多州的广播台存入final_stations中
                final_stations.add(best_station)
                # 从全集中去除已经覆盖的州(差集)
                states_needed = states_needed - states_covered
    return final_stations




if __name__ == "__main__":
    print(greedy_test())

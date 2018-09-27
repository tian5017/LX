import pandas as pd
import numpy as np


def make_df(cols, ind):
    data = {c: [str(c) + str(i) for i in ind] for c in cols}
    return pd.DataFrame(data, ind)


def m_1():
    ser1 = pd.Series(['A', 'B', 'C'], index=[1, 2, 3])
    ser2 = pd.Series(['D', 'E', 'F'], index=[1, 2, 3])
    print(pd.concat([ser1, ser2], ignore_index=True))

    df1 = make_df('ABC', [1, 2, 3])
    df2 = make_df('DEF', [1, 2, 3])
    print(pd.concat([df1, df2], axis=1))


def m_2():
    df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
                        'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})
    print(df1)
    df2 = pd.DataFrame({'group': ['Accounting', 'Accounting', 'Engineering', 'Engineering', 'HR', 'HR'],
                        'skills': ['math', 'spreadsheets', 'coding', 'linux', 'spreadsheets', 'organization']})
    print(df2)
    print(pd.merge(df1, df2))


def m_3():
    df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
                        'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})
    print(df1)
    df2 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                        'salary': [70000, 80000, 120000, 90000]})
    print(df2)
    print(pd.merge(df1, df2, left_on="employee", right_on="name"))
    print(pd.merge(df1, df2, left_on="employee", right_on="name").drop("name", axis=1))


def m_4():
    df1 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                        'rank': [1, 2, 3, 4]})
    print(df1)
    df2 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                        'rank': [3, 1, 4, 2]})
    print(df2)
    print(pd.merge(df1, df2, on="name"))
    print(pd.merge(df1, df2, on="name", suffixes=["_L", "_R"]))


if __name__ == "__main__":
    # df = make_df('ABCDEFGH', [1, 2, 3, 4, 5, 6, 7, 8])
    # print(df)
    # print(df["D"])

    a = np.array([1,2,3,4,5])
    b = np.array([6, 7, 8, 9, 10])
    c = (a - b) / a
    print(c)
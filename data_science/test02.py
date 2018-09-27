import pandas as pd
import numpy as np


pop = pd.read_csv("data/state-population.csv")
areas = pd.read_csv("data/state-areas.csv")
abbrevs = pd.read_csv("data/state-abbrevs.csv")

# 合并pop和abbrevs
mer = pd.merge(pop, abbrevs, how="outer", left_on="state/region", right_on="abbreviation")
# 去掉重复列
mer = mer.drop("abbreviation", axis=1)
print(mer.head())

# 检查缺失值
print(mer.loc[mer["population"].isnull(), "state/region"].unique())
print(mer.loc[mer["state"].isnull(), "state/region"].unique())

# 填充缺失值
mer.loc[mer["state/region"] == "PR", "state"] = "Puerto Rico"
mer.loc[mer["state/region"] == "USA", "state"] = "United States"

# 合并areas
mer_over = pd.merge(mer, areas, on="state")
print(mer_over.head())

mer_over.loc[mer_over["population"].isnull(), "population"] = round(np.mean(mer_over.loc[mer_over["population"].notnull(), "population"]))
print("----------------------------------")
print("检查是否有缺失值：")
print(mer_over.isnull().any())
mer_over.to_csv("data/data-over.csv")

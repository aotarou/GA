import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# データフレームから距離を計算
def calc_distance(dataframe):
    distance = 0
    for col in range(len(dataframe.columns)):   # 列の数だけ繰り返す
        distance += dataframe[col]**2
    distance = np.sqrt(distance) # ユークリッド距離を計算
    return distance

# データフレームの結合
def merge_dataframe(origin, add):
    origin = pd.concat([origin, add], axis=1)
    return origin

# 時系列データとしてグラフを作成
def plot_log(distance, MaxGeneration):
    y_mean = np.array(distance.mean())      # データの平均値を取得
    y_median = np.array(distance.median())  # 中央値を取得
    y_min = np.array(distance.min()) # 最小値を取得
    y_max = np.array(distance.max()) # 最大値を取得
    x = np.arange(len(y_mean))
    xicks = np.arange(0, MaxGeneration+1, MaxGeneration/10)   # MaxGenerationもメモリに表示させるために+1
    plt.plot(x, y_mean, label="mean", color="green")
    plt.plot(x, y_median,label="median", color="blue")
    plt.plot(x, y_min, label="min", color="red")
    plt.plot(x, y_max, label="max", color="cyan")
    plt.xlabel("$Generation$", fontsize=15)
    plt.ylabel("$distance$", fontsize=15)
    plt.xlim(xmin=0)
    plt.ylim(ymin=0)
    plt.grid(True)
    plt.xticks(xicks)
    plt.legend()
    plt.title("20 dimension")
    plt.savefig("analysis_gene.jpg")



MaxGeneration = 2000

for G in range(MaxGeneration):
    if G==0:
        gene_path = "./Out/" + str(G) + ".gene"
        dataframe_0 = pd.read_csv(gene_path, header=None)  # データの読み取り
        distance_0 = calc_distance(dataframe_0)            # データフレームから距離を計算
    else:
        gene_path = "./Out/" + str(G) + ".gene"
        dataframe = pd.read_csv(gene_path, header=None)
        distance = calc_distance(dataframe)
        distance_0 = merge_dataframe(distance_0, distance)

plot_log(distance_0, MaxGeneration)

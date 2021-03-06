import json
import urllib.parse
import urllib.request
import pandas as pd
from pandas.io.pytables import dropna_doc
import ssl

#APIキーの読み込み
api_key = "your_api"

#APIのデータ種部分の入力
url_base = 'https://opendata.resas-portal.go.jp/api/v1/municipality/company/perYear'

l = [] #元データを格納するリスト


"""
元データの取得（注1：存在しないcityCodeを入力するとエラーが出る)
"""

#dataFrameの本体の作成
for city_code in range(1100, 1101): #range部分にcityCodeの範囲を入力（注1）
    url = url_base + '?cityCode=0' + str(city_code) + '&prefCode=1' #url生成
    req = urllib.request.Request(url, headers=api_key) #RESASへリクエスト
    with urllib.request.urlopen(req) as response: #応答の読み込み
        data = response.read()
    d = json.loads(data.decode()) #json形式にデコード
    l.append(pd.json_normalize(d['result'])) #データをpandas Seriesに直してリストに格納
    print(url) #urlが正しいかの確認用
df_all = pd.concat(l, ignore_index=True) #リスト内のデータを結合（pandas dataFrame化）

#dataFrameにデータを追加する関数の定義
def get_data(s_cC, e_cC, c_head, pref_code, df_all):
    l = [] #リストlのリフレッシュ
    for city_code in range(s_cC, e_cC): #range部分にcityCodeの範囲を入力（注1）
        url = url_base + '?cityCode=' + str(c_head) + format(city_code, '04') + '&prefCode=' + str(pref_code) #url生成
        req = urllib.request.Request(url, headers=api_key) #RESASへリクエスト
        with urllib.request.urlopen(req) as response: #応答の読み込み
            data = response.read()
        d = json.loads(data.decode()) #json形式にデコード
        l.append(pd.json_normalize(d['result'])) #データをpandas Seriesに直してリストに格納
        print(url) #urlが正しいかの確認用
    df_all_add = pd.concat(l, ignore_index=True) #リスト内のデータを結合（pandas dataFrame化）

    df_all = pd.concat([df_all, df_all_add]) #データの追加

    return df_all

df_all = get_data(1202, 1232, 0, 1, df_all)
df_all = get_data(1233, 1237, 0, 1, df_all)
df_all = get_data(1303, 1305, 0, 1, df_all)
df_all = get_data(1331, 1335, 0, 1, df_all)
df_all = get_data(1337, 1338, 0, 1, df_all)
df_all = get_data(1343, 1344, 0, 1, df_all)
df_all = get_data(1345, 1348, 0, 1, df_all)
df_all = get_data(1361, 1365, 0, 1, df_all)
df_all = get_data(1367, 1368, 0, 1, df_all)
df_all = get_data(1370, 1372, 0, 1, df_all)
df_all = get_data(1391, 1410, 0, 1, df_all)
df_all = get_data(1423, 1426, 0, 1, df_all)
df_all = get_data(1427, 1435, 0, 1, df_all)
df_all = get_data(1436, 1439, 0, 1, df_all)
df_all = get_data(1452, 1466, 0, 1, df_all)
df_all = get_data(1468, 1473, 0, 1, df_all)
df_all = get_data(1481, 1488, 0, 1, df_all)
df_all = get_data(1511, 1515, 0, 1, df_all)
df_all = get_data(1516, 1521, 0, 1, df_all)
df_all = get_data(1543, 1548, 0, 1, df_all)
df_all = get_data(1549, 1551, 0, 1, df_all)
df_all = get_data(1552, 1553, 0, 1, df_all)
df_all = get_data(1555, 1556, 0, 1, df_all)
df_all = get_data(1559, 1565, 0, 1, df_all)
df_all = get_data(1571, 1572, 0, 1, df_all)
df_all = get_data(1575, 1576, 0, 1, df_all)
df_all = get_data(1578, 1579, 0, 1, df_all)
df_all = get_data(1581, 1582, 0, 1, df_all)
df_all = get_data(1584, 1587, 0, 1, df_all)
df_all = get_data(1601, 1603, 0, 1, df_all)
df_all = get_data(1604, 1605, 0, 1, df_all)
df_all = get_data(1607, 1611, 0, 1, df_all)
df_all = get_data(1631, 1640, 0, 1, df_all)
df_all = get_data(1641, 1650, 0, 1, df_all)
df_all = get_data(1661, 1666, 0, 1, df_all)
df_all = get_data(1667, 1669, 0, 1, df_all)
df_all = get_data(1691, 1695, 0, 1, df_all)
df_all = get_data(2201, 2211, 0, 2, df_all)
df_all = get_data(2301, 2302, 0, 2, df_all)
df_all = get_data(2303, 2305, 0, 2, df_all)
df_all = get_data(2307, 2308, 0, 2, df_all)
df_all = get_data(2321, 2322, 0, 2, df_all)
df_all = get_data(2323, 2324, 0, 2, df_all)
df_all = get_data(2343, 2344, 0, 2, df_all)
df_all = get_data(2361, 2363, 0, 2, df_all)
df_all = get_data(2367, 2368, 0, 2, df_all)
df_all = get_data(2381, 2382, 0, 2, df_all)
df_all = get_data(2384, 2385, 0, 2, df_all)
df_all = get_data(2387, 2388, 0, 2, df_all)
df_all = get_data(2401, 2403, 0, 2, df_all)
df_all = get_data(2405, 2407, 0, 2, df_all)
df_all = get_data(2408, 2409, 0, 2, df_all)
df_all = get_data(2411, 2413, 0, 2, df_all)
df_all = get_data(2423, 2427, 0, 2, df_all)
df_all = get_data(2441, 2444, 0, 2, df_all)
df_all = get_data(2445, 2447, 0, 2, df_all)
df_all = get_data(2450, 2451, 0, 2, df_all)
df_all = get_data(3201, 3204, 0, 3, df_all)
df_all = get_data(3205, 3212, 0, 3, df_all)
df_all = get_data(3213, 3217, 0, 3, df_all)
df_all = get_data(3301, 3304, 0, 3, df_all)
df_all = get_data(3321, 3323, 0, 3, df_all)
df_all = get_data(3366, 3367, 0, 3, df_all)
df_all = get_data(3381, 3382, 0, 3, df_all)
df_all = get_data(3402, 3403, 0, 3, df_all)
df_all = get_data(3441, 3442, 0, 3, df_all)
df_all = get_data(3461, 3462, 0, 3, df_all)
df_all = get_data(3482, 3486, 0, 3, df_all)
df_all = get_data(3501, 3502, 0, 3, df_all)
df_all = get_data(3503, 3504, 0, 3, df_all)
df_all = get_data(3506, 3508, 0, 3, df_all)
df_all = get_data(3524, 3525, 0, 3, df_all)
df_all = get_data(4100, 4101, 0, 4, df_all)
df_all = get_data(4202, 4204, 0, 4, df_all)
df_all = get_data(4205, 4210, 0, 4, df_all)
df_all = get_data(4211, 4217, 0, 4, df_all)
df_all = get_data(4301, 4303, 0, 4, df_all)
df_all = get_data(4321, 4325, 0, 4, df_all)
df_all = get_data(4341, 4342, 0, 4, df_all)
df_all = get_data(4361, 4363, 0, 4, df_all)
df_all = get_data(4401, 4402, 0, 4, df_all)
df_all = get_data(4404, 4405, 0, 4, df_all)
df_all = get_data(4406, 4407, 0, 4, df_all)
df_all = get_data(4421, 4423, 0, 4, df_all)
df_all = get_data(4424, 4425, 0, 4, df_all)
df_all = get_data(4444, 4446, 0, 4, df_all)
df_all = get_data(4501, 4502, 0, 4, df_all)
df_all = get_data(4505, 4506, 0, 4, df_all)
df_all = get_data(4581, 4582, 0, 4, df_all)
df_all = get_data(4606, 4607, 0, 4, df_all)
df_all = get_data(5201, 5205, 0, 5, df_all)
df_all = get_data(5206, 5208, 0, 5, df_all)
df_all = get_data(5209, 5216, 0, 5, df_all)
df_all = get_data(5303, 5304, 0, 5, df_all)
df_all = get_data(5327, 5328, 0, 5, df_all)
df_all = get_data(5346, 5347, 0, 5, df_all)
df_all = get_data(5348, 5350, 0, 5, df_all)
df_all = get_data(5361, 5362, 0, 5, df_all)
df_all = get_data(5363, 5364, 0, 5, df_all)
df_all = get_data(5366, 5367, 0, 5, df_all)
df_all = get_data(5368, 5369, 0, 5, df_all)
df_all = get_data(5434, 5435, 0, 5, df_all)
df_all = get_data(5463, 5465, 0, 5, df_all)
df_all = get_data(6201, 6214, 0, 6, df_all)
df_all = get_data(6301, 6303, 0, 6, df_all)
df_all = get_data(6321, 6325, 0, 6, df_all)
df_all = get_data(6341, 6342, 0, 6, df_all)
df_all = get_data(6361, 6368, 0, 6, df_all)
df_all = get_data(6381, 6383, 0, 6, df_all)
df_all = get_data(6401, 6404, 0, 6, df_all)
df_all = get_data(6426, 6427, 0, 6, df_all)
df_all = get_data(6428, 6429, 0, 6, df_all)
df_all = get_data(6461, 6462, 0, 6, df_all)
df_all = get_data(7201, 7206, 0, 7, df_all)
df_all = get_data(7207, 7215, 0, 7, df_all)
df_all = get_data(7301, 7302, 0, 7, df_all)
df_all = get_data(7303, 7304, 0, 7, df_all)
df_all = get_data(7308, 7309, 0, 7, df_all)
df_all = get_data(7322, 7323, 0, 7, df_all)
df_all = get_data(7342, 7343, 0, 7, df_all)
df_all = get_data(7344, 7345, 0, 7, df_all)
df_all = get_data(7362, 7363, 0, 7, df_all)
df_all = get_data(7364, 7365, 0, 7, df_all)
df_all = get_data(7367, 7369, 0, 7, df_all)
df_all = get_data(7402, 7403, 0, 7, df_all)
df_all = get_data(7405, 7406, 0, 7, df_all)
df_all = get_data(7407, 7409, 0, 7, df_all)
df_all = get_data(7421, 7424, 0, 7, df_all)
df_all = get_data(7444, 7448, 0, 7, df_all)
df_all = get_data(7461, 7462, 0, 7, df_all)
df_all = get_data(7464, 7467, 0, 7, df_all)
df_all = get_data(7481, 7485, 0, 7, df_all)
df_all = get_data(7501, 7506, 0, 7, df_all)
df_all = get_data(7521, 7523, 0, 7, df_all)
df_all = get_data(7541, 7549, 0, 7, df_all)
df_all = get_data(7561, 7562, 0, 7, df_all)
df_all = get_data(7564, 7565, 0, 7, df_all)
df_all = get_data(8201, 8206, 0, 8, df_all)
df_all = get_data(8207, 8209, 0, 8, df_all)
df_all = get_data(8210, 8213, 0, 8, df_all)
df_all = get_data(8214, 8218, 0, 8, df_all)
df_all = get_data(8219, 8237, 0, 8, df_all)
df_all = get_data(8302, 8303, 0, 8, df_all)
df_all = get_data(8309, 8311, 0, 8, df_all)
df_all = get_data(8341, 8342, 0, 8, df_all)
df_all = get_data(8364, 8365, 0, 8, df_all)
df_all = get_data(8442, 8444, 0, 8, df_all)
df_all = get_data(8447, 8448, 0, 8, df_all)
df_all = get_data(8521, 8522, 0, 8, df_all)
df_all = get_data(8542, 8543, 0, 8, df_all)
df_all = get_data(8546, 8547, 0, 8, df_all)
df_all = get_data(8564, 8565, 0, 8, df_all)
df_all = get_data(9201, 9207, 0, 9, df_all)
df_all = get_data(9208, 9212, 0, 9, df_all)
df_all = get_data(9213, 9217, 0, 9, df_all)
df_all = get_data(9301, 9302, 0, 9, df_all)
df_all = get_data(9342, 9346, 0, 9, df_all)
df_all = get_data(9361, 9362, 0, 9, df_all)
df_all = get_data(9364, 9365, 0, 9, df_all)
df_all = get_data(9384, 9385, 0, 9, df_all)
df_all = get_data(9386, 9387, 0, 9, df_all)
df_all = get_data(9407, 9408, 0, 9, df_all)
df_all = get_data(9411, 9412, 0, 9, df_all)
df_all = get_data(201, 213, 1, 10, df_all)
df_all = get_data(344, 346, 1, 10, df_all)
df_all = get_data(366, 368, 1, 10, df_all)
df_all = get_data(382, 385, 1, 10, df_all)
df_all = get_data(421, 422, 1, 10, df_all)
df_all = get_data(424, 427, 1, 10, df_all)
df_all = get_data(428, 430, 1, 10, df_all)
df_all = get_data(443, 445, 1, 10, df_all)
df_all = get_data(448, 450, 1, 10, df_all)
df_all = get_data(464, 465, 1, 10, df_all)
df_all = get_data(521, 526, 1, 10, df_all)
df_all = get_data(1100, 1101, 1, 11, df_all)
df_all = get_data(1201, 1204, 1, 11, df_all)
df_all = get_data(1206, 1213, 1, 11, df_all)
df_all = get_data(1214, 1220, 1, 11, df_all)
df_all = get_data(1221, 1226, 1, 11, df_all)
df_all = get_data(1227, 1236, 1, 11, df_all)
df_all = get_data(1237, 1244, 1, 11, df_all)
df_all = get_data(1245, 1247, 1, 11, df_all)
df_all = get_data(1301, 1302, 1, 11, df_all)
df_all = get_data(1324, 1325, 1, 11, df_all)
df_all = get_data(1326, 1328, 1, 11, df_all)
df_all = get_data(1341, 1344, 1, 11, df_all)
df_all = get_data(1346, 1350, 1, 11, df_all)
df_all = get_data(1361, 1364, 1, 11, df_all)
df_all = get_data(1365, 1366, 1, 11, df_all)
df_all = get_data(1369, 1370, 1, 11, df_all)
df_all = get_data(1381, 1382, 1, 11, df_all)
df_all = get_data(1383, 1384, 1, 11, df_all)
df_all = get_data(1385, 1386, 1, 11, df_all)
df_all = get_data(1408, 1409, 1, 11, df_all)
df_all = get_data(1442, 1443, 1, 11, df_all)
df_all = get_data(1464, 1466, 1, 11, df_all)
df_all = get_data(2100, 2101, 1, 12, df_all)
df_all = get_data(2202, 2209, 1, 12, df_all)
df_all = get_data(2210, 2214, 1, 12, df_all)
df_all = get_data(2215, 2240, 1, 12, df_all)
df_all = get_data(2322, 2323, 1, 12, df_all)
df_all = get_data(2329, 2330, 1, 12, df_all)
df_all = get_data(2342, 2343, 1, 12, df_all)
df_all = get_data(2347, 2348, 1, 12, df_all)
df_all = get_data(2349, 2350, 1, 12, df_all)
df_all = get_data(2403, 2404, 1, 12, df_all)
df_all = get_data(2409, 2411, 1, 12, df_all)
df_all = get_data(2421, 2425, 1, 12, df_all)
df_all = get_data(2426, 2428, 1, 12, df_all)
df_all = get_data(2441, 2442, 1, 12, df_all)
df_all = get_data(2443, 2444, 1, 12, df_all)
df_all = get_data(2463, 2464, 1, 12, df_all)
df_all = get_data(3101, 3124, 1, 13, df_all)
df_all = get_data(3201, 3216, 1, 13, df_all)
df_all = get_data(3218, 3226, 1, 13, df_all)
df_all = get_data(3227, 3230, 1, 13, df_all)
df_all = get_data(3303, 3304, 1, 13, df_all)
df_all = get_data(3305, 3306, 1, 13, df_all)
df_all = get_data(3307, 3309, 1, 13, df_all)
df_all = get_data(3361, 3365, 1, 13, df_all)
df_all = get_data(3381, 3383, 1, 13, df_all)
df_all = get_data(3401, 3403, 1, 13, df_all)
df_all = get_data(3421, 3422, 1, 13, df_all)
df_all = get_data(4100, 4101, 1, 14, df_all)
df_all = get_data(4130, 4131, 1, 14, df_all)
df_all = get_data(4150, 4151, 1, 14, df_all)
df_all = get_data(4201, 4202, 1, 14, df_all)
df_all = get_data(4203, 4209, 1, 14, df_all)
df_all = get_data(4210, 4219, 1, 14, df_all)
df_all = get_data(4301, 4302, 1, 14, df_all)
df_all = get_data(4321, 4322, 1, 14, df_all)
df_all = get_data(4341, 4343, 1, 14, df_all)
df_all = get_data(4361, 4365, 1, 14, df_all)
df_all = get_data(4366, 4367, 1, 14, df_all)
df_all = get_data(4382, 4385, 1, 14, df_all)
df_all = get_data(4401, 4403, 1, 14, df_all)
df_all = get_data(5100, 5101, 1, 15, df_all)
df_all = get_data(5202, 5203, 1, 15, df_all)
df_all = get_data(5204, 5207, 1, 15, df_all)
df_all = get_data(5208, 5214, 1, 15, df_all)
df_all = get_data(5216, 5219, 1, 15, df_all)
df_all = get_data(5222, 5228, 1, 15, df_all)
df_all = get_data(5307, 5308, 1, 15, df_all)
df_all = get_data(5342, 5343, 1, 15, df_all)
df_all = get_data(5361, 5362, 1, 15, df_all)
df_all = get_data(5385, 5386, 1, 15, df_all)
df_all = get_data(5405, 5406, 1, 15, df_all)
df_all = get_data(5461, 5462, 1, 15, df_all)
df_all = get_data(5482, 5483, 1, 15, df_all)
df_all = get_data(5504, 5505, 1, 15, df_all)
df_all = get_data(5581, 5582, 1, 15, df_all)
df_all = get_data(5586, 5587, 1, 15, df_all)
df_all = get_data(6201, 6203, 1, 16, df_all)
df_all = get_data(6204, 6212, 1, 16, df_all)
df_all = get_data(6321, 6324, 1, 16, df_all)
df_all = get_data(6342, 6344, 1, 16, df_all)
df_all = get_data(7201, 7208, 1, 17, df_all)
df_all = get_data(7209, 7213, 1, 17, df_all)
df_all = get_data(7324, 7325, 1, 17, df_all)
df_all = get_data(7361, 7362, 1, 17, df_all)
df_all = get_data(7365, 7366, 1, 17, df_all)
df_all = get_data(7384, 7385, 1, 17, df_all)
df_all = get_data(7386, 7387, 1, 17, df_all)
df_all = get_data(7407, 7408, 1, 17, df_all)
df_all = get_data(7461, 7462, 1, 17, df_all)
df_all = get_data(7463, 7464, 1, 17, df_all)
df_all = get_data(8201, 8203, 1, 18, df_all)
df_all = get_data(8204, 8211, 1, 18, df_all)
df_all = get_data(8322, 8323, 1, 18, df_all)
df_all = get_data(8382, 8383, 1, 18, df_all)
df_all = get_data(8404, 8405, 1, 18, df_all)
df_all = get_data(8423, 8424, 1, 18, df_all)
df_all = get_data(8442, 8443, 1, 18, df_all)
df_all = get_data(8481, 8482, 1, 18, df_all)
df_all = get_data(8483, 8484, 1, 18, df_all)
df_all = get_data(8501, 8502, 1, 18, df_all)
df_all = get_data(9201, 9203, 1, 19, df_all)
df_all = get_data(9204, 9215, 1, 19, df_all)
df_all = get_data(9346, 9347, 1, 19, df_all)
df_all = get_data(9364, 9367, 1, 19, df_all)
df_all = get_data(9368, 9369, 1, 19, df_all)
df_all = get_data(9384, 9385, 1, 19, df_all)
df_all = get_data(9422, 9426, 1, 19, df_all)
df_all = get_data(9429, 9431, 1, 19, df_all)
df_all = get_data(9442, 9444, 1, 19, df_all)
df_all = get_data(201, 216, 2, 20, df_all)
df_all = get_data(217, 221, 2, 20, df_all)
df_all = get_data(303, 308, 2, 20, df_all)
df_all = get_data(309, 310, 2, 20, df_all)
df_all = get_data(321, 322, 2, 20, df_all)
df_all = get_data(323, 325, 2, 20, df_all)
df_all = get_data(349, 351, 2, 20, df_all)
df_all = get_data(361, 364, 2, 20, df_all)
df_all = get_data(382, 387, 2, 20, df_all)
df_all = get_data(388, 389, 2, 20, df_all)
df_all = get_data(402, 405, 2, 20, df_all)
df_all = get_data(407, 408, 2, 20, df_all)
df_all = get_data(409, 418, 2, 20, df_all)
df_all = get_data(422, 424, 2, 20, df_all)
df_all = get_data(425, 426, 2, 20, df_all)
df_all = get_data(429, 431, 2, 20, df_all)
df_all = get_data(432, 433, 2, 20, df_all)
df_all = get_data(446, 447, 2, 20, df_all)
df_all = get_data(448, 449, 2, 20, df_all)
df_all = get_data(450, 453, 2, 20, df_all)
df_all = get_data(481, 483, 2, 20, df_all)
df_all = get_data(485, 487, 2, 20, df_all)
df_all = get_data(521, 522, 2, 20, df_all)
df_all = get_data(541, 542, 2, 20, df_all)
df_all = get_data(543, 544, 2, 20, df_all)
df_all = get_data(561, 564, 2, 20, df_all)
df_all = get_data(583, 584, 2, 20, df_all)
df_all = get_data(588, 589, 2, 20, df_all)
df_all = get_data(590, 591, 2, 20, df_all)
df_all = get_data(602, 603, 2, 20, df_all)
df_all = get_data(1201, 1222, 2, 21, df_all)
df_all = get_data(1302, 1304, 2, 21, df_all)
df_all = get_data(1341, 1342, 2, 21, df_all)
df_all = get_data(1361, 1363, 2, 21, df_all)
df_all = get_data(1381, 1384, 2, 21, df_all)
df_all = get_data(1401, 1402, 2, 21, df_all)
df_all = get_data(1403, 1405, 2, 21, df_all)
df_all = get_data(1421, 1422, 2, 21, df_all)
df_all = get_data(1501, 1508, 2, 21, df_all)
df_all = get_data(1521, 1522, 2, 21, df_all)
df_all = get_data(1604, 1605, 2, 21, df_all)
df_all = get_data(2100, 2101, 2, 22, df_all)
df_all = get_data(2130, 2131, 2, 22, df_all)
df_all = get_data(2203, 2204, 2, 22, df_all)
df_all = get_data(2205, 2217, 2, 22, df_all)
df_all = get_data(2219, 2227, 2, 22, df_all)
df_all = get_data(2301, 2303, 2, 22, df_all)
df_all = get_data(2304, 2307, 2, 22, df_all)
df_all = get_data(2325, 2326, 2, 22, df_all)
df_all = get_data(2341, 2343, 2, 22, df_all)
df_all = get_data(2344, 2345, 2, 22, df_all)
df_all = get_data(2424, 2425, 2, 22, df_all)
df_all = get_data(2429, 2430, 2, 22, df_all)
df_all = get_data(2461, 2462, 2, 22, df_all)
df_all = get_data(3100, 3101, 2, 23, df_all)
df_all = get_data(3201, 3218, 2, 23, df_all)
df_all = get_data(3219, 3239, 2, 23, df_all)
df_all = get_data(3302, 3303, 2, 23, df_all)
df_all = get_data(3342, 3343, 2, 23, df_all)
df_all = get_data(3361, 3363, 2, 23, df_all)
df_all = get_data(3424, 3426, 2, 23, df_all)
df_all = get_data(3427, 3428, 2, 23, df_all)
df_all = get_data(3441, 3443, 2, 23, df_all)
df_all = get_data(3445, 3448, 2, 23, df_all)
df_all = get_data(3501, 3502, 2, 23, df_all)
df_all = get_data(3561, 3564, 2, 23, df_all)
df_all = get_data(4201, 4206, 2, 24, df_all)
df_all = get_data(4207, 4213, 2, 24, df_all)
df_all = get_data(4214, 4217, 2, 24, df_all)
df_all = get_data(4303, 4304, 2, 24, df_all)
df_all = get_data(4324, 4325, 2, 24, df_all)
df_all = get_data(4341, 4342, 2, 24, df_all)
df_all = get_data(4343, 4345, 2, 24, df_all)
df_all = get_data(4441, 4444, 2, 24, df_all)
df_all = get_data(4461, 4462, 2, 24, df_all)
df_all = get_data(4470, 4473, 2, 24, df_all)
df_all = get_data(4543, 4544, 2, 24, df_all)
df_all = get_data(4561, 4563, 2, 24, df_all)
df_all = get_data(5201, 5205, 2, 25, df_all)
df_all = get_data(5206, 5215, 2, 25, df_all)
df_all = get_data(5383, 5385, 2, 25, df_all)
df_all = get_data(5425, 5426, 2, 25, df_all)
df_all = get_data(5441, 5444, 2, 25, df_all)
df_all = get_data(6100, 6101, 2, 26, df_all)
df_all = get_data(6201, 6215, 2, 26, df_all)
df_all = get_data(6303, 6304, 2, 26, df_all)
df_all = get_data(6322, 6323, 2, 26, df_all)
df_all = get_data(6343, 6345, 2, 26, df_all)
df_all = get_data(6364, 6368, 2, 26, df_all)
df_all = get_data(6407, 6408, 2, 26, df_all)
df_all = get_data(6463, 6464, 2, 26, df_all)
df_all = get_data(6465, 6466, 2, 26, df_all)
df_all = get_data(7100, 7101, 2, 27, df_all)
df_all = get_data(7140, 7141, 2, 27, df_all)
df_all = get_data(7202, 7233, 2, 27, df_all)
df_all = get_data(7301, 7302, 2, 27, df_all)
df_all = get_data(7321, 7323, 2, 27, df_all)
df_all = get_data(7341, 7342, 2, 27, df_all)
df_all = get_data(7361, 7363, 2, 27, df_all)
df_all = get_data(7366, 7367, 2, 27, df_all)
df_all = get_data(7381, 7384, 2, 27, df_all)
df_all = get_data(8100, 8101, 2, 28, df_all)
df_all = get_data(8201, 8211, 2, 28, df_all)
df_all = get_data(8212, 8230, 2, 28, df_all)
df_all = get_data(8301, 8302, 2, 28, df_all)
df_all = get_data(8365, 8366, 2, 28, df_all)
df_all = get_data(8381, 8383, 2, 28, df_all)
df_all = get_data(8442, 8444, 2, 28, df_all)
df_all = get_data(8446, 8447, 2, 28, df_all)
df_all = get_data(8464, 8465, 2, 28, df_all)
df_all = get_data(8481, 8482, 2, 28, df_all)
df_all = get_data(8501, 8502, 2, 28, df_all)
df_all = get_data(8585, 8587, 2, 28, df_all)
df_all = get_data(9201, 9213, 2, 29, df_all)
df_all = get_data(9322, 9323, 2, 29, df_all)
df_all = get_data(9342, 9346, 2, 29, df_all)
df_all = get_data(9361, 9364, 2, 29, df_all)
df_all = get_data(9385, 9387, 2, 29, df_all)
df_all = get_data(9401, 9403, 2, 29, df_all)
df_all = get_data(9424, 9428, 2, 29, df_all)
df_all = get_data(9441, 9445, 2, 29, df_all)
df_all = get_data(9446, 9448, 2, 29, df_all)
df_all = get_data(9449, 9454, 2, 29, df_all)
df_all = get_data(201, 210, 3, 30, df_all)
df_all = get_data(304, 305, 3, 30, df_all)
df_all = get_data(341, 342, 3, 30, df_all)
df_all = get_data(343, 345, 3, 30, df_all)
df_all = get_data(361, 363, 3, 30, df_all)
df_all = get_data(366, 367, 3, 30, df_all)
df_all = get_data(381, 384, 3, 30, df_all)
df_all = get_data(390, 393, 3, 30, df_all)
df_all = get_data(401, 402, 3, 30, df_all)
df_all = get_data(404, 405, 3, 30, df_all)
df_all = get_data(406, 407, 3, 30, df_all)
df_all = get_data(421, 423, 3, 30, df_all)
df_all = get_data(424, 425, 3, 30, df_all)
df_all = get_data(427, 429, 3, 30, df_all)
df_all = get_data(1201, 1205, 3, 31, df_all)
df_all = get_data(1302, 1303, 3, 31, df_all)
df_all = get_data(1325, 1326, 3, 31, df_all)
df_all = get_data(1328, 1330, 3, 31, df_all)
df_all = get_data(1364, 1365, 3, 31, df_all)
df_all = get_data(1370, 1373, 3, 31, df_all)
df_all = get_data(1384, 1385, 3, 31, df_all)
df_all = get_data(1386, 1387, 3, 31, df_all)
df_all = get_data(1389, 1391, 3, 31, df_all)
df_all = get_data(1401, 1404, 3, 31, df_all)
df_all = get_data(2201, 2208, 3, 32, df_all)
df_all = get_data(2209, 2210, 3, 32, df_all)
df_all = get_data(2343, 2344, 3, 32, df_all)
df_all = get_data(2386, 2387, 3, 32, df_all)
df_all = get_data(2441, 2442, 3, 32, df_all)
df_all = get_data(2448, 2450, 3, 32, df_all)
df_all = get_data(2501, 2502, 3, 32, df_all)
df_all = get_data(2505, 2506, 3, 32, df_all)
df_all = get_data(2525, 2529, 3, 32, df_all)
df_all = get_data(3100, 3101, 3, 33, df_all)
df_all = get_data(3202, 3206, 3, 33, df_all)
df_all = get_data(3207, 3217, 3, 33, df_all)
df_all = get_data(3346, 3347, 3, 33, df_all)
df_all = get_data(3423, 3424, 3, 33, df_all)
df_all = get_data(3445, 3446, 3, 33, df_all)
df_all = get_data(3461, 3462, 3, 33, df_all)
df_all = get_data(3586, 3587, 3, 33, df_all)
df_all = get_data(3606, 3607, 3, 33, df_all)
df_all = get_data(3622, 3624, 3, 33, df_all)
df_all = get_data(3643, 3644, 3, 33, df_all)
df_all = get_data(3663, 3664, 3, 33, df_all)
df_all = get_data(3666, 3667, 3, 33, df_all)
df_all = get_data(3681, 3682, 3, 33, df_all)
df_all = get_data(4100, 4101, 3, 34, df_all)
df_all = get_data(4202, 4206, 3, 34, df_all)
df_all = get_data(4207, 4216, 3, 34, df_all)
df_all = get_data(4302, 4303, 3, 34, df_all)
df_all = get_data(4304, 4305, 3, 34, df_all)
df_all = get_data(4307, 4308, 3, 34, df_all)
df_all = get_data(4309, 4310, 3, 34, df_all)
df_all = get_data(4368, 4370, 3, 34, df_all)
df_all = get_data(4431, 4432, 3, 34, df_all)
df_all = get_data(4462, 4463, 3, 34, df_all)
df_all = get_data(4545, 4546, 3, 34, df_all)
df_all = get_data(5201, 5205, 3, 35, df_all)
df_all = get_data(5206, 5209, 3, 35, df_all)
df_all = get_data(5210, 5214, 3, 35, df_all)
df_all = get_data(5215, 5217, 3, 35, df_all)
df_all = get_data(5305, 5306, 3, 35, df_all)
df_all = get_data(5321, 5322, 3, 35, df_all)
df_all = get_data(5341, 5342, 3, 35, df_all)
df_all = get_data(5343, 5345, 3, 35, df_all)
df_all = get_data(5502, 5503, 3, 35, df_all)
df_all = get_data(6201, 6209, 3, 36, df_all)
df_all = get_data(6301, 6303, 3, 36, df_all)
df_all = get_data(6321, 6322, 3, 36, df_all)
df_all = get_data(6341, 6343, 3, 36, df_all)
df_all = get_data(6368, 6369, 3, 36, df_all)
df_all = get_data(6383, 6384, 3, 36, df_all)
df_all = get_data(6387, 6389, 3, 36, df_all)
df_all = get_data(6401, 6406, 3, 36, df_all)
df_all = get_data(6468, 6469, 3, 36, df_all)
df_all = get_data(6489, 6490, 3, 36, df_all)
df_all = get_data(7201, 7209, 3, 37, df_all)
df_all = get_data(7322, 7323, 3, 37, df_all)
df_all = get_data(7324, 7325, 3, 37, df_all)
df_all = get_data(7341, 7342, 3, 37, df_all)
df_all = get_data(7364, 7365, 3, 37, df_all)
df_all = get_data(7386, 7388, 3, 37, df_all)
df_all = get_data(7403, 7405, 3, 37, df_all)
df_all = get_data(7406, 7407, 3, 37, df_all)
df_all = get_data(8201, 8208, 3, 38, df_all)
df_all = get_data(8210, 8211, 3, 38, df_all)
df_all = get_data(8213, 8216, 3, 38, df_all)
df_all = get_data(8356, 8357, 3, 38, df_all)
df_all = get_data(8386, 8387, 3, 38, df_all)
df_all = get_data(8401, 8403, 3, 38, df_all)
df_all = get_data(8422, 8423, 3, 38, df_all)
df_all = get_data(8442, 8443, 3, 38, df_all)
df_all = get_data(8484, 8485, 3, 38, df_all)
df_all = get_data(8488, 8489, 3, 38, df_all)
df_all = get_data(8506, 8507, 3, 38, df_all)
df_all = get_data(9201, 9207, 3, 39, df_all)
df_all = get_data(9208, 9213, 3, 39, df_all)
df_all = get_data(9301, 9308, 3, 39, df_all)
df_all = get_data(9341, 9342, 3, 39, df_all)
df_all = get_data(9344, 9345, 3, 39, df_all)
df_all = get_data(9363, 9365, 3, 39, df_all)
df_all = get_data(9386, 9388, 3, 39, df_all)
df_all = get_data(9401, 9404, 3, 39, df_all)
df_all = get_data(9405, 9406, 3, 39, df_all)
df_all = get_data(9410, 9413, 3, 39, df_all)
df_all = get_data(9424, 9425, 3, 39, df_all)
df_all = get_data(9427, 9429, 3, 39, df_all)
df_all = get_data(100, 101, 4, 40, df_all)
df_all = get_data(130, 131, 4, 40, df_all)
df_all = get_data(202, 208, 4, 40, df_all)
df_all = get_data(210, 222, 4, 40, df_all)
df_all = get_data(223, 232, 4, 40, df_all)
df_all = get_data(341, 346, 4, 40, df_all)
df_all = get_data(348, 350, 4, 40, df_all)
df_all = get_data(381, 385, 4, 40, df_all)
df_all = get_data(401, 403, 4, 40, df_all)
df_all = get_data(421, 422, 4, 40, df_all)
df_all = get_data(447, 449, 4, 40, df_all)
df_all = get_data(503, 504, 4, 40, df_all)
df_all = get_data(522, 523, 4, 40, df_all)
df_all = get_data(544, 545, 4, 40, df_all)
df_all = get_data(601, 603, 4, 40, df_all)
df_all = get_data(604, 606, 4, 40, df_all)
df_all = get_data(608, 611, 4, 40, df_all)
df_all = get_data(621, 622, 4, 40, df_all)
df_all = get_data(625, 626, 4, 40, df_all)
df_all = get_data(642, 643, 4, 40, df_all)
df_all = get_data(646, 648, 4, 40, df_all)
df_all = get_data(1201, 1211, 4, 41, df_all)
df_all = get_data(1327, 1328, 4, 41, df_all)
df_all = get_data(1341, 1342, 4, 41, df_all)
df_all = get_data(1345, 1347, 4, 41, df_all)
df_all = get_data(1387, 1388, 4, 41, df_all)
df_all = get_data(1401, 1402, 4, 41, df_all)
df_all = get_data(1423, 1426, 4, 41, df_all)
df_all = get_data(1441, 1442, 4, 41, df_all)
df_all = get_data(2201, 2206, 4, 42, df_all)
df_all = get_data(2207, 2215, 4, 42, df_all)
df_all = get_data(2307, 2309, 4, 42, df_all)
df_all = get_data(2321, 2324, 4, 42, df_all)
df_all = get_data(2383, 2384, 4, 42, df_all)
df_all = get_data(2391, 2392, 4, 42, df_all)
df_all = get_data(2411, 2412, 4, 42, df_all)
df_all = get_data(3100, 3101, 4, 43, df_all)
df_all = get_data(3202, 3207, 4, 43, df_all)
df_all = get_data(3208, 3209, 4, 43, df_all)
df_all = get_data(3210, 3217, 4, 43, df_all)
df_all = get_data(3348, 3349, 4, 43, df_all)
df_all = get_data(3364, 3365, 4, 43, df_all)
df_all = get_data(3367, 3370, 4, 43, df_all)
df_all = get_data(3403, 3405, 4, 43, df_all)
df_all = get_data(3423, 3426, 4, 43, df_all)
df_all = get_data(3428, 3429, 4, 43, df_all)
df_all = get_data(3432, 3434, 4, 43, df_all)
df_all = get_data(3441, 3445, 4, 43, df_all)
df_all = get_data(3447, 3448, 4, 43, df_all)
df_all = get_data(3468, 3469, 4, 43, df_all)
df_all = get_data(3482, 3483, 4, 43, df_all)
df_all = get_data(3484, 3485, 4, 43, df_all)
df_all = get_data(3501, 3502, 4, 43, df_all)
df_all = get_data(3505, 3508, 4, 43, df_all)
df_all = get_data(3510, 3515, 4, 43, df_all)
df_all = get_data(3531, 3532, 4, 43, df_all)
df_all = get_data(4201, 4215, 4, 44, df_all)
df_all = get_data(4322, 4323, 4, 44, df_all)
df_all = get_data(4341, 4342, 4, 44, df_all)
df_all = get_data(4461, 4463, 4, 44, df_all)
df_all = get_data(5201, 5210, 4, 45, df_all)
df_all = get_data(5341, 5342, 4, 45, df_all)
df_all = get_data(5361, 5362, 4, 45, df_all)
df_all = get_data(5382, 5384, 4, 45, df_all)
df_all = get_data(5401, 5407, 4, 45, df_all)
df_all = get_data(5421, 5422, 4, 45, df_all)
df_all = get_data(5429, 5432, 4, 45, df_all)
df_all = get_data(5441, 5444, 4, 45, df_all)
df_all = get_data(6201, 6202, 4, 46, df_all)
df_all = get_data(6203, 6205, 4, 46, df_all)
df_all = get_data(6206, 6207, 4, 46, df_all)
df_all = get_data(6208, 6209, 4, 46, df_all)
df_all = get_data(6210, 6211, 4, 46, df_all)
df_all = get_data(6213, 6226, 4, 46, df_all)
df_all = get_data(6303, 6305, 4, 46, df_all)
df_all = get_data(6392, 6393, 4, 46, df_all)
df_all = get_data(6404, 6405, 4, 46, df_all)
df_all = get_data(6452, 6453, 4, 46, df_all)
df_all = get_data(6468, 6469, 4, 46, df_all)
df_all = get_data(6482, 6483, 4, 46, df_all)
df_all = get_data(6490, 6493, 4, 46, df_all)
df_all = get_data(6501, 6503, 4, 46, df_all)
df_all = get_data(6505, 6506, 4, 46, df_all)
df_all = get_data(6523, 6526, 4, 46, df_all)
df_all = get_data(6527, 6528, 4, 46, df_all)
df_all = get_data(6529, 6536, 4, 46, df_all)
df_all = get_data(7201, 7202, 4, 47, df_all)
df_all = get_data(7205, 7206, 4, 47, df_all)
df_all = get_data(7207, 7216, 4, 47, df_all)
df_all = get_data(7301, 7304, 4, 47, df_all)
df_all = get_data(7306, 7307, 4, 47, df_all)
df_all = get_data(7308, 7309, 4, 47, df_all)
df_all = get_data(7311, 7312, 4, 47, df_all)
df_all = get_data(7313, 7316, 4, 47, df_all)
df_all = get_data(7324, 7330, 4, 47, df_all)
df_all = get_data(7348, 7349, 4, 47, df_all)
df_all = get_data(7350, 7351, 4, 47, df_all)
df_all = get_data(7353, 7363, 4, 47, df_all)
df_all = get_data(7375, 7376, 4, 47, df_all)

"""
必要なデータの取り出し
"""

c_data = df_all.iloc[:,[2,8]] #元データの3列目と9列目のみを取り出す

c_data_1 = c_data.iloc[:, 0] #c_dataの1列目（元データの3列目）を取り出す

#cityCodeの再整形
l_cityC = [] 
for i in c_data_1:
    c_data_1_1 = i #city_Code（元データの3列目）を一つずつ取り出す
    l_cityC.append(c_data_1_1) #リストに格納

data1_all = pd.DataFrame(l_cityC, columns = ['city_Code']) #要素名をつけてリスト内のデータを結合（pandas dataFrame化）
#print(data1_all) #データ確認用

#c_dataの2列目（元データの9列目）の整形
L = []
c_data_2 = c_data.iloc[:, 1] #c_dataの2列目（元データの9列目）を取り出す
#print(c_data_2) #データ確認用

for i in c_data_2:
    c_data_2_1 = pd.json_normalize(i) #データをpandas Seriesに直す
    #print(c_data_2_1) #データ確認用
    c_data_2_2 = c_data_2_1.iat[-1, 1] #value（必要なデータ）の取り出し
    #print(c_data_2_2) #データ確認用
    L.append(c_data_2_2) #リストに格納

data2_all = pd.DataFrame(L, columns = ['value_company']) #valueに要素名をつけてリスト内のデータを結合（pandas dataFrame化）
#print(data2_all) #データ確認用

data_all = pd.concat([data1_all, data2_all], axis = 1) #cityCodeとvalueの結合


"""
csvへの書き出し
"""
data_all.to_csv('your_path', encoding="SHIFT-JIS", index=None)

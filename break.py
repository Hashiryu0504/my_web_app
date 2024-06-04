import pandas as pd

# CSVファイルを読み込む
file_path = 'file.csv'  # アップロードしたファイルのパスに置き換えてください
data = pd.read_csv(file_path)

# 'sort'列でソートする
sorted_data = data.sort_values(by=['sort'])

# 属性のリスト
attributes = ['火', '水', '風', '光', '闇']

# 属性ごとにCSVファイルを作成する関数
def create_sorted_csv_by_sort(data, attribute):
    filtered_data = data[data['attr'] == attribute][['name']]
    filtered_data['file'] = 'static/' + attribute + '属性/' + filtered_data['name'] + '.png'
    output_path = f'characters_{attribute}.csv'
    filtered_data.to_csv(output_path, index=False, header=False, encoding='utf-8', errors='replace')

# 各属性ごとにCSVファイルを作成
for attr in attributes:
    create_sorted_csv_by_sort(sorted_data, attr)

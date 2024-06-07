import os
import shutil

def sort_monster_icons(input_directory):
    # ファイルを格納するディレクトリのパスを取得
    for filename in os.listdir(input_directory):
        if filename.endswith(".png"):
            parts = filename.split('_')
            if len(parts) >= 4:
                number = parts[3].split('.')[0]  # 4つ目の部分の数字を取得
                if number.isdigit() and 1 <= int(number) <= 5:
                    target_directory = os.path.join(input_directory, f'folder_{number}')
                    os.makedirs(target_directory, exist_ok=True)
                    source_path = os.path.join(input_directory, filename)
                    destination_path = os.path.join(target_directory, filename)
                    shutil.move(source_path, destination_path)
                    print(f'Moved: {source_path} to {destination_path}')

# 使用例
input_directory = 'monster_icon'  # 画像が格納されているディレクトリのパスを指定
sort_monster_icons(input_directory)

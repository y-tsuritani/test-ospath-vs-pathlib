import os

directory = "directory"
# リスト内包表記を使って、ディレクトリ内のファイルのリストを作成
files = [
    os.path.join(directory, f)
    for f in os.listdir(directory)
    if os.path.isfile(os.path.join(directory, f))
]
print(files)

# リスト内包表記を使わない場合
for_files = []
for f in os.listdir(directory):
    file_path = os.path.join(directory, f)
    if os.path.isfile(file_path):
        for_files.append(file_path)

print(for_files)

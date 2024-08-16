# file_storage.py
from pathlib import Path

# 必要なディレクトリが存在しない場合は作成する関数
def ensure_directory_exists(file_path: str) -> None:
    directory = Path(file_path).parent
    if not directory.exists():
        directory.mkdir(parents=True, exist_ok=True)

def save_results_to_file(results: list, file_path: str) -> None:
    """結果を指定されたファイルパスに保存します。"""
    ensure_directory_exists(file_path)
    with open(file_path, "w") as file:
        for value in results:
            file.write(f"{value}\n")

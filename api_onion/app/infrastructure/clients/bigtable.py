from dataclasses import dataclass
from app.utils.const import BIGTABLE_PROJECT_ID, BIGTABLE_INSTANCE_ID

@dataclass(frozen=True)
class BigTableClient:
    """
    BigTableへの接続を管理するクラス。
    """
    project_id: str = BIGTABLE_PROJECT_ID
    instance_id: str = BIGTABLE_INSTANCE_ID

    def get_data(self, user_id: str):
        # BigTableからデータを取得する処理
        # コメントアウトされたBigTableアクセスコード
        # from google.cloud import bigtable
        # client = bigtable.Client(project=self.project_id, admin=True)
        # instance = client.instance(self.instance_id)
        # table = instance.table('recommendations')
        # row = table.read_row(user_id)
        # return row.cells['recommendations']
        return ["item1", "item2", "item3"]  # 固定のレスポンス
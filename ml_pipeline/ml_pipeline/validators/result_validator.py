from pydantic import BaseModel, validator
from typing import Any
import pandas as pd
from pydantic import ValidationError

class ResultModel(BaseModel):
    data: pd.DataFrame

    class Config:
        arbitrary_types_allowed = True

    # バリデータメソッドを定義
    @validator('data')
    def validate_data(cls, v):
        # ここにデータのバリデーションロジックを追加します
        # データがNoneでないことを確認
        if v is None or not isinstance(v, pd.DataFrame):
            raise TypeError('Data must be a DataFrame')
        if v.empty:
            raise ValueError('Data cannot be empty')
        # 例として、結果が特定の条件を満たすかどうかを確認
        # ここでは、結果がデータフレームであり、'result'カラムが存在するかどうかを確認
        if 'result' not in v.columns:
            raise ValueError('Data must contain a "result" column')
        return v

def validate_result(result):
    try:
        # ResultModelのインスタンスを作成し、バリデーションを実行
        result_model = ResultModel(data=result)
        # バリデーションに成功した場合、処理を続行
        return result_model.data
    except ValidationError as e:
        raise ValueError(e)

# テストコード
if __name__ == "__main__":
    valid_result = pd.DataFrame({'result': ['success'], 'value': [42]})
    invalid_result = pd.DataFrame({'value': [42]})
    empty_result = pd.DataFrame()

    try:
        print("Valid result:", validate_result(valid_result))
    except ValueError as e:
        print("Validation failed for valid_result:", e)

    try:
        print("Invalid result:", validate_result(invalid_result))
    except ValueError as e:
        print("Validation failed for invalid_result:", e)

    try:
        print("Empty result:", validate_result(empty_result))
    except ValueError as e:
        print("Validation failed for empty_result:", e)

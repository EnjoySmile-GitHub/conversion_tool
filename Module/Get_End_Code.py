import os
import shutil
import module

def get_end_code():
    """処理終了コード取得"""
    try:
        with open(module.constant.SETTING_FILE_NAME, "r", encoding="utf-8") as f:
            data = f.read()
            if data.find(module.constant.END_CODE) != -1:
                code = data[data.find(module.constant.END_CODE):].replace(
                    module.constant.END_CODE, "")
                if code.find("\n") != -1:
                    code = code[:code.find("\n")]
                    return code.upper()
            else:
                print("設定ファイルのパスが見当たりません")
                return module.constant.ERROR_END_CODE
    except Exception as e:
        print(e)
        return module.constant.ERROR_END_CODE
import os
import shutil
import module

def get_new_line():
    """改行コード取得"""
    try:
        with open(module.constant.SETTING_FILE_NAME, "r", encoding="utf-8") as f:
            data = f.read()
            if data.find(module.constant.NEW_LINE) != -1:
                code = data[data.find(module.constant.NEW_LINE):].replace(
                    module.constant.NEW_LINE, "")
                if code.find("\n") != -1:
                    code = code[:code.find("\n")]
                    return code.upper()
            else:
                print("設定ファイルのパスが見当たりません")
                return module.constant.ERROR_NEW_LINE
    except Exception as e:
        print(e)
        return module.constant.ERROR_NEW_LINE
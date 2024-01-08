import os
import shutil
import Module

def get_new_line():
    """改行コード取得"""
    try:
        with open(Module.Constant.SETTING_FILE_NAME, "r", encoding="utf-8") as f:
            data = f.read()
            if data.find(Module.Constant.NEW_LINE) != -1:
                code = data[data.find(Module.Constant.NEW_LINE):].replace(
                    Module.Constant.NEW_LINE, "")
                if code.find("\n") != -1:
                    code = code[:code.find("\n")]
                    return code.upper()
            else:
                print("設定ファイルのパスが見当たりません")
                return Module.Constant.ERROR_NEW_LINE
    except Exception as e:
        print(e)
        return Module.Constant.ERROR_NEW_LINE
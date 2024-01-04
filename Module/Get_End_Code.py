import os
import shutil
import Module

def get_end_code():
    """処理終了コード取得"""
    try:
        with open(Module.Constant.SETTING_FILE_NAME, "r", encoding="utf-8") as f:
            data = f.read()
            if data.find(Module.Constant.END_CODE) != -1:
                code = data[data.find(Module.Constant.END_CODE):].replace(
                    Module.Constant.END_CODE, "")
                if code.find("\n") != -1:
                    code = code[:code.find("\n")]
                    return code.upper()
            else:
                print("設定ファイルのパスが見当たりません")
                return Module.Constant.ERROR_END_CODE
    except Exception as e:
        print(e)
        return Module.Constant.ERROR_END_CODE
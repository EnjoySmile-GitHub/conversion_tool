import os
import shutil
import Module

def setting_file_copy():
    """設定ファイルコピー"""
    try:
        with open(Module.Constant.SETTING_FILE_NAME, "r", encoding="utf-8") as f:
            data = f.read()
            if data.find(Module.Constant.SAVE_FILE_PATH) != -1:
                path = data[data.find(Module.Constant.SAVE_FILE_PATH):].replace(
                    Module.Constant.SAVE_FILE_PATH, "")
                if path.find("\n") != -1:
                    path = path[:path.find("\n")]
            else:
                print("設定ファイルのパスが見当たりません")
                return
        os.makedirs(path, exist_ok=True)
        shutil.copyfile(Module.Constant.SETTING_LIST_FILE_NAME, path +
                        "/" + Module.Constant.SETTING_LIST_FILE_NAME)
        print("ファイルコピー完了:" + path + "\\" + Module.Constant.SETTING_LIST_FILE_NAME)
    except Exception as e:
        print(e)

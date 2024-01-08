import os
import Module


def file_upper_read():
    """大文字変換"""
    while True:
        fileName = input("「大文字変換」 ファイル名入力:")
        if fileName is None or fileName == "":
            print("ファイル名を入力してください。")
            continue
        elif fileName.upper() == Module.Get_End_Code.get_end_code():
            return
        if os.path.isfile(fileName):
            with open(fileName, "r") as f:
                data = f.read()
            while True:
                fileName = input("出力するファイル名入力:")
                if fileName is None or fileName == "":
                    print("入力された文字が空です。")
                    continue
                elif fileName.upper() == Module.Get_End_Code.get_end_code():
                    return
                data = data.upper()
                with open(fileName, "w") as f:
                    f.write(data)
                    print("「大文字変換」 完了")
                    break
        else:
            print("ファイルが存在しません")


def file_upper_csv():
    """大文字変換 CSV変換"""
    while True:
        fileName = input("「大文字変換 CSV変換」 ファイル名入力:")
        if fileName is None or fileName == "":
            print("ファイル名を入力してください。")
            continue
        elif fileName.upper() == Module.Get_End_Code.get_end_code():
            return
        if os.path.isfile(fileName):
            with open(fileName, "r") as f:
                data = f.read()
            while True:
                fileName = input("出力するファイル名入力:")
                if fileName is None or fileName == "":
                    print("入力された文字が空です。")
                    continue
                elif fileName.upper() == Module.Get_End_Code.get_end_code():
                    return
                data = data.replace("\n", ",")
                data = data.replace(
                    "," + Module.Get_New_Line.get_new_line() + ",", "\n")
                data = data.upper()
                with open(fileName, "w") as f:
                    f.write(data)
                    print("「大文字変換 CSV変換」 完了")
                    break
        else:
            print("ファイルが存在しません")


def file_upper_line():
    """大文字変換 改行変換"""
    while True:
        fileName = input("「大文字変換 改行変換」 ファイル名入力:")
        if fileName is None or fileName == "":
            print("ファイル名を入力してください")
            continue
        elif fileName.upper() == Module.Get_End_Code.get_end_code():
            return
        if os.path.isfile(fileName):
            with open(fileName, "r") as f:
                data = f.read()
            while True:
                fileName = input("出力するファイル名入力:")
                if fileName is None or fileName == "":
                    print("入力された文字が空です")
                    continue
                elif fileName.upper() == Module.Get_End_Code.get_end_code():
                    return
                data = data.replace(",", "\n")
                data = data.replace(Module.Get_New_Line.get_new_line(), "")
                data = data.upper()
                with open(fileName, "w") as f:
                    f.write(data)
                    print("「大文字変換 改行変換」 完了")
                    break
        else:
            print("ファイルが存在しません")


def file_lower_read():
    """小文字変換"""
    while True:
        fileName = input("「小文字変換」 ファイル名入力:")
        if fileName is None or fileName == "":
            print("ファイル名を入力してください。")
            continue
        elif fileName.upper() == Module.Get_End_Code.get_end_code():
            return
        if os.path.isfile(fileName):
            with open(fileName, "r") as f:
                data = f.read()
            while True:
                fileName = input("出力するファイル名入力:")
                if fileName is None or fileName == "":
                    print("入力された文字が空です。")
                    continue
                elif fileName.upper() == Module.Get_End_Code.get_end_code():
                    return
                data = data.lower()
                with open(fileName, "w") as f:
                    f.write(data)
                    print("「小文字変換」 完了")
                    break
        else:
            print("ファイルが存在しません")


def file_lower_csv():
    """小文字変換 CSV変換"""
    while True:
        fileName = input("「小文字変換 CSV変換」 ファイル名入力:")
        if fileName is None or fileName == "":
            print("ファイル名を入力してください。")
            continue
        elif fileName.upper() == Module.Get_End_Code.get_end_code():
            return
        if os.path.isfile(fileName):
            with open(fileName, "r") as f:
                data = f.read()
            while True:
                fileName = input("出力するファイル名入力:")
                if fileName is None or fileName == "":
                    print("入力された文字が空です。")
                    continue
                elif fileName.upper() == Module.Get_End_Code.get_end_code():
                    return
                data = data.replace("\n", ",")
                data = data.replace(
                    "," + Module.Get_New_Line.get_new_line() + ",", "\n")
                data = data.lower()
                with open(fileName, "w") as f:
                    f.write(data)
                    print("「小文字変換 CSV変換」 完了")
                    break
        else:
            print("ファイルが存在しません")


def file_lower_line():
    """小文字変換 改行変換"""
    while True:
        fileName = input("「小文字変換 改行変換」 ファイル名入力:")
        if fileName is None or fileName == "":
            print("ファイル名を入力してください")
            continue
        elif fileName.upper() == Module.Get_End_Code.get_end_code():
            return
        if os.path.isfile(fileName):
            with open(fileName, "r") as f:
                data = f.read()
            while True:
                fileName = input("出力するファイル名入力:")
                if fileName is None or fileName == "":
                    print("入力された文字が空です")
                    continue
                elif fileName.upper() == Module.Get_End_Code.get_end_code():
                    return
                data = data.replace(",", "\n")
                data = data.replace(Module.Get_New_Line.get_new_line(), "")
                data = data.lower()
                with open(fileName, "w") as f:
                    f.write(data)
                    print("「小文字変換 改行変換」 完了")
                    break
        else:
            print("ファイルが存在しません")


def file_first_upper_csv():
    """先頭大文字変換 CSV変換"""
    while True:
        fileName = input("「先頭大文字変換 CSV変換」 ファイル名入力:")
        if fileName is None or fileName == "":
            print("ファイル名を入力してください。")
            continue
        elif fileName.upper() == Module.Get_End_Code.get_end_code():
            return
        if os.path.isfile(fileName):
            with open(fileName, "r") as f:
                data = f.read()
            while True:
                fileName = input("出力するファイル名入力:")
                if fileName is None or fileName == "":
                    print("入力された文字が空です。")
                    continue
                elif fileName.upper() == Module.Get_End_Code.get_end_code():
                    return
                data_split = ""
                for temp in data.split("\n"):
                    if data_split == "":
                        data_split += temp[0].upper() + temp[1:]
                    else:
                        data_split += "\n" + temp[0].upper() + temp[1:]
                data = data_split
                data = data.replace("\n", ",")
                data = data.replace(
                    "," + Module.Get_New_Line.get_new_line() + ",", "\n")
                with open(fileName, "w") as f:
                    f.write(data)
                    print("「先頭大文字変換 CSV変換」 完了")
                    break
        else:
            print("ファイルが存在しません")


def file_first_upper_line():
    """先頭大文字変換 改行変換"""
    while True:
        fileName = input("「先頭大文字変換 改行変換」 ファイル名入力:")
        if fileName is None or fileName == "":
            print("ファイル名を入力してください。")
            continue
        elif fileName.upper() == Module.Get_End_Code.get_end_code():
            return
        if os.path.isfile(fileName):
            with open(fileName, "r") as f:
                data = f.read()
            while True:
                fileName = input("出力するファイル名入力:")
                if fileName is None or fileName == "":
                    print("入力された文字が空です。")
                    continue
                elif fileName.upper() == Module.Get_End_Code.get_end_code():
                    return
                data_split = ""
                data = data.replace("\n", ",")
                for temp in data.split(","):
                    if data_split == "":
                        data_split += temp[0].upper() + temp[1:]
                    else:
                        data_split += "," + temp[0].upper() + temp[1:]
                data = data_split
                data = data.replace(",", "\n")
                data = data.replace(
                    "\n" + Module.Get_New_Line.get_new_line(), "\n")
                with open(fileName, "w") as f:
                    f.write(data)
                    print("「先頭大文字変換 改行変換」 完了")
                    break
        else:
            print("ファイルが存在しません")


def file_first_upper_csv_read():
    """先頭大文字変換 CSV読み込み"""
    while True:
        fileName = input("「先頭大文字変換 CSV読み込み」 ファイル名入力:")
        if fileName is None or fileName == "":
            print("ファイル名を入力してください。")
            continue
        elif fileName.upper() == Module.Get_End_Code.get_end_code():
            return
        if os.path.isfile(fileName):
            with open(fileName, "r") as f:
                data = f.read()
            while True:
                fileName = input("出力するファイル名入力:")
                if fileName is None or fileName == "":
                    print("入力された文字が空です。")
                    continue
                elif fileName.upper() == Module.Get_End_Code.get_end_code():
                    return
                save_data = ""
                len_data = ""
                for temp1 in data.split("\n"):
                    save_data = ""
                    for temp2 in temp1.split(","):
                        if save_data == "":
                            save_data += temp2[0].upper() + temp2[1:]
                        else:
                            save_data += "," + temp2[0].upper() + temp2[1:]
                    if len_data == "":
                        len_data += save_data
                    else:
                        len_data += "\n" + save_data
                with open(fileName, "w") as f:
                    f.write(len_data)
                    print("「先頭大文字変換 CSV読み込み」 完了")
                    break
        else:
            print("ファイルが存在しません")


def file_first_upper_line_read():
    """先頭大文字変換 改行読み込み"""
    while True:
        fileName = input("「先頭大文字変換 改行読み込み」 ファイル名入力:")
        if fileName is None or fileName == "":
            print("ファイル名を入力してください。")
            continue
        elif fileName.upper() == Module.Get_End_Code.get_end_code():
            return
        if os.path.isfile(fileName):
            with open(fileName, "r") as f:
                data = f.read()
            while True:
                fileName = input("出力するファイル名入力:")
                if fileName is None or fileName == "":
                    print("入力された文字が空です。")
                    continue
                elif fileName.upper() == Module.Get_End_Code.get_end_code():
                    return
                len_data = ""
                for temp in data.split("\n"):
                    if len_data == "":
                        len_data += temp[0].upper() + temp[1:]
                    else:
                        len_data += "\n" + temp[0].upper() + temp[1:]
                with open(fileName, "w") as f:
                    f.write(len_data)
                    print("「先頭大文字変換 改行読み込み」 完了")
                    break
        else:
            print("ファイルが存在しません")


def Fife_first_lower_csv():
    """先頭小文字変換 CSV変換"""
    while True:
        fileName = input("「先頭小文字変換 CSV変換」 ファイル名入力:")
        if fileName is None or fileName == "":
            print("ファイル名を入力してください。")
            continue
        elif fileName.upper() == Module.Get_End_Code.get_end_code():
            return
        if os.path.isfile(fileName):
            with open(fileName, "r") as f:
                data = f.read()
            while True:
                fileName = input("出力するファイル名入力:")
                if fileName is None or fileName == "":
                    print("入力された文字が空です。")
                    continue
                elif fileName.upper() == Module.Get_End_Code.get_end_code():
                    return
                data_split = ""
                for temp in data.split("\n"):
                    if data_split == "":
                        data_split += temp[0].lower() + temp[1:]
                    else:
                        data_split += "\n" + temp[0].lower() + temp[1:]
                data = data_split
                data = data.replace("\n", ",")
                data = data.replace(
                    "," + Module.Get_New_Line.get_new_line() + ",", "\n")
                with open(fileName, "w") as f:
                    f.write(data)
                    print("「先頭小文字変換 CSV変換」 完了")
                    break
        else:
            print("ファイルが存在しません")


def file_first_lower_line():
    """先頭小文字変換 改行変換"""
    while True:
        fileName = input("「先頭小文字変換 改行変換」 ファイル名入力:")
        if fileName is None or fileName == "":
            print("ファイル名を入力してください。")
            continue
        elif fileName.upper() == Module.Get_End_Code.get_end_code():
            return
        if os.path.isfile(fileName):
            with open(fileName, "r") as f:
                data = f.read()
            while True:
                fileName = input("出力するファイル名入力:")
                if fileName is None or fileName == "":
                    print("入力された文字が空です。")
                    continue
                elif fileName.upper() == Module.Get_End_Code.get_end_code():
                    return
                data_split = ""
                data = data.replace("\n", ",")
                for temp in data.split(","):
                    if data_split == "":
                        data_split += temp[0].lower() + temp[1:]
                    else:
                        data_split += "," + temp[0].lower() + temp[1:]
                data = data_split
                data = data.replace(",", "\n")
                data = data.replace(
                    "\n" + Module.Get_New_Line.get_new_line(), "\n")
                with open(fileName, "w") as f:
                    f.write(data)
                    print("「先頭小文字変換 改行変換」 完了")
                    break
        else:
            print("ファイルが存在しません")


def fife_first_lower_csv_read():
    """先頭小文字変換 CSV読み込み"""
    while True:
        fileName = input("「先頭小文字変換 CSV読み込み」 ファイル名入力:")
        if fileName is None or fileName == "":
            print("ファイル名を入力してください。")
            continue
        elif fileName.upper() == Module.Get_End_Code.get_end_code():
            return
        if os.path.isfile(fileName):
            with open(fileName, "r") as f:
                data = f.read()
            while True:
                fileName = input("出力するファイル名入力:")
                if fileName is None or fileName == "":
                    print("入力された文字が空です。")
                    continue
                elif fileName.upper() == Module.Get_End_Code.get_end_code():
                    return
                save_data = ""
                len_data = ""
                for temp1 in data.split("\n"):
                    save_data = ""
                    for temp2 in temp1.split(","):
                        if save_data == "":
                            save_data += temp2[0].lower() + temp2[1:]
                        else:
                            save_data += "," + temp2[0].lower() + temp2[1:]
                    if len_data == "":
                        len_data += save_data
                    else:
                        len_data += "\n" + save_data
                with open(fileName, "w") as f:
                    f.write(len_data)
                    print("「先頭小文字変換 CSV読み込み」 完了")
                    break
        else:
            print("ファイルが存在しません")


def file_first_lower_line_read():
    """先頭小文字変換 改行読み込み"""
    while True:
        fileName = input("「先頭小文字変換 改行読み込み」 ファイル名入力:")
        if fileName is None or fileName == "":
            print("ファイル名を入力してください。")
            continue
        elif fileName.upper() == Module.Get_End_Code.get_end_code():
            return
        if os.path.isfile(fileName):
            with open(fileName, "r") as f:
                data = f.read()
            while True:
                fileName = input("出力するファイル名入力:")
                if fileName is None or fileName == "":
                    print("入力された文字が空です。")
                    continue
                elif fileName.upper() == Module.Get_End_Code.get_end_code():
                    return
                len_data = ""
                for temp in data.split("\n"):
                    if len_data == "":
                        len_data += temp[0].lower() + temp[1:]
                    else:
                        len_data += "\n" + temp[0].lower() + temp[1:]
                with open(fileName, "w") as f:
                    f.write(len_data)
                    print("「先頭小文字変換 改行読み込み」 完了")
                    break
        else:
            print("ファイルが存在しません")


def file_csv_transform():
    """CSV変換"""
    while True:
        fileName = input("「CSV変換」 ファイル名入力:")
        if fileName is None or fileName == "":
            print("ファイル名を入力してください。")
            continue
        elif fileName.upper() == Module.Get_End_Code.get_end_code():
            return
        if os.path.isfile(fileName):
            with open(fileName, "r") as f:
                data = f.read()
            while True:
                fileName = input("出力するファイル名入力:")
                if fileName is None or fileName == "":
                    print("入力された文字が空です。")
                    continue
                elif fileName.upper() == Module.Get_End_Code.get_end_code():
                    return
                data = data.replace("\n", ",")
                data = data.replace(
                    "," + Module.Get_New_Line.get_new_line() + ",", "\n")
                with open(fileName, "w") as f:
                    f.write(data)
                    print("「CSV変換」 完了")
                    break
        else:
            print("ファイルが存在しません")


def file_line_transform():
    """改行変換"""
    while True:
        fileName = input("「改行変換」 ファイル名入力:")
        if fileName is None or fileName == "":
            print("ファイル名を入力してください。")
            continue
        elif fileName.upper() == Module.Get_End_Code.get_end_code():
            return
        if os.path.isfile(fileName):
            with open(fileName, "r") as f:
                data = f.read()
            while True:
                fileName = input("出力するファイル名入力:")
                if fileName is None or fileName == "":
                    print("入力された文字が空です。")
                    continue
                elif fileName.upper() == Module.Get_End_Code.get_end_code():
                    return
                data = data.replace(",", "\n")
                data = data.replace(
                    "\n" + Module.Get_New_Line.get_new_line(), "\n")
                with open(fileName, "w") as f:
                    f.write(data)
                    print("「改行変換」 完了")
                    break
        else:
            print("ファイルが存在しません")

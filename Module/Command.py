import Module

def command_upper():
    """大文字変換"""
    while True:
        txt = input("大文字変換:")

        if txt is None or txt == "":
            print("文字を入力してください")
            continue
        elif txt.upper() == Module.Get_End_Code.get_end_code():
            break

        print(txt.upper())


def command_lower():
    """小文字変換"""
    while True:
        txt = input("小文字変換:")

        if txt is None or txt == "":
            print("文字を入力してください")
            continue
        elif txt.upper() == Module.Get_End_Code.get_end_code():
            break

        print(txt.lower())


def command_first_upper():
    """先頭文字を大文字変換"""
    while True:
        txt = input("先頭文字を大文字変換:")

        if txt is None or txt == "":
            print("文字を入力してください")
            continue
        elif txt.upper() == Module.Get_End_Code.get_end_code():
            break

        print(txt[0].upper() + txt[1:])


def command_first_lower():
    """先頭小文字変換"""
    while True:
        txt = input("先頭文字を小文字変換:")

        if txt is None or txt == "":
            print("文字を入力してください")
            continue
        elif txt.upper() == Module.Get_End_Code.get_end_code():
            break

        print(txt[0].lower() + txt[1:])

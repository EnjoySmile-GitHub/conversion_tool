import Module


def choice_mode(mode):
    try:
        # 設定モード
        if mode == Module.Constant.SETTING:
            Module.Setting.setting_file_copy()

        # コマンドモード
        elif mode == Module.Constant.COMMAND_UPPER:
            Module.Command.command_upper()
        elif mode == Module.Constant.COMMAND_LOWER:
            Module.Command.command_lower()
        elif mode == Module.Constant.COMMAND_FIRST_UPPER:
            Module.Command.command_first_upper()
        elif mode == Module.Constant.COMMAND_FIRST_LOWER:
            Module.Command.command_first_lower()

        # ファイルモード
        elif mode == Module.Constant.FILE_UPPER_READ:
            Module.File.file_upper_read()
        elif mode == Module.Constant.FILE_UPPER_CSV:
            Module.File.file_upper_csv()
        elif mode == Module.Constant.FILE_UPPER_LINE:
            Module.File.file_upper_line()

        elif mode == Module.Constant.FILE_LOWER_READ:
            Module.File.file_lower_read()
        elif mode == Module.Constant.FILE_LOWER_CSV:
            Module.File.file_lower_csv()
        elif mode == Module.Constant.FILE_LOWER_LINE:
            Module.File.file_lower_line()

        elif mode == Module.Constant.FILE_FIRST_UPPER_CSV:
            Module.File.file_first_upper_csv()
        elif mode == Module.Constant.FILE_FIRST_UPPER_LINE:
            Module.File.file_first_upper_line()
        elif mode == Module.Constant.FILE_FIRST_UPPER_CSV_READ:
            Module.File.file_first_upper_csv_read()
        elif mode == Module.Constant.FILE_FIRST_UPPER_LINE_READ:
            Module.File.file_first_upper_line_read()

        elif mode == Module.Constant.FILE_FIRST_LOWER_CSV:
            Module.File.Fife_first_lower_csv()
        elif mode == Module.Constant.FILE_FIRST_LOWER_LINE:
            Module.File.file_first_lower_line()
        elif mode == Module.Constant.FILE_FIRST_LOWER_CSV_READ:
            Module.File.fife_first_lower_csv_read()
        elif mode == Module.Constant.FILE_FIRST_LOWER_LINE_READ:
            Module.File.file_first_lower_line_read()

        elif mode == Module.Constant.FILE_CSV_TRANSFORM:
            Module.File.file_csv_transform()

        elif mode == Module.Constant.FILE_LINE_TRANSFORM:
            Module.File.file_line_transform()

        else:
            print("指定のModeがありません")
    except Exception as e:
        print(e)

def main():
    while True:
        mode = input("Mode:")

        if mode is None or mode == "":
            print("Modeを入力してください")
            continue
        elif mode.upper() == Module.Get_End_Code.get_end_code():
            return

        choice_mode(mode)


if __name__ == "__main__":
    main()

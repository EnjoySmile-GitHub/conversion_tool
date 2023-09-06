import module


def choice_mode(mode):
    try:
        # 設定モード
        if mode == module.constant.SETTING:
            module.setting.setting_file_copy()

        # コマンドモード
        elif mode == module.constant.COMMAND_UPPER:
            module.command.command_upper()
        elif mode == module.constant.COMMAND_LOWER:
            module.command.command_lower()
        elif mode == module.constant.COMMAND_FIRST_UPPER:
            module.command.command_first_upper()
        elif mode == module.constant.COMMAND_FIRST_LOWER:
            module.command.command_first_lower()

        # ファイルモード
        elif mode == module.constant.FILE_UPPER_READ:
            module.file.file_upper_read()
        elif mode == module.constant.FILE_UPPER_CSV:
            module.file.file_upper_csv()
        elif mode == module.constant.FILE_UPPER_LINE:
            module.file.file_upper_line()

        elif mode == module.constant.FILE_LOWER_READ:
            module.file.file_lower_read()
        elif mode == module.constant.FILE_LOWER_CSV:
            module.file.file_lower_csv()
        elif mode == module.constant.FILE_LOWER_LINE:
            module.file.file_lower_line()

        elif mode == module.constant.FILE_FIRST_UPPER_CSV:
            module.file.file_first_upper_csv()
        elif mode == module.constant.FILE_FIRST_UPPER_LINE:
            module.file.file_first_upper_line()
        elif mode == module.constant.FILE_FIRST_UPPER_CSV_READ:
            module.file.file_first_upper_csv_read()
        elif mode == module.constant.FILE_FIRST_UPPER_LINE_READ:
            module.file.file_first_upper_line_read()

        elif mode == module.constant.FILE_FIRST_LOWER_CSV:
            module.file.Fife_first_lower_csv()
        elif mode == module.constant.FILE_FIRST_LOWER_LINE:
            module.file.file_first_lower_line()
        elif mode == module.constant.FILE_FIRST_LOWER_CSV_READ:
            module.file.fife_first_lower_csv_read()
        elif mode == module.constant.FILE_FIRST_LOWER_LINE_READ:
            module.file.file_first_lower_line_read()

        elif mode == module.constant.FILE_CSV_TRANSFORM:
            module.file.file_csv_transform()

        elif mode == module.constant.FILE_LINE_TRANSFORM:
            module.file.file_line_transform()

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
        elif mode.upper() == module.get_end_code.get_end_code():
            break

        choice_mode(mode)


if __name__ == "__main__":
    main()

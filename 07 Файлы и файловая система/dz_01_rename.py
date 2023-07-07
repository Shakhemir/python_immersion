import os


def group_files_rename(
        path: str = '.',  # путь расположения файлов
        desired_filename: str | None = None,  # желаемое конечное имя файлов
        digits: int = 0,  # количество цифр в порядковом номере
        src_extension: str | None = None,  # расширение исходного файла
        dst_extension: str | None = None,  # расширение конечного файла
        name_range: tuple | None = None  # диапазон сохраняемого оригинального имени
):
    list_dir = os.listdir(path)
    print(list_dir)
    if desired_filename is not None:
        count = 0
    name_prefix = ''
    for src_file in list_dir:
        ext = None
        if '.' in src_file:
            name, ext = src_file.rsplit('.', maxsplit=1)
        else:
            name = src_file
        if src_extension is not None and ext != src_extension:
            continue
        if name_range is not None:
            name_prefix = name[name_range[0]:name_range[1]]
        if desired_filename is not None:
            name = desired_filename + str(count).zfill(digits)
            count += 1
        if dst_extension is not None:
            ext = dst_extension
        dst_file = name_prefix + name
        if ext is not None:
            dst_file += '.' + ext
        os.rename(os.path.join(path, src_file), os.path.join(path, dst_file))


if __name__ == '__main__':
    group_files_rename('Test', desired_filename='new_txt_', digits=3, src_extension='txt', name_range=(0,8))

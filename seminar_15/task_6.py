# Задание No6
# 📌 Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# 📌 Соберите информацию о содержимом в виде объектов namedtuple.
# 📌 Каждый объект хранит:
#    ○ имя файла без расширения или название каталога,
#    ○ расширение, если это файл,
#    ○ флаг каталога,
#    ○ название родительского каталога.
# 📌 В процессе сбора сохраните данные в текстовый файл используя логирование.

from collections import namedtuple
import argparse
import logging
from pathlib import Path

logging.basicConfig(filename='task_06.log', filemode='w', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

File = namedtuple(typename='File', field_names=['name', 'ext', 'is_dir', 'par_dir'])


def read_dir(path: Path) -> None:
    for item in path.iterdir():
        f = File(item.stem if item.is_file() else item.name, item.suffix, item.is_dir(), item.parent)
        logger.info(f)
        if f.is_dir:
            read_dir(Path(f.par_dir) / f.name)


def parse():
    parser = argparse.ArgumentParser(prog='read_dir',
                                     description='Log directory list info to file',
                                     epilog='Usage: read_dir([pathlike string])')
    parser.add_argument('-p', '--path', default='.', help='Directory path (pathlike string)', type=Path)
    args = parser.parse_args()
    return read_dir(args.path)


if __name__ == '__main__':
    parse()
from os.path import split, join, abspath
from os import walk, rename

this_folder = split(abspath(__file__))[0]

absolute_paths_to_flacon_files = list()

for tup in walk(this_folder):
    for file_name in tup[2]:
        if file_name.endswith('.flacon'):
            absolute_paths_to_flacon_files.append(join(tup[0], file_name))

for path_to_flacon_file in absolute_paths_to_flacon_files:
    rename(path_to_flacon_file, path_to_flacon_file[:-2])
    print(path_to_flacon_file, '->', split(path_to_flacon_file[:-2])[1])

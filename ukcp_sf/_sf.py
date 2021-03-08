from os import path


def get_data_dir():

    base_path = path.abspath(path.dirname(__file__))
    data_dir = path.join(base_path, "..", "spatial-files")

    return data_dir

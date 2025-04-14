import zipfile
import pathlib


def compress_file(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for path in filepaths:
            path = pathlib.Path(path)
            archive.write(path, arcname=path.name)



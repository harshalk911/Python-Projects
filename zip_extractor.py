import zipfile


def extractor(filepath, dest_dir):
    with zipfile.ZipFile(filepath, 'r') as extract:
        extract.extractall(dest_dir)


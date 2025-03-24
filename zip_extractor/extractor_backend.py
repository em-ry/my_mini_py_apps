import zipfile


def extract_archive(archive_path, dest_dir):
    """ To extract contents of a zip file"""
    with zipfile.ZipFile(archive_path, "r") as archive:
        archive.extractall(dest_dir)


# code test run
if __name__ == "__main__":
    extract_archive(archive_path="../Bonus example/dummy_dir/compressed.zip", dest_dir="../Bonus example/dummy_dir")

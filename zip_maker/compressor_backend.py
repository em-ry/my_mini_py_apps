import pathlib
import zipfile


def make_archive(filepaths, dest_dir, name):
    """ Iterate over each file and put them in zip file"""
    # specify the destination path
    dest_path = pathlib.Path(dest_dir, f"{name}.zip")
    with zipfile.ZipFile(dest_path, "w") as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            # arcname is used here to prevent the paths from being subfolders in the zip file
            archive.write(filepath, arcname=filepath.name)


# code test run
if __name__ == "__main__":
    make_archive(filepaths=["parser.py", "parse.py"], dest_dir="../Bonus example/dummy_dir", name="chuka")

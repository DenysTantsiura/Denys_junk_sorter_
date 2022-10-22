from pathlib import Path
import shutil
import sys

import folder_scanner as scan
from string_normalize import normalize


def delete_empty_folder(folder: Path) -> None:
    '''
    Delete empty folder.

        Parameters:
            folder(Path): A simple path of folder.

        Returns:
            None
    '''
    try:
        folder.rmdir()
    except OSError:
        print(
            f'Can\'t delete {folder}, an error occurred. The directory must be empty.')


def handle_data(fullname: Path, target_folder: Path) -> None:
    '''
    If not, creates a category folder. Moves the category file 
    with the normalized name to the category folder.

        Parameters:
            fullname(Path): A full path of file.
            target_folder(Path): New destination folder for the file.

        Returns:
            None
    '''
    target_folder.mkdir(exist_ok=True, parents=True)
    name_without_extension = fullname.name[:fullname.name.rfind(
        scan.get_extension(fullname.name))-1]
    fullname.replace(
        target_folder / f'{normalize(name_without_extension)}.{scan.get_extension(fullname.name)}')


def handle_other(fullname: Path) -> None:
    '''
    Normalize name for unknown file (rename to normalized name).

        Parameters:
            fullname(Path): A full path of file.

        Returns:
            None
    '''
    name_without_extension = fullname.name[:fullname.name.rfind(
        scan.get_extension(fullname.name))-1]
    fullname.rename(fullname.parent.resolve(
    ) / f'{normalize(name_without_extension)}.{scan.get_extension(fullname.name)}')


def handle_archive(fullname: Path, target_folder: Path) -> None:
    '''
    If not, creates a folder for archives. Unpack archive file 
    to the normalized name folder with normalized name of archive file.

        Parameters:
            fullname(Path): A full path of file.
            target_folder(Path): New destination category folder for 
                the archive folder.

        Returns:
            None
    '''
    target_folder.mkdir(exist_ok=True, parents=True)
    name_without_extension = fullname.name[:fullname.name.rfind(
        scan.get_extension(fullname.name))-1]
    folder_for_file = target_folder / normalize(name_without_extension)
    folder_for_file.mkdir(exist_ok=True, parents=True)

    try:
        shutil.unpack_archive(str(fullname.resolve()),
                              str(folder_for_file.resolve()))

    except shutil.ReadError:
        print(f'The archive is damaged or it is not an archive: {fullname}!')
        folder_for_file.rmdir()

        return None
    # We delete the quasi-archive, it's junk
    fullname.unlink()


def junk_sorter(folder: Path) -> None:
    '''
    The main function checks the startup parameters and the presence of 
    a folder and starts the sorting process.

        Parameters:
            folder(Path): A simple path of folder.

        Returns:
            None
    '''
    scan.scanning(folder)
    for category in scan.file_paths_by_category:
        if category == 'other':
            for file in scan.file_paths_by_category[category]:
                handle_other(file)
        elif category == 'archives':
            for file in scan.file_paths_by_category[category]:
                handle_archive(file, folder / category)
        else:
            for file in scan.file_paths_by_category[category]:
                handle_data(file, folder / category)

    # Reverse the list to delete all folders
    for folder in scan.FOLDERS[::-1]:
        delete_empty_folder(folder)


if __name__ == '__main__':
    # Start junk sorter. Run: python3 main.py "full folder path for sorting"
    if len(sys.argv) == 2:
        # Make the path absolute
        folder_for_sorting = Path(sys.argv[1]).resolve()
        if folder_for_sorting.is_dir():
            print(f'Start sorting in folder: {folder_for_sorting}')
            junk_sorter(folder_for_sorting)
        else:
            print(f'Sorry, but "{folder_for_sorting}" is NOT a folder! Bye!')
    else:
        print('Sorry, but NO folder specified! Bye!')
        # junk_sorter(Path('D:\\test\\').resolve())

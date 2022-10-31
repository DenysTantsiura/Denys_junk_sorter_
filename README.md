# junk_sorter v.4 by Denys

Creation of the fourth version of the sorter of personal junk (files of different categories in one pile) by category.

A simple junk sorter program.
Many people have a folder on their desktop called something like "unsorted junk"...
This program sorts by certain categories (look in extensions.py) everything known in the specified folder, and even unpacks archives and deletes empty directories.

The script accepts one argument at startup — the name of the folder in which it will sort.

The script must go through the folder specified during the call and sort all files by groups specified in extensions.py.

When sorting, file and folder names are normalized according to the following rules (in order):

- transliteration of Cyrillic characters into Latin;
- replacement of all symbols, except letters of the Latin alphabet and numbers, with the symbol '\_';
- transliteration may not meet the standard;
- uppercase letters remain uppercase and lowercase remain lowercase after transliteration;
- file extensions do not change after renaming;
- the unpacked contents of the archive are transferred to the archives folder in a subfolder named the same as the archive, but without the extension at the end;
- files with unknown extensions remain unchanged (not transferred);
- after sorting empty folders will be deleted.

Run examples:

> > > python junk_sorter.py /user/Desktop/Мотлох/Junk

> > > junk-sorter D:\Junk

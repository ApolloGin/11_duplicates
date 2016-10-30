# 11_duplicates

## Synopsis

Script helps detect duplicates of file in specified directory.

> Note: File are duplicates, if both files have same name and size.

## Quick start

 - Run duplicates.py `python3.5 duplicates.py`
 - **Input**: Directory path, which you want to scan
 - **Output**: List of files which has duplicates and all full paths

## Module functions

 - `find_duplicates(root_directory)` - finds duplicates in directory and all sudirectories in specified path. Return `dict` value. Keys of the folowing dictionary is file names and values is `list` of full paths to the all duplicate files.
 - `show_duplicates(duplicates_dict)` - pretty print the result of the `find_duplicates(root_directory)` function.
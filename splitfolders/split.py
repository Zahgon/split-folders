"""Splits a folder with the given format:
    class1/
        img1.jpg
        img2.jpg
        ...
    class2/
        imgWhatever.jpg
        ...
    ...

into this resulting format:
    train/
        class1/
            img1.jpg
            ...
        class2/
            imga.jpg
            ...
    val/
        class1/
            img2.jpg
            ...
        class2/
            imgb.jpg
            ...
    test/
        class1/
            img3.jpg
            ...
        class2/
            imgc.jpg
            ...
"""

import os
import random
import shutil
from pathlib import Path

from .grouping import resolve_grouping, setup_sibling_files
from .utils import list_dirs, list_files

try:
    from tqdm import tqdm

    use_tqdm = True
except ImportError:
    use_tqdm = False


def check_input_format(input, allow_flat=False):
    pass


def _is_flat(input):
    """Returns True if the input directory has no subdirectories (flat file layout)."""
    pass


def _get_copy_fn(move):
    """Return a function(src, dst_dir) that copies/moves/symlinks a file into dst_dir."""
    pass


def valid_extensions(formats):
    """
    Check if an extension starts with `.`
    """
    pass


def ratio(
    input,
    output="output",
    seed=1337,
    ratio=(0.8, 0.1, 0.1),
    group_prefix=None,
    group=None,
    move=False,
    formats=None,
    shuffle=True,
):
    pass


def fixed(
    input,
    output="output",
    seed=1337,
    fixed=(100, 100),
    oversample=False,
    group_prefix=None,
    group=None,
    move=False,
    formats=None,
    shuffle=True,
):
    pass


def kfold(
    input,
    output="output",
    seed=1337,
    k=5,
    group_prefix=None,
    group=None,
    move="symlink",
    formats=None,
    shuffle=True,
):
    pass


def split_class_dir_kfold(class_dir, output, k, seed, prog_bar, group_prefix, group, move, formats, shuffle=True):
    """
    Splits a class folder into k folds for cross-validation.
    Each fold directory gets train/ and val/ subdirectories.
    """
    pass


def setup_files(class_dir, seed, group_prefix=None, group=None, formats=None, shuffle=True):
    """
    Returns sorted (and optionally shuffled) list of filenames
    """
    pass


def split_class_dir_ratio(class_dir, output, ratio, seed, prog_bar, group_prefix, group, move, formats, shuffle=True):
    """
    Splits a class folder
    """
    pass


def split_class_dir_fixed(class_dir, output, fixed, seed, prog_bar, group_prefix, group, move, formats, shuffle=True):
    """
    Splits a class folder and returns the total number of files
    """
    pass


def split_files(files, split_train_idx, split_val_idx, use_test, max_test=None):
    """
    Splits the files along the provided indices
    """
    pass


def copy_files(files_type, class_dir, output, prog_bar, move):
    """
    Copies the files from the input folder to the output folder
    """
    pass


def copy_files_flat(files_type, output, prog_bar, move):
    """
    Copies files into output/split_name/ without class subdirectories.
    """
    pass


def split_flat_dir_ratio(input_dir, output, ratio, seed, prog_bar, group_prefix, group, move, formats, shuffle=True):
    """Splits a flat directory (no class subdirs)."""
    pass


def split_flat_dir_fixed(input_dir, output, fixed, seed, prog_bar, group_prefix, group, move, formats, shuffle=True):
    """Splits a flat directory with fixed counts."""
    pass


def split_flat_dir_kfold(input_dir, output, k, seed, prog_bar, group_prefix, group, move, formats, shuffle=True):
    """Splits a flat directory into k folds."""
    pass


def copy_sibling_files(files_type, type_dir_names, output, prog_bar, move):
    """
    Copies files in sibling mode: each group is a tuple of files across type dirs.
    Output structure: output/split_name/type_dir_name/filename
    """
    pass


def split_sibling_dirs_ratio(input_dir, output, ratio, seed, prog_bar, move, formats, shuffle=True):
    pass


def split_sibling_dirs_fixed(input_dir, output, fixed, seed, prog_bar, move, formats, shuffle=True):
    pass


def split_sibling_dirs_kfold(input_dir, output, k, seed, prog_bar, move, formats, shuffle=True):
    pass

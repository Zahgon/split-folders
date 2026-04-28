from collections import defaultdict


def group_by_prefix(files, len_pairs):
    """Groups files by Path.stem, validates each group has len_pairs members."""
    pass


def resolve_grouping(files, group_prefix=None, group=None):
    """Central dispatcher. Validates mutual exclusivity, routes to the right strategy."""
    pass


def group_by_stem(files):
    """Groups files by stem. Auto-discovers group size. Validates all groups same size.
    If group size is 1 (no actual grouping), returns flat list of Paths."""
    pass


def setup_sibling_files(input_dir, seed, formats=None, shuffle=True):
    """Lists type dirs, groups files by stem across all dirs.
    Validates every stem exists in every dir. Returns (type_dir_names, groups)."""
    pass

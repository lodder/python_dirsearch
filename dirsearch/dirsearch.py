import os
import glob


def dirsearch(path, extension='*.*', recursive=True):
    if not os.path.isdir(path):
        raise Exception('Invalid directory specified: {}'.format(path))

    if recursive:
        return list([y for x in os.walk(path) for y in _insensitive_glob(os.path.join(x[0], extension))])
    else:
        return list(_insensitive_glob(os.path.join(path, extension)))


def _insensitive_glob(pattern):
    def either(c):
        return '[%s%s]' % (c.lower(), c.upper()) if c.isalpha() else c

    return glob.glob(''.join(map(either, pattern)))

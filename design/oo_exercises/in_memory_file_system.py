"""
check: https://leetcode.com/articles/design-in-memory-file-system/ for performance analysis

* Additional operations that can be implemented:
* `rmdir` and `rm` can also be easily implemented.
 
* Renaming files and dirs will also only entail changing the keys and
  using the old pointer as it is.
 
* Also we can add additional attributes to both dir and files classes also
  to show timestamps, user who created it, permissions on it and so on.
  
* One possible issue with the current design is that for showing only files
  or dirs we still need to traverse the entire children dict and see which
  values are of Object File or Dir
"""
from collections import OrderedDict
from datetime import datetime


class Entry(object):
    def __init__(self, parent_dir, entry_name):
        self.name = entry_name
        # use parent dir to enable cd ../ type operations
        self.parent = parent_dir
        self.created = datetime.now()
        # should be updated by filesystem methods when they access this
        self.last_accessed = datetime.now()
        # self.permissions = Permissions.owner(self.current_user)
        self.mode = ['--']*5


class File(Entry):
    def __init__(self, cur_root, file_name, contents):
        self.contents = contents
        super(File, self).__init__(cur_root, file_name)


class Dir:
    def __init__(self, cur_root, dir_name):
        # These children can be files or dirs
        self.children = OrderedDict()
        super(File, self).__init__(cur_root, dir_name)


class FileSystem:
    def __init__(self):
        self.root = Dir()

    def cd(self, path, root=None):
        """
        Drops to the end of `path` supplied
        You can give it an optional root if you are already in a dir(can be fetched from terminal
        in practice or other tool used to access the file system) otherwise will start from
        base root always.
        """
        if root is None:
            root = self.root
        path = path.strip('/').split('/')
        for index in xrange(len(path)):
            subdir = path[index]
            if subdir != '':
                try:
                    root = root.children[subdir]
                except KeyError:
                    return 'Invalid path %s' % path
        return root

    def ls(self, path):
        root = self.cd(path)
        return root.children.keys()

    def addContentToFile(self, path, contents):
        root = self.cd(path[:-1])
        root.children[path[-1]] = File(contents)

    def readContentFromFile(self, path):
        root = self.cd(path[:-1])
        return root.children[path[-1]].contents

    def mkdir(self, path):
        """
        No point in using _traverse_to_path here since this method
        not only traverses to the path but creates all intermediate
        paths when necessary so will need to call _tra... multiple times
        """
        root = self.root
        path = path.split('/')
        for subdir in path:
            if subdir == '':
                continue
            if not root.children.get(subdir):
                root.children[subdir] = Dir()
            root = root.children[subdir]

if __name__ == '__main__':
    commands = [
        "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
    args = [
        ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]
    fs = FileSystem()
    for command, arg in zip(commands, args):
        print getattr(fs, command)(*arg)

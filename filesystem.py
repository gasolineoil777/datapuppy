#
# Write a script that counts bytes in a file system
#
# example input=file_system = {
#  "file1": 123,
#  "file2": 456,
#  "dir1": {
#    "file3": 234,
#    "file4": 432
#  },
#  "dir2": {
#    "file5": 232,
#    "dir3": {
#      "file6": 212,
#      "dir4": {
#        "file7": 234,
#        "file8": 432
#      },
#      "file9": 654
#    }
#  },
#  "dir3": {
#  }
#}
#
# expected output=3009
#


file_system = {
  "file1": 123,
  "file2": 456,
  "dir1": {
    "file3": 234,
    "file4": 432
  },
  "dir2": {
    "file5": 232,
    "dir3": {
      "file6": 212,
      "dir4": {
        "file7": 234,
        "file8": 432
      },
      "file9": 654
    }
  },
  "dir3": {
  }
}

def size(tree):
  result = 0
  if isinstance(tree, int):
    result = tree
  else:
    for branch in tree:
      result += size(tree[branch])
  return result

print(size(file_system))

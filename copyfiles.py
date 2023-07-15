import shutil

# copyfile() = copies the contents of a file
# copy() = copyfile() + permissions mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)

shutil.copyfile("test.txt", "copy.txt")  # src, dst
#  args are the same for each methods of copying

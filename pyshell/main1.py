from fs.ls import ListOfFiles
from fs.ls import PathFormat

ls = ListOfFiles('/home/dragon')

# files = ls.get_files()
# print(*files, sep="\n")
# dirs = ls.get_directories()
# print(*dirs, sep="\n")

# hidden_files = ls.get_hidden_files()
#
# print(*hidden_files, sep='\n')

files = ls.get_files(PathFormat.absolute)

print('\n', *files, sep='\n')

# hidden_dirs = ls.get_hidden_directories()
#
# print('\n', *hidden_dirs, sep='\n')

dirs = ls.get_directories(PathFormat.absolute)

print('\n', *dirs, sep='\n')
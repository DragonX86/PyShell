import os
import enum


class PathFormat(enum.Enum):
    relative = 0
    absolute = 1


class ListOfFiles:
    def __init__(self, path: str):
        if type(path) == str:
            self.__path = path
        else:
            raise ValueError

    @property
    def current_path(self):
        return self.__path

    def get_files(self, path_format: PathFormat = PathFormat.relative):
        if not isinstance(path_format, PathFormat):
            raise ValueError

        files = [
            file for file in os.listdir(self.__path)
            if os.path.isfile(os.path.join(self.__path, file))
            if not file.startswith('.')
        ]

        if path_format == PathFormat.absolute:
            return [os.path.join(self.__path, file) for file in files]
        elif path_format == PathFormat.relative:
            return files

    def get_hidden_files(self, path_format: PathFormat = PathFormat.relative):
        if not isinstance(path_format, PathFormat):
            raise ValueError

        files = [
            file for file in os.listdir(self.__path)
            if os.path.isfile(os.path.join(self.__path, file))
            if file.startswith('.')
        ]

        if path_format == PathFormat.absolute:
            return [os.path.join(self.__path, file) for file in files]
        elif path_format == PathFormat.relative:
            return files

    def get_directories(self, path_format: PathFormat = PathFormat.relative):
        if not isinstance(path_format, PathFormat):
            raise ValueError

        folders = [
            folder for folder in os.listdir(self.__path)
            if os.path.isdir(os.path.join(self.__path, folder))
            if not folder.startswith('.')
        ]

        if path_format == PathFormat.absolute:
            return [os.path.join(self.__path, folder) for folder in folders]
        elif path_format == PathFormat.relative:
            return folders

    def get_hidden_directories(self, path_format: PathFormat = PathFormat.relative):
        if not isinstance(path_format, PathFormat):
            raise ValueError

        folders = [
            folder for folder in os.listdir(self.__path)
            if os.path.isdir(os.path.join(self.__path, folder))
            if folder.startswith('.')
        ]

        if path_format == PathFormat.absolute:
            return [os.path.join(self.__path, folder) for folder in folders]
        elif path_format == PathFormat.relative:
            return folders

    def get_links(self, path_format: PathFormat = PathFormat.relative):
        if not isinstance(path_format, PathFormat):
            raise ValueError

        links = [
            link for link in os.listdir(self.__path)
            if os.path.isdir(os.path.join(self.__path, link))
            if not link.startswith('.')
        ]

        if path_format == PathFormat.absolute:
            return [os.path.join(self.__path, link) for link in links]
        elif path_format == PathFormat.relative:
            return links

    def get_hidden_links(self, path_format: PathFormat = PathFormat.relative):
        if not isinstance(path_format, PathFormat):
            raise ValueError

        links = [
            link for link in os.listdir(self.__path)
            if os.path.isdir(os.path.join(self.__path, link))
            if link.startswith('.')
        ]

        if path_format == PathFormat.absolute:
            return [os.path.join(self.__path, link) for link in links]
        elif path_format == PathFormat.relative:
            return links

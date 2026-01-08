from abc import ABC, abstractmethod

class FileVideo(ABC):
    def __init__(self, name, library = None):
        self.name = name
        self.library = library
    
    @abstractmethod
    def accept(self, visitor):
        pass

    @classmethod
    def from_name(cls, name):
        return cls(name)
        # example: avi = AVI.from_name("video.avi")

    @classmethod
    def from_name_and_library(cls, name, library):
        return cls(name, library)
        # example: avi = AVI.from_name_and_library("video.avi", "library")

class AVI(FileVideo):
    def __init__(self, name, library = None):
        super().__init__(name, library)

    def accept(self, visitor):
        visitor.visitAVI(self)

class MP4(FileVideo):
    def __init__(self, name, library = None):
        super().__init__(name, library)

    def accept(self, visitor):
        visitor.visitMP4(self)

class MKV(FileVideo):
    def __init__(self, name, library = None):
        super().__init__(name, library)

    def accept(self, visitor):
        visitor.visitMKV(self)

class VOB(FileVideo):
    def __init__(self, name, library = None):
        super().__init__(name, library)

    def accept(self, visitor):
        visitor.visitVOB(self)
    

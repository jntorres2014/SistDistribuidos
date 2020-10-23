from ctypes import *

class Path(Structure):
    _fields_ = [
        ("path", c_wchar_p),
        #("operacion", c_int),
        ]

class PathFiles(Structure):
    _fields_ = [
        ("values", c_wchar_p),
        ]
                
#Armo mis 2 estructuras que tenia en el .proto
class PathRead(Structure):
    _fields_ = [
        ("value", c_int),
        ("offset", c_int),
        ("number_bytes", c_int),
    ]
class FileData(Structure):
    __file__ = [
        ("data", c_byte),
    ]

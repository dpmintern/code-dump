import os
import shutil
from pathlib import Path
from io import BytesIO

override = b"\x43\x6A\xD5\x84\x6C\xBE\xCB\xA3\x8E\x1A\x5E\x05\x9B\xC5\xBA\xD2\xA8\x2D\xC4\xF5\xA3\xE0\x9A\xA0\x36\x4D\xD9\xD5\x66\x16\xA7\xBA\x72\x9C\x22\x29\x1C\x01\x00\x00\x84\x4A\x02\x9E\xD2\x11\x5F\xCD\x00\x00\x00\x00\x00\x00\x00\x00\x9F\x86\x01"
offA = int(0x2050)
offB = int(0x208A)

filepath = os.path.abspath(os.getcwd())
print(filepath)
file = Path(filepath+"/savedata.bin")
backupPath = filepath+"/backup"

shutil.copy(file,backupPath)

with open(file,"rb+") as f:
    f.seek(offA,0)
    f.write(override)
    f.close()

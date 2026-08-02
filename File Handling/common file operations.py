## Both modern and old way

import os
from pathlib import Path

# To create a folder
# os.mkdir("new_folder")
# Path("new").mkdir()


# To delete the file
# os.remove("new1.txt")
# Path("abc.txt").unlink()


# To Rename the file

# os.rename("new.txt", "new1.txt")
# Path("new1.txt").rename("new.txt")

# for f in os.listdir("."):
#     print(f)
for f in Path(".").iterdir():
    print(f)

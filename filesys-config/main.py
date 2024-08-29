import os
import subprocess
import time
def disable_unused_filesystems(filesystems):
    for filesys in filesystems:
        subprocess.run(f"rmmod {filesys}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        filepath = f"/etc/modprobe.d/{filesys}.conf"
        if not os.path.exists(filepath):
            with open(filepath, "w") as file:
                file.write(f"install {filesys} /bin/true\n")
        else:
            with open(filepath, "r") as file:   
                content = file.read()
            if f"install {filesys} /bin/true" not in content:
                with open(filepath, "a") as file:
                    file.write(f"install {filesys} /bin/true\n")

def main():

    unused_filesys = ["cramfs", "freevxfs", "jjfs2", "hfs", "hfsplus", "squashhfs", "udf"]
    disable_unused_filesystems(unused_filesys)

main()
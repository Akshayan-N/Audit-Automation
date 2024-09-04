import os
import subprocess
import time

import services
import file_permission

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
def tmp_config():
    filesys = "tmp"
    cmd = f"mount | grep -E '\\s/{filesys}\\s'"
    
    output = subprocess.run(
        cmd,
        shell=True,
        capture_output=True,
        text=True
    ).stdout

    print(output)
    #todo
    pass

commands_to_fix = []

def aide_setup():
    if not services.is_package_installed("aide"):
        services.install_package("aide")
    #todo 
    """complete 1.3.2"""

def secure_boot_settings():

    ##Boot loader file permission check 
    bootloader_file = { 
        "path" : "/boot/grub/grub.cfg",
        "permissions" : [["read"], [], []],
        "group" : ["root"],
        "cmd_fix": "chmod u-wx,go-rwx ",
    }

    output = file_permission.audit_file_permission(bootloader_file)
    if output == None:
        print("Boot Loader is configured correctly")
    else:
        print("Boot loader is not configured correctly need to be fixed !!!")
        commands_to_fix.append(output)

    #Ensure Bootloader 
    

def main():
    unused_filesys = ["cramfs", "freevxfs", "jjfs2", "hfs", "hfsplus", "squashhfs", "udf", "usb-storage"]
    # disable_unused_filesystems(unused_filesys)

    # tmp_config()

    secure_boot_settings()
    # print(commands_to_fix)
main()
import os
import platform
import sys
import pwd
import grp
import subprocess


def detect_os():
    return platform.system() 

def check_sudo_user():
    if not 'SUDO_UID' in os.environ.keys():
        print("sudo privilige required!!")
        print(f"To run as sudo, use : sudo python {sys.argv[0]}")
        exit()

def get_fileinfo(filename):
    fileinfo = {}
    try: 
        file_stat = os.stat(filename)
        #Converting the file acces mode into codes
        owner_permissions = (file_stat.st_mode & 0o700) >> 6
        group_permissions = (file_stat.st_mode & 0o070) >> 3
        other_permissions = file_stat.st_mode & 0o007 >> 0

        fileinfo["permission"] = f"{owner_permissions}{group_permissions}{other_permissions}"

        # permission_value = f"{owner_permissions}{group_permissions}{other_permissions}"
        # return int(permission_value)    

        uid = file_stat.st_uid
        gid = file_stat.st_gid

        # Get the owner and group names
        owner = pwd.getpwuid(uid).pw_name
        group = grp.getgrgid(gid).gr_name

        fileinfo["owner"] = owner
        fileinfo["group"] = group

    except FileNotFoundError:
        print(f"The file {filename} does not exist.")


    return fileinfo

def mode_info(codes) :
    all_permission = []
    for code in codes:
        code = int(code)
        permissions = []
        if (code // 4 == 1):
            code-=4
            permissions.append("read")
        if (code // 2 == 1):
            code-=2
            permissions.append("write")
        if (code == 1):
            permissions.append("execute")
        all_permission.append(permissions)
    return all_permission

import os
import platform
import sys
import pwd
import grp
import subprocess


def detect_os():
    return platform.system() 

def change_permission(filename, filecmd, fileinfo): 
    try:
        os.system(f"{filecmd} {filename}")

        groups = ["root"]
        if ("shadow-" in filename):
            groups.append("shadow")
        if (fileinfo["owner"] != "root" or fileinfo["group"] not in groups):
            
            if (len(groups) == 1):
                group = "root"
            else :
                for i in range(len(groups)):
                        print(f"{i+1}. {groups[i]}") 
                while True:
                    try:
                        choice = int(input("Enter you choice : ")) - 1
                        group = groups[choice]
                    except:
                        pass
            
            os.system(f"chown root:{group} {filename}")

    # except FileNotFoundError:
    #     print(f"The file {filename} does not exist.")
    # except PermissionError:
    #     print(f"Permission denied. Cannot change permissions for {filename}.")
    except :
        pass

def check_sudo_user():
    if not 'SUDO_UID' in os.environ.keys():
        print("sudo privilige required!!")
        print(f"To run as sudo, use : sudo python {sys.argv[0]}")
        exit()


def check_permission(file):
    filepath = file["path"]
    filecmd = file["cmd"]


    fileinfo_before = get_fileinfo(filepath)

    change_permission(filepath, filecmd, fileinfo_before)

    fileinfo_after = get_fileinfo(filepath)

    if fileinfo_before != fileinfo_after:
        print(f"Incorrect File permission for {filepath}. Fixed")
    else : 
        print(f"file {filepath} are configured correctly")

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

if __name__ == "__main__":

    #Check SUDO 
    check_sudo_user()
    
    print(detect_os())
    files = [
        {"path" : "/etc/shadow",   "cmd" : "chmod o-rwx,g-wx", "permission": "Read"},
        {"path" : "/etc/group",    "cmd" : "chmod o-rwx,g-wx", "permission": "Read"},
        {"path" : "/etc/gshadow",  "cmd" : "chmod o-rwx,g-wx", "permission": "Read"},
        {"path" : "/etc/passwd",   "cmd" : "chmod 644"       , "permission": "Read"},
        {"path" : "/etc/passwd-",  "cmd" : "chmod u-x,go-rwx", "permission": "Read"},
        {"path" : "/etc/shadow-",  "cmd" : "chmod o-rwx,g-wx", "permission": "Read"},
        {"path" : "/etc/group-",   "cmd" : "chmod u-x,go-rwx", "permission": "Read"},
        {"path" : "/etc/gshadow-", "cmd" : "chmod o-rwx,g-rw", "permission": "Read"},
    ]

    for file in files:
        check_permission(file)

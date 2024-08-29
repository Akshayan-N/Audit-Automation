import os

file = "filename.txt" 

def get_permission(filename):
    permissions = {4 : os.R_OK, 2 : os.W_OK, 1 : os.X_OK}
    
    permission_value = 0

    
    for key, value in permissions.items():
        if (os.access(filename, value)):
            permission_value += key
    print()

    print(f"{filename} permssions : {permission_value}", end="")

os.chmod("filename.txt", 0o777)
get_permission("filename.txt")
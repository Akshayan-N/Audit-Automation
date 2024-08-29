import os
import stat

def get_permission(filename):
    # Get the file's status
    file_stat = os.stat(filename)
    
    print(file_stat.st_mode)
    # Extract the permission bits
    owner_permissions = (file_stat.st_mode & 0o700) >> 6
    group_permissions = (file_stat.st_mode & 0o070) >> 3
    other_permissions = file_stat.st_mode & 0o007

    # Combine the permissions into a single value
    permission_value = (owner_permissions * 100) + (group_permissions * 10) + other_permissions

    print(f"{filename} permissions: {permission_value}")

# Example usage
get_permission("filename.txt")

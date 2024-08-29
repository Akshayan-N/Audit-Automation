import os
import pwd
import grp

# Specify the file path
file_path = '/etc/passwd-'

# Get the file's stat information
file_stat = os.stat(file_path)

# Get the owner's user ID and group ID
uid = file_stat.st_uid
gid = file_stat.st_gid

# Get the owner and group names
owner = pwd.getpwuid(uid).pw_name
group = grp.getgrgid(gid).gr_name

print(f"Owner: {owner}")
print(f"Group: {group}")
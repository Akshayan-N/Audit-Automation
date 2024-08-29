import os
import subprocess
import fileinformation

files_benmarks =  [
    {
        "path" : "/etc/passwd",
        "permissions" : [["read", "write"], ["read"], ["read"]],
        "group" : ["root"],
        "cmd_fix": "chmod 644 ",    
    },
    {
        "path" : "/etc/group",
        "permissions" : [["read", "write"], ["read"], ["read"]],
        "group" : ["root"],
        "cmd_fix": "chmod 644 ",
    },
    {
        "path" : "/etc/shadow",
        "permissions" : [["read", "write"], ["read"], []],
        "group": ["root"],
        "cmd_fix": "chmod o-rwx,g-wx "  
    },
    {
        "path" : "/etc/gshadow",
        "permissions" : [["read", "write"], ["read"], []],
        "group": ["root"],
        "cmd_fix": "chmod o-rwx,g-wx "  
    },
    {
        "path" : "/etc/shadow-",
        "permissions" : [["read", "write"], ["read"], []],
        "group": ["root", "shadow"],
        "cmd_fix": "chmod o-rwx,g-wx "  
    },
    {
        "path" : "/etc/gshadow-",
        "permissions" : [["read", "write"], ["read"], []],
        "group": ["root", "shadow"],
        "cmd_fix": "chmod o-rwx,g-wx "  
    },
    {
        "path" : "/etc/passwd-",
        "permissions" : [["read", "write"], [], []],
        "group" : ["root"],
        "cmd_fix": "chmod u-x,go-rwx ",
    },
    {
        "path" : "/etc/group-",
        "permissions" : [["read", "write"], ["read"], ["read"]],
        "group" : ["root"],
        "cmd_fix": "chmod u-x,go-rwx ",
    },
]

commands_to_fix = [] 

def audit_file_permission():
    commands = [] 
    # File permission are checked     
    for file_benchmark in files_benmarks:        
        file = file_benchmark["path"]
        file_info = fileinformation.get_fileinfo(file)
        if file_info["owner"] != "root" or file_info["group"] not in file_benchmark["group"]:
            commands_to_fix.append(f"chown root:root {file}")
            print(f"{file} ownership incorrect.")
        file_permissions = fileinformation.mode_info(file_info["permission"])
        
        error_flag = False
        for current_permissions, benchmark_permission in zip(file_permissions, file_benchmark["permissions"]):
            if error_flag:
                break
            for permission in current_permissions:
                if permission == ["any"]:
                    print(True)
                    break
                if permission not in benchmark_permission:
                    print(f"{file} permission incorrect.")
                    # commands_to_fix.append(f"{file_benchmark["cmd_fix"]} {file}")
                    
                    error_flag = True
                    break             
    
    
    print(commands_to_fix)
    if commands_to_fix == []:
        print("All configuration set correctly")
    else:
        commands_to_fix.extend(commands)
    

        
def execute_audit(command):
    output = subprocess.run(
        command, 
        capture_output=True, 
        text=True, 
        shell=True
    ).stdout.split('\n')[:-1]

    return output

def audit_worldwide_write():
    commands = []
    cmd = "df --local -P | awk '{if (NR!=1) print $6}' | xargs -I '{}' find '{}' -xdev -type f -perm -0002"
    output = subprocess.run(cmd, capture_output=True, text=True, shell=True).stdout.split('\n')[:-1]

    for i in output:       
        if (i.endswith("Permission denied")):
            output.remove(i)

    if output == []:
        print("No worldwide writable file exists")
    else:
        for file in output:
            commands.append(f"chmod o-w {file}") 

    commands_to_fix.extend(commands)
def audit_unowned_files():
    commands = []
    cmd = " df --local -P | awk {'if (NR!=1) print $6'} | xargs -I '{}' find '{}' -xdev -nouser"
    output = subprocess.run(cmd, capture_output=True, text=True, shell=True).stdout.split('\n')[:-1]

    for i in output:       
        if (i.endswith("Permission denied")):
            output.remove(i)

    if output == []:
        print("No unowned file exists")
    else:
        ''' Assign the file to active user '''
        pass
        #todo
        for file in output:
            pass
    print(output[:10])
    commands_to_fix.extend(commands)

def audit_ungrped_files():
    commands = []
    cmd = "df --local -P | awk '{if (NR!=1) print $6}' | xargs -I '{}' find '{}' -xdev -nogroup"
    output = subprocess.run(cmd, capture_output=True, text=True, shell=True).stdout.split('\n')[:-1]

    for i in output:       
        if (i.endswith("Permission denied")):
            output.remove(i)

    if output == []:
        print("No ungrouped file exists")
    else:
        ''' Assign the file to active group '''
        pass
        #todo
        for file in output:
            pass
    print(output[:10])
    commands_to_fix.extend(commands)
def fix_audits():
    for command in commands_to_fix:
        os.system(command)
def main():
    # audit_file_permission()
    # audit_worldwide_write()
    # audit_unowned_files()
    # audit_ungrped_files()
    # fix_audits()

    with open('/etc/os-release', 'r') as file:
        file = file.readlines()
        print(file)
    pass
main()
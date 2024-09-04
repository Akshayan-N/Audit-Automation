import os
import subprocess
import filedata
import benmarks

files_benmarks = benmarks.files_benmarks

commands_to_fix = [] 

def audit_file_permission(file_benchmark):
    file = file_benchmark["path"]
    file_info = filedata.get_fileinfo(file)
    if file_info["owner"] != "root" or file_info["group"] not in file_benchmark["group"]:
        commands_to_fix.append(f"chown root:root {file}")
        print(f"{file} ownership incorrect.")
    file_permissions = filedata.mode_info(file_info["permission"])
    

    for current_permissions, benchmark_permission in zip(file_permissions, file_benchmark["permissions"]):
        for permission in current_permissions:
            if permission == ["any"]:
                break
            if permission not in benchmark_permission:
                print(f"{file} permission incorrect.")
                return f"{file_benchmark["cmd_fix"]} {file}"

      
            
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
    for file_benmark in files_benmarks:
        output = audit_file_permission(file_benmark)
        if output == None:
            print(f"{file_benmark["path"]} is configured correctly")
        else:
            commands_to_fix.append(output)
    # audit_worldwide_write()
    # audit_unowned_files()
    # audit_ungrped_files()
    # fix_audits()

    # with open('/etc/os-release', 'r') as file:
    #     file = file.readlines()
    #     print(file)
    # pass

if __name__ == "__main__":
    main()
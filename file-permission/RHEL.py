import subprocess
#RHEL audit
# def audit_rootID():
#     cmd = "awk -F: '$3 == 0 {print $1}' /etc/passwd"
#     output = subprocess.run(cmd, capture_output=True, text=True, shell=True).stdout.split('\n')[:-1]
#     print(output)
#     if (output == ['root']):
#         print("root ID is configured correctly")
#     else:
#         ''' remove or change users from uid0 expect "root" '''
#         #todo
#         pass
import subprocess

commands_to_fix = []
def audit_passwd():
    pass

def audit_legacy_entries(file):
    output = subprocess.run(
        f"grep '^\\+:' {file}",
        capture_output=True,
        text=True,
        shell=True
    ).stdout.split('\n')[:-1]

    if output == []:
        print(f"No Legacy entries in {file}")
    else:
        print(f"Legacy Entries found in {file}. Need to be removed")
        commands_to_fix.append(f"sudo sed -i '/^+:/d' {file}")

def audit_rootID():
    cmd = "awk -F: '$3 == 0 {print $1}' /etc/passwd"
    output = subprocess.run(cmd, capture_output=True, text=True, shell=True).stdout.split('\n')[:-1]
    print(output)
    if (output == ['root']):
        print("root ID is configured correctly")
    else:
        print(''' remove or change users from uid0 expect "root" ''')
        #todo
        pass

def rootpath_intergrity():
    subprocess.run("user-grp-setting/rootpath-intergrity.sh")
def main():
    # audit_passwd()

    for file in ["/etc/passwd", "/etc/shadow", "/etc/group"]:
        audit_legacy_entries(file)

    # rootpath_intergrity()
main()
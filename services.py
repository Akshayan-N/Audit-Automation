import subprocess

def detect_os():
    return "Ubuntu"
def is_package_installed(package_name):
    try:
        # Check if the package is installed
        subprocess.run(
            f"dpkg -s {package_name}", 
            check=True, 
            shell=True,
            stdout=subprocess.DEVNULL, 
            stderr=subprocess.DEVNULL
        )
        return True
    except subprocess.CalledProcessError:
        return False
def install_package(package_name):
    try:
        # Update the package list
        subprocess.run(['sudo', 'apt-get', 'update'], check=True)
        # Install the package
        subprocess.run(['sudo', 'apt-get', 'install', '-y', package_name], check=True)
        print(f"Package '{package_name}' has been installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install the package '{package_name}'. Error: {e}")

def time_sync():
    if not is_package_installed("ntp"):
        install_package("ntp")

def remove_services(services):
    for service in services:
        output = subprocess.run(
            "dpkg-query -W -f='${binary:Package}\t${Status}\t${db:Status-Status}\n' " + service,
            capture_output=True,
            text=True,
            shell=True
        ).stdout.split()
        
        if "installed" in output:
            subprocess.run(
                ""
            )
    
def main():
    os = detect_os()

    if (os == "Ubuntu"):
        package_manger = "apt"
    elif (os == "RHEL"):
        package_manger = "yum"
    else:
        print("OS not supported")
        exit()
    
    # time_sync()

    unwanted_services = ["apache2", "nfs-kernel-server"]
    remove_services(unwanted_services)


if __name__ == "__main__":
    main()
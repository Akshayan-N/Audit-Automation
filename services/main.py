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

    
    
def main():
    os = detect_os()

    if (os == "Ubuntu"):
        package_manger = "apt"
    elif (os == "RHEL"):
        package_manger = "yum"
    else:
        print("OS not supported")
        exit()
    
    time_sync()
main()
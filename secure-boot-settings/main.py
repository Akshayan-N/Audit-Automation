import os

def find_bootloader():
    if os.path.exists('/boot/grub/grub.cfg'):
        return "GRUB detected"
    elif os.path.exists('/boot/loader/entries/'):
        return "systemd-boot detected"
    elif os.path.exists('/boot/efi/EFI/microsoft/boot/bootmgfw.efi'):
        return "Windows Boot Manager detected"
    elif os.path.exists('/boot/lilo.conf'):
        return "LILO detected"
    else:
        return "Bootloader not found or unsupported."

# Example usage
bootloader = find_bootloader()
print(bootloader)
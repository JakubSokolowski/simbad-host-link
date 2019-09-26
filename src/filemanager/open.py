import os
import platform
import subprocess


def open_system_file_manager(path: str) -> None:
    """
    Opens default file manager for current os at specified path
    :param path: absolute path to file
    """
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])

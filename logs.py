import logging

import os
import pathlib
import platform
import subprocess

FILENAME = "logs.txt"

file = pathlib.Path().stem

if file :
    if platform.system() == "Windows":
        subprocess.run(["type", FILENAME, ], shell=True)  
    elif platform.system() in ["Linux", "Darwin"]:
        subprocess.run(["echo", "$HOME"], shell=True)

logger = logging.getLogger(__name__)
if not logger.handlers:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
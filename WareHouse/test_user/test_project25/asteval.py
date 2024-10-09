# Install asteval library if not already installed
import subprocess
subprocess.check_call(["pip", "install", "asteval"])
from ast import literal_eval  # safer evaluation library
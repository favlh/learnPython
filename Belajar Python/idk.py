# Checking for vulnerable software versions.

import subprocess

result = subprocess.run(["pip", "list", "--outdated"], capture_output=True, text=True)
print(result.stdout)
import subprocess
import sys

def save_requirements():
    with open('requirements.txt', 'w') as f:
        result = subprocess.run(['pip', 'freeze'], stdout=f, text=True)

def pip_install(package):
    subprocess.run([sys.executable, "-m", "pip", "install", package])
    save_requirements()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pip_install.py <package_name>")
    else:
        package_name = sys.argv[1]
        pip_install(package_name)

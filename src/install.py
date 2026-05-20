import subprocess
neededpackages = ["flask"]

def main():
    for package in neededpackages:
        subprocess.call(["pip", "install", package])

if __name__ == "__main__":
    main()
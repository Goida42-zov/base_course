import sys, os

print(os.getcwd()) # Путь где лежит файл


os.system('echo hi!')
# os.system('python3 sys_and_os.py')


print("Python version is:", sys.version)
print(sys.path)
print(sys.platform)

	
print(dir(sys))
print(dir(os))
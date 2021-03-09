from stdlib_list import stdlib_list
if __name__ == "__main__":
    libraries = stdlib_list("3.6")
    f = open("check_requirements.txt", 'r')
    print("Libraries that are not in the standard library are:")
    for lib in f:
        lib = ''.join(e for e in lib if e.isalnum())
        if not lib in libraries:
            print(lib)
from importlib import import_module
import sys
sys.path.append("src/")
sys.path.append("examples/")
sys.path.append("tests/")

if len(sys.argv) > 1:
    module_name = 'test_' + sys.argv[1]
    try:
        import_module(module_name)
    except:
        print("Test does not exist...")
else:
    print("Please indicate which test do you want to pass...")

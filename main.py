from importlib import import_module
import sys,os

path_src = "src/"
path_exa = "examples/"
path_tes = "tests/"

sys.path.append(path_src)
sys.path.append(path_exa)
sys.path.append(path_tes)

if len(sys.argv) > 1:
    module_name = 'test_' + sys.argv[1]
    fn = path_tes + module_name + ".py"
    if os.path.exists(fn):
        try:
            import_module(module_name)
        except Exception as e:
            print("Error while trying to load the test:\n\t", e)
    else:
        print("Test does not exist...")
else:
    print("Please indicate which test do you want to pass...")

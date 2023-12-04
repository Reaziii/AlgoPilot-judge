import shutil

def copy_folder(source_folder, destination_folder):
    try:
        shutil.copytree(source_folder, destination_folder)
        return True
    except Exception as e:
        return False


def copy_code_to_maincpp(subid,code):
    try:
        with open(subid+"/main.cpp", "w") as file:
            file.write(code)
        return True
    except Exception as e:
        print(e)
        return False
    
def copy_testcase_to_input(subid,input, output,tcid, key):
    try:
        with open(subid+f"/input{str(key)}.txt", "w") as file:
            file.write(input)
        with open(subid+f"/output{str(key)}.txt", "w") as file:
            file.write(output)
        with open(subid+f"/testcase{str(key)}.txt", "w") as file:
            file.write(tcid)
        return True
    except Exception as e:
        print(e)
        return False


def delete_submission_file(subid):
    try:
        shutil.rmtree(subid)
        print("folder deleted - ", subid)
        return True
    except Exception as e:
        print("Failed to remove file : ", e)

def add_code_details(subid, timilimit, memeorylimit):
    try:
        with open(subid+f"/subid.txt", "w") as file:
            file.write(subid)
        with open(subid+f"/timelimit.txt", "w") as file:
            file.write(timilimit)
        with open(subid+f"/memorylimit.txt", "w") as file:
            file.write(memeorylimit)
        return True
    except Exception as e:
        print(e)
        return False
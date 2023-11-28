from files import (
    copy_code_to_maincpp,
    copy_folder,
    copy_testcase_to_input,
    add_code_details,
    delete_submission_file
)
import os
import subprocess


def start_running(
    code, checker, testcases, timelimit, memorylimit, sub_id, checker_enable
):
    print("okay lets start process!")
    print("start creating a file and coping")
    folder = copy_folder("cpp", sub_id)
    if folder is False:
        print("Failed to create folder")
        return False

    print("Files created successfully!")
    print("Now copy the code to main.cpp")

    copy = copy_code_to_maincpp(sub_id, code)
    if copy is False:
        print("Failed to copy")
        return False

    print("Code copied to file/main.cpp")
    print("Add the contest details")
    add_code_details(sub_id, timelimit, memorylimit)
    copy_testcases(sub_id, testcases, checker)
    run_code(sub_id)
    # delete_submission_file(sub_id)

    return True


def copy_testcases(subid, testcases, checker) -> bool:
    i = 0
    for testcase in testcases:
        print("Coping the testcase #", i)
        copy_testcase_to_input(
            subid, testcase["input"], testcase["output"], testcase["id"], i
        )
        i = i + 1
    return True


def run_code(container_name: str):
    process = "docker build -t " + container_name + " ./" + container_name
    process2 = "docker run --network host " + container_name
    process3 = "docker rmi " + container_name + " --force"
    os.system(process)
    os.system(process2)
    os.system(process3)
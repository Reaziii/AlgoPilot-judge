import os
import subprocess
from judge.VERDICTS import VERDICTS
def run_code(code:str, timelimit:str,container_name:str, memorylimit:str, input:str):
    process = "docker build -t "+container_name+" ./judge/cpp/docker"
    process2 = "docker run --env CODE=\""+code+"\" --env INPUT=\""+input+"\" --env TTIMELIMIT=\""+timelimit+"\" --env MMEMORYLIMIT=\""+memorylimit+"\" "+container_name
    os.system(process)
    code_output = subprocess.check_output(process2, shell=True, text=True).strip()
    os.system("docker rmi "+container_name+" --force")
    return code_output


def get_verdict(code:str, timelimit:str, container_name:str, memorylimit:str, input:str, checker:str):
    code_output = run_code(code, timelimit, container_name, memorylimit, input)
    if(code_output[0]!='0'):
        return VERDICTS[code_output[0]]
    checker_output = run_code(checker, "5", container_name, "1000000", input+"\n\n"+code_output[2:])
    if(checker_output[0]!='0'):
        return VERDICTS["6"]
    
    if(checker_output[2]=="1"):
        return "accepted"
    return "wrong answer"


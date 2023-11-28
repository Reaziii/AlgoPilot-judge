import requests
import json
from status import status
from runner import start_running

def yes_i_am_free():
    print("And I am free!!!")
    print("Lets see what is the task!")
    # request for a submission
    auth_token = status.get("token")
    url = status["server"] + "/judge/"
    data = {"key1": "value1", "key2": "value2"}
    headers = {
        "Content-Type": "application/json",
        "authorization": f"{auth_token}",  # Include your authorization token here
    }
    response = requests.post(url, data=json.dumps(data), headers=headers)
    if(response.status_code  != 200):
        return False
    _status: bool = response.json().get("status")
    if _status is False:
        return

    code = (response.json().get('submission')['code'])
    checker =""
    enable = (response.json().get('submission')['enable'])
    sub_id = (response.json().get('submission')['sub_id'])
    testcases = (response.json().get('submission')['testcases'])
    timelimit = (response.json().get('submission')['timelimit'])
    memorylimit = (response.json().get('submission')['memorylimit'])
    print(response.json().get("submission"))
    start_running(code, checker, testcases, timelimit, memorylimit, sub_id, enable)




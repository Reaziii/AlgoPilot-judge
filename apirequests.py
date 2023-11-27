import requests
import json
from status import status


def yes_i_am_free():
    print("Hey I have new job!!!!")

    # request for a submission
    auth_token = status.get("token")
    url = status["server"] + "/judge/"
    data = {"key1": "value1", "key2": "value2"}
    headers = {
        "Content-Type": "application/json",
        "authorization": f"{auth_token}",  # Include your authorization token here
    }
    response = requests.post(url, data=json.dumps(data), headers=headers)
    _status: bool = response.json().get("status")
    if _status is False:
        return

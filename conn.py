import socketio
from status import status
from serverstatus import is_processor_free
import requests 
from apirequests import yes_i_am_free
class Connection:
    sio = socketio.Client()
    connected = False
    def __init__(self, status: dict) -> None:
        if status.get("server"):
            self.server = status.get("server")
        else:
            print("No server found")
            return
        if status.get("token"):
            self.token = status.get("token")
        else:
            print("No token found")
            return

    def connect(self):
        try:
            # fetchurl = self.server+"/api/socket"
            # headers = {"Content-Type": "application/json"}
            # response = requests.get(fetchurl, headers=headers)
            # if response.status_code != 200:
            #     raise ""
            print("connecting...")
            #after connecting to the server ws
            @self.sio.on("connect")
            def on_connect():
                self.connected = True
                print("Connected to the server - ", self.server)
                self.sio.emit("judgelogin", self.token)

            # request to check if the server is free
            @self.sio.on("areyoufree")
            def checkfree(data):
                print("areyoufree")
                print(is_processor_free())
                if(is_processor_free()):
                    yes_i_am_free()


            # lets handle the disconnect too
            @self.sio.on("disconnect")
            def on_disconnect():
                print("server ws disconnected")
                self.connected = False
                self.connect()

            # now lets connect the server
            self.sio.connect(self.server)

            # need to wait
            self.sio.wait()
        except:
            print("Failed to connect to the server - ", self.server)



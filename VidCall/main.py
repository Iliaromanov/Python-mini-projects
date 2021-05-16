from vidstream import AudioSender, AudioReceiver, ScreenShareClient, CameraClient, StreamingServer
import tkinter as tk
import socket
import threading
import requests

local_ip_address = socket.gethostbyname(socket.gethostname()) # get users private ip address
public_ip_address = requests.get('https://api.ipify.org').text # use an API to get public ip address

# Server for audio is only created once (not every time audio stream button is clicked)
server = StreamingServer(local_ip_address, 9999) # Host server uses local ip
reciever = AudioReceiver(local_ip_address, 8888)

def start_listening():
    t1 = threading.Thread(target=server.start_server) # The start_server function is only called when thread started
    t2 = threading.Thread(target=reciever.start_server) # ^^^
    t1.start()
    t2.start()


# New server for video is created every time video stream button is pressed 
#   (could define variables outside of func like for audio to only do once)
def start_camera_stream():
    camera_client = CameraClient(text_target_ip.get(1.0, 'end-1c'), 7777)
    t = threading.Thread(target=camera_client.start_stream)
    t.start()


# New server for screen share is created every time screen share stream is pressed 
#   (could define variables outside of func like for audio to only do once)
def start_screen_share():
    screen_client = ScreenShareClient(text_target_ip.get(1.0, 'end-1c'), 7777)
    t = threading.Thread(target=screen_client.start_stream)
    t.start()


# New server for audio sream is created every time audio stream button is pressed 
#   (could define variables outside of func like for audio to only do once)
def start_audio_stream():
    audio_sender = AudioSender(text_target_ip.get(1.0, 'end-1c'), 6666)
    t = threading.Thread(target=audio_sender.start_stream)
    t.start()


# GUI
window = tk.Tk()
window.title("VidCall v0.0.1")
window.geometry('300x200')

label_target_ip = tk.Label(window, text="Target ip address:")
label_target_ip.pack()

text_target_ip = tk.Text(window, height=1) # textbox to enter ip address
text_target_ip.pack()

btn_listen = tk.Button(window, text="Start Listening", width=50, command=start_listening)
btn_listen.pack(anchor=tk.CENTER, expand=True)

btn_camera = tk.Button(window, text="Start Camera Stream", width=50, command=start_camera_stream)
btn_camera.pack(anchor=tk.CENTER, expand=True)

btn_screen = tk.Button(window, text="Start Screen Share", width=50, command=start_screen_share)
btn_screen.pack(anchor=tk.CENTER, expand=True)

btn_audio = tk.Button(window, text="Start Audio Stream", width=50, command=start_audio_stream)
btn_audio.pack(anchor=tk.CENTER, expand=True)

window.mainloop()

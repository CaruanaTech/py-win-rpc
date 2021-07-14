from pypresence import Presence
import time
from winutils import get_full_window, beautify_window_name


client_id = ""  # Enter your Application ID here.
wait_time = 15  # 15 is the fastest time for updates

RPC = Presence(client_id=client_id)
RPC.connect()

# get initial window name
current_window = beautify_window_name(get_full_window())

# image stuff
large_image = None
large_text = None
small_image = None
small_text = None

# general stuff
state = current_window['primary'] if current_window['primary'] else "no window open"
details = current_window['secondary'] if current_window['secondary'] else "N/A"

start = time.time()
buttons = [
    {"label": "Label1", "url": "http://www.loaf.wtf",},
    {"label": "Label2", "url": "http://www.loaf.wtf"}
]

# other/advanced stuff
party_id = None
party_size = None
join = None
spectate = None
match = None
pid = 0
instance = None

while True:
    
    # prepare for switch
    new_window = beautify_window_name(get_full_window())
    if new_window['primary'] != current_window['primary']:
        print(f"detected change in windows:\n'{new_window['primary']} is not {current_window['primary']}")
        start = time.time()

        state = new_window['primary'] if new_window['primary'] else "no window open"
        details = new_window['secondary'] if new_window['secondary'] else "N/A"
        current_window = new_window
    else:
        pass

    # perform update
    RPC.update(
        large_image=large_image, large_text=large_text, small_image=small_image, small_text=small_text,
        state=state, details=details, start=start, buttons=buttons, party_id=party_id, party_size=party_size,
        join=join, spectate=spectate, match=match, instance=instance, pid=0
    )
        
    time.sleep(wait_time) # Can only update presence every 15 seconds

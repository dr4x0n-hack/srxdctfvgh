from flask import Flask, request
from osint_hub import port_scan, subfinder, username_osint, exif_reader
import io, sys

app = Flask(__name__)

def capture(func, *args):
    buf = io.StringIO()
    sys.stdout = buf
    func(*args)
    sys.stdout = sys.__stdout__
    return buf.getvalue()

@app.post("/run")
def run():
    cmd = request.json["command"].split()
    if not cmd:
        return ""

    c = cmd[0]

    try:
        if c == "portscan":
            return capture(port_scan, cmd[1])

        if c == "subfinder":
            return capture(subfinder, cmd[1])

        if c == "username":
            return capture(username_osint, cmd[1])

        if c == "exif":
            return capture(exif_reader, cmd[1])

        if c == "help":
            return """
Available commands:
  portscan <ip>
  subfinder <domain>
  username <username>
  exif <image>
"""

        return "Unknown command. Type 'help'"
    except:
        return "Error executing command."

app.run(port=5000)

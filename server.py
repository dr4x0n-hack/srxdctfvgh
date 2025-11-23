from flask import Flask, request
from osint_hub import port_scan, subfinder, username_osint, exif_reader
import io
import sys

app = Flask(__name__)

def capture_output(func, *args):
    buffer = io.StringIO()
    sys.stdout = buffer
    func(*args)
    sys.stdout = sys.__stdout__
    return buffer.getvalue()

@app.post("/run")
def run():
    cmd = request.json.get("command")

    try:
        parts = cmd.split()
        command = parts[0]

        if command == "portscan":
            return capture_output(port_scan, parts[1])

        elif command == "subfinder":
            return capture_output(subfinder, parts[1])

        elif command == "username":
            return capture_output(username_osint, parts[1])

        elif command == "exif":
            return capture_output(exif_reader, parts[1])

        elif command == "help":
            return """
Hammasi:
  portscan <ip>
  subfinder <domain>
  username <username>
  exif <image.jpg>
"""

        else:
            return "Nomaʼlum buyruq"

    except Exception as e:
        return "Xatolik: " + str(e)

app.run(port=5000)

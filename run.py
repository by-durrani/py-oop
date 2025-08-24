# run.py
import sys
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class RestartHandler(FileSystemEventHandler):
    def __init__(self, command):
        self.command = command
        self.process = None
        self.restart()

    def restart(self):
        if self.process:
            self.process.terminate()
            self.process.wait()
        self.process = subprocess.Popen(self.command, shell=True)

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print(f"🔄 Restarting due to change in {event.src_path}")
            self.restart()

if __name__ == "__main__":
    path = "."
    handler = RestartHandler([sys.executable, "main.py"])
    observer = Observer()
    observer.schedule(handler, path=path, recursive=True)
    observer.start()
    print("👀 Watching for changes...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

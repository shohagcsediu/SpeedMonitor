import psutil
import tkinter as tk
from time import sleep
from threading import Thread


class NetSpeedMonitor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Internet Speed Monitor")
        self.geometry("200x100")
        self.configure(bg="black")
        
        # Make the window resizable
        self.resizable(True, True)

        # Labels to display download and upload speeds
        self.download_label = tk.Label(self, text="Download: 0 Mbps", font=("Arial", 12), fg="lime", bg="black")
        self.download_label.pack(pady=10, expand=True)
        self.upload_label = tk.Label(self, text="Upload: 0 Mbps", font=("Arial", 12), fg="cyan", bg="black")
        self.upload_label.pack(pady=10, expand=True)
        
        self.running = True
        self.update_speed()

    def update_speed(self):
        def monitor():
            old_net = psutil.net_io_counters()
            while self.running:
                sleep(1)
                new_net = psutil.net_io_counters()
                
                download_speed = (new_net.bytes_recv - old_net.bytes_recv) / (1024 * 1024) * 8  # Convert to Mbps
                upload_speed = (new_net.bytes_sent - old_net.bytes_sent) / (1024 * 1024) * 8  # Convert to Mbps
                
                self.download_label.config(text=f"Download: {download_speed:.2f} Mbps")
                self.upload_label.config(text=f"Upload: {upload_speed:.2f} Mbps")
                
                old_net = new_net

        Thread(target=monitor, daemon=True).start()


if __name__ == "__main__":
    app = NetSpeedMonitor()
    app.protocol("WM_DELETE_WINDOW", lambda: setattr(app, 'running', False) or app.destroy())
    app.mainloop()

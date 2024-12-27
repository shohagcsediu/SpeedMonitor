import psutil
import tkinter as tk
from time import sleep
from threading import Thread


class NetSpeedMonitor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Internet Speed Monitor")
        self.geometry("250x120")
        self.configure(bg="black")
        
        # Allow resizing
        self.resizable(True, True)

        # Create a container for rounded-corner effects
        self.container = tk.Frame(self, bg="black")
        self.container.pack(expand=True, fill="both", padx=10, pady=10)

        # Labels for download and upload speeds
        self.download_label = tk.Label(self.container, text="Download: 0 Mbps", font=("Arial", 14), fg="lime", bg="black")
        self.download_label.pack(pady=5, fill="x", expand=True)
        self.upload_label = tk.Label(self.container, text="Upload: 0 Mbps", font=("Arial", 14), fg="cyan", bg="black")
        self.upload_label.pack(pady=5, fill="x", expand=True)

        # Button to toggle pinning window on top
        self.pin_button = tk.Button(self.container, text="Pin on Top", command=self.toggle_pin)
        self.pin_button.pack(pady=5)

        # Enable dragging
        self.bind("<Button-1>", self.start_drag)
        self.bind("<B1-Motion>", self.do_drag)

        self.running = True
        self.is_pinned = False  # Flag to track if the window is pinned
        self.update_speed()

    # Start dragging
    def start_drag(self, event):
        self._drag_x = event.x
        self._drag_y = event.y

    # Perform dragging
    def do_drag(self, event):
        x = self.winfo_x() + (event.x - self._drag_x)
        y = self.winfo_y() + (event.y - self._drag_y)
        self.geometry(f"+{x}+{y}")

    # Update internet speed
    def update_speed(self):
        def monitor():
            old_net = psutil.net_io_counters()
            while self.running:
                sleep(1)
                new_net = psutil.net_io_counters()

                download_speed = (new_net.bytes_recv - old_net.bytes_recv) / (1024 * 1024) * 8  # Mbps
                upload_speed = (new_net.bytes_sent - old_net.bytes_sent) / (1024 * 1024) * 8  # Mbps

                self.download_label.config(text=f"Download: {download_speed:.2f} Mbps")
                self.upload_label.config(text=f"Upload: {upload_speed:.2f} Mbps")

                old_net = new_net

        Thread(target=monitor, daemon=True).start()

    # Toggle pinning window on top
    def toggle_pin(self):
        if self.is_pinned:
            self.attributes("-topmost", 0)  # Remove topmost attribute
            self.is_pinned = False
            self.pin_button.config(text="Pin on Top")
        else:
            self.attributes("-topmost", 1)  # Set topmost attribute
            self.is_pinned = True
            self.pin_button.config(text="Unpin from Top")


if __name__ == "__main__":
    app = NetSpeedMonitor()
    app.protocol("WM_DELETE_WINDOW", lambda: setattr(app, 'running', False) or app.destroy())
    app.mainloop()

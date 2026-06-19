import customtkinter as ctk
from tkinter import messagebox
import threading
import datetime

from config import CREATOR_NAME


class InstagramUI:

    def __init__(self):

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()

        self.root.geometry("900x650")
        self.root.title(
            f"Instagram Auto Poster - {CREATOR_NAME}"
        )

        self.build_ui()

    def build_ui(self):

        title = ctk.CTkLabel(
            self.root,
            text="🚀 Instagram Reel Automation",
            font=("Poppins", 30, "bold")
        )

        title.pack(pady=20)

        self.caption_box = ctk.CTkTextbox(
            self.root,
            width=700,
            height=150
        )

        self.caption_box.pack(pady=20)

        self.caption_box.insert(
            "1.0",
            "Daily Reel by Shaurya 🔥"
        )

        self.status = ctk.CTkLabel(
            self.root,
            text="Ready",
            font=("Arial", 16)
        )

        self.status.pack(pady=10)

        upload_btn = ctk.CTkButton(
            self.root,
            text="Upload Now",
            width=220,
            height=50,
            command=self.manual_upload
        )

        upload_btn.pack(pady=10)

        start_btn = ctk.CTkButton(
            self.root,
            text="Start 24 Hour Scheduler",
            width=220,
            height=50,
            command=self.start_scheduler
        )

        start_btn.pack(pady=10)

        self.logs = ctk.CTkTextbox(
            self.root,
            width=750,
            height=220
        )

        self.logs.pack(pady=20)

    def log(self, message):

        timestamp = datetime.datetime.now()

        self.logs.insert(
            "end",
            f"[{timestamp}] {message}\n"
        )

    def manual_upload(self):

        self.log("Upload Started")

        # upload code here

        self.log("Upload Finished")

        messagebox.showinfo(
            "Success",
            "Reel Uploaded Successfully"
        )

    def start_scheduler(self):

        self.log(
            "24 Hour Auto Posting Enabled"
        )

        threading.Thread(
            target=self.scheduler_thread,
            daemon=True
        ).start()

    def scheduler_thread(self):

        while True:
            pass

    def run(self):

        self.root.mainloop()


if __name__ == "__main__":

    app = InstagramUI()
    app.run()

import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
from core.organizer import organize_folder


class QuickSortApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QuickSort")
        self.root.geometry("520x300")
        self.root.resizable(False, False)
        self.root.configure(bg="#F7F7F7")

        self.folder_path = None
        self.selected_path = tk.StringVar(value="No folder selected")
        self.status = tk.StringVar(value="Ready")

        self._build_ui()

    def _build_ui(self):
        title = tk.Label(
            self.root,
            text="QuickSort",
            font=("Helvetica", 22, "bold"),
            bg="#F7F7F7",
            fg="#222222"
        )
        title.pack(pady=(22, 4))

        tagline = tk.Label(
            self.root,
            text="Organize your files in one click",
            font=("Helvetica", 11),
            bg="#F7F7F7",
            fg="#555555"
        )
        tagline.pack(pady=(0, 18))

        description = tk.Label(
            self.root,
            text="Select a folder like Downloads or Desktop.\n"
                 "Files will be neatly organized into folders.",
            font=("Helvetica", 10),
            bg="#F7F7F7",
            fg="#333333",
            justify="center"
        )
        description.pack(pady=(0, 16))

        path_label = tk.Label(
            self.root,
            textvariable=self.selected_path,
            font=("Helvetica", 9),
            bg="#F7F7F7",
            fg="#666666",
            wraplength=460
        )
        path_label.pack(pady=(0, 16))

        button_frame = tk.Frame(self.root, bg="#F7F7F7")
        button_frame.pack(pady=8)

        self.choose_button = tk.Button(
            button_frame,
            text="Choose Folder",
            width=16,
            command=self.choose_folder
        )
        self.choose_button.grid(row=0, column=0, padx=8)

        self.organize_button = tk.Button(
            button_frame,
            text="Organize Files",
            width=16,
            bg="#4A90E2",
            fg="white",
            activebackground="#357ABD",
            activeforeground="white",
            command=self.organize_files,
            state="disabled"
        )
        self.organize_button.grid(row=0, column=1, padx=8)

        status_label = tk.Label(
            self.root,
            textvariable=self.status,
            font=("Helvetica", 9),
            bg="#F7F7F7",
            fg="#777777"
        )
        status_label.pack(side="bottom", pady=14)

    def choose_folder(self):
        path = filedialog.askdirectory()
        if not path:
            return

        self.folder_path = path
        self.selected_path.set(path)
        self.organize_button.config(state="normal")
        self.status.set("Folder selected. Ready to organize.")

    def _count_files(self, folder):
        return sum(1 for p in Path(folder).iterdir() if p.is_file())

    def _count_dirs(self, folder):
        return sum(1 for p in Path(folder).iterdir() if p.is_dir())

    def organize_files(self):
        try:
            before_files = self._count_files(self.folder_path)
            before_dirs = self._count_dirs(self.folder_path)

            self.status.set("Organizing files...")
            self.root.update_idletasks()

            organize_folder(self.folder_path)

            after_files = self._count_files(self.folder_path)
            after_dirs = self._count_dirs(self.folder_path)

            moved = before_files - after_files
            created = max(0, after_dirs - before_dirs)

            self.status.set("Done")

            messagebox.showinfo(
                "QuickSort",
                f"Files organized successfully.\n\n"
                f"• Files moved: {moved}\n"
                f"• Folders created: {created}"
            )

        except Exception as e:
            self.status.set("Error")
            messagebox.showerror("QuickSort", str(e))


def main():
    root = tk.Tk()
    QuickSortApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
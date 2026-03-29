import os
import shutil
import customtkinter as ctk
from tkinter import filedialog, messagebox

ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class FileSorterApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("File Sorter")
        self.geometry("500x300")
        self.resizable(False, False)

        # Create widgets
        self.label = ctk.CTkLabel(self, text="Select a folder to sort files by extension", font=ctk.CTkFont(size=16, weight="bold"))
        self.label.pack(pady=20)

        self.select_button = ctk.CTkButton(self, text="Select Folder", command=self.select_folder, font=ctk.CTkFont(size=14))
        self.select_button.pack(pady=10)

        self.folder_label = ctk.CTkLabel(self, text="No folder selected", font=ctk.CTkFont(size=12))
        self.folder_label.pack(pady=10)

        self.sort_button = ctk.CTkButton(self, text="Sort Files", command=self.sort_files, state="disabled", font=ctk.CTkFont(size=14))
        self.sort_button.pack(pady=10)

        self.status_label = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=12))
        self.status_label.pack(pady=10)

        self.folder_path = None

    def select_folder(self):
        folder = filedialog.askdirectory(title="Select Folder to Sort")
        if folder:
            self.folder_path = folder
            self.folder_label.configure(text=f"Selected: {os.path.basename(folder)}")
            self.sort_button.configure(state="normal")
            self.status_label.configure(text="")

    def sort_files(self):
        if not self.folder_path:
            messagebox.showerror("Error", "No folder selected!")
            return

        try:
            self.sort_files_by_extension(self.folder_path)
            self.status_label.configure(text="Sorting complete!", text_color="green")
            messagebox.showinfo("Success", "Files sorted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def sort_files_by_extension(self, folder_path):
        """
        Scans the given folder, groups files by their extensions,
        creates subfolders for each extension, and moves files accordingly.
        Ignores subdirectories and files without extensions.
        """
        # Dictionary to hold files grouped by extension
        files_by_ext = {}

        # List all items in the folder
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            # Only process files, not directories
            if os.path.isfile(item_path):
                # Get file extension (lowercase for consistency)
                _, ext = os.path.splitext(item)
                ext = ext.lower()
                if ext:  # Only if there's an extension
                    if ext not in files_by_ext:
                        files_by_ext[ext] = []
                    files_by_ext[ext].append(item)

        # Create subfolders and move files
        for ext, files in files_by_ext.items():
            # Create subfolder name (e.g., 'pdf' for .pdf files)
            subfolder_name = ext[1:]  # Remove the leading dot
            subfolder_path = os.path.join(folder_path, subfolder_name)
            # Create subfolder if it doesn't exist
            os.makedirs(subfolder_path, exist_ok=True)
            # Move each file to the subfolder
            for file in files:
                src = os.path.join(folder_path, file)
                dst = os.path.join(subfolder_path, file)
                shutil.move(src, dst)

if __name__ == "__main__":
    app = FileSorterApp()
    app.mainloop()

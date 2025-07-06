import os
import sys
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

from config_agent import ConfigAgent
from frame_loader import FrameLoader
from flf2v_interpolator import FLF2VInterpolator
from video_stitcher import VideoStitcher


class GUIController:
    """Minimal Tkinter GUI for FLF2V generation."""

    def __init__(self, config: ConfigAgent):
        self.config = config
        self.root = tk.Tk()
        self.root.title("FLF2V Generator")

        self.paths: list[str] = []
        self.status_var = tk.StringVar(value="Select 3 keyframes")

        self.select_btn = tk.Button(self.root, text="Select Frames", command=self.select_files)
        self.select_btn.pack(padx=10, pady=5)

        self.generate_btn = tk.Button(self.root, text="Generate Video", command=self.generate)
        self.generate_btn.pack(padx=10, pady=5)

        self.preview_btn = tk.Button(self.root, text="Preview Video", command=self.preview, state=tk.DISABLED)
        self.preview_btn.pack(padx=10, pady=5)

        tk.Label(self.root, textvariable=self.status_var).pack(pady=5)

    def select_files(self):
        paths = filedialog.askopenfilenames(
            title="Select exactly 3 keyframes",
            filetypes=[("PNG images", "*.png")],
        )
        if len(paths) != 3:
            messagebox.showerror("Error", "Please select exactly three images")
            return
        self.paths = list(paths)
        self.status_var.set("Selected files: " + ", ".join(os.path.basename(p) for p in self.paths))

    def generate(self):
        if len(self.paths) != 3:
            messagebox.showerror("Error", "Please select three images first")
            return
        try:
            self.status_var.set("Loading frames...")
            self.root.update_idletasks()
            frames = FrameLoader.load_frames(self.paths)

            self.status_var.set("Interpolating...")
            self.root.update_idletasks()
            interpolator = FLF2VInterpolator()
            clips = interpolator.interpolate(frames, self.config.get_frame_rate())

            self.status_var.set("Stitching video...")
            self.root.update_idletasks()
            stitcher = VideoStitcher(codec=self.config.get_video_codec())
            output = stitcher.stitch(clips, self.config.get_output_path(), self.config.get_frame_rate())

            self.status_var.set(f"Video saved to {output}")
            self.preview_btn.config(state=tk.NORMAL)
        except Exception as exc:
            messagebox.showerror("Error", str(exc))
            self.status_var.set("Generation failed")

    def preview(self):
        path = self.config.get_output_path()
        if os.path.exists(path):
            try:
                if os.name == "nt":
                    os.startfile(path)  # type: ignore[attr-defined]
                elif sys.platform == "darwin":
                    subprocess.run(["open", path], check=False)
                else:
                    subprocess.run(["xdg-open", path], check=False)
            except Exception as exc:
                messagebox.showerror("Error", str(exc))
        else:
            messagebox.showerror("Error", "Output file not found")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    cfg = ConfigAgent()
    GUIController(cfg).run()

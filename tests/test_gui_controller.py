import os
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from gui_controller import GUIController


class DummyConfig:
    def __init__(self, path):
        self.path = path
    def get_output_path(self):
        return self.path


class TestGUIControllerPreview(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.path = os.path.join(self.tmpdir.name, "out.mp4")
        with open(self.path, "w", encoding="utf-8"):
            pass
        self.cfg = DummyConfig(self.path)

    def tearDown(self):
        self.tmpdir.cleanup()

    def create_controller(self):
        gui = GUIController.__new__(GUIController)
        gui.config = self.cfg
        return gui

    @patch("tkinter.messagebox.showerror")
    def test_preview_windows_uses_startfile(self, mock_error):
        gui = self.create_controller()
        with patch("os.name", "nt"), patch("os.startfile", create=True) as start:
            gui.preview()
            start.assert_called_with(self.path)
            mock_error.assert_not_called()

    @patch("tkinter.messagebox.showerror")
    def test_preview_linux_uses_xdg_open(self, mock_error):
        gui = self.create_controller()
        with patch("os.name", "posix"), patch("sys.platform", "linux"), \
             patch("subprocess.run") as run:
            gui.preview()
            run.assert_called_with(["xdg-open", self.path], check=False)
            mock_error.assert_not_called()


if __name__ == "__main__":
    unittest.main()

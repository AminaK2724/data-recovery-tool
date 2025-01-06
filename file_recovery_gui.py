from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog, QVBoxLayout, QLineEdit
from file_recovery import recover_files
from file_scanner import read_raw_data, find_files

class FileRecoveryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("Select a disk or type a path:")
        layout.addWidget(self.label)

        self.path_input = QLineEdit(self)
        self.path_input.setPlaceholderText("Enter disk path (e.g., /dev/rdisk4)")
        layout.addWidget(self.path_input)

        self.select_button = QPushButton("Select Image File")
        self.select_button.clicked.connect(self.select_image)
        layout.addWidget(self.select_button)

        self.scan_button = QPushButton("Scan & Recover")
        self.scan_button.clicked.connect(self.scan_manual_path)
        layout.addWidget(self.scan_button)

        self.setLayout(layout)

    def select_image(self):
        image, _ = QFileDialog.getOpenFileName(self, "Select Disk Image", "/", "All Files (*)")
        if image:
            self.path_input.setText(image)

    def scan_manual_path(self):
        self.selected_image = self.path_input.text()
        if self.selected_image:
            raw_data = read_raw_data(self.selected_image)
            found_files = find_files(raw_data)
            recover_files(self.selected_image, found_files)
            self.label.setText("Recovery Complete!")
        else:
            self.label.setText("No disk selected!")

app = QApplication([])
window = FileRecoveryApp()
window.show()
app.exec_()

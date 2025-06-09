from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QColorDialog, QVBoxLayout,
    QHBoxLayout, QComboBox, QLineEdit, QCheckBox, QSlider, QFileDialog, QFontComboBox,
    QSpinBox, QTextEdit, QSplitter
)
from PyQt6.QtGui import (
    QColor, QFont, QPainter, QPen, QBrush, QFontDatabase, QPixmap, QPainterPath
)
from PyQt6.QtCore import Qt, QRect, QRectF
import sys
import os


class ColorPickerGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Selene Color Scheme Designer")
        self.setGeometry(100, 100, 1200, 900)
        self.setFixedSize(1200, 900)

        # Main colors
        self.bg_color = QColor(10, 10, 30, 190)
        self.fg_color = QColor(0, 255, 255, 60)
        self.text_color = QColor(255, 255, 255, 255)
        
        # Dropdown colors
        self.dd_selected_bg_color = QColor(40, 40, 60, 220)  # Selected item background
        self.dd_selected_text_color = QColor(255, 255, 255, 255)  # Selected item text
        self.dd_menu_bg_color = QColor(20, 20, 40, 240)  # Dropdown menu background
        self.dd_menu_text_color = QColor(200, 200, 200, 255)  # Dropdown menu text
        self.dd_highlight_color = QColor(0, 255, 255, 180)  # Hover highlight

        # Effects
        self.glow_enabled = False
        self.glow_color = QColor(0, 255, 255, 128)
        self.glow_radius = 10
        self.opacity = 255

        self.font_path = "gui/fonts/"
        self.load_custom_fonts()

        self.init_ui()

    def load_custom_fonts(self):
        if os.path.exists(self.font_path):
            for file in os.listdir(self.font_path):
                if file.lower().endswith(".ttf"):
                    QFontDatabase.addApplicationFont(os.path.join(self.font_path, file))

    def init_ui(self):
        layout = QVBoxLayout()

        # Color Pickers Row 1
        color_layout1 = QHBoxLayout()
        self.bg_button = QPushButton("Background")
        self.bg_button.clicked.connect(lambda: self.choose_color('bg'))
        self.fg_button = QPushButton("Foreground")
        self.fg_button.clicked.connect(lambda: self.choose_color('fg'))
        self.txt_button = QPushButton("Text")
        self.txt_button.clicked.connect(lambda: self.choose_color('text'))
        self.glow_button = QPushButton("Glow Color")
        self.glow_button.clicked.connect(lambda: self.choose_color('glow'))

        color_layout1.addWidget(self.bg_button)
        color_layout1.addWidget(self.fg_button)
        color_layout1.addWidget(self.txt_button)
        color_layout1.addWidget(self.glow_button)
        layout.addLayout(color_layout1)

        # Color Pickers Row 2 (Dropdown colors)
        color_layout2 = QHBoxLayout()
        self.dd_selected_bg_button = QPushButton("DD Selected BG")
        self.dd_selected_bg_button.clicked.connect(lambda: self.choose_color('dd_selected_bg'))
        self.dd_selected_text_button = QPushButton("DD Selected Text")
        self.dd_selected_text_button.clicked.connect(lambda: self.choose_color('dd_selected_text'))
        self.dd_menu_bg_button = QPushButton("DD Menu BG")
        self.dd_menu_bg_button.clicked.connect(lambda: self.choose_color('dd_menu_bg'))
        self.dd_menu_text_button = QPushButton("DD Menu Text")
        self.dd_menu_text_button.clicked.connect(lambda: self.choose_color('dd_menu_text'))
        self.dd_highlight_button = QPushButton("DD Highlight")
        self.dd_highlight_button.clicked.connect(lambda: self.choose_color('dd_highlight'))

        color_layout2.addWidget(self.dd_selected_bg_button)
        color_layout2.addWidget(self.dd_selected_text_button)
        color_layout2.addWidget(self.dd_menu_bg_button)
        color_layout2.addWidget(self.dd_menu_text_button)
        color_layout2.addWidget(self.dd_highlight_button)
        layout.addLayout(color_layout2)

        # Font and text input
        font_layout = QHBoxLayout()
        self.font_select = QFontComboBox()
        self.font_select.setFixedWidth(200)
        self.font_select.setCurrentFont(QFont("Arial"))
        
        self.font_size_spin = QSpinBox()
        self.font_size_spin.setRange(8, 72)
        self.font_size_spin.setValue(20)
        self.font_size_spin.setSuffix(" pt")
        
        self.text_input = QLineEdit("Sample Text")
        self.text_input.setMaxLength(25)
        
        font_layout.addWidget(QLabel("Font:"))
        font_layout.addWidget(self.font_select)
        font_layout.addWidget(QLabel("Size:"))
        font_layout.addWidget(self.font_size_spin)
        font_layout.addWidget(QLabel("Text:"))
        font_layout.addWidget(self.text_input)
        layout.addLayout(font_layout)

        # Dropdown Sample
        dd_layout = QHBoxLayout()
        self.combo = QComboBox()
        self.combo.addItems(["Select", "one", "TWO", "tHr33"])
        dd_layout.addWidget(QLabel("Dropdown:"))
        dd_layout.addWidget(self.combo)
        layout.addLayout(dd_layout)

        # Text effect toggles
        effect_layout = QHBoxLayout()
        self.bold_cb = QCheckBox("Bold")
        self.italic_cb = QCheckBox("Italic")
        self.underline_cb = QCheckBox("Underline")
        self.strike_cb = QCheckBox("Strike-through")
        self.glow_cb = QCheckBox("Glow Effect")
        effect_layout.addWidget(self.bold_cb)
        effect_layout.addWidget(self.italic_cb)
        effect_layout.addWidget(self.underline_cb)
        effect_layout.addWidget(self.strike_cb)
        effect_layout.addWidget(self.glow_cb)
        layout.addLayout(effect_layout)

        # Sliders
        slider_layout = QHBoxLayout()
        
        # Opacity slider
        opacity_layout = QVBoxLayout()
        opacity_layout.addWidget(QLabel("Opacity:"))
        self.opacity_slider = QSlider(Qt.Orientation.Horizontal)
        self.opacity_slider.setRange(0, 255)
        self.opacity_slider.setValue(255)
        self.opacity_label = QLabel("255")
        opacity_layout.addWidget(self.opacity_slider)
        opacity_layout.addWidget(self.opacity_label)
        
        # Glow radius slider
        glow_layout = QVBoxLayout()
        glow_layout.addWidget(QLabel("Glow Radius:"))
        self.glow_slider = QSlider(Qt.Orientation.Horizontal)
        self.glow_slider.setRange(0, 30)
        self.glow_slider.setValue(10)
        self.glow_radius_label = QLabel("10")
        glow_layout.addWidget(self.glow_slider)
        glow_layout.addWidget(self.glow_radius_label)
        
        slider_layout.addLayout(opacity_layout)
        slider_layout.addLayout(glow_layout)
        layout.addLayout(slider_layout)

        # Create splitter for display and code
        splitter = QSplitter(Qt.Orientation.Vertical)
        
        # Sample Display
        self.display = QLabel()
        self.display.setMinimumHeight(300)
        self.display.setFixedSize(1150, 300)
        self.display.setStyleSheet("border: 2px solid #00ffff;")
        splitter.addWidget(self.display)

        # Code Display
        self.code_display = QTextEdit()
        self.code_display.setMinimumHeight(200)
        self.code_display.setMaximumHeight(200)
        self.code_display.setReadOnly(True)
        self.code_display.setStyleSheet("""
            QTextEdit {
                background-color: #1a1a1a;
                color: #00ff00;
                font-family: 'Consolas', 'Monaco', monospace;
                font-size: 10pt;
                border: 2px solid #00ffff;
                padding: 8px;
            }
        """)
        splitter.addWidget(self.code_display)
        
        layout.addWidget(splitter)
        self.setLayout(layout)
        
        # Connect signals AFTER widgets are created
        self.font_select.currentFontChanged.connect(self.update_display)
        self.font_size_spin.valueChanged.connect(self.update_display)
        self.text_input.textChanged.connect(self.update_display)
        self.combo.currentIndexChanged.connect(self.update_display)
        self.bold_cb.stateChanged.connect(self.update_display)
        self.italic_cb.stateChanged.connect(self.update_display)
        self.underline_cb.stateChanged.connect(self.update_display)
        self.strike_cb.stateChanged.connect(self.update_display)
        self.glow_cb.stateChanged.connect(self.update_display)
        self.opacity_slider.valueChanged.connect(self.on_opacity_changed)
        self.glow_slider.valueChanged.connect(self.on_glow_changed)

        # Update display after everything is set up
        self.update_display()
        self.update_combo_style()

    def on_opacity_changed(self, value):
        self.opacity = value
        self.opacity_label.setText(str(value))
        self.update_display()

    def on_glow_changed(self, value):
        self.glow_radius = value
        self.glow_radius_label.setText(str(value))
        self.update_display()

    def choose_color(self, which):
        color = QColorDialog.getColor()
        if color.isValid():
            if which == 'bg':
                self.bg_color = color
            elif which == 'fg':
                self.fg_color = color
            elif which == 'text':
                self.text_color = color
            elif which == 'glow':
                self.glow_color = color
            elif which == 'dd_selected_bg':
                self.dd_selected_bg_color = color
            elif which == 'dd_selected_text':
                self.dd_selected_text_color = color
            elif which == 'dd_menu_bg':
                self.dd_menu_bg_color = color
            elif which == 'dd_menu_text':
                self.dd_menu_text_color = color
            elif which == 'dd_highlight':
                self.dd_highlight_color = color
            self.update_display()
            self.update_combo_style()

    def update_combo_style(self):
        """Enhanced combo box styling with proper color separation"""
        self.combo.setStyleSheet(f"""
            QComboBox {{
                background-color: rgba({self.dd_selected_bg_color.red()}, {self.dd_selected_bg_color.green()}, {self.dd_selected_bg_color.blue()}, {self.dd_selected_bg_color.alpha()});
                color: rgba({self.dd_selected_text_color.red()}, {self.dd_selected_text_color.green()}, {self.dd_selected_text_color.blue()}, {self.dd_selected_text_color.alpha()});
                border: 2px solid #00ffff;
                padding: 6px;
                border-radius: 3px;
                font-size: 14px;
                selection-background-color: rgba({self.dd_highlight_color.red()}, {self.dd_highlight_color.green()}, {self.dd_highlight_color.blue()}, {self.dd_highlight_color.alpha()});
            }}
            QComboBox::drop-down {{
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-left-width: 1px;
                border-left-color: #00ffff;
                border-left-style: solid;
                border-top-right-radius: 3px;
                border-bottom-right-radius: 3px;
                background-color: rgba({self.dd_selected_bg_color.red()}, {self.dd_selected_bg_color.green()}, {self.dd_selected_bg_color.blue()}, {self.dd_selected_bg_color.alpha()});
            }}
            QComboBox::down-arrow {{
                image: none;
                border-left: 4px solid transparent;
                border-right: 4px solid transparent;
                border-top: 4px solid rgba({self.dd_selected_text_color.red()}, {self.dd_selected_text_color.green()}, {self.dd_selected_text_color.blue()}, {self.dd_selected_text_color.alpha()});
                margin: 0px;
            }}
            QComboBox QAbstractItemView {{
                background-color: rgba({self.dd_menu_bg_color.red()}, {self.dd_menu_bg_color.green()}, {self.dd_menu_bg_color.blue()}, {self.dd_menu_bg_color.alpha()});
                color: rgba({self.dd_menu_text_color.red()}, {self.dd_menu_text_color.green()}, {self.dd_menu_text_color.blue()}, {self.dd_menu_text_color.alpha()});
                border: 2px solid #00ffff;
                selection-background-color: rgba({self.dd_highlight_color.red()}, {self.dd_highlight_color.green()}, {self.dd_highlight_color.blue()}, {self.dd_highlight_color.alpha()});
                selection-color: rgba({self.dd_selected_text_color.red()}, {self.dd_selected_text_color.green()}, {self.dd_selected_text_color.blue()}, {self.dd_selected_text_color.alpha()});
                outline: none;
            }}
            QComboBox QAbstractItemView::item {{
                padding: 4px;
                border: none;
            }}
            QComboBox QAbstractItemView::item:hover {{
                background-color: rgba({self.dd_highlight_color.red()}, {self.dd_highlight_color.green()}, {self.dd_highlight_color.blue()}, {self.dd_highlight_color.alpha()});
                color: rgba({self.dd_selected_text_color.red()}, {self.dd_selected_text_color.green()}, {self.dd_selected_text_color.blue()}, {self.dd_selected_text_color.alpha()});
            }}
        """)

    def draw_glow_text(self, painter, rect, text, font, text_color, glow_color, glow_radius):
        """Draw text with proper glow effect around the font"""
        if glow_radius > 0:
            # Create text path for glow effect
            path = QPainterPath()
            path.addText(rect.center().x() - rect.width() // 4, rect.center().y() + rect.height() // 6, font, text)
            
            # Draw multiple glow layers with decreasing opacity and increasing size
            for i in range(glow_radius, 0, -1):
                glow_alpha = int(glow_color.alpha() * (glow_radius - i + 1) / glow_radius / 2)
                temp_glow = QColor(glow_color.red(), glow_color.green(), glow_color.blue(), glow_alpha)
                
                # Create pen with thickness for glow
                glow_pen = QPen(temp_glow, i * 2)
                glow_pen.setCapStyle(Qt.PenCapStyle.RoundCap)
                glow_pen.setJoinStyle(Qt.PenJoinStyle.RoundJoin)
                
                painter.setPen(glow_pen)
                painter.setBrush(Qt.BrushStyle.NoBrush)
                painter.drawPath(path)
        
        # Draw main text on top
        painter.setPen(QPen(text_color))
        painter.setBrush(QBrush(text_color))
        painter.setFont(font)
        painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, text)

    def generate_code_output(self):
        """Generate code representation of current settings"""
        code = "# Color Configuration\n"
        code += f"bg_color = QColor({self.bg_color.red()}, {self.bg_color.green()}, {self.bg_color.blue()}, {self.bg_color.alpha()})\n"
        code += f"fg_color = QColor({self.fg_color.red()}, {self.fg_color.green()}, {self.fg_color.blue()}, {self.fg_color.alpha()})\n"
        code += f"text_color = QColor({self.text_color.red()}, {self.text_color.green()}, {self.text_color.blue()}, {self.text_color.alpha()})\n"
        
        if self.glow_cb.isChecked():
            code += f"glow_color = QColor({self.glow_color.red()}, {self.glow_color.green()}, {self.glow_color.blue()}, {self.glow_color.alpha()})\n"
            code += f"glow_radius = {self.glow_radius}\n"
        
        code += "\n# Dropdown Colors\n"
        code += f"dd_selected_bg = QColor({self.dd_selected_bg_color.red()}, {self.dd_selected_bg_color.green()}, {self.dd_selected_bg_color.blue()}, {self.dd_selected_bg_color.alpha()})\n"
        code += f"dd_selected_text = QColor({self.dd_selected_text_color.red()}, {self.dd_selected_text_color.green()}, {self.dd_selected_text_color.blue()}, {self.dd_selected_text_color.alpha()})\n"
        code += f"dd_menu_bg = QColor({self.dd_menu_bg_color.red()}, {self.dd_menu_bg_color.green()}, {self.dd_menu_bg_color.blue()}, {self.dd_menu_bg_color.alpha()})\n"
        code += f"dd_menu_text = QColor({self.dd_menu_text_color.red()}, {self.dd_menu_text_color.green()}, {self.dd_menu_text_color.blue()}, {self.dd_menu_text_color.alpha()})\n"
        code += f"dd_highlight = QColor({self.dd_highlight_color.red()}, {self.dd_highlight_color.green()}, {self.dd_highlight_color.blue()}, {self.dd_highlight_color.alpha()})\n"
        
        code += "\n# Font Settings\n"
        code += f"font_family = '{self.font_select.currentFont().family()}'\n"
        code += f"font_size = {self.font_size_spin.value()}\n"
        code += f"font_bold = {self.bold_cb.isChecked()}\n"
        code += f"font_italic = {self.italic_cb.isChecked()}\n"
        code += f"font_underline = {self.underline_cb.isChecked()}\n"
        code += f"font_strikeout = {self.strike_cb.isChecked()}\n"
        
        code += "\n# Effects\n"
        code += f"glow_enabled = {self.glow_cb.isChecked()}\n"
        code += f"opacity = {self.opacity}\n"
        
        code += "\n# CSS/StyleSheet Equivalent\n"
        code += f'background: rgba({self.bg_color.red()}, {self.bg_color.green()}, {self.bg_color.blue()}, {self.bg_color.alpha()/255:.2f});\n'
        code += f'color: rgba({self.text_color.red()}, {self.text_color.green()}, {self.text_color.blue()}, {self.text_color.alpha()/255:.2f});\n'
        code += f'font: {self.font_size_spin.value()}pt "{self.font_select.currentFont().family()}";\n'
        
        if self.glow_cb.isChecked():
            code += f'text-shadow: 0 0 {self.glow_radius}px rgba({self.glow_color.red()}, {self.glow_color.green()}, {self.glow_color.blue()}, {self.glow_color.alpha()/255:.2f});\n'
        
        return code

    def update_display(self):
        """Enhanced update_display method with proper glow effects"""
        # Get dimensions
        width = 1150
        height = 300
        
        # Create a valid pixmap
        pixmap = QPixmap(width, height)
        if pixmap.isNull():
            print("Failed to create pixmap")
            return
            
        # Fill with transparent background first
        pixmap.fill(Qt.GlobalColor.transparent)

        # Create painter and check if it's valid
        painter = QPainter(pixmap)
        if not painter.isActive():
            print("Failed to activate painter")
            painter.end()
            return

        try:
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            painter.setRenderHint(QPainter.RenderHint.TextAntialiasing)
            
            # Background with opacity
            bg_color_with_opacity = QColor(self.bg_color.red(), self.bg_color.green(), self.bg_color.blue(), self.opacity)
            rect = QRect(0, 0, width, height)
            painter.fillRect(rect, bg_color_with_opacity)
            
            # Chat bubble rectangle with opacity
            fg_color_with_opacity = QColor(self.fg_color.red(), self.fg_color.green(), self.fg_color.blue(), self.opacity)
            chat_rect = QRect(50, 75, width - 100, 150)
            painter.fillRect(chat_rect, fg_color_with_opacity)
            
            # Font setup
            font = self.font_select.currentFont()
            font.setPointSize(self.font_size_spin.value())
            if self.bold_cb.isChecked():
                font.setBold(True)
            if self.italic_cb.isChecked():
                font.setItalic(True)
            if self.underline_cb.isChecked():
                font.setUnderline(True)
            if self.strike_cb.isChecked():
                font.setStrikeOut(True)
            
            sample_text = self.text_input.text()
            text_color_with_opacity = QColor(self.text_color.red(), self.text_color.green(), self.text_color.blue(), self.opacity)
            
            # Draw text with or without glow
            if self.glow_cb.isChecked():
                self.draw_glow_text(painter, chat_rect, sample_text, font, text_color_with_opacity, self.glow_color, self.glow_radius)
            else:
                painter.setFont(font)
                painter.setPen(QPen(text_color_with_opacity))
                painter.drawText(chat_rect, Qt.AlignmentFlag.AlignCenter, sample_text)
            
        except Exception as e:
            print(f"Painting error: {e}")
        finally:
            painter.end()

        # Set the pixmap to the label
        self.display.setPixmap(pixmap)
        
        # Update code display
        self.code_display.setPlainText(self.generate_code_output())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ColorPickerGUI()
    window.show()
    sys.exit(app.exec())
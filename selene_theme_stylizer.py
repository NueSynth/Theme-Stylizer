from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QColorDialog, QVBoxLayout,
    QHBoxLayout, QComboBox, QLineEdit, QCheckBox, QSlider, QFontComboBox,
    QSpinBox, QTextEdit, QSplitter
)
from PyQt6.QtGui import (
    QColor, QFont, QPainter, QPen, QBrush, QFontDatabase, QPixmap, QPainterPath
)
from PyQt6.QtCore import Qt, QRect
import sys
import os
import logging
from typing import Optional

# Constants
WINDOW_TITLE = "Selene Theme Stylize"   # Title of the main window
WINDOW_WIDTH = 1200 # Width of the main window
WINDOW_HEIGHT = 900 # Height of the main window
DISPLAY_WIDTH = 1150    # Width of the display area
DISPLAY_HEIGHT = 300    # Height of the display area
FONT_PATH = os.path.join("gui", "fonts")    # Path to custom fonts directory

# Configure logging
logging.basicConfig(level=logging.INFO)     
logger = logging.getLogger(__name__)        


class ColorPickerGUI(QWidget):      
    """
    Main GUI for the color and font scheme designer.    
    
    This tool leverages PyQt6 to allow users to visually select colors,
    fonts, and text effects, generate configuration code and style sheets.
    """
    def __init__(self) -> None:
        super().__init__()                  
        self.setWindowTitle(WINDOW_TITLE)   # Set the window title
        self.setGeometry(100, 100, WINDOW_WIDTH, WINDOW_HEIGHT) # Set the initial geometry of the window
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)  # Set a fixed size for the window

        # Initialize settings
        self._init_colors()
        self.opacity: int = 255 # Default opacity value
        self.glow_radius: int = 10  # Default glow radius value

        self._load_custom_fonts()   # Load custom fonts from the specified directory
        self._init_ui()           # Initialize the user interface components

    def _init_colors(self) -> None:
        """Initialize default color values."""
        self.bg_color = QColor(10, 10, 30, 190) # Background color
        self.fg_color = QColor(0, 255, 255, 60) # Foreground color
        self.text_color = QColor(255, 255, 255, 255)    # Text color
        self.dropdown_selected_bg_color = QColor(40, 40, 60, 220)   # Dropdown selected background color
        self.dropdown_selected_text_color = QColor(255, 255, 255, 255)  # Dropdown selected text color
        self.dropdown_menu_bg_color = QColor(20, 20, 40, 240)   # Dropdown menu background color
        self.dropdown_menu_text_color = QColor(200, 200, 200, 255)  # Dropdown menu text color
        self.dropdown_highlight_color = QColor(0, 255, 255, 180)    # Dropdown highlight color
        self.glow_color = QColor(0, 255, 255, 128)  # Glow color for text effects

    def _load_custom_fonts(self) -> None:   
        """Load custom TrueType fonts from FONT_PATH if available."""   
        if os.path.exists(FONT_PATH):   # Check if the font directory exists
            for file in os.listdir(FONT_PATH):      # Iterate through files in the font directory
                if file.lower().endswith(".ttf"):       # Check if the file is a TrueType font
                    font_file = os.path.join(FONT_PATH, file)   # Construct the full path to the font file
                    QFontDatabase.addApplicationFont(font_file) # Load the font into the application
                    logger.info("Loaded font: %s", font_file)   # Log the loaded font file

    def _init_ui(self) -> None:
        """Initialize and layout all UI components."""
        main_layout = QVBoxLayout()

        main_layout.addLayout(self._create_color_picker_row())  # Create and add the main color picker row
        main_layout.addLayout(self._create_dropdown_color_picker_row()) # Create and add the dropdown color picker row
        main_layout.addLayout(self._create_font_input_row())        # Create and add the font selection and text input row
        main_layout.addLayout(self._create_dropdown_sample_row())   # Create and add the dropdown sample row
        main_layout.addLayout(self._create_text_effects_row())  # Create and add the text effects toggles row
        main_layout.addLayout(self._create_sliders_row())   # Create and add the opacity and glow sliders row
        main_layout.addWidget(self._create_splitter())  # Create and add the splitter for display and code preview

        self.setLayout(main_layout) # Set the main layout for the widget
        self._connect_signals() # Connect UI signals to their respective handlers

        # Initial update of display and dropdown    
        self.update_display()   
        self.update_dropdown_style()        

    def _create_color_picker_row(self) -> QHBoxLayout:
        """Create row for main color pickers."""    
        row = QHBoxLayout()     
        color_buttons = [
            ("Background", 'bg'),       
            ("Foreground", 'fg'),       
            ("Text", 'text'),       
            ("Glow Color", 'glow')
        ]
        for label, key in color_buttons:    
            btn = QPushButton(label)    # Create a button for each color setting
            btn.clicked.connect(lambda _, w=key: self.choose_color(w))  # Connect button click to color selection
            row.addWidget(btn)  # Add button to the row
        return row

    def _create_dropdown_color_picker_row(self) -> QHBoxLayout:     
        """Create row for dropdown color pickers."""
        row = QHBoxLayout()     # Create a horizontal layout for dropdown color pickers
        dropdown_buttons = [
            ("Dropdown Selected BG", 'dropdown_selected_bg'),
            ("Dropdown Selected Text", 'dropdown_selected_text'),
            ("Dropdown Menu BG", 'dropdown_menu_bg'),
            ("Dropdown Menu Text", 'dropdown_menu_text'),
            ("Dropdown Highlight", 'dropdown_highlight')
        ]
        for label, key in dropdown_buttons:
            btn = QPushButton(label)# Create a button for each dropdown color setting
            btn.clicked.connect(lambda _, w=key: self.choose_color(w))  # Connect button click to color selection
            row.addWidget(btn)  # Add button to the row
        return row  

    def _create_font_input_row(self) -> QHBoxLayout:
        """Create row for font selection and text input."""
        row = QHBoxLayout()
        self.font_select = QFontComboBox()  # Create a font combo box for font selection
        self.font_select.setFixedWidth(200) # Set a fixed width for the font combo box
        self.font_select.setCurrentFont(QFont("Arial")) # Set a default font for the combo box

        self.font_size_spin = QSpinBox()
        self.font_size_spin.setRange(8, 72) # Set range for font size selection
        self.font_size_spin.setValue(20)    # Set default font size
        self.font_size_spin.setSuffix(" pt")    # Add suffix to indicate point size

        self.text_input = QLineEdit("Sample Text")  # Create a line edit for text input
        self.text_input.setMaxLength(25)    # Limit the input length to 25 characters

        row.addWidget(QLabel("Font:"))  # Add label for font selection
        row.addWidget(self.font_select) # Add font combo box to the row
        row.addWidget(QLabel("Size:"))  # Add label for font size selection
        row.addWidget(self.font_size_spin)  # Add font size spin box to the row
        row.addWidget(QLabel("Text:"))  # Add label for text input
        row.addWidget(self.text_input)  # Add text input line edit to the row
        return row

    def _create_dropdown_sample_row(self) -> QHBoxLayout:       
        """Create row for dropdown sample."""
        row = QHBoxLayout() 
        self.combo = QComboBox()    # Create a combo box for dropdown sample
        self.combo.addItems(["Select", "one", "TWO", "tHr33"])  # Add sample items to the combo box
        row.addWidget(QLabel("Dropdown:"))  # Add label for dropdown sample
        row.addWidget(self.combo)   # Add combo box to the row
        return row      

    def _create_text_effects_row(self) -> QHBoxLayout:      
        """Create row for text effect toggles."""
        row = QHBoxLayout()     
        self.bold_cb = QCheckBox("Bold")
        self.italic_cb = QCheckBox("Italic")
        self.underline_cb = QCheckBox("Underline")
        self.strike_cb = QCheckBox("Strike-through")
        self.glow_cb = QCheckBox("Glow Effect")
        for cb in [self.bold_cb, self.italic_cb, self.underline_cb, self.strike_cb, self.glow_cb]:  # Create checkboxes for text effects
            row.addWidget(cb)   # Add each checkbox to the row
        return row

    def _create_sliders_row(self) -> QHBoxLayout:   # Create a row for opacity and glow sliders
        """Create row for opacity and glow sliders."""
        row = QHBoxLayout()     
        # Opacity controls
        opacity_layout = QVBoxLayout()
        opacity_layout.addWidget(QLabel("Opacity:"))
        self.opacity_slider = QSlider(Qt.Orientation.Horizontal)    # Create a horizontal slider for opacity
        self.opacity_slider.setRange(0, 255)    # Set range for opacity slider
        self.opacity_slider.setValue(self.opacity)  # Set default opacity value
        self.opacity_label = QLabel(str(self.opacity))  # Label to display current opacity value
        opacity_layout.addWidget(self.opacity_slider)   # Add opacity slider to the layout
        opacity_layout.addWidget(self.opacity_label)        # Add label to display current opacity value

        # Glow controls
        glow_layout = QVBoxLayout()     
        glow_layout.addWidget(QLabel("Glow Radius:"))   # Add label for glow radius
        self.glow_slider = QSlider(Qt.Orientation.Horizontal)   # Create a horizontal slider for glow radius
        self.glow_slider.setRange(0, 30)    # Set range for glow radius slider
        self.glow_slider.setValue(self.glow_radius) # Set default glow radius value
        self.glow_radius_label = QLabel(str(self.glow_radius))  # Label to display current glow radius value
        glow_layout.addWidget(self.glow_slider)  # Add glow radius slider to the layout
        glow_layout.addWidget(self.glow_radius_label)   # Add label to display current glow radius value

        row.addLayout(opacity_layout)   # Add opacity controls layout to the row
        row.addLayout(glow_layout)  # Add glow controls layout to the row
        return row  

    def _create_splitter(self) -> QSplitter:        
        """Create a splitter widget for display and code preview."""
        splitter = QSplitter(Qt.Orientation.Vertical)   
        self.display = QLabel()         
        self.display.setMinimumHeight(DISPLAY_HEIGHT)
        self.display.setFixedSize(DISPLAY_WIDTH, DISPLAY_HEIGHT)
        self.display.setStyleSheet("border: 2px solid #00ffff;")
        splitter.addWidget(self.display)

        self.code_display = QTextEdit()     
        self.code_display.setMinimumHeight(200)   # Set minimum height for code display
        self.code_display.setMaximumHeight(200)   # Set maximum height for code display
        self.code_display.setReadOnly(True) # Make code display read-only
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
        return splitter

    def _connect_signals(self) -> None:
        """Connect UI signals to their respective handlers."""
        self.font_select.currentFontChanged.connect(self.update_display)    # Connect font selection changes to update display
        self.font_size_spin.valueChanged.connect(self.update_display)   # Connect font size changes to update display
        self.text_input.textChanged.connect(self.update_display)    # Connect text input changes to update display
        self.combo.currentIndexChanged.connect(self.update_display) # Connect dropdown selection changes to update display
        self.bold_cb.stateChanged.connect(self.update_display)  # Connect bold checkbox state changes to update display
        self.italic_cb.stateChanged.connect(self.update_display)    # Connect italic checkbox state changes to update display
        self.underline_cb.stateChanged.connect(self.update_display) # Connect underline checkbox state changes to update display
        self.strike_cb.stateChanged.connect(self.update_display)    # Connect strike-through checkbox state changes to update display
        self.glow_cb.stateChanged.connect(self.update_display)  # Connect glow effect checkbox state changes to update display
        self.opacity_slider.valueChanged.connect(self._on_opacity_changed)  # Connect opacity slider value changes to update opacity
        self.glow_slider.valueChanged.connect(self._on_glow_changed)    # Connect glow radius slider value changes to update glow radius

    def _on_opacity_changed(self, value: int) -> None:
        """Update opacity value and label, then refresh display."""
        self.opacity = value        # Update the opacity value
        self.opacity_label.setText(str(value))  # Update the label to reflect the new opacity value
        self.update_display()   # Refresh the display to apply the new opacity

    def _on_glow_changed(self, value: int) -> None:
        """Update glow radius and label, then refresh display."""
        self.glow_radius = value    # Update the glow radius value
        self.glow_radius_label.setText(str(value))  # Update the label to reflect the new glow radius value
        self.update_display()   # Refresh the display to apply the new glow radius

    def choose_color(self, which: str) -> None:
        """
        Open a color dialog to select a color and update the corresponding attribute.

        :param which: Identifier for the color setting to update.
        """
        color: QColor = QColorDialog.getColor() # Open color dialog to select a color
        if not color.isValid(): # Check if the selected color is valid
            return

        mapping = {
            'bg': 'bg_color',
            'fg': 'fg_color',
            'text': 'text_color',
            'glow': 'glow_color',
            'dropdown_selected_bg': 'dropdown_selected_bg_color',
            'dropdown_selected_text': 'dropdown_selected_text_color',
            'dropdown_menu_bg': 'dropdown_menu_bg_color',
            'dropdown_menu_text': 'dropdown_menu_text_color',
            'dropdown_highlight': 'dropdown_highlight_color',
        }
        attr: Optional[str] = mapping.get(which)
        if attr:
            setattr(self, attr, color)  # Update the corresponding attribute with the selected color
            self.update_display()   # Refresh the display to apply the new color
            self.update_dropdown_style()    # Update the dropdown style to reflect the new color settings

    def update_dropdown_style(self) -> None:
        """Update the style sheet of the dropdown based on current color settings."""
        self.combo.setStyleSheet(f"""
            QComboBox {{
                background-color: rgba({self.dropdown_selected_bg_color.red()}, {self.dropdown_selected_bg_color.green()}, {self.dropdown_selected_bg_color.blue()}, {self.dropdown_selected_bg_color.alpha()});
                color: rgba({self.dropdown_selected_text_color.red()}, {self.dropdown_selected_text_color.green()}, {self.dropdown_selected_text_color.blue()}, {self.dropdown_selected_text_color.alpha()});
                border: 2px solid #00ffff;
                padding: 6px;
                border-radius: 3px;
                font-size: 14px;
                selection-background-color: rgba({self.dropdown_highlight_color.red()}, {self.dropdown_highlight_color.green()}, {self.dropdown_highlight_color.blue()}, {self.dropdown_highlight_color.alpha()});
            }}
            QComboBox::drop-down {{
                background-color: rgba({self.dropdown_selected_bg_color.red()}, {self.dropdown_selected_bg_color.green()}, {self.dropdown_selected_bg_color.blue()}, {self.dropdown_selected_bg_color.alpha()});
            }}
            QComboBox QAbstractItemView {{
                background-color: rgba({self.dropdown_menu_bg_color.red()}, {self.dropdown_menu_bg_color.green()}, {self.dropdown_menu_bg_color.blue()}, {self.dropdown_menu_bg_color.alpha()});
                color: rgba({self.dropdown_menu_text_color.red()}, {self.dropdown_menu_text_color.green()}, {self.dropdown_menu_text_color.blue()}, {self.dropdown_menu_text_color.alpha()});
                border: 2px solid #00ffff;
                selection-background-color: rgba({self.dropdown_highlight_color.red()}, {self.dropdown_highlight_color.green()}, {self.dropdown_highlight_color.blue()}, {self.dropdown_highlight_color.alpha()});
                selection-color: rgba({self.dropdown_selected_text_color.red()}, {self.dropdown_selected_text_color.green()}, {self.dropdown_selected_text_color.blue()}, {self.dropdown_selected_text_color.alpha()});
            }}
        """)

    def draw_glow_text(self, painter: QPainter, rect: QRect, text: str, font: QFont,
                       text_color: QColor, glow_color: QColor, glow_radius: int) -> None:
        """
        Draw text with a glow effect.

        :param painter: QPainter object.
        :param rect: QRect defining drawing area.
        :param text: Text to be drawn.
        :param font: QFont to use.
        :param text_color: Base text color.
        :param glow_color: Color for glow.
        :param glow_radius: Intensity radius for glow effect.
        """
        if glow_radius > 0:
            path = QPainterPath()
            # Position text approximately centered within rect
            text_x = rect.center().x() - rect.width() // 4
            text_y = rect.center().y() + rect.height() // 6
            path.addText(text_x, text_y, font, text)
            for i in range(glow_radius, 0, -1):
                # Gradually reduce alpha for each glow layer
                glow_alpha = int(glow_color.alpha() * (glow_radius - i + 1) / glow_radius / 2)
                temp_glow = QColor(glow_color.red(), glow_color.green(), glow_color.blue(), glow_alpha)
                glow_pen = QPen(temp_glow, i * 2)
                glow_pen.setCapStyle(Qt.PenCapStyle.RoundCap)
                glow_pen.setJoinStyle(Qt.PenJoinStyle.RoundJoin)
                painter.setPen(glow_pen)
                painter.setBrush(Qt.BrushStyle.NoBrush)
                painter.drawPath(path)

        painter.setPen(QPen(text_color))
        painter.setBrush(QBrush(text_color))
        painter.setFont(font)
        painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, text)

    def generate_code_output(self) -> str:
        """
        Generate a code representation of the current settings in both Python and CSS formats.

        :return: String containing the configuration code.
        """
        code = "# Color Configuration\n"
        code += f"bg_color = QColor({self.bg_color.red()}, {self.bg_color.green()}, {self.bg_color.blue()}, {self.bg_color.alpha()})\n"
        code += f"fg_color = QColor({self.fg_color.red()}, {self.fg_color.green()}, {self.fg_color.blue()}, {self.fg_color.alpha()})\n"
        code += f"text_color = QColor({self.text_color.red()}, {self.text_color.green()}, {self.text_color.blue()}, {self.text_color.alpha()})\n"
        if self.glow_cb.isChecked():
            code += f"glow_color = QColor({self.glow_color.red()}, {self.glow_color.green()}, {self.glow_color.blue()}, {self.glow_color.alpha()})\n"
            code += f"glow_radius = {self.glow_radius}\n"
        code += "\n# Dropdown Colors\n"
        code += f"dropdown_selected_bg = QColor({self.dropdown_selected_bg_color.red()}, {self.dropdown_selected_bg_color.green()}, {self.dropdown_selected_bg_color.blue()}, {self.dropdown_selected_bg_color.alpha()})\n"
        code += f"dropdown_selected_text = QColor({self.dropdown_selected_text_color.red()}, {self.dropdown_selected_text_color.green()}, {self.dropdown_selected_text_color.blue()}, {self.dropdown_selected_text_color.alpha()})\n"
        code += f"dropdown_menu_bg = QColor({self.dropdown_menu_bg_color.red()}, {self.dropdown_menu_bg_color.green()}, {self.dropdown_menu_bg_color.blue()}, {self.dropdown_menu_bg_color.alpha()})\n"
        code += f"dropdown_menu_text = QColor({self.dropdown_menu_text_color.red()}, {self.dropdown_menu_text_color.green()}, {self.dropdown_menu_text_color.blue()}, {self.dropdown_menu_text_color.alpha()})\n"
        code += f"dropdown_highlight = QColor({self.dropdown_highlight_color.red()}, {self.dropdown_highlight_color.green()}, {self.dropdown_highlight_color.blue()}, {self.dropdown_highlight_color.alpha()})\n"
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

    def update_display(self) -> None:
        """
        Render the sample display and update the code preview based on current settings.
        """
        width, height = DISPLAY_WIDTH, DISPLAY_HEIGHT
        pixmap = QPixmap(width, height)
        if pixmap.isNull():
            logger.error("Failed to create pixmap")
            return

        pixmap.fill(Qt.GlobalColor.transparent)
        painter = QPainter(pixmap)
        if not painter.isActive():
            logger.error("Painter failed to activate")
            painter.end()
            return

        try:
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            painter.setRenderHint(QPainter.RenderHint.TextAntialiasing)
            
            # Draw background with current opacity
            bg_color = QColor(self.bg_color.red(), self.bg_color.green(), self.bg_color.blue(), self.opacity)
            painter.fillRect(QRect(0, 0, width, height), bg_color)
            
            # Draw foreground area (chat display)
            fg_color = QColor(self.fg_color.red(), self.fg_color.green(), self.fg_color.blue(), self.opacity)
            chat_rect = QRect(50, 75, width - 100, 150)
            painter.fillRect(chat_rect, fg_color)
            
            # Configure text font settings
            font = self.font_select.currentFont()
            font.setPointSize(self.font_size_spin.value())
            font.setBold(self.bold_cb.isChecked())
            font.setItalic(self.italic_cb.isChecked())
            font.setUnderline(self.underline_cb.isChecked())
            font.setStrikeOut(self.strike_cb.isChecked())
            sample_text = self.text_input.text()
            text_color = QColor(self.text_color.red(), self.text_color.green(), self.text_color.blue(), self.opacity)
            
            if self.glow_cb.isChecked():
                self.draw_glow_text(painter, chat_rect, sample_text, font, text_color, self.glow_color, self.glow_radius)
            else:
                painter.setFont(font)
                painter.setPen(QPen(text_color))
                painter.drawText(chat_rect, Qt.AlignmentFlag.AlignCenter, sample_text)
        except Exception as e:
            logger.error("Painting error: %s", e)
        finally:
            painter.end()
        
        self.display.setPixmap(pixmap)
        self.code_display.setPlainText(self.generate_code_output())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ColorPickerGUI()
    window.show()
    sys.exit(app.exec())
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QColorDialog, QVBoxLayout,
    QHBoxLayout, QComboBox, QLineEdit, QCheckBox, QSlider, QFontComboBox,
    QSpinBox, QTextEdit, QSplitter, QFileDialog, QMessageBox, QTabWidget,
    QGroupBox, QGridLayout, QScrollArea, QFrame, QButtonGroup, QRadioButton,
    QListWidget, QListWidgetItem, QTreeWidget, QTreeWidgetItem, QToolButton,
    QMenu, QAction, QSpacerItem, QSizePolicy, QProgressBar, QDial, QDoubleSpinBox
)
from PyQt6.QtGui import (
    QColor, QFont, QPainter, QPen, QBrush, QFontDatabase, QPixmap, QPainterPath,
    QLinearGradient, QRadialGradient, QConicalGradient, QPolygonF, QPainterPathStroker,
    QTransform, QIcon, QKeySequence, QAction as QGuiAction, QPalette, QFontMetrics,
    QTextOption, QTextDocument, QTextCursor, QTextCharFormat
)
from PyQt6.QtCore import (
    Qt, QRect, QRectF, QPointF, QSizeF, QTimer, QPropertyAnimation, QEasingCurve,
    QSequentialAnimationGroup, QParallelAnimationGroup, pyqtSignal, QObject,
    QThread, QMutex, QSettings, QStandardPaths, QDir, QUrl, QMimeData, QIODevice
)
import sys
import os
import platform
import logging
import json
import math
import random
from typing import Optional, List, Dict, Any, Tuple, Union, Callable
from dataclasses import dataclass, asdict
from enum import Enum, auto
from pathlib import Path
import xml.etree.ElementTree as ET

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
WINDOW_TITLE = "Selene Theme Stylizer Pro"
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 1200
PREVIEW_WIDTH = 800
PREVIEW_HEIGHT = 600
CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 800

# System font directories
SYSTEM_FONT_PATHS = {
    'Windows': [
        'C:/Windows/Fonts',
        os.path.expanduser('~/AppData/Local/Microsoft/Windows/Fonts')
    ],
    'Linux': [
        '/usr/share/fonts',
        '/usr/local/share/fonts',
        os.path.expanduser('~/.fonts'),
        os.path.expanduser('~/.local/share/fonts')
    ],
    'Darwin': [
        '/System/Library/Fonts',
        '/Library/Fonts',
        os.path.expanduser('~/Library/Fonts')
    ]
}

# Enums and Data Classes
class ShapeType(Enum):
    RECTANGLE = auto()
    ELLIPSE = auto()
    POLYGON = auto()
    LINE = auto()
    BEZIER_CURVE = auto()
    TEXT = auto()
    STAR = auto()
    SPEECH_BUBBLE = auto()

class GradientType(Enum):
    LINEAR = auto()
    RADIAL = auto()
    CONICAL = auto()
    NONE = auto()

class BlendMode(Enum):
    NORMAL = auto()
    MULTIPLY = auto()
    SCREEN = auto()
    OVERLAY = auto()
    SOFT_LIGHT = auto()
    HARD_LIGHT = auto()
    COLOR_DODGE = auto()
    COLOR_BURN = auto()

class AnimationType(Enum):
    FADE = auto()
    SCALE = auto()
    ROTATE = auto()
    TRANSLATE = auto()
    COLOR_TRANSITION = auto()

@dataclass
class ColorStop:
    position: float
    color: QColor
    
@dataclass
class GradientData:
    type: GradientType
    start_point: QPointF
    end_point: QPointF
    radius: float
    angle: float
    stops: List[ColorStop]

@dataclass
class ShapeData:
    shape_type: ShapeType
    position: QPointF
    size: QSizeF
    rotation: float
    fill_color: QColor
    stroke_color: QColor
    stroke_width: float
    gradient: Optional[GradientData]
    opacity: float
    blend_mode: BlendMode
    z_index: int
    visible: bool
    locked: bool
    name: str
    custom_properties: Dict[str, Any]

@dataclass
class FontData:
    family: str
    size: int
    weight: int
    italic: bool
    underline: bool
    strikeout: bool
    letter_spacing: float
    line_height: float

@dataclass
class TextEffectData:
    glow_enabled: bool
    glow_color: QColor
    glow_radius: int
    shadow_enabled: bool
    shadow_color: QColor
    shadow_offset: QPointF
    shadow_blur: float
    outline_enabled: bool
    outline_color: QColor
    outline_width: float

@dataclass
class AnimationData:
    type: AnimationType
    duration: int
    easing: str
    start_value: Any
    end_value: Any
    loop_count: int

class LayerManager(QObject):
    """Manages layers and their z-ordering."""
    
    layerChanged = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.layers: List[ShapeData] = []
        self.selected_layers: List[int] = []
        
    def add_layer(self, shape: ShapeData) -> int:
        """Add a new layer and return its index."""
        self.layers.append(shape)
        self.layerChanged.emit()
        return len(self.layers) - 1
    
    def remove_layer(self, index: int) -> bool:
        """Remove layer at index."""
        if 0 <= index < len(self.layers):
            del self.layers[index]
            if index in self.selected_layers:
                self.selected_layers.remove(index)
            self.layerChanged.emit()
            return True
        return False
    
    def move_layer(self, from_index: int, to_index: int) -> bool:
        """Move layer from one position to another."""
        if 0 <= from_index < len(self.layers) and 0 <= to_index < len(self.layers):
            layer = self.layers.pop(from_index)
            self.layers.insert(to_index, layer)
            self.layerChanged.emit()
            return True
        return False
    
    def get_sorted_layers(self) -> List[Tuple[int, ShapeData]]:
        """Get layers sorted by z-index."""
        indexed_layers = [(i, layer) for i, layer in enumerate(self.layers)]
        return sorted(indexed_layers, key=lambda x: x[1].z_index)

class ColorPalette:
    """Manages color palettes and harmony generation."""
    
    def __init__(self):
        self.palettes: Dict[str, List[QColor]] = {
            "Default": [
                QColor(255, 87, 87),   # Red
                QColor(255, 193, 7),   # Yellow
                QColor(76, 175, 80),   # Green
                QColor(33, 150, 243),  # Blue
                QColor(156, 39, 176),  # Purple
            ]
        }
        
    def generate_complementary(self, base_color: QColor) -> List[QColor]:
        """Generate complementary color scheme."""
        h, s, v, a = base_color.getHsv()
        comp_h = (h + 180) % 360
        return [base_color, QColor.fromHsv(comp_h, s, v, a)]
    
    def generate_triadic(self, base_color: QColor) -> List[QColor]:
        """Generate triadic color scheme."""
        h, s, v, a = base_color.getHsv()
        return [
            base_color,
            QColor.fromHsv((h + 120) % 360, s, v, a),
            QColor.fromHsv((h + 240) % 360, s, v, a)
        ]
    
    def generate_analogous(self, base_color: QColor) -> List[QColor]:
        """Generate analogous color scheme."""
        h, s, v, a = base_color.getHsv()
        return [
            QColor.fromHsv((h - 30) % 360, s, v, a),
            base_color,
            QColor.fromHsv((h + 30) % 360, s, v, a)
        ]

class AdvancedCanvas(QLabel):
    """Advanced canvas with shape drawing and manipulation capabilities."""
    
    shapeSelected = pyqtSignal(int)
    shapeModified = pyqtSignal(int)
    
    def __init__(self, layer_manager: LayerManager):
        super().__init__()
        self.layer_manager = layer_manager
        self.setMinimumSize(CANVAS_WIDTH, CANVAS_HEIGHT)
        self.setStyleSheet("border: 2px solid #333; background: white;")
        self.setAcceptDrops(True)
        
        # Drawing state
        self.drawing_mode = False
        self.current_tool = ShapeType.RECTANGLE
        self.start_point = QPointF()
        self.current_point = QPointF()
        self.grid_enabled = True
        self.grid_size = 20
        self.snap_to_grid = True
        
        # Zoom and pan
        self.zoom_factor = 1.0
        self.pan_offset = QPointF(0, 0)
        
        self.layer_manager.layerChanged.connect(self.update)
        
    def paintEvent(self, event):
        """Custom paint event for canvas rendering."""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Fill background
        painter.fillRect(self.rect(), QColor(255, 255, 255))
        
        # Draw grid
        if self.grid_enabled:
            self.draw_grid(painter)
        
        # Apply zoom and pan
        painter.scale(self.zoom_factor, self.zoom_factor)
        painter.translate(self.pan_offset)
        
        # Draw layers
        for index, layer in self.layer_manager.get_sorted_layers():
            if layer.visible:
                self.draw_shape(painter, layer)
        
        # Draw current shape being created
        if self.drawing_mode:
            self.draw_preview_shape(painter)
    
    def draw_grid(self, painter: QPainter):
        """Draw grid lines."""
        painter.setPen(QPen(QColor(220, 220, 220), 1, Qt.PenStyle.DotLine))
        
        for x in range(0, self.width(), self.grid_size):
            painter.drawLine(x, 0, x, self.height())
        
        for y in range(0, self.height(), self.grid_size):
            painter.drawLine(0, y, self.width(), y)
    
    def draw_shape(self, painter: QPainter, shape: ShapeData):
        """Draw a shape on the canvas."""
        painter.save()
        
        # Apply transformations
        painter.translate(shape.position)
        painter.rotate(shape.rotation)
        painter.setOpacity(shape.opacity)
        
        # Set up brush and pen
        if shape.gradient:
            brush = self.create_gradient_brush(shape.gradient)
        else:
            brush = QBrush(shape.fill_color)
        
        pen = QPen(shape.stroke_color, shape.stroke_width)
        painter.setBrush(brush)
        painter.setPen(pen)
        
        # Draw based on shape type
        if shape.shape_type == ShapeType.RECTANGLE:
            painter.drawRect(QRectF(0, 0, shape.size.width(), shape.size.height()))
        elif shape.shape_type == ShapeType.ELLIPSE:
            painter.drawEllipse(QRectF(0, 0, shape.size.width(), shape.size.height()))
        elif shape.shape_type == ShapeType.POLYGON:
            # Draw a hexagon as example
            points = self.create_polygon_points(shape.size, 6)
            painter.drawPolygon(points)
        elif shape.shape_type == ShapeType.STAR:
            points = self.create_star_points(shape.size, 5)
            painter.drawPolygon(points)
        
        painter.restore()
    
    def create_gradient_brush(self, gradient: GradientData) -> QBrush:
        """Create a gradient brush from gradient data."""
        if gradient.type == GradientType.LINEAR:
            grad = QLinearGradient(gradient.start_point, gradient.end_point)
        elif gradient.type == GradientType.RADIAL:
            grad = QRadialGradient(gradient.start_point, gradient.radius)
        else:  # CONICAL
            grad = QConicalGradient(gradient.start_point, gradient.angle)
        
        for stop in gradient.stops:
            grad.setColorAt(stop.position, stop.color)
        
        return QBrush(grad)
    
    def create_polygon_points(self, size: QSizeF, sides: int) -> QPolygonF:
        """Create polygon points."""
        points = QPolygonF()
        center = QPointF(size.width() / 2, size.height() / 2)
        radius = min(size.width(), size.height()) / 2
        
        for i in range(sides):
            angle = 2 * math.pi * i / sides
            x = center.x() + radius * math.cos(angle)
            y = center.y() + radius * math.sin(angle)
            points.append(QPointF(x, y))
        
        return points
    
    def create_star_points(self, size: QSizeF, points: int) -> QPolygonF:
        """Create star points."""
        star = QPolygonF()
        center = QPointF(size.width() / 2, size.height() / 2)
        outer_radius = min(size.width(), size.height()) / 2
        inner_radius = outer_radius * 0.4
        
        for i in range(points * 2):
            angle = math.pi * i / points
            radius = outer_radius if i % 2 == 0 else inner_radius
            x = center.x() + radius * math.cos(angle - math.pi / 2)
            y = center.y() + radius * math.sin(angle - math.pi / 2)
            star.append(QPointF(x, y))
        
        return star
    
    def draw_preview_shape(self, painter: QPainter):
        """Draw preview of shape being created."""
        painter.setPen(QPen(QColor(100, 100, 100), 1, Qt.PenStyle.DashLine))
        painter.setBrush(Qt.BrushStyle.NoBrush)
        
        rect = QRectF(self.start_point, self.current_point).normalized()
        if self.current_tool == ShapeType.RECTANGLE:
            painter.drawRect(rect)
        elif self.current_tool == ShapeType.ELLIPSE:
            painter.drawEllipse(rect)
    
    def mousePressEvent(self, event):
        """Handle mouse press for shape creation."""
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing_mode = True
            self.start_point = QPointF(event.position())
            self.current_point = self.start_point
    
    def mouseMoveEvent(self, event):
        """Handle mouse move for shape preview."""
        if self.drawing_mode:
            self.current_point = QPointF(event.position())
            if self.snap_to_grid:
                self.current_point = self.snap_to_grid_point(self.current_point)
            self.update()
    
    def mouseReleaseEvent(self, event):
        """Handle mouse release to create shape."""
        if event.button() == Qt.MouseButton.LeftButton and self.drawing_mode:
            self.drawing_mode = False
            rect = QRectF(self.start_point, self.current_point).normalized()
            
            if rect.width() > 5 and rect.height() > 5:  # Minimum size
                shape = ShapeData(
                    shape_type=self.current_tool,
                    position=rect.topLeft(),
                    size=rect.size(),
                    rotation=0.0,
                    fill_color=QColor(100, 150, 255, 200),
                    stroke_color=QColor(50, 100, 200),
                    stroke_width=2.0,
                    gradient=None,
                    opacity=1.0,
                    blend_mode=BlendMode.NORMAL,
                    z_index=len(self.layer_manager.layers),
                    visible=True,
                    locked=False,
                    name=f"{self.current_tool.name.title()} {len(self.layer_manager.layers) + 1}",
                    custom_properties={}
                )
                self.layer_manager.add_layer(shape)
            self.update()
    
    def snap_to_grid_point(self, point: QPointF) -> QPointF:
        """Snap point to grid."""
        x = round(point.x() / self.grid_size) * self.grid_size
        y = round(point.y() / self.grid_size) * self.grid_size
        return QPointF(x, y)

class ThemeExporter:
    """Handles theme export in various formats."""
    
    @staticmethod
    def export_to_python(theme_data: Dict[str, Any]) -> str:
        """Export theme as Python code."""
        code_lines = [
            "# Generated by Selene Theme Stylizer Pro",
            "from PyQt6.QtGui import QColor, QFont, QLinearGradient",
            "from PyQt6.QtCore import Qt",
            "",
            "# Theme Configuration",
            "class Theme:",
            "    def __init__(self):",
        ]
        
        # Colors
        if 'colors' in theme_data:
            code_lines.append("        # Colors")
            for name, color_data in theme_data['colors'].items():
                if isinstance(color_data, dict):
                    r, g, b, a = color_data['r'], color_data['g'], color_data['b'], color_data['a']
                    code_lines.append(f"        self.{name} = QColor({r}, {g}, {b}, {a})")
        
        # Fonts
        if 'fonts' in theme_data:
            code_lines.append("        # Fonts")
            for name, font_data in theme_data['fonts'].items():
                code_lines.append(f"        self.{name} = QFont('{font_data['family']}', {font_data['size']})")
                if font_data.get('bold'):
                    code_lines.append(f"        self.{name}.setBold(True)")
                if font_data.get('italic'):
                    code_lines.append(f"        self.{name}.setItalic(True)")
        
        # Stylesheets
        if 'stylesheets' in theme_data:
            code_lines.append("        # Stylesheets")
            for widget_type, styles in theme_data['stylesheets'].items():
                code_lines.append(f"        self.{widget_type}_style = '''")
                for property_name, value in styles.items():
                    code_lines.append(f"            {property_name}: {value};")
                code_lines.append("        '''")
        
        return "\n".join(code_lines)
    
    @staticmethod
    def export_to_css(theme_data: Dict[str, Any]) -> str:
        """Export theme as CSS/Qt StyleSheet."""
        css_lines = ["/* Generated by Selene Theme Stylizer Pro */", ""]
        
        if 'stylesheets' in theme_data:
            for widget_type, styles in theme_data['stylesheets'].items():
                css_lines.append(f"{widget_type} {{")
                for property_name, value in styles.items():
                    css_lines.append(f"    {property_name}: {value};")
                css_lines.append("}")
                css_lines.append("")
        
        return "\n".join(css_lines)
    
    @staticmethod
    def export_to_json(theme_data: Dict[str, Any]) -> str:
        """Export theme as JSON."""
        return json.dumps(theme_data, indent=2, default=str)

class AdvancedThemeStyler(QWidget):
    """Main application class with advanced theming capabilities."""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle(WINDOW_TITLE)
        self.setGeometry(100, 100, WINDOW_WIDTH, WINDOW_HEIGHT)
        
        # Initialize core systems
        self.layer_manager = LayerManager()
        self.color_palette = ColorPalette()
        self.settings = QSettings("Selene", "ThemeStyler")
        
        # Initialize state
        self.current_theme_data = {}
        self.animation_timers = {}
        self.custom_font_paths = []
        
        # Load fonts and setup UI
        self._load_system_fonts()
        self._init_ui()
        self._load_settings()
    
    def _load_system_fonts(self):
        """Load system fonts."""
        system_name = platform.system()
        font_paths = SYSTEM_FONT_PATHS.get(system_name, [])
        
        loaded_count = 0
        for font_dir in font_paths:
            if os.path.exists(font_dir):
                loaded_count += self._load_fonts_from_directory(font_dir)
        
        logger.info("Loaded %d system fonts from %s", loaded_count, system_name)
    
    def _load_fonts_from_directory(self, directory: str) -> int:
        """Load fonts from directory."""
        loaded_count = 0
        try:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if file.lower().endswith(('.ttf', '.otf', '.woff', '.woff2')):
                        font_file = os.path.join(root, file)
                        try:
                            font_id = QFontDatabase.addApplicationFont(font_file)
                            if font_id != -1:
                                loaded_count += 1
                        except Exception as e:
                            logger.warning("Failed to load font %s: %s", font_file, e)
        except Exception as e:
            logger.warning("Error accessing font directory %s: %s", directory, e)
        
        return loaded_count
    
    def _init_ui(self):
        """Initialize the user interface."""
        main_layout = QHBoxLayout(self)
        
        # Create main splitter
        main_splitter = QSplitter(Qt.Orientation.Horizontal)
        
        # Left panel - Tools and properties
        left_panel = self._create_left_panel()
        main_splitter.addWidget(left_panel)
        
        # Center panel - Canvas and preview
        center_panel = self._create_center_panel()
        main_splitter.addWidget(center_panel)
        
        # Right panel - Layers and code
        right_panel = self._create_right_panel()
        main_splitter.addWidget(right_panel)
        
        # Set splitter ratios
        main_splitter.setSizes([300, 800, 400])
        main_layout.addWidget(main_splitter)
    
    def _create_left_panel(self) -> QWidget:
        """Create left tool panel."""
        panel = QWidget()
        layout = QVBoxLayout(panel)
        
        # Tool selection
        tools_group = QGroupBox("Tools")
        tools_layout = QGridLayout(tools_group)
        
        self.tool_buttons = QButtonGroup()
        tools = [
            ("Rectangle", ShapeType.RECTANGLE),
            ("Ellipse", ShapeType.ELLIPSE),
            ("Polygon", ShapeType.POLYGON),
            ("Line", ShapeType.LINE),
            ("Star", ShapeType.STAR),
            ("Text", ShapeType.TEXT)
        ]
        
        for i, (name, shape_type) in enumerate(tools):
            btn = QRadioButton(name)
            btn.setProperty("shape_type", shape_type)
            self.tool_buttons.addButton(btn, i)
            tools_layout.addWidget(btn, i // 2, i % 2)
        
        self.tool_buttons.buttons()[0].setChecked(True)  # Default to rectangle
        self.tool_buttons.buttonClicked.connect(self._on_tool_changed)
        
        layout.addWidget(tools_group)
        
        # Color controls
        colors_group = self._create_color_controls()
        layout.addWidget(colors_group)
        
        # Gradient controls
        gradient_group = self._create_gradient_controls()
        layout.addWidget(gradient_group)
        
        # Typography controls
        typography_group = self._create_typography_controls()
        layout.addWidget(typography_group)
        
        # Effects controls
        effects_group = self._create_effects_controls()
        layout.addWidget(effects_group)
        
        layout.addStretch()
        return panel
    
    def _create_color_controls(self) -> QGroupBox:
        """Create color control group."""
        group = QGroupBox("Colors")
        layout = QVBoxLayout(group)
        
        # Primary colors
        primary_layout = QGridLayout()
        
        color_controls = [
            ("Fill", "fill_color"),
            ("Stroke", "stroke_color"),
            ("Background", "bg_color"),
            ("Text", "text_color")
        ]
        
        self.color_buttons = {}
        for i, (label, key) in enumerate(color_controls):
            lbl = QLabel(label + ":")
            btn = QPushButton()
            btn.setMinimumSize(50, 30)
            btn.setStyleSheet("background-color: #4CAF50; border: 1px solid #333;")
            btn.clicked.connect(lambda checked, k=key: self._choose_color(k))
            
            primary_layout.addWidget(lbl, i, 0)
            primary_layout.addWidget(btn, i, 1)
            self.color_buttons[key] = btn
        
        layout.addLayout(primary_layout)
        
        # Color harmony generator
        harmony_layout = QHBoxLayout()
        harmony_layout.addWidget(QLabel("Harmony:"))
        
        self.harmony_combo = QComboBox()
        self.harmony_combo.addItems(["Complementary", "Triadic", "Analogous"])
        harmony_layout.addWidget(self.harmony_combo)
        
        generate_btn = QPushButton("Generate")
        generate_btn.clicked.connect(self._generate_color_harmony)
        harmony_layout.addWidget(generate_btn)
        
        layout.addLayout(harmony_layout)
        
        return group
    
    def _create_gradient_controls(self) -> QGroupBox:
        """Create gradient control group."""
        group = QGroupBox("Gradients")
        layout = QVBoxLayout(group)
        
        # Gradient type
        type_layout = QHBoxLayout()
        type_layout.addWidget(QLabel("Type:"))
        
        self.gradient_type = QComboBox()
        self.gradient_type.addItems(["None", "Linear", "Radial", "Conical"])
        type_layout.addWidget(self.gradient_type)
        
        layout.addLayout(type_layout)
        
        # Gradient direction (for linear)
        direction_layout = QHBoxLayout()
        direction_layout.addWidget(QLabel("Angle:"))
        
        self.gradient_angle = QDial()
        self.gradient_angle.setRange(0, 360)
        self.gradient_angle.setValue(0)
        self.gradient_angle.setMaximumSize(80, 80)
        direction_layout.addWidget(self.gradient_angle)
        
        self.angle_label = QLabel("0°")
        direction_layout.addWidget(self.angle_label)
        
        layout.addLayout(direction_layout)
        
        # Gradient stops
        stops_label = QLabel("Color Stops:")
        layout.addWidget(stops_label)
        
        self.gradient_stops = QListWidget()
        self.gradient_stops.setMaximumHeight(100)
        layout.addWidget(self.gradient_stops)
        
        # Add/Remove stops
        stops_buttons = QHBoxLayout()
        add_stop_btn = QPushButton("Add Stop")
        remove_stop_btn = QPushButton("Remove Stop")
        stops_buttons.addWidget(add_stop_btn)
        stops_buttons.addWidget(remove_stop_btn)
        
        layout.addLayout(stops_buttons)
        
        return group
    
    def _create_typography_controls(self) -> QGroupBox:
        """Create typography control group."""
        group = QGroupBox("Typography")
        layout = QVBoxLayout(group)
        
        # Font selection
        font_layout = QGridLayout()
        
        font_layout.addWidget(QLabel("Family:"), 0, 0)
        self.font_combo = QFontComboBox()
        font_layout.addWidget(self.font_combo, 0, 1)
        
        font_layout.addWidget(QLabel("Size:"), 1, 0)
        self.font_size = QSpinBox()
        self.font_size.setRange(6, 200)
        self.font_size.setValue(12)
        self.font_size.setSuffix(" pt")
        font_layout.addWidget(self.font_size, 1, 1)
        
        font_layout.addWidget(QLabel("Weight:"), 2, 0)
        self.font_weight = QComboBox()
        self.font_weight.addItems(["Normal", "Bold", "Light", "Thin", "Black"])
        font_layout.addWidget(self.font_weight, 2, 1)
        
        layout.addLayout(font_layout)
        
        # Font styles
        styles_layout = QHBoxLayout()
        self.italic_cb = QCheckBox("Italic")
        self.underline_cb = QCheckBox("Underline")
        self.strikeout_cb = QCheckBox("Strikeout")
        
        styles_layout.addWidget(self.italic_cb)
        styles_layout.addWidget(self.underline_cb)
        styles_layout.addWidget(self.strikeout_cb)
        
        layout.addLayout(styles_layout)
        
        # Text spacing
        spacing_layout = QGridLayout()
        
        spacing_layout.addWidget(QLabel("Letter Spacing:"), 0, 0)
        self.letter_spacing = QDoubleSpinBox()
        self.letter_spacing.setRange(-10.0, 10.0)
        self.letter_spacing.setSingleStep(0.1)
        self.letter_spacing.setSuffix(" px")
        spacing_layout.addWidget(self.letter_spacing, 0, 1)
        
        spacing_layout.addWidget(QLabel("Line Height:"), 1, 0)
        self.line_height = QDoubleSpinBox()
        self.line_height.setRange(0.5, 3.0)
        self.line_height.setSingleStep(0.1)
        self.line_height.setValue(1.2)
        spacing_layout.addWidget(self.line_height, 1, 1)
        
        layout.addLayout(spacing_layout)
        
        # Custom fonts button
        custom_fonts_btn = QPushButton("Load Custom Fonts...")
        custom_fonts_btn.clicked.connect(self._load_custom_fonts)
        layout.addWidget(custom_fonts_btn)
        
        return group
    
    def _create_effects_controls(self) -> QGroupBox:
        """Create effects control group."""
        group = QGroupBox("Effects")
        layout = QVBoxLayout(group)
        
        # Glow effect
        glow_group = QGroupBox("Glow")
        glow_layout = QGridLayout(glow_group)
        
        self.glow_enabled = QCheckBox("Enable Glow")
        glow_layout.addWidget(self.glow_enabled, 0, 0, 1, 2)
        
        glow_layout.addWidget(QLabel("Radius:"), 1, 0)
        self.glow_radius = QSlider(Qt.Orientation.Horizontal)
        self.glow_radius.setRange(0, 50)
        self.glow_radius.setValue(10)
        glow_layout.addWidget(self.glow_radius, 1, 1)
        
        glow_layout.addWidget(QLabel("Color:"), 2, 0)
        self.glow_color_btn = QPushButton()
        self.glow_color_btn.setMinimumSize(50, 25)
        self.glow_color_btn.setStyleSheet("background-color: #FFD700; border: 1px solid #333;")
        self.glow_color_btn.clicked.connect(lambda: self._choose_color("glow_color"))
        glow_layout.addWidget(self.glow_color_btn, 2, 1)
        
        layout.addWidget(glow_group)
        
        # Shadow effect
        shadow_group = QGroupBox("Shadow")
        shadow_layout = QGridLayout(shadow_group)
        
        self.shadow_enabled = QCheckBox("Enable Shadow")
        shadow_layout.addWidget(self.shadow_enabled, 0, 0, 1, 2)
        
        shadow_layout.addWidget(QLabel("Offset X:"), 1, 0)
        self.shadow_x = QSpinBox()
        self.shadow_x.setRange(-50, 50)
        self.shadow_x.setValue(2)
        shadow_layout.addWidget(self.shadow_x, 1, 1)
        
        shadow_layout.addWidget(QLabel("Offset Y:"), 2, 0)
        self.shadow_y = QSpinBox()
        self.shadow_y.setRange(-50, 50)
        self.shadow_y.setValue(2)
        shadow_layout.addWidget(self.shadow_y, 2, 1)
        
        shadow_layout.addWidget(QLabel("Blur:"), 3, 0)
        self.shadow_blur = QSlider(Qt.Orientation.Horizontal)
        self.shadow_blur.setRange(0, 30)
        self.shadow_blur.setValue(5)
        shadow_layout.addWidget(self.shadow_blur, 3, 1)
        
        layout.addWidget(shadow_group)
        
        # Opacity and blend mode
        blend_layout = QGridLayout()
        
        blend_layout.addWidget(QLabel("Opacity:"), 0, 0)
        self.opacity_slider = QSlider(Qt.Orientation.Horizontal)
        self.opacity_slider.setRange(0, 100)
        self.opacity_slider.setValue(100)
        blend_layout.addWidget(self.opacity_slider, 0, 1)
        
        blend_layout.addWidget(QLabel("Blend Mode:"), 1, 0)
        self.blend_mode = QComboBox()
        self.blend_mode.addItems([mode.name.title().replace('_', ' ') for mode in BlendMode])
        blend_layout.addWidget(self.blend_mode, 1, 1)
        
        layout.addLayout(blend_layout)
        
        return group
    
    def _create_center_panel(self) -> QWidget:
        """Create center panel with canvas and preview."""
        panel = QWidget()
        layout = QVBoxLayout(panel)
        
        # Toolbar
        toolbar = self._create_toolbar()
        layout.addWidget(toolbar)
        
        # Canvas area
        canvas_scroll = QScrollArea()
        self.canvas = AdvancedCanvas(self.layer_manager)
        canvas_scroll.setWidget(self.canvas)
        canvas_scroll.setWidgetResizable(True)
        
        layout.addWidget(canvas_scroll, 1)
        
        # Preview area
        preview_group = QGroupBox("Live Preview")
        preview_layout = QVBoxLayout(preview_group)
        
        self.preview_widget = QLabel()
        self.preview_widget.setMinimumSize(400, 200)
        self.preview_widget.setStyleSheet("border: 1px solid #ccc; background: white;")
        preview_layout.addWidget(self.preview_widget)
        
        layout.addWidget(preview_group)
        
        return panel
    
    def _create_toolbar(self) -> QWidget:
        """Create toolbar with common actions."""
        toolbar = QWidget()
        layout = QHBoxLayout(toolbar)
        
        # File operations
        new_btn = QPushButton("New")
        open_btn = QPushButton("Open")
        save_btn = QPushButton("Save")
        export_btn = QPushButton("Export")
        
        layout.addWidget(new_btn)
        layout.addWidget(open_btn)
        layout.addWidget(save_btn)
        layout.addWidget(export_btn)
        
        layout.addWidget(QLabel("|"))  # Separator
        
        # View controls
        zoom_out_btn = QPushButton("Zoom Out")
        zoom_in_btn = QPushButton("Zoom In")
        fit_btn = QPushButton("Fit to Window")
        grid_btn = QCheckBox("Show Grid")
        grid_btn.setChecked(True)
        
        layout.addWidget(zoom_out_btn)
        layout.addWidget(zoom_in_btn)
        layout.addWidget(fit_btn)
        layout.addWidget(grid_btn)
        
        layout.addStretch()
        
        # Connect signals
        new_btn.clicked.connect(self._new_project)
        open_btn.clicked.connect(self._open_project)
        save_btn.clicked.connect(self._save_project)
        export_btn.clicked.connect(self._export_theme)
        grid_btn.toggled.connect(self._toggle_grid)
        
        return toolbar
    
    def _create_right_panel(self) -> QWidget:
        """Create right panel with layers and code."""
        panel = QWidget()
        layout = QVBoxLayout(panel)
        
        # Layers panel
        layers_group = QGroupBox("Layers")
        layers_layout = QVBoxLayout(layers_group)
        
        # Layer controls
        layer_controls = QHBoxLayout()
        add_layer_btn = QPushButton("Add")
        delete_layer_btn = QPushButton("Delete")
        move_up_btn = QPushButton("↑")
        move_down_btn = QPushButton("↓")
        
        layer_controls.addWidget(add_layer_btn)
        layer_controls.addWidget(delete_layer_btn)
        layer_controls.addWidget(move_up_btn)
        layer_controls.addWidget(move_down_btn)
        layers_layout.addLayout(layer_controls)
        
        # Layer list
        self.layer_tree = QTreeWidget()
        self.layer_tree.setHeaderLabels(["Name", "Visible", "Locked"])
        self.layer_tree.setRootIsDecorated(False)
        layers_layout.addWidget(self.layer_tree)
        
        layout.addWidget(layers_group)
        
        # Properties panel
        properties_group = QGroupBox("Properties")
        properties_layout = QVBoxLayout(properties_group)
        
        self.properties_scroll = QScrollArea()
        self.properties_widget = QWidget()
        self.properties_layout = QVBoxLayout(self.properties_widget)
        self.properties_scroll.setWidget(self.properties_widget)
        self.properties_scroll.setWidgetResizable(True)
        
        properties_layout.addWidget(self.properties_scroll)
        layout.addWidget(properties_group)
        
        # Code output
        code_group = QGroupBox("Generated Code")
        code_layout = QVBoxLayout(code_group)
        
        # Code format selection
        format_layout = QHBoxLayout()
        format_layout.addWidget(QLabel("Format:"))
        
        self.code_format = QComboBox()
        self.code_format.addItems(["Python", "CSS", "JSON"])
        self.code_format.currentTextChanged.connect(self._update_code_output)
        format_layout.addWidget(self.code_format)
        
        copy_btn = QPushButton("Copy")
        copy_btn.clicked.connect(self._copy_code)
        format_layout.addWidget(copy_btn)
        
        code_layout.addLayout(format_layout)
        
        # Code display
        self.code_display = QTextEdit()
        self.code_display.setReadOnly(True)
        self.code_display.setFont(QFont("Consolas", 9))
        self.code_display.setStyleSheet("""
            QTextEdit {
                background-color: #1e1e1e;
                color: #d4d4d4;
                border: 1px solid #333;
                padding: 8px;
            }
        """)
        code_layout.addWidget(self.code_display)
        
        layout.addWidget(code_group)
        
        # Connect layer manager signals
        self.layer_manager.layerChanged.connect(self._update_layer_tree)
        
        return panel
    
    def _on_tool_changed(self, button):
        """Handle tool change."""
        shape_type = button.property("shape_type")
        self.canvas.current_tool = shape_type
        logger.info(f"Tool changed to: {shape_type.name}")
    
    def _choose_color(self, color_key: str):
        """Open color dialog and update color."""
        color = QColorDialog.getColor()
        if color.isValid():
            # Update button color
            if color_key in self.color_buttons:
                self.color_buttons[color_key].setStyleSheet(
                    f"background-color: {color.name()}; border: 1px solid #333;"
                )
            
            # Store in theme data
            if 'colors' not in self.current_theme_data:
                self.current_theme_data['colors'] = {}
            
            self.current_theme_data['colors'][color_key] = {
                'r': color.red(),
                'g': color.green(),
                'b': color.blue(),
                'a': color.alpha()
            }
            
            self._update_code_output()
            logger.info(f"Color {color_key} updated to {color.name()}")
    
    def _generate_color_harmony(self):
        """Generate color harmony based on selected type."""
        if 'colors' not in self.current_theme_data or 'fill_color' not in self.current_theme_data['colors']:
            QMessageBox.warning(self, "Warning", "Please select a base fill color first.")
            return
        
        base_color_data = self.current_theme_data['colors']['fill_color']
        base_color = QColor(base_color_data['r'], base_color_data['g'], base_color_data['b'], base_color_data['a'])
        
        harmony_type = self.harmony_combo.currentText()
        
        if harmony_type == "Complementary":
            colors = self.color_palette.generate_complementary(base_color)
        elif harmony_type == "Triadic":
            colors = self.color_palette.generate_triadic(base_color)
        else:  # Analogous
            colors = self.color_palette.generate_analogous(base_color)
        
        # Update color buttons with harmony colors
        color_keys = ['fill_color', 'stroke_color', 'bg_color', 'text_color']
        for i, color in enumerate(colors[:len(color_keys)]):
            key = color_keys[i]
            self.current_theme_data['colors'][key] = {
                'r': color.red(),
                'g': color.green(),
                'b': color.blue(),
                'a': color.alpha()
            }
            
            if key in self.color_buttons:
                self.color_buttons[key].setStyleSheet(
                    f"background-color: {color.name()}; border: 1px solid #333;"
                )
        
        self._update_code_output()
        logger.info(f"Generated {harmony_type} color harmony")
    
    def _load_custom_fonts(self):
        """Load custom fonts from selected directory."""
        directory = QFileDialog.getExistingDirectory(
            self, "Select Custom Fonts Directory", os.path.expanduser("~")
        )
        
        if directory and directory not in self.custom_font_paths:
            self.custom_font_paths.append(directory)
            loaded_count = self._load_fonts_from_directory(directory)
            
            if loaded_count > 0:
                # Refresh font combo
                current_font = self.font_combo.currentFont()
                self.font_combo.clear()
                
                font_db = QFontDatabase()
                families = sorted(font_db.families())
                for family in families:
                    self.font_combo.addItem(family)
                
                # Restore selection
                index = self.font_combo.findText(current_font.family())
                if index >= 0:
                    self.font_combo.setCurrentIndex(index)
                
                QMessageBox.information(
                    self, "Success", 
                    f"Loaded {loaded_count} fonts from {directory}"
                )
            else:
                QMessageBox.warning(
                    self, "No Fonts Found",
                    f"No supported fonts found in {directory}"
                )
    
    def _new_project(self):
        """Create new project."""
        reply = QMessageBox.question(
            self, "New Project",
            "Are you sure you want to create a new project? Unsaved changes will be lost.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            self.layer_manager.layers.clear()
            self.current_theme_data.clear()
            self._update_layer_tree()
            self._update_code_output()
            self.canvas.update()
            logger.info("New project created")
    
    def _open_project(self):
        """Open project file."""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open Project", "", "Selene Theme Files (*.stheme);;JSON Files (*.json)"
        )
        
        if file_path:
            try:
                with open(file_path, 'r') as f:
                    data = json.load(f)
                
                self.current_theme_data = data.get('theme', {})
                # TODO: Load layers from data
                
                self._update_code_output()
                logger.info(f"Project loaded from {file_path}")
                
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load project: {str(e)}")
                logger.error(f"Failed to load project: {e}")
    
    def _save_project(self):
        """Save project file."""
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Project", "", "Selene Theme Files (*.stheme);;JSON Files (*.json)"
        )
        
        if file_path:
            try:
                project_data = {
                    'version': '1.0',
                    'theme': self.current_theme_data,
                    'layers': [asdict(layer) for layer in self.layer_manager.layers]
                }
                
                with open(file_path, 'w') as f:
                    json.dump(project_data, f, indent=2, default=str)
                
                logger.info(f"Project saved to {file_path}")
                
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save project: {str(e)}")
                logger.error(f"Failed to save project: {e}")
    
    def _export_theme(self):
        """Export theme in various formats."""
        file_path, file_type = QFileDialog.getSaveFileName(
            self, "Export Theme", "", 
            "Python Files (*.py);;CSS Files (*.css);;JSON Files (*.json)"
        )
        
        if file_path:
            try:
                if file_type == "Python Files (*.py)":
                    content = ThemeExporter.export_to_python(self.current_theme_data)
                elif file_type == "CSS Files (*.css)":
                    content = ThemeExporter.export_to_css(self.current_theme_data)
                else:  # JSON
                    content = ThemeExporter.export_to_json(self.current_theme_data)
                
                with open(file_path, 'w') as f:
                    f.write(content)
                
                logger.info(f"Theme exported to {file_path}")
                
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to export theme: {str(e)}")
                logger.error(f"Failed to export theme: {e}")
    
    def _toggle_grid(self, enabled: bool):
        """Toggle grid display."""
        self.canvas.grid_enabled = enabled
        self.canvas.update()
    
    def _update_layer_tree(self):
        """Update layer tree widget."""
        self.layer_tree.clear()
        
        for i, layer in enumerate(self.layer_manager.layers):
            item = QTreeWidgetItem()
            item.setText(0, layer.name)
            item.setCheckState(1, Qt.CheckState.Checked if layer.visible else Qt.CheckState.Unchecked)
            item.setCheckState(2, Qt.CheckState.Checked if layer.locked else Qt.CheckState.Unchecked)
            item.setData(0, Qt.ItemDataRole.UserRole, i)
            
            self.layer_tree.addTopLevelItem(item)
    
    def _update_code_output(self):
        """Update code output based on current format."""
        format_type = self.code_format.currentText()
        
        try:
            if format_type == "Python":
                code = ThemeExporter.export_to_python(self.current_theme_data)
            elif format_type == "CSS":
                code = ThemeExporter.export_to_css(self.current_theme_data)
            else:  # JSON
                code = ThemeExporter.export_to_json(self.current_theme_data)
            
            self.code_display.setPlainText(code)
            
        except Exception as e:
            self.code_display.setPlainText(f"Error generating code: {str(e)}")
            logger.error(f"Code generation error: {e}")
    
    def _copy_code(self):
        """Copy code to clipboard."""
        clipboard = QApplication.clipboard()
        clipboard.setText(self.code_display.toPlainText())
        logger.info("Code copied to clipboard")
    
    def _load_settings(self):
        """Load application settings."""
        self.restoreGeometry(self.settings.value("geometry", b""))
        
        # Load custom font paths
        font_paths = self.settings.value("custom_font_paths", [])
        if isinstance(font_paths, str):
            font_paths = [font_paths]
        
        for path in font_paths:
            if os.path.exists(path):
                self.custom_font_paths.append(path)
                self._load_fonts_from_directory(path)
    
    def _save_settings(self):
        """Save application settings."""
        self.settings.setValue("geometry", self.saveGeometry())
        self.settings.setValue("custom_font_paths", self.custom_font_paths)
    
    def closeEvent(self, event):
        """Handle application close."""
        self._save_settings()
        event.accept()

def main():
    """Main application entry point."""
    app = QApplication(sys.argv)
    app.setApplicationName("Selene Theme Stylizer Pro")
    app.setApplicationVersion("2.0.0")
    app.setOrganizationName("Selene Framework")
    
    # Set application icon (if available)
    # app.setWindowIcon(QIcon("icon.png"))
    
    # Apply dark theme
    app.setStyle("Fusion")
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
    palette.setColor(QPalette.ColorRole.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(0, 0, 0))
    palette.setColor(QPalette.ColorRole.ToolTipText, QColor(255, 255, 255))
    palette.setColor(QPalette.ColorRole.Text, QColor(255, 255, 255))
    palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ButtonText, QColor(255, 255, 255))
    palette.setColor(QPalette.ColorRole.BrightText, QColor(255, 0, 0))
    palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor(0, 0, 0))
    app.setPalette(palette)
    
    window = AdvancedThemeStyler()
    window.show()
    
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
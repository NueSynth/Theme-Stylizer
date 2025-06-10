# Selene Theme Stylizer Pro

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PyQt6](https://img.shields.io/badge/PyQt6-Required-green.svg)](https://pypi.org/project/PyQt6/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

**Selene Theme Stylizer Pro** is a professional-grade, comprehensive GUI theme and interface designer that empowers developers, designers, and accessibility experts to create, preview, and export sophisticated color schemes, typography configurations, and complete interface layouts. Built with PyQt6, this advanced tool provides real-time visual feedback, shape drawing capabilities, layer management, and generates production-ready code snippets for immediate integration into your projects.

Originally developed as part of the Selene Framework ecosystem, Theme Stylizer Pro is now available as a standalone utility that streamlines the complete design workflow for Qt-based applications and beyond.

---

## 🎨 Key Features

### Advanced Visual Design Tools
- **Professional Shape Drawing**: Rectangle, ellipse, polygon, star, speech bubble, and custom path creation
- **Layer Management System**: Complete z-order control, visibility toggles, and layer grouping
- **Interactive Canvas**: Zoom, pan, grid system with snap-to-grid functionality
- **Advanced Color Management**: Color harmony generation (complementary, triadic, analogous)
- **Gradient System**: Linear, radial, and conical gradients with multiple color stops
- **Typography Studio**: System and custom font integration with advanced spacing controls

### Professional Design Tools
- **Real-time Preview**: Live widget preview with actual PyQt6 components
- **Transform Tools**: Rotation, scaling, skewing, and reflection capabilities
- **Effects Engine**: Glow, drop shadow, outline, and blend mode effects
- **Animation System**: Property animations with easing curves and timing control
- **Asset Management**: Built-in icon library and custom asset integration

### Advanced Workflow Features
- **Multi-format Export**: Python, CSS, JSON, and SVG export capabilities
- **Project Management**: Save/load complete projects with version control
- **Template System**: Pre-built themes and component templates
- **Code Generation**: Real-time Python and CSS code output
- **Accessibility Tools**: WCAG contrast checking and color-blind simulation

### Professional UI Framework
- **Tabbed Interface**: Organized tool panels and property inspectors
- **Dockable Panels**: Customizable workspace layout
- **Layer Tree**: Visual hierarchy management with drag-and-drop
- **Properties Inspector**: Context-sensitive property editing
- **Dark Theme**: Professional dark UI optimized for design work

---

## 🚀 Quick Start Guide

### Prerequisites

Ensure your development environment meets these requirements:

- **Python 3.8 or higher**
- **PyQt6 library**

Install PyQt6 using pip:
```bash
pip install PyQt6
```

### Installation & Launch

1. **Download the application:**
   ```bash
   git clone https://github.com/NueSynth/Theme-Stylizer.git
   cd Theme-Stylizer
   ```

2. **Launch Theme Stylizer Pro:**
   ```bash
   python selene_theme_stylizer.py
   ```

3. **Start designing immediately** - the application auto-loads system fonts and provides a complete design environment!

---

## 📋 User Interface Guide

### Left Panel - Design Tools

**Shape Tools:**
- **Rectangle**: Basic and rounded rectangles with corner radius control
- **Ellipse**: Perfect circles and oval shapes
- **Polygon**: Custom polygon creation with configurable sides
- **Star**: Multi-pointed stars with inner/outer radius control
- **Line**: Straight lines with arrow heads and custom endpoints
- **Text**: Rich text with advanced typography controls

**Color Management:**
- **Fill Color**: Shape and element fill colors
- **Stroke Color**: Border and outline colors
- **Background**: Canvas and interface backgrounds
- **Text Color**: Typography color control
- **Harmony Generator**: Automatic color scheme generation

**Gradient Controls:**
- **Linear Gradients**: Direction and multi-stop control
- **Radial Gradients**: Center point and radius adjustment
- **Conical Gradients**: Angle-based color wheels
- **Color Stops**: Precise gradient point management

**Typography Studio:**
- **Font Family**: System and custom font selection
- **Font Properties**: Size, weight, style, and spacing
- **Text Effects**: Glow, shadow, outline, and 3D effects
- **Letter Spacing**: Character and line spacing control
- **Custom Font Loading**: Directory-based font integration

**Advanced Effects:**
- **Glow Effects**: Radius, color, and intensity control
- **Drop Shadows**: Offset, blur, and color customization
- **Blend Modes**: Multiple blending options for layer compositing
- **Opacity Control**: Fine-grained transparency adjustment

### Center Panel - Canvas & Preview

**Interactive Canvas:**
- **Drawing Area**: 1200x800 pixel canvas with zoom and pan
- **Grid System**: Configurable grid with snap-to-grid functionality
- **Shape Creation**: Click and drag to create shapes
- **Transform Handles**: Visual transformation controls
- **Layer Selection**: Click to select and modify shapes

**Live Preview:**
- **Widget Preview**: Real PyQt6 widget rendering
- **Theme Application**: Live theme preview on actual components
- **Interactive Testing**: Click, hover, and focus state testing
- **Responsive Preview**: Different screen size simulation

**Canvas Toolbar:**
- **File Operations**: New, open, save, and export projects
- **View Controls**: Zoom in/out, fit to window, grid toggle
- **Transform Tools**: Rotate, scale, align, and distribute
- **Layer Controls**: Move to front/back, group/ungroup

### Right Panel - Layers & Code

**Layer Management:**
- **Layer Tree**: Hierarchical layer organization
- **Visibility Control**: Show/hide individual layers
- **Lock System**: Prevent accidental layer modification
- **Z-Order Control**: Front/back layer positioning
- **Layer Properties**: Name, opacity, and blend mode editing

**Properties Inspector:**
- **Shape Properties**: Position, size, rotation, and color
- **Typography Properties**: Font, size, effects, and spacing
- **Effect Properties**: Glow, shadow, and blend settings
- **Custom Properties**: User-defined metadata

**Code Generation:**
- **Python Export**: Complete PyQt6 widget classes and theme objects
- **CSS Export**: Qt StyleSheet compatible CSS rules
- **JSON Export**: Structured theme data for external tools
- **Live Updates**: Real-time code generation as you design
- **Copy to Clipboard**: One-click code copying

---

## 🎯 Advanced Usage

### Professional Font Management

**System Font Integration:**
The application automatically loads fonts from your operating system:

- **Windows**: `C:\Windows\Fonts` and user fonts directory
- **macOS**: System, Library, and user fonts directories  
- **Linux**: `/usr/share/fonts`, `/usr/local/share/fonts`, and user fonts

**Custom Font Loading:**
1. Click **"Load Custom Fonts..."** in the Typography panel
2. Select any directory containing font files
3. Supported formats: `.ttf`, `.otf`, `.woff`, `.woff2`
4. Fonts are immediately available in the font selector
5. Custom font paths are saved with your project

**Font Management Features:**
- **Recursive Loading**: Automatically finds fonts in subdirectories
- **Duplicate Prevention**: Avoids loading the same directory twice
- **Error Handling**: Continues loading even if individual fonts fail
- **Live Updates**: Font list refreshes immediately when new fonts are added

### Advanced Shape Creation

**Shape Drawing Workflow:**
1. Select a shape tool from the left panel
2. Click and drag on the canvas to create the shape
3. Use transform handles to resize and rotate
4. Modify colors, gradients, and effects in real-time
5. Layer management for complex compositions

**Advanced Shape Features:**
- **Snap to Grid**: Automatic alignment to grid points
- **Proportional Scaling**: Hold Shift while resizing
- **Rotation**: Precise degree control with visual feedback
- **Custom Properties**: Add metadata and custom attributes

### Layer Management System

**Layer Organization:**
- **Hierarchical Structure**: Group related elements
- **Visual Indicators**: Icons show layer type and status  
- **Drag and Drop**: Reorder layers by dragging in the tree
- **Bulk Operations**: Select multiple layers for group actions

**Advanced Layer Features:**
- **Blend Modes**: Control how layers interact visually
- **Opacity Control**: Per-layer transparency settings
- **Lock/Unlock**: Prevent accidental modifications
- **Visibility Toggle**: Temporarily hide layers during design

### Project Workflow

**Project Management:**
- **Save Projects**: Complete project state in `.stheme` format
- **Version Control**: Track changes and maintain project history
- **Template System**: Save and reuse common design patterns
- **Export Options**: Multiple output formats for different use cases

**Integration Workflows:**

**For Qt/PyQt Applications:**
1. Design your complete interface in the visual editor
2. Export as Python code with complete widget classes
3. Import generated classes directly into your application
4. Apply themes using the generated theme objects

**For Web Development:**
1. Create color schemes and typography in the visual editor
2. Export as CSS with Qt StyleSheet syntax
3. Convert to standard CSS for web use
4. Use generated color values in your CSS framework

**For Design Systems:**
1. Create comprehensive color palettes and typography scales
2. Export as JSON for design system documentation
3. Generate style guides with accessibility information
4. Share themes across team members and projects

---

## ♿ Accessibility Features

Selene Theme Stylizer Pro includes comprehensive accessibility tools:

### Visual Accessibility Tools
- **WCAG Contrast Checker**: Real-time contrast ratio calculation
- **Color Blind Simulation**: Preview themes with different types of color blindness
- **High Contrast Testing**: Verify readability in high contrast mode
- **Font Legibility Assessment**: Test typography across different weights and sizes

### Inclusive Design Features
- **Accessibility Warnings**: Built-in alerts for problematic color combinations
- **Font Recommendations**: Suggestions for accessible font choices
- **Size Guidelines**: Minimum size recommendations for text and interactive elements
- **Color Alternative Suggestions**: Alternative colors that meet accessibility standards

### Compliance Tools
- **WCAG 2.1 Compliance**: Built-in checking for AA and AAA standards
- **Section 508 Support**: Federal accessibility standard compliance
- **Export Metadata**: Include accessibility information in exported themes
- **Documentation Generation**: Automatic accessibility documentation

---

## 💻 Technical Specifications

### System Requirements
- **Operating System**: Windows 10+, macOS 10.14+, Linux (Ubuntu 18.04+)
- **Python Version**: 3.8, 3.9, 3.10, 3.11, 3.12
- **Memory**: 512MB RAM minimum, 1GB recommended
- **Display**: 1600x1200 minimum resolution for optimal experience
- **Storage**: 100MB free space for application and projects

### Dependencies
- **PyQt6**: Complete GUI framework and widgets
- **Python Standard Library**: os, sys, logging, typing, json, xml, math
- **Optional**: Additional font libraries for extended font support

### Performance Specifications
- **Startup Time**: < 3 seconds on modern hardware
- **Real-time Updates**: 60 FPS refresh rate for smooth interaction
- **Memory Usage**: ~100MB typical operation with large projects
- **Export Speed**: < 1 second for code generation
- **Canvas Performance**: Handles 1000+ shapes with smooth interaction

### File Format Support
- **Project Files**: `.stheme` (JSON-based project format)
- **Export Formats**: `.py`, `.css`, `.json`, `.svg`, `.png`
- **Font Formats**: `.ttf`, `.otf`, `.woff`, `.woff2`
- **Import Formats**: `.stheme`, `.json` (theme data)

---

## 🔧 Troubleshooting

### Common Issues & Solutions

**"PyQt6 module not found"**
```bash
# Solution: Install PyQt6
pip install --upgrade PyQt6
```

**"Application interface is too small"**
- Increase display scaling in system settings
- Use zoom controls in the canvas toolbar
- Adjust window size and panel ratios

**"Custom fonts not loading"**
- Verify font files are in correct format (.ttf, .otf)
- Check file permissions are readable
- Use "Load Custom Fonts..." button instead of manual directory
- Restart application if fonts still don't appear

**"Canvas performance is slow"**
- Reduce number of visible layers
- Disable grid if not needed
- Close other graphics-intensive applications
- Reduce canvas zoom level

**"Export code contains errors"**
- Verify all colors are properly selected
- Check that gradients have at least 2 color stops
- Ensure layer names don't contain special characters
- Try exporting in different format (Python vs CSS)

### Advanced Troubleshooting

**Memory Issues:**
- Close unused projects
- Reduce canvas size for complex projects
- Limit number of gradient stops
- Disable real-time preview for very complex themes

**Display Issues:**
- Update graphics drivers
- Try different PyQt6 versions: `pip install PyQt6==6.4.0`
- Disable hardware acceleration if available
- Use software rendering mode

**Font Issues:**
- Clear font cache: Delete `~/.cache/fontconfig/` (Linux) or similar
- Reinstall problematic fonts
- Use system font directories instead of custom paths
- Check font licensing for distribution rights

---

## 🤝 Contributing

We welcome contributions from designers, developers, and accessibility experts!

### Areas for Contribution

**New Features:**
- Additional shape tools (bezier curves, custom paths)
- Animation timeline editor
- More export formats (Sketch, Figma)
- Plugin system for custom tools

**Design Improvements:**
- UI/UX enhancements
- Icon design and illustrations
- Documentation graphics
- Video tutorials and demos

**Accessibility:**
- Screen reader compatibility improvements
- Keyboard navigation enhancements  
- Voice control integration
- Alternative input method support

**Code Quality:**
- Performance optimizations
- Code refactoring and cleanup
- Additional unit tests
- Documentation improvements

### Development Setup

1. **Fork and Clone:**
   ```bash
   git clone https://github.com/your-username/Theme-Stylizer.git
   cd Theme-Stylizer
   ```

2. **Create Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   venv\Scripts\activate  # Windows
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   pip install -e .  # Development install
   ```

4. **Run Tests:**
   ```bash
   python -m pytest tests/
   ```

### Code Contribution Guidelines

- **Code Style**: Follow PEP 8 and use type hints
- **Documentation**: Document all public methods and classes
- **Testing**: Add tests for new functionality
- **Commits**: Use conventional commit messages
- **Pull Requests**: Include detailed description and screenshots

---

## 📄 License & Legal

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for complete details.

### Third-Party Acknowledgments
- **PyQt6**: Cross-platform GUI toolkit (Riverbank Computing Limited)
- **Qt Framework**: Application development framework (The Qt Company)
- **System Fonts**: Respective font foundries and designers

### Trademark Notice
"Selene" and "Selene Framework" are trademarks of NueSynth. This software is part of the open-source Selene ecosystem.

### Usage Rights
- ✅ Commercial use permitted
- ✅ Private use permitted  
- ✅ Modification permitted
- ✅ Distribution permitted
- ❌ No warranty provided
- ❌ No liability accepted

---

## 🔗 Resources & Links

### Documentation & Tutorials
- [Selene Framework Documentation](https://docs.selene-framework.org)
- [PyQt6 Official Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt6/)
- [Qt StyleSheet Reference](https://doc.qt.io/qt-6/stylesheet-reference.html)
- [Theme Design Best Practices](https://docs.selene-framework.org/theming)
- [Accessibility Guidelines](https://docs.selene-framework.org/accessibility)

### Community & Support
- [GitHub Repository](https://github.com/NueSynth/Theme-Stylizer)
- [Issue Tracker](https://github.com/NueSynth/Theme-Stylizer/issues)
- [Discussions Forum](https://github.com/NueSynth/Theme-Stylizer/discussions)
- [Discord Community](https://discord.gg/selene-framework)
- [Stack Overflow Tag](https://stackoverflow.com/questions/tagged/selene-theme-stylizer)

### Related Projects & Tools
- [Selene Framework](https://github.com/NueSynth/Selene-Framework) - Complete application framework
- [Qt Design Studio](https://www.qt.io/product/ui-design-tools) - Official Qt design tools
- [PyQt Examples](https://github.com/pyqt/examples) - PyQt code examples
- [Material Design](https://material.io/design) - Google's design system
- [Fluent Design](https://www.microsoft.com/design/fluent/) - Microsoft's design system

### Educational Resources
- [Color Theory for Developers](https://docs.selene-framework.org/color-theory)
- [Typography in UI Design](https://docs.selene-framework.org/typography)
- [Accessibility in Design](https://docs.selene-framework.org/accessibility-design)
- [PyQt6 Best Practices](https://docs.selene-framework.org/pyqt-best-practices)

---

## 📞 Support & Contact

### Getting Help
1. **Documentation**: Check this README and linked documentation first
2. **Community**: Post questions in GitHub Discussions or Discord
3. **Bug Reports**: Use the GitHub Issues tracker with detailed reproduction steps
4. **Feature Requests**: Submit enhancement requests with use cases and mockups

### Professional Services
For enterprise support, custom development, training, or integration assistance:

- **Email**: support@nuesynth.com
- **Website**: [www.nuesynth.com](https://www.nuesynth.com)
- **Enterprise Portal**: [enterprise.selene-framework.org](https://enterprise.selene-framework.org)

**Enterprise Services Include:**
- Custom theme development
- Team training and workshops
- Integration consulting
- Priority support and maintenance
- Custom feature development

### Security & Privacy
For security vulnerabilities or privacy concerns:
- **Security Email**: security@selene-framework.org
- **GPG Key**: Available on our website
- **Responsible Disclosure**: 90-day disclosure timeline

---

**Made with ❤️ by the Selene Framework Team**

*Empowering designers and developers to create beautiful, accessible interfaces since 2024*

---

## 🎯 Version History

**v2.0.0 - Current (Pro Release)**
- Complete application rewrite with advanced features
- Professional shape drawing and layer management
- Advanced typography and effects system
- Multi-format export capabilities
- Accessibility tools and WCAG compliance

**v1.0.0 - Initial Release**
- Basic color and font selection
- Simple preview system
- Python code generation
- Custom font loading

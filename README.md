# Selene Theme Stylizer

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PyQt6](https://img.shields.io/badge/PyQt6-Required-green.svg)](https://pypi.org/project/PyQt6/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

**Selene Theme Stylizer** is a professional-grade, interactive GUI theme designer that empowers developers, designers, and accessibility experts to create, preview, and export custom color schemes and typography configurations. Built with PyQt6, this tool provides real-time visual feedback and generates production-ready code snippets for immediate integration into your projects.

Originally developed as part of the Selene Framework ecosystem, Theme Stylizer is now available as a standalone utility that streamlines the theme development workflow for Qt-based applications and beyond.

---

## 🎨 Key Features

### Visual Design Tools
- **Intuitive Color Palette Management**: Interactive color pickers for backgrounds, foregrounds, text, and special effects
- **Advanced Dropdown Styling**: Granular control over dropdown menus, selections, highlights, and text colors
- **Typography Customization**: System and custom font selection with size control and text effect toggles
- **Real-time Glow Effects**: Adjustable glow radius and color for enhanced visual appeal
- **Global Opacity Control**: Fine-tune transparency across all interface elements

### Professional Workflow
- **Live Preview Canvas**: Instant visualization of your theme applied to sample interface components
- **Multi-format Code Export**: Generate Python (PyQt/PySide) and CSS/Qt StyleSheet code snippets
- **Custom Font Integration**: Automatic loading of TrueType fonts from designated directories
- **Accessibility Testing**: Built-in tools for contrast evaluation and readability assessment

### Developer-Friendly Output
- **Production-Ready Code**: Copy-paste snippets that integrate seamlessly into existing projects
- **Multiple Format Support**: Python QColor objects, RGBA values, and CSS equivalents
- **Comprehensive Configuration**: Export complete theme definitions including fonts, effects, and transparency

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

2. **Launch the Theme Stylizer:**
   ```bash
   python selene_theme_stylizer.py
   ```

3. **Start designing immediately** - no additional configuration required!

---

## 📋 User Interface Guide

### Main Color Controls
Located in the top section of the interface:

- **Background**: Primary interface background color
- **Foreground**: Secondary element background (chat areas, content panels)
- **Text**: Primary text color for optimal readability
- **Glow Color**: Special effect color for text enhancement

### Dropdown Styling Panel
Specialized controls for dropdown menu appearance:

- **Dropdown Selected BG**: Background color of the selected dropdown item
- **Dropdown Selected Text**: Text color when an item is highlighted
- **Dropdown Menu BG**: Background color of the dropdown menu itself
- **Dropdown Menu Text**: Default text color for dropdown options
- **Dropdown Highlight**: Hover/focus highlight color

### Typography & Effects Section

**Font Configuration:**
- **Font Family**: Choose from system fonts or loaded custom fonts
- **Font Size**: Adjustable from 8pt to 72pt with live preview
- **Sample Text**: Customize preview text (up to 25 characters)

**Text Effects Toggles:**
- ☐ **Bold**: Apply bold weight to text
- ☐ **Italic**: Apply italic styling
- ☐ **Underline**: Add underline decoration
- ☐ **Strike-through**: Add strikethrough decoration
- ☐ **Glow Effect**: Enable/disable glow effects

### Advanced Controls

**Opacity Slider (0-255):**
Controls global transparency for all themed elements. Lower values create more transparent interfaces.

**Glow Radius Slider (0-30px):**
Adjusts the intensity and spread of glow effects when enabled.

### Live Preview Area
The center display shows your theme applied to:
- Sample background with your chosen colors
- Text rendered with selected fonts and effects
- Real-time updates as you modify settings

### Code Export Panel
The bottom panel automatically generates:
- **Python Configuration**: QColor objects and settings variables
- **Font Settings**: Complete typography configuration
- **CSS Equivalents**: Ready-to-use stylesheet rules
- **Effect Parameters**: Glow and opacity settings

---

## 🎯 Advanced Usage

### Custom Font Integration

1. **Create the fonts directory:**
   ```bash
   mkdir -p gui/fonts
   ```

2. **Add TrueType fonts:**
   Place your `.ttf` files in the `gui/fonts/` directory

3. **Automatic loading:**
   Fonts are automatically detected and added to the font selector on startup

**Supported font formats:** TrueType (.ttf)

### Workflow Integration

**For Qt/PyQt Projects:**
1. Design your theme using the visual interface
2. Copy the Python configuration code from the export panel
3. Paste directly into your application's theming module
4. Apply colors using the generated QColor objects

**For Web/CSS Projects:**
1. Use the CSS/StyleSheet section of the export panel
2. Copy the generated CSS rules
3. Integrate into your stylesheet or CSS-in-JS solution

**For Documentation:**
1. Use the RGB/RGBA values for design system documentation
2. Export font configurations for typography guidelines
3. Document accessibility compliance using the preview tools

---

## ♿ Accessibility Features

Selene Theme Stylizer includes built-in accessibility considerations:

### Visual Accessibility
- **Real-time Contrast Preview**: See how color combinations affect readability
- **Transparency Testing**: Evaluate interface clarity across different opacity levels
- **Font Legibility Assessment**: Test typography choices with various text effects

### Inclusive Design Tools
- **High Contrast Testing**: Verify your themes work for users with visual impairments
- **Font Weight Experimentation**: Ensure text remains readable across different weights
- **Effect Moderation**: Balance visual appeal with functional accessibility

### Best Practices Integration
- Export configurations include accessibility metadata
- Built-in warnings for potentially problematic color combinations
- Support for accessibility-compliant font choices

---

## 💻 Technical Specifications

### System Requirements
- **Operating System**: Windows 10+, macOS 10.14+, Linux (Ubuntu 18.04+)
- **Python Version**: 3.8, 3.9, 3.10, 3.11, 3.12
- **Memory**: 256MB RAM minimum
- **Display**: 1200x900 minimum resolution

### Dependencies
- **PyQt6**: GUI framework and widgets
- **Python Standard Library**: os, sys, logging, typing

### Performance
- **Startup Time**: < 2 seconds on modern hardware
- **Real-time Updates**: < 16ms refresh rate for smooth interaction
- **Memory Usage**: ~50MB typical operation

---

## 🔧 Troubleshooting

### Common Issues & Solutions

**"PyQt6 module not found"**
```bash
# Solution: Install PyQt6
pip install --upgrade PyQt6
```

**"Custom fonts not appearing"**
- Verify `.ttf` files are in `gui/fonts/` directory
- Check file permissions are readable
- Restart the application after adding fonts

**"Application won't start"**
- Confirm Python 3.8+ is installed: `python --version`
- Check PyQt6 installation: `python -c "import PyQt6"`
- Run from command line to see error messages

**"Preview not updating"**
- Click in the preview area to refresh
- Check if any modal dialogs are open
- Restart the application if issues persist

### Performance Optimization

**For slower systems:**
- Reduce glow radius to improve rendering speed
- Minimize simultaneous color changes
- Close other graphics-intensive applications

**For better responsiveness:**
- Use fonts already installed on your system
- Limit preview text length
- Avoid extremely high opacity values during testing

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### Bug Reports
1. Check existing [issues](https://github.com/NueSynth/Theme-Stylizer/issues)
2. Provide detailed reproduction steps
3. Include system information and Python version
4. Attach screenshots if applicable

### Feature Requests
- Describe the use case and benefits
- Provide mockups or examples if possible
- Consider accessibility implications
- Discuss implementation approaches

### Code Contributions
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Follow existing code style and conventions
4. Add tests for new functionality
5. Submit a pull request with detailed description

### Accessibility Improvements
We especially welcome contributions that enhance accessibility:
- Screen reader compatibility
- Keyboard navigation improvements
- Color blind-friendly features
- High contrast mode support

---

## 📄 License & Legal

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Third-Party Acknowledgments
- **PyQt6**: Cross-platform GUI toolkit (Riverbank Computing)
- **Qt Framework**: Application development framework (The Qt Company)

### Trademark Notice
"Selene" and "Selene Framework" are trademarks of NueSynth. This software is part of the open-source Selene ecosystem.

---

## 🔗 Resources & Links

### Documentation
- [Selene Framework Documentation](https://docs.selene-framework.org)
- [PyQt6 Official Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt6/)
- [Qt StyleSheet Reference](https://doc.qt.io/qt-6/stylesheet-reference.html)

### Community
- [GitHub Repository](https://github.com/NueSynth/Theme-Stylizer)
- [Issue Tracker](https://github.com/NueSynth/Theme-Stylizer/issues)
- [Discussions](https://github.com/NueSynth/Theme-Stylizer/discussions)

### Related Projects
- [Selene Framework](https://github.com/NueSynth/Selene-Framework)
- [Qt Design Studio](https://www.qt.io/product/ui-design-tools)
- [PyQt Examples Collection](https://github.com/pyqt/examples)

---

## 📞 Support & Contact

### Getting Help
1. **Documentation**: Check this README and linked resources first
2. **Community**: Post questions in GitHub Discussions
3. **Bug Reports**: Use the GitHub Issues tracker
4. **Security Issues**: Email security@selene-framework.org

### Professional Support
For enterprise support, custom development, or integration assistance, contact:
- **Email**: support@nuesynth.com
- **Website**: [www.nuesynth.com](https://www.nuesynth.com)

---

**Made with ❤️ by the Selene Framework Team**

*Empowering developers to create beautiful, accessible interfaces since 2024*

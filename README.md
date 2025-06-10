# Selene Theme Stylizer (`selene_theme_stylizer.py`)

**Selene Theme Stylizer** is a modern, user-friendly graphical tool for designing, previewing, and exporting custom color and font schemes for GUIs and applications. Built with PyQt6, this rebooted version offers a streamlined interface and advanced features for effortless theme creation and code export.

Originally developed as part of the Selene Framework, Theme Stylizer is now a fully stand-alone utility for designers, developers, and accessibility experts.

---

## Features

- **Visual Color Selection:**  
  Pick and preview background, foreground, text, glow, and dropdown colors with intuitive dialogs.
- **Dropdown & Menu Styling:**  
  Style dropdowns with separate controls for selected, menu, highlight, and text colors.
- **Font Customization:**  
  Choose from system and custom fonts, set size, and toggle bold, italic, underline, and strike-through.
- **Glow & Effects:**  
  Add glow effects to text with adjustable color and radius; control global opacity for all elements.
- **Live Preview:**  
  Instantly see your theme applied to a sample interface and dropdown.
- **Code Export:**  
  Generate ready-to-use Python and CSS/Qt stylesheet snippets reflecting your current selections.
- **Accessibility Tools:**  
  Adjust alpha/transparency, preview contrast, and experiment with fonts for clarity and inclusivity.

---

## Getting Started

### 1. Prerequisites

- **Python 3.8+**  
- **PyQt6**  
  Install via pip:
  ```bash
  pip install PyQt6
  ```

### 2. Download

Download `selene_theme_stylizer.py` and (optionally) the `gui/fonts/` directory for custom fonts.

### 3. Run the Tool

```bash
python selene_theme_stylizer.py
```

### 4. Interface Overview

- **Color Pickers:**  
  Use the top rows of buttons to select colors for backgrounds, text, dropdown elements, and highlight effects.
- **Font & Text:**  
  Choose a font, set its size, and enter sample text to see how your style will appear.
- **Dropdown Preview:**  
  Interactively preview and style a dropdown (combo box).
- **Text Effects:**  
  Toggle bold, italic, underline, strike-through, and glow effects.
- **Glow & Opacity Controls:**  
  Adjust the strength of glow and the overall opacity of interface elements.
- **Live Sample:**  
  View a real-time sample of your design, including all selected effects and colors.
- **Code Display:**  
  Copy out the generated code for immediate use in your own PyQt or Qt-based project.

---

## Custom Fonts

To use custom fonts, place `.ttf` files in the `gui/fonts/` directory (create this directory if it does not exist). The tool will automatically load any valid TTF font files.

---

## Exporting Your Scheme

At the bottom of the tool you’ll find a pane displaying:

- **Python code:**  
  Instantly usable color and font configuration snippets.
- **CSS/StyleSheet equivalents:**  
  Quick copy-paste for Qt style sheets or web preview.

---

## Accessibility

Selene Theme Stylizer is designed to help ensure your interfaces are visually accessible and inclusive:

- **Transparency Controls:**  
  Adjust alpha channels to test clarity against varied backgrounds.
- **Live Contrast Preview:**  
  Instantly see how your color and font combinations affect readability.
- **Font Customization:**  
  Experiment with various font faces and weights to ensure clarity for all users.

---

## Contribution

Contributions, feedback, and accessibility suggestions are welcome! Please open an issue or submit a pull request on the [repository](https://github.com/NueSynth/Selene-Framework).

---

## Acknowledgments

Developed as part of the [Selene Framework](https://github.com/NueSynth/Selene-Framework).  
Thanks to the open-source PyQt community for making GUI development accessible and powerful.

---

## Troubleshooting

- **PyQt6 Not Found:**  
  Ensure you have installed PyQt6 (`pip install PyQt6`).
- **Fonts Not Loading:**  
  Double-check your `.ttf` files are in `gui/fonts/` relative to the script.
- **GUI Won't Launch:**  
  Make sure you are running Python 3.8 or higher.

---

## Screenshots

*(Add screenshots of the tool in use for higher engagement and clarity!)*

---

## Contact

For feature requests or support, please [open an issue](https://github.com/NueSynth/Selene-Framework/issues) or contact the maintainer via GitHub.

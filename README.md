
# 🧶 Crochet Pattern Tracker

A Python-based tool that converts images into pixelated crochet patterns and visualizes them as stitch grids. Perfect for planning tapestry crochet projects like scarves, sweaters, or wall art — and eventually, tracking stitch progress row-by-row.

---

## ✨ Features

- 🖼️ Convert images to crochet stitch grids
- 🎨 Supports custom stitch dimensions (e.g. `sc`, `hdc`, `dc`)
- 🔲 Pixel-perfect pattern visualization
- 📄 Extracts color-coded patterns row by row
- 🔁 Reversible rows to match crochet direction (bottom-up)
- 🧵 Designed with tapestry crochet in mind

---

## 🗂️ Project Structure

```
crochet-tracker/
├── main.py                  # Entry point: pixelate, extract, visualize
├── visualizer.py            # Grid rendering with Matplotlib
├── image_tools.py           # Image pixelation and pattern extraction
├── pattern_parser.py        # Optional: text pattern parser
├── testpattern.txt          # Example pattern file
```

---

## 🧪 How to Run

1. Install dependencies:
   ```bash
   pip install matplotlib pillow
   ```

2. Run the main script:
   ```bash
   python main.py
   ```

3. Modify `main.py` to change:
   - Input image
   - Grid size (stitch count)
   - Stitch type

---

## 🚧 Planned Features

- 🖱️ Interactive stitch tracker UI
- 🔄 Undo/redo functionality
- 💾 Save/load pattern progress
- 🧶 Map colors to yarn palettes

---

## 🤝 Contributions

Suggestions, issues, and PRs welcome! Feel free to fork and customize for your own crochet projects 🎨🪡


---



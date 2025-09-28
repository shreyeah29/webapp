Investor Pitch Deck Generator
=============================

Quick start
-----------

1) Ensure dependencies are installed (already handled by the automation you ran):

```bash
/workspace/.venv/bin/python -m pip install python-pptx pillow
```

2) Generate the deck:

```bash
/workspace/.venv/bin/python /workspace/generate_pitch_deck.py
```

This will create `/workspace/Investor_Pitch_Deck.pptx`.

Customize
---------

- Open `generate_pitch_deck.py` and update:
  - Company name and tagline in `build_pitch_deck(...)` call
  - Slide content in the sections (Problem, Solution, Market, etc.)
  - Colors via `THEME_PRIMARY`, `THEME_SECONDARY`, `THEME_ACCENT`, `THEME_TEXT`

- Add your logo:
  - Replace the "Your Logo" rounded rectangle on the title slide with an image in PowerPoint, or extend the script to insert an image using `slide.shapes.add_picture(...)`.

Slides included (18)
-------------------

1. Title
2. Problem
3. Solution
4. Market Size (chart)
5. Product (2-column)
6. Business Model
7. Traction (chart)
8. Competitive Landscape (table)
9. Defensibility (Moat)
10. Go-To-Market
11. Roadmap (timeline)
12. Unit Economics (chart)
13. 3-Year Projections (chart)
14. Team
15. The Ask
16. Use of Funds (table)
17. Milestones (timeline)
18. Thank You / Contact

Tips
----

- Keep text concise. Aim for ~3 bullets per slide, max 6.
- Replace the illustrative numbers with your own data.
- Ensure font choices are available on the presenting machine (defaults to Calibri).


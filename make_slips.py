"""Generate a printable A4 sheet of numbered slips for the pairing activity.

    python3 make_slips.py [count] [output.pdf]

Defaults to 20 slips on a single page, 4 across by 5 down.
"""
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

MAROON = (0x77 / 255, 0x24 / 255, 0x32 / 255)
GREY = (0.55, 0.55, 0.55)
CUT = (0.72, 0.72, 0.72)

COLS, ROWS = 4, 5
MARGIN = 12 * mm


def draw_page(c, numbers, page_w, page_h):
    cell_w = (page_w - 2 * MARGIN) / COLS
    cell_h = (page_h - 2 * MARGIN) / ROWS

    # dashed cut guides across the whole block
    c.setStrokeColorRGB(*CUT)
    c.setLineWidth(0.5)
    c.setDash(2, 3)
    for i in range(COLS + 1):
        x = MARGIN + i * cell_w
        c.line(x, MARGIN, x, page_h - MARGIN)
    for j in range(ROWS + 1):
        y = MARGIN + j * cell_h
        c.line(MARGIN, y, page_w - MARGIN, y)
    c.setDash()

    for idx, n in enumerate(numbers):
        col = idx % COLS
        row = idx // COLS
        cx = MARGIN + col * cell_w + cell_w / 2
        top = page_h - MARGIN - row * cell_h
        cy = top - cell_h / 2

        c.setFillColorRGB(*GREY)
        c.setFont("Helvetica", 6.5)
        c.drawCentredString(cx, top - 13 * mm, "CHILDHOOD MEMORIES")

        c.setFillColorRGB(*MAROON)
        size = 82
        c.setFont("Times-Bold", size)
        c.drawCentredString(cx, cy - size * 0.34, str(n))

        c.setFillColorRGB(*GREY)
        c.setFont("Helvetica", 6.5)
        c.drawCentredString(cx, MARGIN + (ROWS - 1 - row) * cell_h + 11 * mm,
                            "keep this number all session")


def main():
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    out = sys.argv[2] if len(sys.argv) > 2 else "pairing-slips.pdf"
    page_w, page_h = A4

    c = canvas.Canvas(out, pagesize=A4)
    c.setTitle("Pairing slips — Childhood Memories")
    per_page = COLS * ROWS
    for start in range(0, count, per_page):
        draw_page(c, range(start + 1, min(start + per_page, count) + 1), page_w, page_h)
        c.showPage()
    c.save()
    print("wrote %s (%d slips)" % (out, count))


if __name__ == "__main__":
    main()

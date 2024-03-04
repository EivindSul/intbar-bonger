# Simple file to learn and test functionality of reportlab
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

pdf_path = "littbong.pdf"
c = canvas.Canvas(pdf_path, pagesize=A4)

cm = A4[0] / 21.0
margin_y = 1 * cm
margin_x = 0.5 * cm

dark_red = (0.7, 0, 0)
black = (0, 0, 0)
white = (1, 1, 1)

line_width = 1

bong_count_x = 10
bong_count_y = 5

bong_size_x = 45
bong_size_y = 155

margin_x = (A4[0] - (bong_size_x * bong_count_x)) / (bong_count_x + 1)
margin_y = (A4[1] - (bong_size_y * bong_count_y)) / (bong_count_y + 1)

id_box_size = 15 # Size of the rounded off part at the end of the bong

logo = ImageReader("assets/intbar-logo.png")
logo_scale_factor = 0.12
logo_size_x = logo.getSize()[0] * logo_scale_factor
logo_size_y = logo.getSize()[1] * logo_scale_factor

def draw_bongs():

    c.setStrokeColorRGB(*dark_red)
    c.setFillColorRGB(*white)
    c.setLineWidth(line_width)
    c.translate(margin_x, margin_y)

    for row in range(bong_count_y):
        c.saveState()
        c.translate(0, row * (bong_size_y + margin_y))
        for _ in range(bong_count_x):
            draw_bong_front(c)
            c.translate(margin_x + bong_size_x, 0)
        c.restoreState()

    c.showPage()

    c.setStrokeColorRGB(*dark_red)
    c.setFillColorRGB(*white)
    c.setLineWidth(line_width)
    c.translate(margin_x, margin_y)

    for row in range(bong_count_y):
        c.saveState()
        c.translate(0, row * (bong_size_y + margin_y))
        for _ in range(bong_count_x):
            draw_bong_back(c)
            c.translate(margin_x + bong_size_x, 0)
        c.restoreState()

    c.save()


def draw_bong_front(c):
    c.roundRect(0, 0, bong_size_x, bong_size_y, 5)
    c.rect(0, id_box_size, bong_size_x, bong_size_y - 2 * id_box_size)
    c.saveState()
    c.setFillColorRGB(*black)
    c.translate(bong_size_x / 2, bong_size_y / 2)
    c.rotate(90)
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(5 + (logo_size_x / 2), 7, "Integrerbar")
    c.drawImage(logo, -37, 7, logo_size_x, logo_size_y, mask=[0,0,0,0,0,0])
    c.setFont("Helvetica", 8)
    c.drawCentredString(0, -8, "Verdi: 65kr")
    c.drawCentredString(0, -18, "Gyldig til: 29-02-2024")
    c.rotate(90)
    c.setFont("Helvetica", 12)
    c.drawCentredString(0, (bong_size_y / 2) - 12, "A001")
    c.rotate(180)
    c.drawCentredString(0, (bong_size_y / 2) - 12, "A001")
    c.restoreState()

def draw_bong_back(c):
    c.roundRect(0, 0, bong_size_x, bong_size_y, 5)
    c.saveState()
    c.setFillColorRGB(*black)
    c.translate(bong_size_x / 2, bong_size_y / 2)
    c.rotate(90)
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(0, -6, "A001-10101")
    c.restoreState()

draw_bongs()

# Simple file to learn and test functionality of reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def draw_red_rectangles(pdf_file_path):
    # Create a canvas
    c = canvas.Canvas(pdf_file_path, pagesize=A4)

    cm = A4[0] / 21.0
    margin_x = 1 * cm
    margin_y = 0.5 * cm

    # Set the border color to red
    border_color = (0.7, 0, 0)

    # Set the fill color to white
    fill_color = (1, 1, 1)

    # Set the line width for the border
    line_width = 1

    bong_width = 1.55 * cm
    bong_height = 4.74 * cm

    # Draw the first red rectangle with a red border
    c.setStrokeColorRGB(*border_color)
    c.setFillColorRGB(*fill_color)
    c.setLineWidth(line_width)
    c.translate(margin_y, 0)
    # c.roundRect(0, 0, bong_width, bong_height, 5, fill=True)
    # c.rect(0, 15, bong_width, bong_height - 30, fill=True)
    text_color = (0, 0, 0)

    for row in range(5):
        c.saveState()
        c.translate(0, row*(bong_height + margin_x) + margin_y)
        for _ in range(10):
            c.setFillColorRGB(*fill_color)
            c.roundRect(0, 0, bong_width, bong_height, 5, fill=True)
            c.rect(0, 15, bong_width, bong_height - 30, fill=True)

            # Write text
            c.saveState()
            c.setFillColorRGB(*text_color)
            c.setFont("Helvetica-Bold", 15)
            c.drawCentredString(0, 0, ".")
            c.rotate(90)
            c.setFont("Helvetica-Bold", 12)
            c.drawString(50, -15, "Integerbar")
            c.setFont("Helvetica", 8)
            c.drawString(30, -25, "Verdi: 65kr")
            c.drawString(20, -35, "Gyldig til: 29-02-2024")
            c.rotate(90)
            c.setFont("Helvetica", 12)
            c.drawString(-35, -12, "A001")
            c.translate(bong_height - 4, bong_width - 15)
            c.rotate(180)
            c.setFont("Helvetica-Bold", 15)
            c.drawCentredString(0, 0, ".")
            c.setFont("Helvetica", 12)
            c.drawString(-35, -12, "A001")
            # c.rotate(180)
            # c.drawString(0, 0, "A001")
            c.restoreState()

            c.translate(bong_width + margin_y, 0)
        c.restoreState()


    # Draw rotated text inside the first rectangle
    # c.translate(125, 525)
    # c.rotate(rotation_angle)
    # c.setFillColorRGB(*text_color)
    # c.drawString(0, 0, "Tekst 1")

    # Reset the rotation for the second rectangle

    # Save the PDF file
    c.save()

# Specify the path where you want to save the PDF
pdf_path = "red_rectangles_updated.pdf"

# Call the function to draw red rectangles and save the PDF
draw_red_rectangles(pdf_path)

from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import datetime, timedelta
import math
import random

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

box_size = (A4[1] - 2 * margin_y) / 20

margin_x = (A4[0] - (bong_size_x * bong_count_x)) / (bong_count_x + 1)
margin_y = (A4[1] - (bong_size_y * bong_count_y)) / (bong_count_y + 1)

id_box_size = 15 # Size of the rounded off part at the end of the bong

logo = ImageReader("assets/intbar-logo.png")
logo_scale_factor = 0.12
logo_size_x = logo.getSize()[0] * logo_scale_factor
logo_size_y = logo.getSize()[1] * logo_scale_factor

class BongGenerator:

    def __init__(self,
        count = 50,
        series = "A",
        description = "Integrerbar arrangementer",
        value = 65, 
        expiration = None):

        self.used_control_numbers = []
        self.count = count
        self.series = series
        self.description = description
        self.value = value
        if expiration == None:
            self.expiration = self.get_time_in_1_year(datetime.now())
        else:
            self.expiration = expiration


    def get_time_in_1_year(self, current_time = datetime.now()):
        in_one_year = current_time + timedelta(days=365)
        return in_one_year.strftime("%d-%m-%Y")

    def generate_pdf(self):
        """ 
            TODO: documentation
        """

        all_bongs = self.generate_bongs()
        bongs = [all_bongs[i:i+50] for i in range(0, len(all_bongs), 50)]
        checking_bongs = [all_bongs[i:i+200] for i in range(0, len(all_bongs), 200)]

        page_count = math.ceil(self.count / 50)
        checking_page_count = math.ceil(self.count / 200) 

        c = canvas.Canvas(f"serie-{self.series}.pdf", pagesize=A4)
        for i in range(page_count):
            c = self.generate_front_page(c, bongs[i])
            c.showPage()
            c = self.generate_back_page(c, bongs[i])
            c.showPage()

        for i in range(checking_page_count):
            c = self.generate_checking_page(c, checking_bongs[i])
            c.showPage()

        c.save()

        # except Exception as e:
        #     print(f"An error occured:\n{e}")

    def generate_bongs(self):
        bongs = []
        for i in range(self.count):
            control_number = self.get_control_number()
            bong = {
                    "id": (self.series + str(i+1).zfill(3)),
                    "control_number": (control_number),
                    "value": self.value,
                    "expiration": self.expiration
                    }
            bongs.append(bong)

        return bongs

    def get_control_number(self):
        control_number = ''.join([str(random.randint(0, 9)) for _ in range(5)])
        self.used_control_numbers.append(control_number)
        return control_number

    def generate_front_page(self, c, bongs):
        bong_counter = 0
        if len(bongs) > 50:
            raise ValueError("Received more than 50 bongs in generate_front_page. Aborting...")

        c.setStrokeColorRGB(*dark_red)
        c.setFillColorRGB(*white)
        c.setLineWidth(line_width)
        c.translate(margin_x, margin_y)

        for row in range(bong_count_y):
            c.saveState()
            c.translate(0, row * (bong_size_y + margin_y))
            for _ in range(bong_count_x):
                if bong_counter == len(bongs):
                    break

                self.draw_bong_front(c, bongs[bong_counter])
                c.translate(margin_x + bong_size_x, 0)
                bong_counter += 1
            c.restoreState()

        return c

    def generate_back_page(self, c, bongs):
        bong_counter = 0
        if len(bongs) > 50:
            raise ValueError("Received more than 50 bongs in generate_back_page. Aborting...")

        c.setStrokeColorRGB(*dark_red)
        c.setFillColorRGB(*white)
        c.setLineWidth(line_width)
        c.translate(A4[0] - margin_x, margin_y)

        for row in range(bong_count_y):
            c.saveState()
            c.translate(0, row * (bong_size_y + margin_y))
            c.translate( - bong_size_x, 0)
            for _ in range(bong_count_x):
                if bong_counter == len(bongs):
                    break
                self.draw_bong_back(c, bongs[bong_counter])
                c.translate( - (margin_x + bong_size_x), 0)
                bong_counter += 1
            c.restoreState()

        return c

    def generate_checking_page(self, c, bongs):
        bong_counter = 0

        if len(bongs) > 200:
            raise ValueError("Received more than 200 bongs in generate_checking_page. Aborting...")

        c.setStrokeColorRGB(*black)
        c.setFillColorRGB(*black)
        c.setLineWidth(line_width)
        c.rotate(90)
        c.translate(2 * margin_x, -4 * margin_y)
        c.setFont("Helvetica", 20)
        c.drawString(0, 0, f"{self.description}")
        c.drawString(0, -30, f"Bongserie: {self.series}")

        c.saveState()
        c.translate(A4[1] / 2, 0)
        c.rotate(-90)
        c.translate(-10, 0)
        self.draw_bong_front(c, bongs[0])
        c.translate(0, bong_size_y + 2 * margin_y)
        self.draw_bong_back(c, bongs[0])
        c.restoreState()

        c.translate(0, -6 * margin_y)

        for row in range(math.ceil(len(bongs) / 20)):
            c.saveState()
            c.translate(0, - row * box_size)
            for _ in range(20):
                if bong_counter == len(bongs):
                    break
                self.draw_checking_page_tile(c, bongs[bong_counter])
                c.translate(box_size, 0)
                bong_counter += 1
            c.restoreState()

        return c

    def draw_bong_front(self, c, bong):
        value = bong.get("value")
        expiration = bong.get("expiration")
        id = bong.get("id")

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
        c.drawCentredString(0, -8, f"Verdi: {value}kr")
        c.drawCentredString(0, -18, f"Gyldig til: {expiration}")
        c.rotate(90)
        c.setFont("Helvetica", 12)
        c.drawCentredString(0, (bong_size_y / 2) - 12, f"{id}")
        c.rotate(180)
        c.drawCentredString(0, (bong_size_y / 2) - 12, f"{id}")
        c.restoreState()
        return c

    def draw_bong_back(self, c, bong):
        id = bong.get("id")
        control_number = bong.get("control_number")

        c.roundRect(0, 0, bong_size_x, bong_size_y, 5)
        c.saveState()
        c.setFillColorRGB(*black)
        c.translate(bong_size_x / 2, bong_size_y / 2)
        c.rotate(90)
        c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(0, -6, f"{id}-{control_number}")
        c.restoreState()
        return c

    def draw_checking_page_tile(self, c, bong):

        id = bong.get("id")[-3:]
        control_number = bong.get("control_number")

        c.rect(0, - box_size, box_size, box_size)

        c.setFont("Helvetica-Bold", 12)
        c.drawString(3, -12, f"{id}")
        c.setFont("Helvetica", 10)
        c.drawString(3, -22, f"{control_number}")

        return c


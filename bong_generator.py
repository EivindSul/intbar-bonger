from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import datetime, timedelta
import math
import random

# TODO: Restructure as class with instance variables instead of everything being passed around
class BongGenerator:

    def __init__(self,
        count = 50,
        series = "A",
        value = 65, # Verdi i kr
        expiration = None):

        self.used_control_numbers = []
        self.count = count
        self.series = "A" if series == "A" else self.get_next_series()
        self.value = value
        if expiration == None:
            self.expiration = self.get_time_in_1_year(datetime.now())
        else:
            self.expiration = expiration

    def get_next_series(self):
        # TODO:
        # return the next letter that is not in use in the output folder. 
        pass

    def get_time_in_1_year(self, current_time = datetime.now()):
        in_one_year = current_time + timedelta(days=365)
        return in_one_year.strftime("%d-%m-%Y")

    def generate_pdf(self):
        """ TODO:
            Generate each bong as a tuple with name {Series}{Number} and controlnumber.
            Generate all the pages necessary in a loop.
            Front -> Back -> Check -> Front etc.

            Use specific methods for each of the smaller functions to make debugging
            and maintenance easier.
        """

        bongs = self.generate_bongs()

        page_count = math.ceil(self.count / 50)
        # TODO: Change 300 to be whatever the size limit of a checking page is
        checking_page_count = math.ceil(self.count / 300) 




        # TODO: slice bongs list to create only 50 in each

        c = canvas.Canvas(f"serie-{self.series}.pdf", pagesize=A4)
        for _ in range(page_count):
            c = self.generate_front_page(c, bongs)
            c = self.generate_back_page(c, bongs)

        # TODO: Make it conform to the checking page size limit
        for _ in range(checking_page_count):
            c = self.generate_checking_page(c, bongs)

        """
        PSEUDO:
            Create canvas
            Create front page:
                for bong in bongs:
                    draw bong
                    c.translate

            Create back page:
                for bong in bongs:
                    draw bong
                    c.translate

            Create page 3
            Draw all bongs in order in table

            save pdf

            What do bongs need to draw?
            Position
            Position is determined by the number of rows and columns, as well as the size of the canvas.
            Canvas has pagesize A4.
            I want bongs to have a margin of 0.5cm in height, and 1cm in width, including the edge of the paper.
            50 bongs is 5*10. 
            The width of each bong is the width of A4 (297mm) minus 6 margins of 1cm divided by 5. 
            This is 47.4.
            The height of each bong is the height of A4 (210mm) minus 11 margins of 0.5cm divided by 10. 
            This is 15.5mm.

            Each bong is approximately 47.4 * 15.5
        """

    def generate_bongs(self):
        bongs = []
        for i in range(self.count):
            control_number = self.get_control_number()
            bong = {
                    "id": (self.series + str(i+1), control_number),
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
        if len(bongs) > 50:
            print("Received more than 50 bongs in generate_front_page. Aborting...")
        for i, bong in enumerate(bongs):
            c = self.draw_bong_front(c, bong)

        return c

    def generate_back_page(self, bongs, c):
        if len(bongs) > 50:
            print("Received more than 50 bongs in generate_back_page. Aborting...")
        for i, bong in enumerate(bongs):
            c = self.draw_bong_back(c, bong)

        return c

    def generate_checking_page(self, c, bongs):
        return c

    def draw_bong_front(self, c, bong):
        return c

    def draw_bong_back(self, c, bong):
        return c


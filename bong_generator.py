# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import letter
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

        for _ in range(page_count):
            self.generate_front_page(bongs)
            self.generate_back_page(bongs)

        self.generate_checking_page(bongs)

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

    def generate_front_page(self, bongs):
        if len(bongs) > 50:
            print("Received more than 50 bongs in generate_front_page. Aborting...")
        for i, bong in enumerate(bongs):
            self.draw_bong_front(bong, i)

    def generate_back_page(self, bongs):
        if len(bongs) > 50:
            print("Received more than 50 bongs in generate_back_page. Aborting...")
        for i, bong in enumerate(bongs):
            self.draw_bong_back(bong, i)

    def generate_checking_page(self, bongs):
        pass

    def draw_bong_front(self, bong, i):
        pass

    def draw_bong_back(self, bong, i):
        pass


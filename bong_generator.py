from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import datetime, timedelta
import Math
import random

# TODO: Restructure as class with instance variables instead of everything being passed around

used_control_numbers = []

def get_next_series():
    # TODO:
    # return the next letter that is not in use in the output folder. 
    pass

def get_expiration_date():
    current_time = datetime.now()
    expiration_date = current_time + timedelta(days=365)
    return expiration_date.strftime("%d-%m-%Y")

def generate_pdf(
        count = 50,
        series = get_next_series(),
        value = 65, # Verdi i kr
        expiration = get_expiration_date()
        ):
    """ TODO:
        Generate each bong as a tuple with name {Series}{Number} and controlnumber.
        Generate all the pages necessary in a loop.
        Front -> Back -> Check -> Front etc.

        Use specific methods for each of the smaller functions to make debugging
        and maintenance easier.
    """

    bongs = generate_bongs(count, series, value, expiration)

    page_count = Math.ceil(count / 50)

    for _ in range(page_count):
        generate_front_page(bongs)
        generate_back_page(bongs)

    generate_checking_page(bongs)

def generate_bongs(count, series, value, expiration):
    bongs = []
    for i in range(count):
        control_number = get_control_number()
        bong = {
                "id": (series + str(i+1), control_number),
                "value": value,
                "expiration": expiration
                }
        bongs.append(bong)

    return bongs

def get_control_number():
    control_number = ''.join([str(random.randint(0, 9)) for _ in range(5)])
    used_control_numbers.append(control_number)
    return control_number

def generate_front_page(bongs):
    if len(bongs) > 50:
        print("Received more than 50 bongs in generate_front_page. Aborting...")
    for i, bong in enumerate(bongs):
        draw_bong_front(bong, i)

def generate_back_page(bongs):
    if len(bongs) > 50:
        print("Received more than 50 bongs in generate_back_page. Aborting...")
    for i, bong in enumerate(bongs):
        draw_bong_back(bong, i)

def generate_checking_page(bongs):
    pass

def draw_bong_front(bong, i):
    pass

def draw_bong_back(bong, i):
    pass


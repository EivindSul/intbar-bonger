# Test file that I could start using auto-run script to test bong_generator
import bong_generator

bonger = bong_generator.BongGenerator(series="X", value=80, count=300)
bonger.generate_pdf()

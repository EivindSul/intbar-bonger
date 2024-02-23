import tkinter as tk
from tkinter import filedialog
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

class TicketGeneratorApp:
    def __init__(self, main):
        self.main = main
        self.main.title("Ticket Generator")

        self.ticket_contents = []

        # GUI components
        self.label = tk.Label(main, text="Enter Ticket Content:")
        self.label.pack()

        self.entry = tk.Entry(main)
        self.entry.pack()

        self.add_button = tk.Button(main, text="Add Ticket", command=self.add_ticket)
        self.add_button.pack()

        self.generate_button = tk.Button(main, text="Generate PDF", command=self.generate_pdf)
        self.generate_button.pack()

    def add_ticket(self):
        content = self.entry.get()
        if content:
            self.ticket_contents.append(content)
            self.entry.delete(0, tk.END)

    def generate_pdf(self):
        pdf_file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

        if pdf_file_path:
            for i, content in enumerate(self.ticket_contents, start=1):
                self.create_ticket(f'ticket_{i}.pdf', content)

            self.ticket_contents = []  # Clear ticket contents after generating PDF

    def create_ticket(self, pdf_file, ticket_content):
        pdf_canvas = canvas.Canvas(pdf_file, pagesize=letter)
        pdf_canvas.setFont("Helvetica", 12)
        pdf_canvas.drawString(100, 700, "Ticket:")
        pdf_canvas.drawString(100, 680, ticket_content)
        pdf_canvas.save()

if __name__ == "__main__":
    root = tk.Tk()
    app = TicketGeneratorApp(root)
    root.mainloop()


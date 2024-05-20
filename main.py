from fpdf import FPDF
from PIL import Image

class Prescription:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.age = input("Enter your age: ")
        self.gender = input("Enter your gender: ")
        self.address = input("Enter your address: ")
        self.pdf = FPDF()
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=14)
        self.create_pdf()

    def add_image(self, image_path, y_position):
        with Image.open(image_path) as img:
            w, h = img.size
        img_height = h * (210 / w)
        self.pdf.image(image_path, x=0, y=y_position, w=210, h=img_height)
        return img_height

    def add_patient_details(self, y_position):
        self.pdf.cell(50, y_position+40, txt=f"Name: {self.name}", ln=False, align='C')
        self.pdf.cell(30, y_position+40, txt=f"Gender: {self.gender}", ln=False, align='C')
        self.pdf.cell(30, y_position+40, txt=f"Age: {self.age}", ln=False, align='C')
        self.pdf.cell(50, y_position+40, txt=f"Address: {self.address}", ln=True, align='C')

    def create_pdf(self):
        header_height = self.add_image('header.png', 10)
        details_height = 10  # reduce the space for the patient's details
        self.add_patient_details(header_height + details_height)
        body_height = self.add_image('body.png', header_height + details_height * 2)  # adjust the y-position of the body
        footer_y_position = 297-11 # adjust the y-position of the footer
        self.add_image('footer.png', footer_y_position)
        self.pdf.output(f"prescription_{self.name}.pdf")

a = Prescription()
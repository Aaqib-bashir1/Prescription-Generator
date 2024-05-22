from reportlab.pdfgen import canvas
from datetime import date
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet


class prescription:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter
    from svglib.svglib import svg2rlg
    from reportlab.graphics import renderPDF
    def __init__(self):
        self.patient_details()
        self.doctor_details()
        self.create_pdf()


    def doctor_details(self):
        self.docter_name="John Smith"#input("Enter the name of the doctor: ")
        self.qualifications="MBBS MS MD RMCP FCPS"#input("Enter the qualifications: ")
        self.mobile="0123456789"#input("Enter the mobile number:")
        self.alternate="0123456789"#input("Enter the alternate phone number:")
        self.email="test.mail.com"#input("Enter the email address: ")
        self.website= "www.website.com"#input("Enter the web address: ")


    def patient_details(self):
        self.name= "John Doe" #input("Enter the name of the patient: ")
        self.age= "22"#input("Enter the age of the patient: ")
        self.gender= "Male"#input("Enter the gender of the patient: ")
        self.address=""#input("Enter the address of the patient: ")

    def text_width(self,text,font,size):
        return self.c.stringWidth(text,font,size)
    def doc_header(self):


        self.c=canvas.Canvas(f"prescription{self.name}.pdf",pagesize=A4)
        text_object=self.c.beginText()
        doc_coordinate = 595 -self.text_width(self.docter_name, "Helvetica", 34)-70
        text_object.setTextOrigin(doc_coordinate,795)
        text_object.setFont("Helvetica", 34)  # Set the font and size
        text_object.setFillColor("SkyBlue")
        text_object.textLines(f"Dr. {self.docter_name}")

        text_object.setFont("Helvetica", 12)
        qualification_coordinate = 595-self.text_width(self.qualifications, "Helvetica", 12)-20
        text_object.setTextOrigin(qualification_coordinate, 775)
        text_object.setFillColor("Black")
        text_object.textLines(self.qualifications)
        text_object.setFont("Helvetica", 28)  # Set the font and size
        self.c.setStrokeColor("SkyBlue")
        self.c.setLineWidth(2)
        self.c.line(doc_coordinate, 770, 580, 770)

        text_object.setFont("Helvetica", 12)
        mobile = self.mobile + self.alternate
        mobile_coordinate = 595-self.text_width(mobile, "Helvetica", 12)-70
        text_object.setTextOrigin(mobile_coordinate, 755)
        text_object.setFillColor("Black")

        text_object.textLines(f"+91 {self.mobile}| +91 {self.alternate}")
        email_coordinate = 595-self.text_width(self.email, "Helvetica", 12)-20
        text_object.setTextOrigin(email_coordinate, 740)
        text_object.textLines(self.email)
        web_coordinate = 595-self.text_width(self.website, "Helvetica", 12)-20
        text_object.setTextOrigin(web_coordinate, 725)
        text_object.textLines(self.website)
        self.c.drawText(text_object)

    def patient_header(self):

        texts = [
            f"Name: {self.name}",
            f"Age: {self.age}",
            f"Gender: {self.gender}",
            f"Date: {date.today()}",
            f"Address: {self.address}"
        ]
        x_coordinate = 10  # Starting x-coordinate
        y_coordinate = 690  # Starting y-coordinate

        for text in texts:
            text_object = self.c.beginText()
            text_object.setTextOrigin(x_coordinate, y_coordinate)
            text_object.setFont("Helvetica", 14)
            text_object.textLines(text)

            self.c.drawText(text_object)

            # Calculate the new x-coordinate for the next text object
            text_width = self.c.stringWidth(text, "Helvetica", 14)
            x_coordinate += text_width +40
            self.c.setStrokeColor("SkyBlue")
            self.c.setLineWidth(3)
            self.c.line(0, 683, 600, 683)

    def logo(self):
        # logo_path = " "
        # self.c.drawImage(logo_path, 10, 730, width=100, height=100)

        pdfmetrics.registerFont(TTFont('Arial Unicode MS', '/Library/Fonts/Arial Unicode.ttf'))  # Register the font
        rx_sign = "\u211E"
        text_object = self.c.beginText()
        text_object.setTextOrigin(50, 635)
        text_object.setFont("Arial Unicode MS", 36)  # Use the "Arial Unicode MS" font
        text_object.setFillColor("SkyBLue")
        text_object.textLines(rx_sign)
        self.c.drawText(text_object)
    def symptoms(self):
        text_object = self.c.beginText()
        text_object.setTextOrigin(10, 615)
        text_object.setFont("Helvetica", 12)
        text_object.textLines("Symptoms: ")
        self.c.drawText(text_object)
        text_object.setFillColor("Black")
        symptoms="Experiencing Headache, vomitting, sesitive to light, unequal pupils "*2 #input("enter symptoms")
        style = getSampleStyleSheet()["Normal"]
        para=Paragraph(symptoms,style)
        para.wrapOn(self.c,A4[0]-400,A4[1])
        para.drawOn(self.c, 74, 570)

    def diagnosis(self):

        text_object = self.c.beginText()
        text_object.setTextOrigin(10, 500)
        text_object.setFont("Helvetica", 12)
        text_object.setFillColor("SkyBLue")
        text_object.textLines("Diagnosis: ")
        text_object.setFillColor("Black")
        self.c.drawText(text_object)
        symptoms = " Concussion"  # input("enter Diagnosis")
        style = getSampleStyleSheet()["Normal"]
        para = Paragraph(symptoms, style)
        para.wrapOn(self.c, A4[0] - 400, A4[1])
        para.drawOn(self.c, 74, 480)

    def  prescription(self):
        text_object = self.c.beginText()
        text_object.setTextOrigin(10, 430)
        text_object.setFillColor("SkyBLue")
        text_object.setFont("Helvetica", 12)
        text_object.textLines("prescription: ")
        text_object.setFillColor("BLack")

        # Get multiple lines of input
        prescriptions = []
        i=10
        while True:
            line = input("Enter prescription (or 'done' to finish): ")
            if line.lower() == 'done':
                break
            prescriptions.append(line)
            text_object.setTextOrigin(70, 430-i)

        for prescription in prescriptions:
            text_object.textLines(prescription)

        self.c.drawText(text_object)

    def advice(self):


        text_object = self.c.beginText()
        text_object.setTextOrigin(10, 300)
        text_object.setFillColor("SkyBLue")
        text_object.setFont("Helvetica", 12)
        text_object.textLines("Advice: ")
        text_object.setFillColor("Black")
        self.c.drawText(text_object)
        advice= "take rest " # input("enter advice")
        style = getSampleStyleSheet()["Normal"]
        para = Paragraph(advice, style)
        para.wrapOn(self.c, A4[0] - 400, A4[1])
        para.drawOn(self.c, 60, 290)

    def footer(self):
        width, height = A4  # Get the dimensions of the page

        # Draw a blue rectangle as the footer
        self.c.setFillColorRGB(135/255, 206/255, 235/255)  # Set color to blue
        self.c.rect(0, 0, width, 20, fill=True)

        # Add some white text in the center of the footer
        self.c.setFillColorRGB(0, 0, 0)  # Set colo r to white
        self.c.setFont("Helvetica", 12)
        self.c.drawCentredString(width / 2.0, 8, "95 Roman Rd LEBBERSTON YO11 2LD")



    def create_pdf(self):
        self.doc_header()
        self.patient_header()
        self.logo()
        self.symptoms()
        self.diagnosis()
        self.prescription()
        self.advice()
        self.footer()
        self.c.save()

t=prescription()


from fpdf import FPDF
pdf=FPDF()

imagelist=["myqr.png"]
for image in imagelist:
    pdf.add_page()
    #pdf.image(image,x,y,w,h)
    pdf.image(image)
    pdf.output("mypdf.pdf",'F')

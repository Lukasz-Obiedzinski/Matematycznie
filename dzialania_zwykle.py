__author__='dev'
from fpdf import FPDF
import random

import time
from datetime import date


num_script=1
uczen=input("Imie ucznia: ") 
liczba_gen=260

column_width = 2.0
column_spacing = 0.15

for j in range(num_script):

    pdf=FPDF(format='letter', unit='in')
    pdf2=FPDF(format='letter', unit='in')
    
    pdf.compress = False
    pdf.add_page()
    pdf.set_font('Arial', '', 10)

    pdf2.compress = False
    pdf2.add_page()
    pdf2.set_font('Arial', '', 10)

    ybefore = pdf.get_y()
    ybefore2 = pdf2.get_y()
    i=0

    z=0
    x=0
    y=0

    #petla for
    for i in range(liczba_gen):
        if i<65:

            pierwsza=random.randint(1,100)
            druga=random.randint(1,100)
            trzecia=random.randint(1,100)
            pdf.multi_cell(column_width, 0.15,("{0}. {1}+{2}-{3}=".format(i+1,pierwsza,druga,trzecia)))

            wynik=pierwsza+druga-trzecia
            pdf2.multi_cell(column_width, 0.15,("{0}. {1}+{2}-{3}={4}".format(i+1,pierwsza,druga,trzecia,wynik)))
        elif i<2*65:

            pdf.set_xy(column_width + pdf.l_margin + column_spacing, ybefore+z)
            pdf2.set_xy(column_width + pdf.l_margin + column_spacing, ybefore2+z)

            pierwsza=random.randint(1,100)
            druga=random.randint(1,100)
            trzecia=random.randint(1,100)
            pdf.multi_cell(column_width, 0.15,("{0}. {1}+{2}-{3}=".format(i+1,pierwsza,druga,trzecia)))

            wynik=pierwsza+druga-trzecia
            pdf2.multi_cell(column_width, 0.15,("{0}. {1}+{2}-{3}={4}".format(i+1,pierwsza,druga,trzecia,wynik)))
            z+=0.15
        elif i<3*65:

            pdf.set_xy(2*column_width + pdf.l_margin + column_spacing, ybefore+x)
            pdf2.set_xy(2*column_width + pdf.l_margin + column_spacing, ybefore2+x)

            pierwsza=random.randint(1,100)
            druga=random.randint(1,100)
            trzecia=random.randint(1,100)
            pdf.multi_cell(column_width, 0.15,("{0}. {1}+{2}-{3}=".format(i+1,pierwsza,druga,trzecia)))

            wynik=pierwsza+druga-trzecia
            pdf2.multi_cell(column_width, 0.15,("{0}. {1}+{2}-{3}={4}".format(i+1,pierwsza,druga,trzecia,wynik)))
            x+=0.15
        elif i<4*65:

            pdf.set_xy(3*column_width + pdf.l_margin + column_spacing, ybefore+y)
            pdf2.set_xy(3*column_width + pdf.l_margin + column_spacing, ybefore2+y)

            pierwsza=random.randint(1,100)
            druga=random.randint(1,100)
            trzecia=random.randint(1,100)
            pdf.multi_cell(column_width, 0.15,("{0}. {1}+{2}-{3}=".format(i+1,pierwsza,druga,trzecia)))

            wynik=pierwsza+druga-trzecia
            pdf2.multi_cell(column_width, 0.15,("{0}. {1}+{2}-{3}={4}".format(i+1,pierwsza,druga,trzecia,wynik)))
            y+=0.15

        column_width = 2.0
        column_spacing = 0.15

    j+=1

    pdf.output('Dodawanie_i_odejmowanie_{}.pdf'.format(uczen), 'F')
    pdf2.output('Dodawanie_i_odejmowanie_{}_wyniki.pdf'.format(uczen), 'F')
    print("wygenerowano Dodawanie_i_odejmowanie_{}.pdf".format(uczen))
    print("wygenerowano Dodawanie_i_odejmowanie_{}_wyniki.pdf".format(uczen))

    

###############
###############
###############
###############

# Proste 


for j in range(num_script):

    pdf=FPDF(format='letter', unit='in')
    pdf2=FPDF(format='letter', unit='in')
    
    pdf.compress = False
    pdf.add_page()
    pdf.set_font('Arial', '', 10)

    pdf2.compress = False
    pdf2.add_page()
    pdf2.set_font('Arial', '', 10)

    ybefore = pdf.get_y()
    ybefore2 = pdf2.get_y()
    i=0

    z=0
    x=0
    y=0

    #petla for
    for i in range(liczba_gen):
        if i<65:

            pierwsza=random.randint(1,100)
            druga=random.randint(1,100)
            pdf.multi_cell(column_width, 0.15,("{0}. {1}+{2}=".format(i+1,pierwsza,druga,trzecia)))

            wynik=pierwsza+druga
            pdf2.multi_cell(column_width, 0.15,("{0}. {1}+{2}={3}".format(i+1,pierwsza,druga,wynik)))
        elif i<2*65:

            pdf.set_xy(column_width + pdf.l_margin + column_spacing, ybefore+z)
            pdf2.set_xy(column_width + pdf.l_margin + column_spacing, ybefore2+z)

            pierwsza=random.randint(1,100)
            druga=random.randint(1,100)

            pdf.multi_cell(column_width, 0.15,("{0}. {1}+{2}=".format(i+1,pierwsza,druga,trzecia)))

            wynik=pierwsza+druga
            pdf2.multi_cell(column_width, 0.15,("{0}. {1}+{2}={3}".format(i+1,pierwsza,druga,wynik)))
            z+=0.15
        elif i<3*65:

            pdf.set_xy(2*column_width + pdf.l_margin + column_spacing, ybefore+x)
            pdf2.set_xy(2*column_width + pdf.l_margin + column_spacing, ybefore2+x)

            pierwsza=random.randint(1,100)
            druga=random.randint(1,100)

            pdf.multi_cell(column_width, 0.15,("{0}. {1}+{2}=".format(i+1,pierwsza,druga,trzecia)))

            wynik=pierwsza+druga
            pdf2.multi_cell(column_width, 0.15,("{0}. {1}+{2}={3}".format(i+1,pierwsza,druga,wynik)))
            x+=0.15
        elif i<4*65:

            pdf.set_xy(3*column_width + pdf.l_margin + column_spacing, ybefore+y)
            pdf2.set_xy(3*column_width + pdf.l_margin + column_spacing, ybefore2+y)

            pierwsza=random.randint(1,100)
            druga=random.randint(1,100)

            pdf.multi_cell(column_width, 0.15,("{0}. {1}+{2}=".format(i+1,pierwsza,druga,trzecia)))
            wynik=pierwsza+druga
            pdf2.multi_cell(column_width, 0.15,("{0}. {1}+{2}={3}".format(i+1,pierwsza,druga,wynik)))
            y+=0.15

        column_width = 2.0
        column_spacing = 0.15

    j+=1

    pdf.output('Dodawanie_{}.pdf'.format(uczen), 'F')
    pdf2.output('Dodawanie_{}_wyniki.pdf'.format(uczen), 'F')
    print("wygenerowano Dodawanie_{}.pdf".format(uczen))
    print("wygenerowano Dodawanie_{}_wyniki.pdf".format(uczen))


###############
###############
#ODEJMOWANIE
###############

    
for j in range(num_script):

    pdf=FPDF(format='letter', unit='in')
    pdf2=FPDF(format='letter', unit='in')
    
    pdf.compress = False
    pdf.add_page()
    pdf.set_font('Arial', '', 10)

    pdf2.compress = False
    pdf2.add_page()
    pdf2.set_font('Arial', '', 10)

    ybefore = pdf.get_y()
    ybefore2 = pdf2.get_y()
    i=0

    z=0
    x=0
    y=0

    #petla for
    for i in range(liczba_gen):
        if i<65:

            pierwsza=random.randint(1,100)
            druga=random.randint(1,100)
            pdf.multi_cell(column_width, 0.15,("{0}. {1}-{2}=".format(i+1,pierwsza,druga,trzecia)))

            wynik=pierwsza-druga
            pdf2.multi_cell(column_width, 0.15,("{0}. {1}-{2}={3}".format(i+1,pierwsza,druga,wynik)))
        elif i<2*65:

            pdf.set_xy(column_width + pdf.l_margin + column_spacing, ybefore+z)
            pdf2.set_xy(column_width + pdf.l_margin + column_spacing, ybefore2+z)

            pierwsza=random.randint(1,100)
            druga=random.randint(1,100)

            pdf.multi_cell(column_width, 0.15,("{0}. {1}-{2}=".format(i+1,pierwsza,druga,trzecia)))

            wynik=pierwsza-druga
            pdf2.multi_cell(column_width, 0.15,("{0}. {1}-{2}={3}".format(i+1,pierwsza,druga,wynik)))
            z+=0.15
        elif i<3*65:

            pdf.set_xy(2*column_width + pdf.l_margin + column_spacing, ybefore+x)
            pdf2.set_xy(2*column_width + pdf.l_margin + column_spacing, ybefore2+x)

            pierwsza=random.randint(1,100)
            druga=random.randint(1,100)

            pdf.multi_cell(column_width, 0.15,("{0}. {1}-{2}=".format(i+1,pierwsza,druga,trzecia)))

            wynik=pierwsza-druga
            pdf2.multi_cell(column_width, 0.15,("{0}. {1}-{2}={3}".format(i+1,pierwsza,druga,wynik)))
            x+=0.15
        elif i<4*65:

            pdf.set_xy(3*column_width + pdf.l_margin + column_spacing, ybefore+y)
            pdf2.set_xy(3*column_width + pdf.l_margin + column_spacing, ybefore2+y)

            pierwsza=random.randint(1,100)
            druga=random.randint(1,100)

            pdf.multi_cell(column_width, 0.15,("{0}. {1}-{2}=".format(i+1,pierwsza,druga,trzecia)))
            wynik=pierwsza-druga
            pdf2.multi_cell(column_width, 0.15,("{0}. {1}-{2}={3}".format(i+1,pierwsza,druga,wynik)))
            y+=0.15

        column_width = 2.0
        column_spacing = 0.15

    j+=1

    pdf.output('Odejmowanie_{}.pdf'.format(uczen), 'F')
    pdf2.output('Odejmowanie_{}_wyniki.pdf'.format(uczen), 'F')
    print("wygenerowano Odejmowanie_{}.pdf".format(uczen))
    print("wygenerowano Odejmowanie_{}_wyniki.pdf".format(uczen))


###############
###############
#MNOZENIE
###############

for j in range(num_script):

    pdf=FPDF(format='letter', unit='in')
    pdf2=FPDF(format='letter', unit='in')
    
    pdf.compress = False
    pdf.add_page()
    pdf.set_font('Arial', '', 10)

    pdf2.compress = False
    pdf2.add_page()
    pdf2.set_font('Arial', '', 10)

    ybefore = pdf.get_y()
    ybefore2 = pdf2.get_y()
    i=0

    z=0
    x=0
    y=0

    #petla for
    for i in range(liczba_gen):
        if i<65:

            pierwsza=random.randint(1,10)
            druga=random.randint(1,10)
            pdf.multi_cell(column_width, 0.15,("{0}. {1}*{2}=".format(i+1,pierwsza,druga,trzecia)))

            wynik=pierwsza*druga
            pdf2.multi_cell(column_width, 0.15,("{0}. {1}*{2}={3}".format(i+1,pierwsza,druga,wynik)))
        elif i<2*65:

            pdf.set_xy(column_width + pdf.l_margin + column_spacing, ybefore+z)
            pdf2.set_xy(column_width + pdf.l_margin + column_spacing, ybefore2+z)

            pierwsza=random.randint(1,100)
            druga=random.randint(1,100)

            pdf.multi_cell(column_width, 0.15,("{0}. {1}*{2}=".format(i+1,pierwsza,druga,trzecia)))

            wynik=pierwsza*druga
            pdf2.multi_cell(column_width, 0.15,("{0}. {1}*{2}={3}".format(i+1,pierwsza,druga,wynik)))
            z+=0.15
        elif i<3*65:

            pdf.set_xy(2*column_width + pdf.l_margin + column_spacing, ybefore+x)
            pdf2.set_xy(2*column_width + pdf.l_margin + column_spacing, ybefore2+x)

            pierwsza=random.randint(1,10)
            druga=random.randint(1,10)

            pdf.multi_cell(column_width, 0.15,("{0}. {1}*{2}=".format(i+1,pierwsza,druga,trzecia)))

            wynik=pierwsza*druga
            pdf2.multi_cell(column_width, 0.15,("{0}. {1}*{2}={3}".format(i+1,pierwsza,druga,wynik)))
            x+=0.15
        elif i<4*65:

            pdf.set_xy(3*column_width + pdf.l_margin + column_spacing, ybefore+y)
            pdf2.set_xy(3*column_width + pdf.l_margin + column_spacing, ybefore2+y)

            pierwsza=random.randint(1,100)
            druga=random.randint(1,100)

            pdf.multi_cell(column_width, 0.15,("{0}. {1}*{2}=".format(i+1,pierwsza,druga,trzecia)))
            wynik=pierwsza*druga
            pdf2.multi_cell(column_width, 0.15,("{0}. {1}*{2}={3}".format(i+1,pierwsza,druga,wynik)))
            y+=0.15

        column_width = 2.0
        column_spacing = 0.15

    j+=1

    pdf.output('Mnozenie_{}.pdf'.format(uczen), 'F')
    pdf2.output('Mnozenie_{}_wyniki.pdf'.format(uczen), 'F')
    print("wygenerowano Mnozenie_{}.pdf".format(uczen))
    print("wygenerowano Mnozenie_{}_wyniki.pdf".format(uczen))


###############
###############
#Ułamki
###############


for j in range(num_script):

    pdf=FPDF(format='letter', unit='in')
    pdf2=FPDF(format='letter', unit='in')
    
    pdf.compress = False
    pdf.add_page()
    pdf.set_font('Arial', '', 10)

    pdf2.compress = False
    pdf2.add_page()
    pdf2.set_font('Arial', '', 10)

    ybefore = pdf.get_y()
    ybefore2 = pdf2.get_y()
    i=0

    z=0
    x=0
    y=0

    #petla for
    for i in range(liczba_gen):
        if i<65:

            pierwsza=random.randint(1,10)
            druga=random.randint(1,10)
            trzecia=random.randint(1,10)
            czwarta=random.randint(1,10)
            pdf.multi_cell(column_width, 0.15,("{0}. {1}/{2}+{3}/{4}=".format(i+1,pierwsza,druga,trzecia,czwarta)))

            wynik1=(czwarta*pierwsza+trzecia*druga)
            wynik2=druga*czwarta
            pdf2.multi_cell(column_width, 0.15,("{0}. {1}/{2}+{3}/{4}={5}/{6}".format(i+1,pierwsza,druga,trzecia,czwarta,wynik1,wynik2)))
        elif i<2*65:

            pdf.set_xy(column_width + pdf.l_margin + column_spacing, ybefore+z)
            pdf2.set_xy(column_width + pdf.l_margin + column_spacing, ybefore2+z)

            pierwsza=random.randint(1,10)
            druga=random.randint(1,10)
            trzecia=random.randint(1,10)
            czwarta=random.randint(1,10)
            pdf.multi_cell(column_width, 0.15,("{0}. {1}/{2}-{3}/{4}=".format(i+1,pierwsza,druga,trzecia,czwarta)))

            wynik1=(czwarta*pierwsza-trzecia*druga)
            wynik2=druga*czwarta
            pdf2.multi_cell(column_width, 0.15,("{0}. {1}/{2}-{3}/{4}={5}/{6}".format(i+1,pierwsza,druga,trzecia,czwarta,wynik1,wynik2)))
            z+=0.15
        elif i<3*65:

            pdf.set_xy(2*column_width + pdf.l_margin + column_spacing, ybefore+x)
            pdf2.set_xy(2*column_width + pdf.l_margin + column_spacing, ybefore2+x)

            pierwsza=random.randint(1,10)
            druga=random.randint(1,10)
            trzecia=random.randint(1,10)
            czwarta=random.randint(1,10)
            pdf.multi_cell(column_width, 0.15,("{0}. {1}/{2}+{3}/{4}=".format(i+1,pierwsza,druga,trzecia,czwarta)))

            wynik1=(czwarta*pierwsza+trzecia*druga)
            wynik2=druga*czwarta
            pdf2.multi_cell(column_width, 0.15,("{0}. {1}/{2}+{3}/{4}={5}/{6}".format(i+1,pierwsza,druga,trzecia,czwarta,wynik1,wynik2)))
            x+=0.15
        elif i<4*65:

            pdf.set_xy(3*column_width + pdf.l_margin + column_spacing, ybefore+y)
            pdf2.set_xy(3*column_width + pdf.l_margin + column_spacing, ybefore2+y)

            pierwsza=random.randint(1,10)
            druga=random.randint(1,10)
            trzecia=random.randint(1,10)
            czwarta=random.randint(1,10)
            pdf.multi_cell(column_width, 0.15,("{0}. {1}/{2}-{3}/{4}=".format(i+1,pierwsza,druga,trzecia,czwarta)))

            wynik1=(czwarta*pierwsza-trzecia*druga)
            wynik2=druga*czwarta
            pdf2.multi_cell(column_width, 0.15,("{0}. {1}/{2}-{3}/{4}={5}/{6}".format(i+1,pierwsza,druga,trzecia,czwarta,wynik1,wynik2)))
            y+=0.15

        column_width = 2.0
        column_spacing = 0.15

    j+=1

    pdf.output('Ulamki_zwykle_{}.pdf'.format(uczen), 'F')
    pdf2.output('Ulamki_zwykle_{}_wyniki.pdf'.format(uczen), 'F')
    print("wygenerowano Ulamki_zwykle_{}.pdf".format(uczen))
    print("wygenerowano Ulamki_zwykle_{}_wyniki.pdf".format(uczen))


###############
###############
# Dzielenie


for j in range(num_script):

    pdf=FPDF(format='letter', unit='in')
    pdf2=FPDF(format='letter', unit='in')
    
    pdf.compress = False
    pdf.add_page()
    pdf.set_font('Arial', '', 10)

    pdf2.compress = False
    pdf2.add_page()
    pdf2.set_font('Arial', '', 10)

    ybefore = pdf.get_y()
    ybefore2 = pdf2.get_y()
    i=0

    z=0
    x=0
    y=0

    #petla for
    for i in range(liczba_gen):
        if i<65:

            pierwsza=random.randint(1,10)
            druga=random.randint(1,10)
            trzecia=random.randint(1,10)
            czwarta=random.randint(1,10)
            pdf.multi_cell(column_width, 0.15,("{0}. {1}/{2}:{3}/{4}=".format(i+1,pierwsza,druga,trzecia,czwarta)))

            wynik1=(czwarta*pierwsza)
            wynik2=druga*trzecia
            pdf2.multi_cell(column_width, 0.15,("{0}. {1}/{2}:{3}/{4}={5}/{6}".format(i+1,pierwsza,druga,trzecia,czwarta,wynik1,wynik2)))
        elif i<2*65:

            pdf.set_xy(column_width + pdf.l_margin + column_spacing, ybefore+z)
            pdf2.set_xy(column_width + pdf.l_margin + column_spacing, ybefore2+z)

            pierwsza=random.randint(1,100)
            druga=random.randint(1,10)
            trzecia=random.randint(1,100)
            czwarta=random.randint(1,10)
            pdf.multi_cell(column_width, 0.15,("{0}. {1}/{2}*{3}/{4}=".format(i+1,pierwsza,druga,trzecia,czwarta)))

            wynik1=(czwarta*pierwsza)
            wynik2=druga*trzecia
            pdf2.multi_cell(column_width, 0.15,("{0}. {1}/{2}*{3}/{4}={5}/{6}".format(i+1,pierwsza,druga,trzecia,czwarta,wynik1,wynik2)))
            z+=0.15
        elif i<3*65:

            pdf.set_xy(2*column_width + pdf.l_margin + column_spacing, ybefore+x)
            pdf2.set_xy(2*column_width + pdf.l_margin + column_spacing, ybefore2+x)

            pierwsza=random.randint(1,100)
            druga=random.randint(1,10)
            pdf.multi_cell(column_width, 0.15,("{0}. {1}:{2}=".format(i+1,pierwsza,druga)))

            wynik=pierwsza/druga
            pdf2.multi_cell(column_width, 0.15,("{0}. {1}:{2}={3:.2f}".format(i+1,pierwsza,druga,wynik)))
            x+=0.15
        elif i<4*65:

            pdf.set_xy(3*column_width + pdf.l_margin + column_spacing, ybefore+y)
            pdf2.set_xy(3*column_width + pdf.l_margin + column_spacing, ybefore2+y)

            pierwsza=random.randint(1,1000)
            druga=random.randint(1,10)
            pdf.multi_cell(column_width, 0.15,("{0}. {1}:{2}=".format(i+1,pierwsza,druga)))

            wynik=pierwsza/druga
            pdf2.multi_cell(column_width, 0.15,("{0}. {1}:{2}={3:.2f}".format(i+1,pierwsza,druga,wynik)))
            y+=0.15

        column_width = 2.0
        column_spacing = 0.15

    j+=1

    pdf.output('Dzielenie_ulamkow_{}.pdf'.format(uczen), 'F')
    pdf2.output('Dzielenie_ulamkow_{}_wyniki.pdf'.format(uczen), 'F')
    print("wygenerowano Dzielenie_ulamkow_{}.pdf".format(uczen))
    print("wygenerowano Dzielenie_ulamkow_{}_wyniki.pdf".format(uczen))







    
    



from datetime import date, datetime
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from models import *
from PIL import ImageTk
import PIL.Image

from tkinter import *

import logging

logger = logging.getLogger(__name__)
logger_file = logging.FileHandler("produktai_receptai.log")
logger.addHandler(logger_file)
logger.setLevel(logging.INFO)
logger_formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(module)s:%(lineno)d:%(message)s")
logger_file.setFormatter(logger_formatter)

streamer_handler = logging.StreamHandler()
streamer_handler.setFormatter(logger_formatter)
logger.addHandler(streamer_handler)

engine = create_engine("sqlite:///produktai_receptai.db")
session = sessionmaker(bind=engine)()

class Pagrindinis:
    def __init__(self, langas):
        self.langas = langas
        langas.title("Skanaus!")
        photo = PhotoImage(file = "a.png")
        langas.iconphoto(False, photo)
        self.langas.geometry("550x600")
        self.pasirinkimas = Label(langas, text="Pasirinkite ką norite daryt: ")
        self.label1 = Label(langas, text="---------PRIDEJIMAS---------")
        self.pridetiproduktapasiul = Button(langas, text="Pridėti produkta prie pasiūlos", command=self.prideti_produkta_pasiul)
        self.pridetiprodukta = Button(langas, text="Pridėti pasirinkta produkta prie turimų", command=self.prideti_produkta_turim)
        self.pridetirecepta = Button(langas, text="Pridėti recepta", command=self.prideti_recepta)
        self.pridetiproduktarecep = Button(langas, text="Pridėti produkta prie recepto", command=self.prideti_produkta_recep)
        self.label2 = Label(langas, text="---------PERZIURA---------")
        self.pamatytipasiula = Button(langas, text="Pamatyti produktu pasiula", command=self.perziureti_pasiula)
        self.pamatytiproduktus = Button(langas, text="Pamatyti visus turimus produktus", command=self.perziureti_produktus)
        self.pamatytireceptus = Button(langas, text="Pamatyti visus turimus receptus", command=self.perziureti_receptus)
        self.kagalimepagaminti = Button(langas, text="Pamatyti visus imanomus pagaminti receptus", command=self.galimpagaminti)
        self.pamatytiingredientus = Button(langas, text="Pamatyti visus ingredientus pasirinktam receptui", command=self.perziureti_ingredientus)
        self.label3 = Label(langas, text="---------PRODUKTU SUNAUDOJIMAS---------")
        self.gaminam = Button(langas, text="Gaminti recepta", command=self.gaminame)
        self.label4 = Label(langas, text="---------TRINIMAS---------")
        self.istrintiprodukta = Button(langas, text="Istrinti produkta", command=self.trinuprod)
        self.istrintirecepta = Button(langas, text="Istrinti recepta", command=self.trinurec)
        self.label5 = Label(langas, text="---------ATNAUJINIMAS---------")
        self.atnaujintiprodukta = Button(langas, text="Atnaujinti turima produkta", command=self.atnaujintiprod)
        self.atnaujintirecepta = Button(langas, text="Atnaujinti turima recepta", command=self.atnaujintirec)
        self.label6 = Label(langas, text="---------UZDARYMAS---------")
        self.exit = Button(langas, text="Iseiti", command=self.uzdaryti)
        self.listboxas = Listbox(langas, width=45)
        # self.frame = Frame(langas, width=100, height=100)
        # image1=PhotoImage(file = "a.png")
        # self.label = Label(self.frame, image=image1)
        # self.label.image = image1
        self.pasirinkimas.grid(row=0, column=1)
        self.label1.grid(row=1, column=1)
        self.pridetiproduktapasiul.grid(row=2, column=1)
        self.pridetiprodukta.grid(row=3, column=1)
        self.pridetirecepta.grid(row=22, column=1)
        self.pridetiproduktarecep.grid(row=4, column=1)
        self.label2.grid(row=5, column=1)
        self.pamatytipasiula.grid(row=6, column=1)
        self.pamatytiproduktus.grid(row=7, column=1)
        self.pamatytireceptus.grid(row=8, column=1)
        self.kagalimepagaminti.grid(row=9, column=1)
        self.pamatytiingredientus.grid(row=10, column=1)
        self.label3.grid(row=11, column=1)
        self.gaminam.grid(row=12, column=1)
        self.label4.grid(row=13, column=1)
        self.istrintiprodukta.grid(row=14, column=1)
        self.istrintirecepta.grid(row=15, column=1)
        self.label5.grid(row=16, column=1)
        self.atnaujintiprodukta.grid(row=17, column=1)
        self.atnaujintirecepta.grid(row=18, column=1)
        self.label6.grid(row=19, column=1)
        self.exit.grid(row=20, column=1)
        # self.frame.grid(row=8, column=2, sticky=E)
        # self.label.pack()
        self.listboxas.grid(row=1, rowspan=6, column=2)


    def prideti_produkta_pasiul(self):
        self.pridejimo = Toplevel(self.langas) 
        self.label1 = Label(self.pridejimo, text= "Irasykite produkto pavadinima")
        self.label2 = Label(self.pridejimo, text= "Irasykite kaip produktas matuojamas")
        self.entry1 = Entry(self.pridejimo)
        self.entry2 = Entry(self.pridejimo)
        self.button = Button(self.pridejimo, text="Spauskite, kad prideti", command=self.prid_pasiul_spaud)
        self.label1.grid(row=0, column=0)
        self.label2.grid(row=1, column=0)
        self.entry1.grid(row=0, column=1)
        self.entry2.grid(row=1, column=1)
        self.button.grid(row=5, columnspan=2)
        
         
    def prid_pasiul_spaud(self):
        pavadinimas = self.entry1.get()
        mato_vnt = self.entry2.get()
        try:
            produktas = Produktas(pavadinimas=pavadinimas, mato_vnt=mato_vnt)
            session.add(produktas)
            session.commit()
            self.entry1.delete(0, END)
            self.entry2.delete(0, END)
        except:
            print("Kažką blogai įrašėte")

    
    def prideti_produkta_turim(self):
        self.pridejimo = Toplevel(self.langas) 
        self.label1 = Label(self.pridejimo, text= "Irasykite produkto ID is pasiulos")
        self.label2 = Label(self.pridejimo, text= "Irasykite kiek turime")
        self.entry1 = Entry(self.pridejimo)
        self.entry2 = Entry(self.pridejimo)
        self.button = Button(self.pridejimo, text="Spauskite, kad prideti", command=self.prid_turim_spaud)
        self.label1.grid(row=0, column=0)
        self.label2.grid(row=1, column=0)
        self.entry1.grid(row=0, column=1)
        self.entry2.grid(row=1, column=1)
        self.button.grid(row=5, columnspan=2)

    def prid_turim_spaud(self):
        produktas_id = self.entry1.get()
        kiekis = self.entry2.get()
        try:
            produktas = TurimasProduktas(produktas_id=produktas_id, kiekis=kiekis)
            session.add(produktas)
            session.commit()
        except:
            print("Kažką blogai įrašėte")
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)


    def prideti_recepta(self):
        self.pridejimo = Toplevel(self.langas) 
        self.label1 = Label(self.pridejimo, text= "Irasykite recepto pavadinima")
        self.entry1 = Entry(self.pridejimo)
        self.button = Button(self.pridejimo, text="Spauskite, kad prideti", command=self.prid_recep_spaud)
        self.label1.grid(row=0, column=0)
        self.entry1.grid(row=0, column=1)
        self.button.grid(row=1, columnspan=2)

    def prid_recep_spaud(self):
        pavadinimas = self.entry1.get()
        try:
            receptas = Receptas(pavadinimas=pavadinimas)
            session.add(receptas)
            session.commit()
        except:
            print("Kažką blogai įrašėte")
        self.entry1.delete(0, END)

    def prideti_produkta_recep(self):
        self.pridejimo = Toplevel(self.langas) 
        self.label1 = Label(self.pridejimo, text= "Irasykite recepto ID is receptu saraso")
        self.label2 = Label(self.pridejimo, text= "Irasykite produkto ID is produktu saraso")
        self.label3 = Label(self.pridejimo, text= "Irasykite produkto kieki")
        self.entry1 = Entry(self.pridejimo)
        self.entry2 = Entry(self.pridejimo)
        self.entry3 = Entry(self.pridejimo)
        self.button = Button(self.pridejimo, text="Spauskite, kad prideti", command=self.prideti_produkta_recep_spaud)
        self.label1.grid(row=0, column=0)
        self.label2.grid(row=1, column=0)
        self.label3.grid(row=2, column=0)
        self.entry1.grid(row=0, column=1)
        self.entry2.grid(row=1, column=1)
        self.entry3.grid(row=2, column=1)
        self.button.grid(row=3, columnspan=2)

    def prideti_produkta_recep_spaud(self):
        receptas_id = self.entry1.get()
        produktas_id = self.entry2.get()
        kiekis = self.entry3.get()
        try:
            produktas = ProduktasRecepte(receptas_id=receptas_id, produktas_id=produktas_id, kiekis=kiekis)
            session.add(produktas)
            session.commit()
        except:
            print("Kažką blogai įrašėte")
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)

    def perziureti_pasiula(self):
        self.listboxas.delete(0, END)
        visi = session.query(Produktas).all()
        for produktas in visi:
            self.listboxas.insert(END, produktas)

    def perziureti_produktus(self):
        self.listboxas.delete(0, END)
        visi = session.query(TurimasProduktas).all()
        for produktas in visi:
            self.listboxas.insert(END, produktas)

    def perziureti_receptus(self):
        self.listboxas.delete(0, END)
        visi = session.query(Receptas).all()
        for receptas in visi:
            self.listboxas.insert(END, receptas)

    def galimpagaminti(self):
        sarasas = []
        turimi = session.query(TurimasProduktas).all()
        for produktas_turimas in turimi:
            sarasas.append(produktas_turimas.produktas_id)
        for receptas in session.query(Receptas).all():
            atfiltruoti = session.query(ProduktasRecepte).filter(ProduktasRecepte.receptas_id == receptas.id)
            print("---")
            a = 0
            for produktas in atfiltruoti:
                if produktas.produktas_id in sarasas:
                    pass
                else:
                    a += 1
            if a == 0:
                print(receptas.pavadinimas)
            else:
                print(f"{receptas.pavadinimas} neuztenka produktu")


    def perziureti_ingredientus(self):
        self.pridejimo = Toplevel(self.langas) 
        self.label1 = Label(self.pridejimo, text= "Irasykite recepto ID is receptu saraso")
        self.entry1 = Entry(self.pridejimo)
        self.button = Button(self.pridejimo, text="Spauskite, kad perziureti", command=self.perziureti_ingredientus_spaud)
        self.label1.grid(row=0, column=0)
        self.entry1.grid(row=0, column=1)
        self.button.grid(row=1, columnspan=2)
        

    def perziureti_ingredientus_spaud(self):
        self.listboxas.delete(0, END)
        visi = session.query(ProduktasRecepte).all()
        for ingredientas in visi:
            if ingredientas.receptas_id == int(self.entry1.get()):
                self.listboxas.insert(END, ingredientas)
            
            

    def gaminame(self):
        pass

    def trinuprod(self):
        self.trinimo = Toplevel(self.langas) 
        self.label1 = Label(self.trinimo, text= "Irasykite trinamo produkto ID is turimu produktu saraso")
        self.entry1 = Entry(self.trinimo)
        self.button = Button(self.trinimo, text="Spauskite, kad trinti", command=self.trinuprod_spaud)
        self.label1.grid(row=0, column=0)
        self.entry1.grid(row=0, column=1)
        self.button.grid(row=1, columnspan=2)

    def trinuprod_spaud(self):
        session.query(TurimasProduktas).filter(TurimasProduktas.id == int(self.entry1.get())).delete()
        session.commit()
        self.perziureti_produktus()

    def trinurec(self):
        self.trinimo = Toplevel(self.langas) 
        self.label1 = Label(self.trinimo, text= "Irasykite trinamo recepto ID is receptu saraso")
        self.entry1 = Entry(self.trinimo)
        self.button = Button(self.trinimo, text="Spauskite, kad trinti", command=self.trinurec_spaud)
        self.label1.grid(row=0, column=0)
        self.entry1.grid(row=0, column=1)
        self.button.grid(row=1, columnspan=2)

    def trinurec_spaud(self):
        session.query(Receptas).filter(Receptas.id == int(self.entry1.get())).delete()
        session.commit()
        self.perziureti_receptus()


    def atnaujintiprod(self):
        selected_checkbox = self.listboxas.curselection()
        for i in selected_checkbox:
            id = self.listboxas.get(i).split()[0]
            print(id)
            produktas = session.query(TurimasProduktas).filter(TurimasProduktas.id==id).one()
            print(produktas.kiekis)
        self.pridejimo = Toplevel(self.langas) 
        self.label1 = Label(self.pridejimo, text= "Irasykite kiek turime")
        self.entry1 = Entry(self.pridejimo)
        self.entry1.insert(0, produktas.kiekis)
        self.button = Button(self.pridejimo, text="Spauskite, kad atnaujinti", command=self.atnaujinti_prod_spaud)
        self.label1.grid(row=0, column=0)
        self.entry1.grid(row=0, column=1)
        self.button.grid(row=1, columnspan=2)
    
    def atnaujinti_prod_spaud(self):
        pass
        
    
    
    
    def atnaujintirec(self):
        pass

    


    def perziureti(self):
        # self.listboxas.delete(0, END)
        # visi = session.query(Uzt2).all()
        # for darbuotojas in visi:
        #     self.listboxas.insert(END, darbuotojas)
        pass

    def trinu(self):
        # selected_checkbox = self.listboxas.curselection()
        # for i in selected_checkbox:
        #     id = self.listboxas.get(i).split()[0]
        #     session.query(Uzt2).filter(Uzt2.id==id).delete()
        #     session.commit()
        #     self.listboxas.delete(selected_checkbox)
        pass
        
    def atnauj_spaud(self, darbuotojas):
        # darbuotojas.vardas = self.entry11.get()
        # darbuotojas.pavarde = self.entry21.get()
        # darbuotojas.gime = self.entry31.get()
        # darbuotojas.pareigos = self.entry41.get()
        # darbuotojas.atlyginimas = self.entry51.get()
        # session.commit()
        # self.perziureti()
        pass


    def atnaujinti(self):
        # selected_checkbox = self.listboxas.curselection()
        # for i in selected_checkbox:
        #     id = self.listboxas.get(i).split()[0]
        #     darbuotojas = session.query(Uzt2).filter(Uzt2.id==id).one()
        # self.atnaujinimo = Toplevel(self.langas) 
        # self.label1 = Label(self.atnaujinimo, text= "Irasykit varda")
        # self.label2 = Label(self.atnaujinimo, text= "Irasykit pavarde")
        # self.label3 = Label(self.atnaujinimo, text= "Irasykit kada gime")
        # self.label4 = Label(self.atnaujinimo, text= "Irasykit pareigas")
        # self.label5 = Label(self.atnaujinimo, text= "Irasykit atlyginima")
        # self.entry11 = Entry(self.atnaujinimo)
        # self.entry11.insert(0, darbuotojas.vardas)
        # self.entry21 = Entry(self.atnaujinimo)
        # self.entry21.insert(0, darbuotojas.pavarde)
        # self.entry31 = Entry(self.atnaujinimo)
        # self.entry31.insert(0, darbuotojas.gime)
        # self.entry41 = Entry(self.atnaujinimo)
        # self.entry41.insert(0, darbuotojas.pareigos)
        # self.entry51 = Entry(self.atnaujinimo)
        # self.entry51.insert(0, darbuotojas.atlyginimas)
        # self.button7 = Button(self.atnaujinimo, text="Spauskite, kad atnaujinti")
        # self.button7.bind("<Button-1>", lambda event: self.atnauj_spaud(darbuotojas))
        # self.label1.grid(row=0, column=0)
        # self.label2.grid(row=1, column=0)
        # self.label3.grid(row=2, column=0)
        # self.label4.grid(row=3, column=0)
        # self.label5.grid(row=4, column=0)
        # self.entry11.grid(row=0, column=1)
        # self.entry21.grid(row=1, column=1)
        # self.entry31.grid(row=2, column=1)
        # self.entry41.grid(row=3, column=1)
        # self.entry51.grid(row=4, column=1)
        # self.button7.grid(row=5, columnspan=2)
        pass
        
       

    def uzdaryti(self):
        self.langas.destroy()



def main():
    langas = Tk()
    app = Pagrindinis(langas)
    langas.mainloop()


if __name__ == '__main__':
    main()
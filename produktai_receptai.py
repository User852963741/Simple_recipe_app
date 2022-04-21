from datetime import date, datetime
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from models import *
from PIL import ImageTk
import PIL.Image

from tkinter import *

# import logging

# logger = logging.getLogger(__name__)
# logger_file = logging.FileHandler("produktai_receptai.log")
# logger.addHandler(logger_file)
# logger.setLevel(logging.INFO)
# logger_formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(module)s:%(lineno)d:%(message)s")
# logger_file.setFormatter(logger_formatter)

# streamer_handler = logging.StreamHandler()
# streamer_handler.setFormatter(logger_formatter)
# logger.addHandler(streamer_handler)

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
        self.mygtukas_prideti_produkta_pasiul = Button(langas, text="Pridėti produkta prie pasiūlos", command=self.prideti_produkta_pasiul)
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
        self.label6 = Label(langas, text="---------UZDARYMAS---------")
        self.exit = Button(langas, text="Iseiti", command=self.uzdaryti)
        self.listboxas = Listbox(langas, width=45)
        # self.frame = Frame(langas, width=100, height=100)
        # image1=PhotoImage(file = "a.png")
        # self.label = Label(self.frame, image=image1)
        # self.label.image = image1
        self.pasirinkimas.grid(row=0, column=1)
        self.label1.grid(row=1, column=1)
        self.mygtukas_prideti_produkta_pasiul.grid(row=2, column=1)
        self.pridetiprodukta.grid(row=3, column=1)
        self.pridetirecepta.grid(row=4, column=1)
        self.pridetiproduktarecep.grid(row=5, column=1)
        self.label2.grid(row=6, column=1)
        self.pamatytipasiula.grid(row=7, column=1)
        self.pamatytiproduktus.grid(row=8, column=1)
        self.pamatytireceptus.grid(row=9, column=1)
        self.kagalimepagaminti.grid(row=10, column=1)
        self.pamatytiingredientus.grid(row=11, column=1)
        self.label3.grid(row=12, column=1)
        self.gaminam.grid(row=13, column=1)
        self.label4.grid(row=14, column=1)
        self.istrintiprodukta.grid(row=15, column=1)
        self.istrintirecepta.grid(row=16, column=1)
        self.label5.grid(row=17, column=1)
        self.atnaujintiprodukta.grid(row=18, column=1)
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
        self.label1 = Label(self.pridejimo, text="Irasykite produkto ID is pasiulos")
        self.label2 = Label(self.pridejimo, text="Irasykite kiek turime")
        self.entry1 = Entry(self.pridejimo)
        self.entry2 = Entry(self.pridejimo)
        self.button = Button(self.pridejimo, text="Spauskite, kad prideti", command=self.prid_turim_spaud)
        self.label1.grid(row=0, column=0)
        self.label2.grid(row=1, column=0)
        self.entry1.grid(row=0, column=1)
        self.entry2.grid(row=1, column=1)
        self.button.grid(row=5, columnspan=2)

    def prid_turim_spaud(self):
        sarasas = []
        turimi = session.query(TurimasProduktas).all()
        for produktas_turimas in turimi:
            sarasas.append(produktas_turimas.produktas_id)
        produktas_id = self.entry1.get()
        kiekis = self.entry2.get()
        if int(produktas_id) in sarasas:
            self.eroras = Toplevel(self.pridejimo)
            self.label1 = Label(self.eroras, text="Toks produktas jau egzistuoja, atnaujinkite kieki")
            self.label1.grid(row=0, column=0)
        else:
            try:
                produktas = TurimasProduktas(produktas_id=produktas_id, kiekis=kiekis)
                session.add(produktas)
                session.commit()
            except:
                print("Kažką blogai įrašėte")
            else:
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
        self.listboxas.delete(0, END)
        sarasas = []
        sarasiukas = []
        turimi = session.query(TurimasProduktas).all()
        for produktas_turimas in turimi:
            sarasas.append(produktas_turimas.produktas_id)
        for receptas in session.query(Receptas).all():
            atfiltruoti = session.query(ProduktasRecepte).filter(ProduktasRecepte.receptas_id == receptas.id)
            trukumas = 0
            for produktas in atfiltruoti:
                turimas_produktas = session.query(TurimasProduktas).filter(TurimasProduktas.produktas_id == produktas.produktas_id).first()
                if produktas.produktas_id in sarasas:
                    if produktas.kiekis > turimas_produktas.kiekis:
                        trukumas += 1
                else:
                    trukumas += 1
            if trukumas == 0:
                self.listboxas.insert(END, receptas)
                sarasiukas.append(receptas.id)
            else:
                pass
        return sarasiukas
                
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
        self.gaminimo = Toplevel(self.langas) 
        self.label1 = Label(self.gaminimo, text= "Irasykite gaminamo recepto ID is receptu saraso")
        self.entry1 = Entry(self.gaminimo)
        self.button = Button(self.gaminimo, text="Spauskite, kad gaminti", command=self.gaminame_spaud)
        self.label1.grid(row=0, column=0)
        self.entry1.grid(row=0, column=1)
        self.button.grid(row=1, columnspan=2)

    def gaminame_spaud(self):
        id =  self.entry1.get()
        atfiltruoti = session.query(ProduktasRecepte).filter(ProduktasRecepte.receptas_id == int(id))
        sarasiukas = self.galimpagaminti()
        if int(id) in sarasiukas:
            for produktas in atfiltruoti:
                turimas_produktas = session.query(TurimasProduktas).filter(TurimasProduktas.produktas_id == produktas.produktas_id).first()
                turimas_produktas.kiekis -= produktas.kiekis
            self.skanaus = Toplevel(self.gaminimo)
            self.label1 = Label(self.skanaus, text=f"Niam niam, skanaus")
            self.label1.grid(row=0, column=0)
        else:
            self.eroras = Toplevel(self.gaminimo)
            self.label1 = Label(self.eroras, text="Neuztenka produktu siam receptui pagaminti")
            self.label1.grid(row=0, column=0)

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
        self.atnaujinimo = Toplevel(self.langas) 
        self.label1 = Label(self.atnaujinimo, text= "Irasykite atnaujinamo produkto ID is turimu produktu saraso")
        self.entry1 = Entry(self.atnaujinimo)
        self.label2 = Label(self.atnaujinimo, text= "Iveskite nauja kieki")
        self.entry2 = Entry(self.atnaujinimo)
        self.button = Button(self.atnaujinimo, text="Spauskite, kad atnaujinti", command=self.atnaujinti_prod_spaud)
        self.label1.grid(row=0, column=0)
        self.entry1.grid(row=0, column=1)
        self.label2.grid(row=1, column=0)
        self.entry2.grid(row=1, column=1)
        self.button.grid(row=2, columnspan=3)

    def atnaujinti_prod_spaud(self):
        produktas = session.query(TurimasProduktas).filter(TurimasProduktas.id==int(self.entry1.get())).one()
        if int(self.entry2.get()) > 0:
            produktas.kiekis = int(self.entry2.get())
        else:
            session.query(TurimasProduktas).filter(TurimasProduktas.id==int(self.entry1.get())).delete()
        session.commit()
        self.perziureti_produktus()

    def uzdaryti(self):
        self.langas.destroy()

def main():
    langas = Tk()
    app = Pagrindinis(langas)
    langas.mainloop()

if __name__ == '__main__':
    main()

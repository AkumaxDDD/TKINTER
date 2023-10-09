from PIL import ImageTk , Image
from tkinter import * 
from tkinter import ttk 
import tkinter as tk

ventana = tk.Tk() 
ventana.title("Calculadora de BTU/Frigorias")
ventana.iconbitmap("icono.ico")
ventana.config(width = 1000 , height = 1000 , bg= "#52AC9C")
fondo=PhotoImage(file="o.gif")
lblFondo=Label(ventana,border=0,image=fondo).place(x=0,y=0)
def calcular_total():
    cargatermicapers= int (cajadetexto_carga_termica_pers.get())
    carga_termica_pers= (cargatermicapers * 500)
    cargatermicatvs= int (cajadetexto_carga_termica_tvs.get())
    carga_termica_tvs= (cargatermicatvs * 600)
    cargatermicapcs= int (cajadetexto_carga_termica_pcs.get())
    carga_termica_pcs= (cargatermicapcs * 400)
    cargatermicalam= int (cajadetexto_carga_termica_lam.get())
    carga_termica_lam= (cargatermicalam * 200)
    
    cargatermica= int ()
    carga_termica= int(carga_termica_pers + carga_termica_tvs + carga_termica_pcs + carga_termica_lam)
    etiquete_carga_termica_tvs.config(text=f"btu tvs: {carga_termica_tvs}",background="#52AC9C")
    etiquete_carga_termica_pers.config(text=f"btu personas: {carga_termica_pers}",background="#52AC9C") 
    etiquete_carga_termica_pcs.config(text=f"btu computadoras: {carga_termica_pcs}",background="#52AC9C")
    etiquete_carga_termica_lam.config(text=f"btu lamparas: {carga_termica_lam}",background="#52AC9C")
    etiquete_carga_termica.config(text=f"La carga termica es: {carga_termica}",background="#52AC9C")    
    etiquete_carga_termica.configure(font=("Arial", 10))
etiquete_carga_termica=ttk.Label(text="Carga Termica",background="#52AC9C")
etiquete_carga_termica.configure(font=("Arial", 10))
etiquete_carga_termica.place (x=20, y=200)

boton_ok0 = ttk.Button (text="total",command=calcular_total)
boton_ok0.place(x=220, y=200)

etiquete_carga_termica_pers=ttk.Label(text="personas",background="#52AC9C")
etiquete_carga_termica_pers.place (x=20, y=240)

default_value = "0"

cajadetexto_carga_termica_pers=ttk.Entry()
cajadetexto_carga_termica_pers.place(x=160, y =240,width=50)
cajadetexto_carga_termica_pers.insert(0, default_value)

etiquete_carga_termica_tvs=ttk.Label(text="televisores",background="#52AC9C")
etiquete_carga_termica_tvs.place (x=20, y=280)

cajadetexto_carga_termica_tvs= ttk.Entry()
cajadetexto_carga_termica_tvs.place(x=160, y =280,width=50)
cajadetexto_carga_termica_tvs.insert(0,default_value)

etiquete_carga_termica_pcs=ttk.Label(text="computadoras",background="#52AC9C")
etiquete_carga_termica_pcs.place (x=20, y=320)

cajadetexto_carga_termica_pcs= ttk.Entry()
cajadetexto_carga_termica_pcs.place(x=160, y =320,width=50)
cajadetexto_carga_termica_pcs.insert(0,default_value)

etiquete_carga_termica_lam=ttk.Label(text="lamparas",background="#52AC9C")
etiquete_carga_termica_lam.place (x=20, y=360)

cajadetexto_carga_termica_lam= ttk.Entry()
cajadetexto_carga_termica_lam.place(x=160, y =360,width=50)
cajadetexto_carga_termica_lam.insert(0,default_value)

def selection_changed(event):
    selection = clima.get()
    
    if (clima.get() == "Frio"): 
        etiqueta_txt2.config(text= f"clima selecionado: {clima.get()} y suma {500} BTU")
        etiqueta_txt2.configure(font=("Arial", 10))
    elif (clima.get() == "Templado"): 
        etiqueta_txt2.config(text=f"clima selecionado: {clima.get()} y suma {550} BTU")
        etiqueta_txt2.configure(font=("Arial", 10))
    elif (clima.get() == "Calido"): 
        etiqueta_txt2.config(text=f" clima selecionado: {clima.get()} y suma {600} BTU")
        etiqueta_txt2.configure(font=("Arial", 10))
    else:
        etiqueta_txt2.config(text=f"clima selecionado: {clima.get()} y suma {650} BTU")
        etiqueta_txt2.configure(font=("Arial", 10))
    etiqueta_txt2.config (text=f" {selection_changed(event)} ")

clima = ttk.Combobox(values=["Frio","Templado", "Calido", "Muy calido"])
clima.bind("<<ComboboxSelected>>",selection_changed )
clima.place(x=140, y=120)
clima.insert(0,"Frio")

etiqueta_txt2 = ttk.Label (text=f"clima seleccionado: {clima.get()} y suma {500} BTU",background="#52AC9C")
etiqueta_txt2.place(x=160 , y=150)

etiqueta_txt = ttk.Label (text="Seleccione su clima: ",background="#52AC9C")
etiqueta_txt2.configure(font=("Arial", 10))
etiqueta_txt.place(x=140 , y=80)

def calcular_btuarea():

    btuarea= int(cajadetexto_btu_area.get())
    btu_area= (btuarea * 650)
    etiquete_btu_area.config(text=f"BTU AREA: {btu_area}")
    etiquete_btu_area.configure(font=("Arial", 10))

etiquete_btu_area=ttk.Label(text="Area en m2 ",background="#52AC9C")
etiquete_btu_area.configure(font=("Arial", 10))
etiquete_btu_area.place (x=20, y=20)

cajadetexto_btu_area= ttk.Entry()
cajadetexto_btu_area.place(x=160, y =20,width=50)
cajadetexto_btu_area.insert(0,default_value)

etiquete_btu_area = ttk.Label (text= "Total BTU del Area en m2",background="#52AC9C")
etiquete_btu_area.configure(font=("Arial", 10))
etiquete_btu_area.place(x=20, y=50)

boton_Aceptar = ttk.Button (text="calcular BTU",command=calcular_btuarea)
boton_Aceptar.place(x=220, y=20)

def calcular_frigorias():
    btuarea= int (cajadetexto_btu_area.get())
    btu_area= (btuarea * 650)
    if (clima.get() == "Frio"): 
        climatico=500
    elif (clima.get() == "Templado"): 
        climatico=550
    elif (clima.get() == "Calido"): 
        climatico=600
    else:
        climatico=650
    cargatermicapers= float (cajadetexto_carga_termica_pers.get())
    carga_termica_pers= (cargatermicapers * 500)
    cargatermicatvs= float (cajadetexto_carga_termica_tvs.get())
    carga_termica_tvs= (cargatermicatvs * 600)
    cargatermicapcs= float (cajadetexto_carga_termica_pcs.get())
    carga_termica_pcs= (cargatermicapcs * 400)
    cargatermicalam= float (cajadetexto_carga_termica_lam.get())
    carga_termica_lam= (cargatermicalam * 200)
    
    cargatermica= float ()
    carga_termica= float(carga_termica_pers + carga_termica_tvs + carga_termica_pcs + carga_termica_lam)
    
    btu_fgs=int( carga_termica + btu_area + climatico) / 4 
    etiquete_btu_fgs.config(text=f"Frigorias : {int(btu_fgs)}")
etiquete_btu_fgs = ttk.Label (text= "Total de Frigorias: ",background="#52AC9C",)
etiquete_btu_fgs.configure(font=("Arial",14))
etiquete_btu_fgs.place(x=20, y=400)

boton_Aceptar = ttk.Button (text="calcular Frigorias",command=calcular_frigorias)
boton_Aceptar.place(x=200, y=400)

def calcular_watts():
    btuarea= int (cajadetexto_btu_area.get())
    btu_area= (btuarea * 650)
    if (clima.get() == "Frio"): 
        climatico=500
    elif (clima.get() == "Templado"): 
        climatico=550
    elif (clima.get() == "Calido"): 
        climatico=600
    else:
        climatico=650
    cargatermicapers= float (cajadetexto_carga_termica_pers.get())
    carga_termica_pers= (cargatermicapers * 500)
    cargatermicatvs= float (cajadetexto_carga_termica_tvs.get())
    carga_termica_tvs= (cargatermicatvs * 600)
    cargatermicapcs= float (cajadetexto_carga_termica_pcs.get())
    carga_termica_pcs= (cargatermicapcs * 400)
    cargatermicalam= float (cajadetexto_carga_termica_lam.get())
    carga_termica_lam= (cargatermicalam * 200)
    
    cargatermica= float ()
    carga_termica= float(carga_termica_pers + carga_termica_tvs + carga_termica_pcs + carga_termica_lam)
    btu_fgs=int( carga_termica + btu_area + climatico) / 4 
    fgs_watts=int(btu_fgs*1.14)
    etiquete_fgs_watts.config(text=f"Watts : {fgs_watts}")
etiquete_fgs_watts = ttk.Label (text= "Total de Watts: ",background="#52AC9C")
etiquete_fgs_watts.configure(font=("Arial",14,))
etiquete_fgs_watts.place(x=20, y=440)


boton_Aceptar = ttk.Button (text="Convertir a Watts",command=calcular_watts)
boton_Aceptar.place(x=200, y=440)

ventana.mainloop()


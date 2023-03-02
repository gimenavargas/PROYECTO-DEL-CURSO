import tkinter

#------------------------ Window ------------------------

ventana = tkinter.Tk()
ventana.title("FERRETERIA EL TORNILLO FELIZ")
ventana.config(background="#808080")
ventana. geometry("700x500")
ventana. resizable(0, 0)

#------------------------ Functions ------------------------

def calcular():
    subtotal1 = float(precio1Txt.get())*float(cantidad1Txt.get())
    importe1Txt.insert(0,str(subtotal1))

    subtotal2 = float(precio2Txt.get())*float(cantidad2Txt.get())
    importe2Txt.insert(0,str(subtotal2))

    subtotal3 = float(precio3Txt.get())*float(cantidad3Txt.get())
    importe3Txt.insert(0,str(subtotal3))

    subtotal4 = float(precio4Txt.get())*float(cantidad4Txt.get())
    importe4Txt.insert(0,str(subtotal4))

    totaltodos = float(importe1Txt.get()) + float(importe2Txt.get()) + float(importe3Txt.get()) + float(importe4Txt.get())
    totalTxt.insert(0, str(totaltodos)) 
    

def detallarPrecios1(nombre):
    precio1Txt.delete(0, tkinter.END)
    precio1Txt.insert(0, productos[nombre])

def detallarPrecios2(nombre):
    precio2Txt.delete(0, tkinter.END)
    precio2Txt.insert(0, productos[nombre])

def detallarPrecios3(nombre):
    precio3Txt.delete(0, tkinter.END)
    precio3Txt.insert(0, productos[nombre])

def detallarPrecios4(nombre):
    precio4Txt.delete(0, tkinter.END)
    precio4Txt.insert(0, productos[nombre])              
  
def eliminarTexto():
  apellidoTxt.delete(0, tkinter.END)
  dniTxt.delete(0, tkinter.END)
  nombreTxt.delete(0, tkinter.END)
  telefonoTxt.delete(0, tkinter.END)
  correoTxt.delete(0, tkinter.END)
  precio1Txt.delete(0, tkinter.END)
  precio2Txt.delete(0, tkinter.END)
  precio3Txt.delete(0, tkinter.END)
  precio4Txt.delete(0, tkinter.END)
  cantidad1Txt.delete(0, tkinter.END)
  cantidad2Txt.delete(0, tkinter.END)
  cantidad3Txt.delete(0, tkinter.END)
  cantidad4Txt.delete(0, tkinter.END)
  importe1Txt.delete(0, tkinter.END)
  importe2Txt.delete(0, tkinter.END)
  importe3Txt.delete(0, tkinter.END)
  importe4Txt.delete(0, tkinter.END)
  totalTxt.delete(0, tkinter.END)

#------------------------ Products ------------------------  

productos = {
    "Martillo"                : 25,
    "Guantes de seguridad"    : 12,
    "Llave Inglesa"           : 10,
    "Taladro"                 : 45,
    "Destornillador"          : 18,
    "Cerraduras"              : 30,
    "Alicate"                 : 14
}

#------------------------ Labels, Text boxes and Buttons ------------------------

tiendaSticker = tkinter.Label(ventana, text = "FERRETERIA EL TORNILLO FELIZ", font= "ALGERIAN 16", bg="#707070", fg="white" )
nombresSticker = tkinter.Label(ventana, text = "Nombre(s):", font= "Arial 14", bg="#707070")
apellidosSticker = tkinter.Label(ventana, text = "Apellidos:", font= "Arial 14", bg="#707070")
dniSticker = tkinter.Label(ventana, text = "DNI:", font= "Arial 14", bg="#707070")
telefonoSticker = tkinter.Label(ventana, text = "Teléfono:", font= "Arial 14", bg= "#707070")
correoSticker = tkinter.Label(ventana, text = "Correo:", font= "Arial 14", bg= "#707070")
productoSticker = tkinter.Label(ventana, text = "Producto:", font= "Arial 14", bg= "#707070")
precioSticker = tkinter.Label(ventana, text = "Precio:", font= "Arial 14", bg= "#707070")
cantidadSticker = tkinter.Label(ventana, text = "Cantidad:", font= "Arial 14", bg= "#707070")
importeSticker = tkinter.Label(ventana, text = "Importe:", font= "Arial 14", bg= "#707070")
totalSticker = tkinter.Label(ventana, text = "Total:", font= "Arial 14", bg= "#707070")

tiendaSticker.place(x=220, y=20)
apellidosSticker.place(x= 50, y= 75)
dniSticker.place(x= 70, y= 120)
nombresSticker.place(x= 410, y= 70)
telefonoSticker.place(x= 410, y= 120)
correoSticker.place(x= 50 ,y= 180)
productoSticker.place(x= 100 ,y= 250)
precioSticker.place(x= 300 ,y= 250)
cantidadSticker.place(x= 440 ,y= 250)
importeSticker.place(x= 580 ,y= 250)
totalSticker.place(x= 480 ,y= 460)

apellidoTxt = tkinter.Entry(ventana, width=18 ,font = "Arial 12")
dniTxt = tkinter.Entry(ventana, width=18, font = "Arial 12")
nombreTxt = tkinter.Entry(ventana, width=18, font = "Arial 12")
telefonoTxt = tkinter.Entry(ventana, width=18, font = "Arial 12")
correoTxt = tkinter.Entry(ventana, width=55, font = "Arial 12")
precio1Txt = tkinter.Entry(ventana, width=10, font = "Arial 12")
precio2Txt = tkinter.Entry(ventana, width=10, font = "Arial 12")
precio3Txt = tkinter.Entry(ventana, width=10, font = "Arial 12")
precio4Txt = tkinter.Entry(ventana, width=10, font = "Arial 12")
cantidad1Txt = tkinter.Entry(ventana, width=10, font = "Arial 12")
cantidad2Txt = tkinter.Entry(ventana, width=10, font = "Arial 12")
cantidad3Txt = tkinter.Entry(ventana, width=10, font = "Arial 12")
cantidad4Txt = tkinter.Entry(ventana, width=10, font = "Arial 12")
importe1Txt = tkinter.Entry(ventana, width=10, font = "Arial 12")
importe2Txt = tkinter.Entry(ventana, width=10, font = "Arial 12")
importe3Txt = tkinter.Entry(ventana, width=10, font = "Arial 12")
importe4Txt = tkinter.Entry(ventana, width=10, font = "Arial 12")
totalTxt = tkinter.Entry(ventana, width=10, font = "Arial 12")

apellidoTxt.place(x= 175, y = 75)
dniTxt.place(x= 175, y = 120)
nombreTxt.place(x= 520, y = 74)
telefonoTxt.place(x= 520, y = 120)
correoTxt.place(x= 175, y = 180)
precio1Txt.place(x= 285, y = 300)
precio2Txt.place(x= 285, y = 340)
precio3Txt.place(x= 285, y = 380)
precio4Txt.place(x= 285, y = 420)
cantidad1Txt.place(x= 435, y = 300)
cantidad2Txt.place(x= 435, y = 340)
cantidad3Txt.place(x= 435, y = 380)
cantidad4Txt.place(x= 435, y = 420)
importe1Txt.place(x= 575, y = 300)
importe2Txt.place(x= 575, y = 340)
importe3Txt.place(x= 575, y = 380)
importe4Txt.place(x= 575, y = 420)
totalTxt.place(x= 575, y = 460)

boton1= tkinter.Button(ventana, text = "Calcular", font= "Arial 12", bg="white", fg="blue", command= calcular)
boton2= tkinter.Button(ventana, text = "Reiniciar", font= "Arial 12", bg="white", fg="red", command= eliminarTexto)

boton1.place(x= 55 , y = 460)
boton2.place(x= 150 , y = 460)

#------------------------ Products and prices modules ------------------------


tuplaProductos1 = ("Martillo", "guantes de seguridad", "Llave Inglesa", "Taladro", "Destornillador", "Cerraduras", "Alicate")

itemProductos1 = tkinter.StringVar(ventana, value = "Selecciona un producto")

listaProductos1 = tkinter.OptionMenu(ventana, itemProductos1, *tuplaProductos1, command= detallarPrecios1)

listaProductos1.place(x= 55 ,y= 300)

tuplaProductos2 = ("Martillo", "Guantes de seguridad", "Llave Inglesa", "Taladro", "Destornillador", "Cerraduras", "Alicate")

itemProductos2 = tkinter.StringVar(ventana, value = "Selecciona un producto")

listaProductos2 = tkinter.OptionMenu(ventana, itemProductos2, *tuplaProductos2, command= detallarPrecios2)

listaProductos2.place(x= 55 ,y= 340)

tuplaProductos3 = ("Martillo", "Guantes de seguridad", "Llave Inglesa", "Taladro", "Destornillador", "Cerradura", "Alicate")

itemProductos3 = tkinter.StringVar(ventana, value = "Selecciona un producto")

listaProductos3 = tkinter.OptionMenu(ventana, itemProductos3, *tuplaProductos3, command= detallarPrecios3)

listaProductos3.place(x= 55 ,y= 380)

tuplaProductos4 = ("Martillo", "Guantes de seguridad ", "Llave Inglesa", "Taladro", "Destornillador", "Cerraduras", "Alicate")

itemProductos4 = tkinter.StringVar(ventana, value = "Selecciona un producto")

listaProductos4 = tkinter.OptionMenu(ventana, itemProductos4, *tuplaProductos4, command= detallarPrecios4)

listaProductos4.place(x= 55 ,y= 420)

ventana.mainloop()
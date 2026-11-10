from coches import coches
from tkinter import *
from tkinter import messagebox

class App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestion de Coches")
        self.ventana.geometry("1300x800")
        self.ventana.resizable(0,0)
        self.main()

    #   VISTAS del SISTEMA
    def borrarPantalla(self):
        for witget in self.ventana.winfo_children():
            witget.destroy()

    def menu_acciones(self):
        self.borrarPantalla()
        tipo = "Coches"
        Label(self.ventana, text = f"\n...::: Menu de {tipo} :::...").pack(pady=10)
        Button(self.ventana, text = "1.- Agregar", command = self.insertar_view).pack(pady=5)
        Button(self.ventana, text = "2.- Borrar", command = self.eliminar_view).pack(pady=5)
        Button(self.ventana, text = "3.- Modificar", command = self.modificar_view).pack(pady=5)
        Button(self.ventana, text = "4.- Mostrar", command = self.mostrar_view).pack(pady=5)
        Button(self.ventana, text = "5.- Regresar", command = self.main).pack(pady=5)

    def main(self):
            self.borrarPantalla()
            Label(self.ventana, text = "\n...::: M E N U  P R I N C I P A L :::...").pack(pady=10)
            Button(self.ventana, text = "1.- Coches", command = self.menu_acciones).pack(pady=5)
            Button(self.ventana, text = "2.- Salir", command = self.ventana.quit).pack(pady=5)

    def insertar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text = "...Ingresar los datos del coche...").pack(pady = 10)


        Label(self.ventana, text = "Marca:").pack(pady = 5)
        self.marca = Entry(self.ventana)
        self.marca.focus()
        self.marca.pack(pady = 5)

        Label(self.ventana, text = "Color:").pack(pady = 5)
        self.color = Entry(self.ventana)
        self.color.pack(pady = 5)

        Label(self.ventana, text = "Modelo:").pack(pady = 5)
        self.Modelo = Entry(self.ventana)
        self.Modelo.pack(pady = 5)

        Label(self.ventana, text = "Velociadad:").pack(pady = 5)
        self.velocidad = Entry(self.ventana)
        self.velocidad.pack(pady = 5)

        Label(self.ventana, text = "Potencia:").pack(pady = 5)
        self.potencia = Entry(self.ventana)
        self.potencia.pack(pady = 5)

        Label(self.ventana, text = "Asientos:").pack(pady = 5)
        self.asientos = Entry(self.ventana)
        self.asientos.pack(pady = 5)


        Button(self.ventana, text = "Guardar", command = self.insertar_controller).pack(pady = 10)
        Button(self.ventana, text = "Regresar", command = self.menu_acciones).pack(pady = 5)

    def eliminar_view(self):
            self.borrarPantalla()
            Label(self.ventana, text = "...Ingresar el ID del coches a elimiar...").pack(pady = 10)

            Label(self.ventana, text = "ID:").pack(pady = 5)
            self.id = Entry(self.ventana)
            self.id.focus()
            self.id.pack(pady = 5)

            Button(self.ventana, text = "Eliminar", command = self.eliminar_controller).pack(pady = 10)
            Button(self.ventana, text = "Regresar", command = self.menu_acciones).pack(pady = 5)

    def modificar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text = "...Ingresar el ID del coches a modificar...").pack(pady = 10)

        Label(self.ventana, text = "ID:").pack(pady = 5)
        self.id = Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady = 5)


        Label(self.ventana, text = "Nueva Marca:").pack(pady = 5)
        self.marca = Entry(self.ventana)
        self.marca.pack(pady = 5)

        Label(self.ventana, text = "Nuevo Color:").pack(pady = 5)
        self.color = Entry(self.ventana)
        self.color.pack(pady = 5)

        Label(self.ventana, text = "Nuevo Modelo:").pack(pady = 5)
        self.Modelo = Entry(self.ventana)
        self.Modelo.pack(pady = 5)

        Label(self.ventana, text = "Nueva Velociadad:").pack(pady = 5)
        self.velocidad = Entry(self.ventana)
        self.velocidad.pack(pady = 5)

        Label(self.ventana, text = "Nueva Potencia:").pack(pady = 5)
        self.potencia = Entry(self.ventana)
        self.potencia.pack(pady = 5)

        Label(self.ventana, text = "Nuevos Asientos:").pack(pady = 5)
        self.asientos = Entry(self.ventana)
        self.asientos.pack(pady = 5)


        Button(self.ventana, text = "Guardar", command = self.modificar_controller).pack(pady = 10)
        Button(self.ventana, text = "Regresar", command = self.menu_acciones).pack(pady = 5)

    def mostrar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text = "...Consultar los coches...").pack(pady = 10)

        filas = ""
        filas = self.consultar_controller(filas)
        Label(self.ventana, text = f"{'NO.':<22}{'ID':<22}{'MARCA':<22}{'COLOR':<22}{'MODELO':<22}{'VELOCIDAD':<22}{'POTENCIA':<22}{'ASIENTOS'}").pack(pady = 5)
        Label(self.ventana, text = f"{'-'*200}").pack(pady = 5)
        Label(self.ventana, text = f"{filas}").pack(pady = 5)

        Button(self.ventana, text = "Regresar", command = self.menu_acciones).pack(pady = 5)


    #   CONTROLADOR del SISTEMA
    def respuesta_sql(self, respuesta):
        if respuesta:
            messagebox.showinfo(title = "...Exitoso...", message = "...Accion realizada con exito...")
        else:
            messagebox.showerror(title = "...Verifica porfavor...", message = "...Esta accion no pudo realizarse...")
    
    def insertar_controller(self):
        coche1 = coches.Coches(self.marca.get(), self.color.get(), self.Modelo.get(), self.velocidad.get(), self.potencia.get(), self.asientos.get())
        respuesta = coche1.insertar()
        self.respuesta_sql(respuesta)
        del coche1

    def eliminar_controller(self):
        id = self.id.get()
        respuesta = coches.Coches.eliminar(id)
        self.respuesta_sql(respuesta)

    def consultar_controller(self, filas):
        registros = coches.Coches.consultar()

        if len(registros) > 0:
            num_coches = 1
            for fila in registros:
                filas=filas+f"\n{num_coches:<20} \t {fila[0]:<13} \t {fila[1]:<15} \t {fila[2]:<15} \t {fila[3]:<15} \t {fila[4]:<20} \t {fila[5]:<20} \t {fila[6]}\n"
                num_coches += 1
        else:
            filas=" NO existen datos que mostrar por el momento"

        return filas

    def modificar_controller(self):
        id = self.id.get()
        coche1 = coches.Coches(self.marca.get(), self.color.get(), self.Modelo.get(), self.velocidad.get(), self.potencia.get(), self.asientos.get())

        respuesta = coche1.actualizar(id)
        self.respuesta_sql(respuesta)
        del coche1



if __name__ == "__main__":
    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()

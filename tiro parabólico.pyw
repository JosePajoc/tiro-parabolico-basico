from tkinter import Tk, Label, Entry, Button, Canvas, messagebox
import math

ventana = Tk()
ventana.title("Tiro Parabólico")
ventana.geometry("650x400")
Label(ventana, text="Ingrese velocidad inicial en m/s").place(x=5, y=10)
txtV0 = Entry(ventana, width=5)
txtV0.place(x=70, y=40)
Label(ventana, text="Ingrese ángulo de tiro en grados").place(x=5, y=70)
txtAngulo = Entry(ventana, width=5)
txtAngulo.place(x=70, y=100)

def cacular():
    try:
        v0 = float(txtV0.get().strip())
        angulo = math.radians(float(txtAngulo.get().strip()))

        if (angulo>=0 and angulo<=90) and (v0>=0):
            H = (v0**2 * (math.sin(angulo)**2)) / (2 * 9.8)
            distancia = (v0**2 * math.sin(2*angulo)) / (9.8)
            tVuelo = (2*v0*math.sin(angulo)) / (9.8)

            resultados = f"Distancia máxima: {round(distancia, 2)}m\nAltura máxima: {round(H,2)}m\nTiempo de vuelo: {round(tVuelo, 2)}s"
            lblResultados.config(text=resultados)

            lienzo.delete("curva")
            #parábola
            #Se usa como referencia el tiempo de vuelo (con paso de 0.5) y no la distancia en el eje x
            #Para ser proporcional al plano cartesiano se divide dentro de 10
            #xi=Vo⋅cos⁡(θ)⋅t
            #yi=Vo⋅sin⁡(θ)⋅t−(1/2)⋅g⋅t^2
            t = 0
            while t < tVuelo:
                x1 = (v0 * math.cos(angulo) * t) / 10
                y1 = (v0 * math.sin(angulo) * t - 0.5 * 9.8 * t**2 ) / 10
                x2 = (v0 * math.cos(angulo) * (t+0.5) ) / 10
                y2 = (v0 * math.sin(angulo) * (t+0.5) - 0.5 * 9.8 * (t+0.5)**2 ) / 10
                
                lienzo.create_line(50 + 25 * x1, 350 - 25 * y1, 50 + 25 * x2, 350 - 25 * y2, tags="curva")
                if 350 - 25 * y2>=350:
                    break
                
                t += 0.5
        else:
            messagebox.showerror(message="Solo se permiten ángulos\nentre 0 - 90 grados \ny una velocidad inicial positiva")
    except:
        messagebox.showerror(message="Solo se permiten números")


Button(ventana, text="Calcular y graficar", command=cacular).place(x=20, y=150)

lblResultados = Label(ventana, text="Resultados:\nSi utiliza una \nvelocidad inicial muy \nalta la curva no podrá \nvisualizarse de \nforma completa.")
lblResultados.place(x=5, y=210)

lienzo = Canvas(ventana, width=450, height=400, bg="lightblue")
lienzo.place(x=200, y=0)
lienzo.create_line(50, 25, 50, 350)
lienzo.create_line(50, 350, 375, 350)
lienzo.create_text(400, 330, text="Distancia en m")
lienzo.create_text(50, 10, text="Altura en m")

#ejes
for i in range(1,14):
    lienzo.create_line(50 + 25 * i, 340, 50 + 25 * i, 360)
    lienzo.create_text(50 + 25 * i, 370, text=i*10)

    lienzo.create_line(40, 350 - i * 25, 60, 350 - i * 25)
    lienzo.create_text(30, 350 - i * 25, text=i*10)

ventana.mainloop()
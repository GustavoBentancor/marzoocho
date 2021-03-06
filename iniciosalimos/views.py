import sqlite3

from django.shortcuts import render, render_to_response


def inicio(request):
    return render(request, "inicio/Inicio.html", {})


def cine_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    cursor.execute("Select * from Funiciones")
    Funciones = cursor.fetchall()
    db.commit()
    return render_to_response('Categorias/Cine/Cine.html', {'Funciones': Funciones})

def festi_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    cursor.execute("Select * from Eventos where IdCategoria in (4,11)")
    Festivales = cursor.fetchall()
    db.commit()
    return render_to_response('Categorias/Festivales/Festivales.html', {'Festivales': Festivales})


def detalle_festi_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    id_Detalle_Festivales = request.GET.get('id_Festivales', 0)
    Detalle_Festivales = cursor.execute("Select * from Eventos where IdEvento=" + id_Detalle_Festivales)
    Detalle_Festivales = cursor.fetchall()
    db.commit()
    return render_to_response('Categorias/Festivales/Detalle_Festivales.html', {'item': Detalle_Festivales[0]})


def crio_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    cursor.execute("Select * from Eventos where IdCategoria in (1,4)")
    Criollas = cursor.fetchall()
    db.commit()
    return render_to_response('Categorias/Criollas/Criollas.html', {'Criollas': Criollas})


def gastro_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    cursor.execute("Select * from Lugares where IdCategoria in (8,2)")
    Gastronomia = cursor.fetchall()
    db.commit()
    return render_to_response('Categorias/Gastronomia/Gastronomia.html', {'Gastronomia': Gastronomia})


def detalle_gastro_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    id_Detalle_Gastronomia = request.GET.get('id_Gastronomia', 0)
    Detalle_Gastronomia = cursor.execute("Select * from Lugares where IdLugar=" + id_Detalle_Gastronomia)
    Detalle_Gastronomia = cursor.fetchall()
    db.commit()
    return render_to_response('Categorias/Gastronomia/Detalle_Gastronomia.html', {'item': Detalle_Gastronomia[0]})


def teatro_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    cursor.execute("Select * from Lugares where IdCategoria=5")
    Teatros = cursor.fetchall()
    db.commit()
    return render_to_response('Categorias/Teatros/Teatros.html', {'Teatros': Teatros})

def toques_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    cursor.execute("Select * from Eventos where IdCategoria=6")
    Toques = cursor.fetchall()
    db.commit()
    return render_to_response('Categorias/Toques/Toques.html', {'Toques': Toques})

def boli_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    cursor.execute("Select * from Lugares where IdCategoria in (8,9)")
    Boliches = cursor.fetchall()
    db.commit()
    return render_to_response('Categorias/Boliches/Boliches.html', {'Boliches': Boliches})

def artdep_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    cursor.execute("Select * from Eventos where IdCategoria=10")
    Artdep = cursor.fetchall()
    db.commit()
    return render_to_response('Categorias/Artdep/Artdep.html', {'Artdep': Artdep})


def enfamilia_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    cursor.execute("Select * from Lugares")
    Lugares = cursor.execute("select Lugares.Nombre ,Lugares.Ciudad ,Lugares.Telefono, Lugares.Direccion, Lugares.Horario, Lugares.IdLugar from Lugares")
    db.commit()
    return render_to_response('Mievento/Enfamilia/enfamilia.html', {'Lugares': Lugares})


def conamigos_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    cursor.execute("Select * from Categorias")
    Eventos = cursor.execute(
        "select Eventos.Nombre ,Eventos.Ciudad ,Eventos.Detalle, Eventos.FechaInicio, Eventos.Contacto from Eventos")
    db.commit()
    return render_to_response('Mievento/Conamigos/conamigos.html', {'Eventos': Eventos})


def ninos_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    cursor.execute("Select * from Eventos")
    Eventos = cursor.execute("select Eventos.Nombre,Eventos.Ciudad ,Eventos.Detalle, Eventos.Contacto from Eventos")
    db.commit()
    return render_to_response('Mievento/Paraninos/ninos.html', {'Eventos': Eventos})


def paseos_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    cursor.execute("Select * from Lugares")
    Lugares = cursor.execute("select Lugares.Nombre ,Lugares.Direccion, Lugares.Barrio from Lugares")
    db.commit()
    return render_to_response('Mievento/Paseos/paseos.html', {'Lugares': Lugares})


def turismo_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    cursor.execute("Select * from Lugares")
    Lugares = cursor.execute("select Lugares.Nombre ,Lugares.Direccion, Lugares.Barrio from Lugares")
    db.commit()
    return render_to_response('Mievento/LugaresTuri/turismo.html', {'Lugares': Lugares})


def airlib_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    # cursor.execute("Select * from Eventos")
    Evento = cursor.execute("select Eventos.Nombre ,Eventos.Detalle, Eventos.Ciudad from Eventos")
    db.commit()
    return render_to_response('Mievento/LugaresTuri/turismo.html', {'Evento': Evento})


def montevideo_inicio_list(request):
    return render_to_response('Departamentos/Montevideo_inicio.html')


def montevideo_eventos_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    # cursor.execute("Select * from Eventos")
    Montevideo = cursor.execute("select * from eventos where eventos.IdDepartamento=10")
    db.commit()
    return render_to_response('Departamentos/Montevideo_eventos.html', {'Montevideo': Montevideo})


def montevideo_lugares_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    # cursor.execute("Select * from Eventos")
    Montevideo = cursor.execute("select * from lugares where iddepartamento=10")
    db.commit()
    return render_to_response('Departamentos/Montevideo_lugares.html', {'Montevideo': Montevideo})


def rocha_inicio_list(request):
    return render_to_response('Departamentos/Rocha_inicio.html')


def rocha_eventos_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    Rocha = cursor.execute("select * from eventos where eventos.IdDepartamento=14")
    db.commit()
    return render_to_response('Departamentos/Rocha_eventos.html', {'Rocha': Rocha})

def rocha_lugares_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    Rocha = cursor.execute("select * from lugares where iddepartamento=14")
    db.commit()
    return render_to_response('Departamentos/Rocha_lugares.html', {'Rocha': Rocha})

def detalle_eventos_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    id_detalle_evento = request.GET.get('id_evento', 0)
    Detalle_eventos = cursor.execute("select * from eventos where idevento=" + id_detalle_evento)
    db.commit()
    return render_to_response('Departamentos/Detalle_eventos.html', {'item': Detalle_eventos.fetchone()})


def detalle_lugares_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    id_detalle_lugar = request.GET.get('id_lugar', 0)
    Detalle_lugares = cursor.execute("select * from lugares where idlugar=" + id_detalle_lugar)
    db.commit()
    return render_to_response('Departamentos/Detalle_lugares.html', {'item': Detalle_lugares.fetchone()})


def Detalleenfamilia_list(request):
    db = sqlite3.connect(database='salimos.db')
    cursor = db.cursor()
    id_detalle_enfamilia = request.GET.get('id_enfamilia', 0)
    detalle_enfamilia = cursor.execute("select * from Lugares where IdLugar=" + id_detalle_enfamilia)
    db.commit()
    return render_to_response('Mievento/Enfamilia/detalle_enfamilia.html', {'item': detalle_enfamilia.fetchone()})

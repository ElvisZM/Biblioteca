from django.urls import path, include, re_path
from .import views

urlpatterns =[
        
    path('',views.index,name='index'),#en vista.py coge la funcion index y la ejecuta
    
    path('libros/lista',views.listar_libros,name='lista_libros'),
    
    path('libros/<int:id_libro>/',views.dame_libro,name='dame_libro'),
    
    path('libros/lista/<int:anyo_libro>/<int:mes_libro>/',views.dame_libros_fecha,name='dame_libros_fecha'),
    
     path('libros/lista/<str:idioma>/',views.dame_libros_idioma,name='dame_libros_idioma'),
     
     path('biblioteca/<int:id_biblioteca>/libros/<str:texto_libro>',views.dame_libros_biblioteca,name='dame_libros_biblioteca'),
    
    path ('ultimo-cliente-libro/<int:libro>',views.dame_ultimo_cliente_libro,name='ultimo_cliente_libro'),
    
    re_path(r"^filtro[0-9]$", views.libros_no_prestados,name="libros_no_prestados"),
    
    #path('biblioteca/biblioteca',views.datos_biblio,name='datos_biblio'),#el primer elemento de la tupla es el que hay que poner en la url para que cargue
    
    #path('cliente/cliente',views.clientes_registrados,name='clientes_registrados'),#el segundo elemento es el nombre de la funcion en el archivo views.py
    
    path('libros_no_prestados/', views.libros_no_prestados,name="libros_no_prestados"),
]

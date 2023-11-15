from django import forms
from .models import Biblioteca, Autor, Libro, Cliente, DatosCliente, Prestamo

class LibroForm(forms.Form):
    #Definimos un campo de tipo Texto para el nombre
    nombre = forms.CharField(label = "Nombre",
                             required=True,
                             max_length=200,
                             help_text="200 carácteres como máximo"
                             )
    
    #Definimos un campo de Tipo Textarea para la descripción
    descripcion = forms.CharField(label="Descripcion",
                                  required=False,
                                  widget=forms.Textarea()
                                  )
    
    #Definimos un campo Select para seleccionar el Idioma
    idioma = forms.ChoiceField(choices=Libro.IDIOMAS,
                               initial="ES"
                               )
    
    #Definimos un campo Select para seleccionar una biblioteca que es una relacion ManyToOne
    bibliotecasDisponibles = Biblioteca.objects.all()
    biblioteca = forms.ModelChoiceField(
            queryset = bibliotecasDisponibles,
            widget=forms.Select,
            required=True,
            empty_label="Ninguna"
    )
    
    #Definimos un campo Select Múltiple para seleccionar autores en una relación ManyToMany
    autoresDisponibles = Autor.objects.all()
    autores = forms.ModelMultipleChoiceField(
        queryset=autoresDisponibles,
        required=True,
        help_text="Mantén pulsada la tecla control para seleccionar varios elementos"
    )
        
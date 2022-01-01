from django import forms

PREDICTION_CHOICES = (
    ('#1', 'Tendencia de la infección por Covid-19 en un País.'),
    ('#2', 'Predicción de Infertados en un País.'),
    ('#3', 'Indice de Progresión de la pandemia.'),
    ('#4', 'Predicción de mortalidad por COVID en un Departamento.'),
    ('#5', 'Predicción de mortalidad por COVID en un País.'),
    ('#6', 'Análisis del número de muertes por coronavirus en un País.'),
    ('#7', 'Tendencia del número de infectados por día de un País.'),
    ('#8', 'Predicción de casos de un país para un año.'),
    ('#9', 'Tendencia de la vacunación de en un País.'),
    ('#10', 'Ánalisis Comparativo de Vacunaciópn entre 2 paises.'),
    ('#11', 'Porcentaje de hombres infectados por covid-19 en un País desde el primer caso activo'),
    ('#12', 'Ánalisis Comparativo entres 2 o más paises o continentes.'),
    ('#13', 'Muertes promedio por casos confirmados y edad de covid 19 en un País.'),
    ('#14', 'Muertes según regiones de un país - Covid 19.'),
    ('#15', 'Tendencia de casos confirmados de Coronavirus en un departamento de un País.'),
    ('#16', 'Porcentaje de muertes frente al total de casos en un país, región o continente.'),
    ('#17', 'Tasa de comportamiento de casos activos en relación al número de muertes en un continente.'),
    ('#18', 'Comportamiento y clasificación de personas infectadas por COVID-19 por municipio en un País.'),
    ('#19', 'Predicción de muertes en el último día del primer año de infecciones en un país.'),
    ('#20', 'Tasa de crecimiento de casos de COVID-19 en relación con nuevos casos diarios y tasa de muerte por COVID-19'),
    ('#21', 'Predicciones de casos y muertes en todo el mundo - Neural Network MLPRegressor'),
    ('#22', 'Tasa de mortalidad por coronavirus (COVID-19) en un país.'),
    ('#23', 'Factores de muerte por COVID-19 en un país.'),
    ('#24', 'Comparación entre el número de casos detectados y el número de pruebas de un país.'),
    ('#25', 'Predicción de casos confirmados por día'),
)

class PredictionSelectionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PredictionSelectionForm, self).__init__(*args, **kwargs)
        self.fields['prediction'].label = "Selecciona el enunciado a analizar"
    prediction = forms.ChoiceField(choices=PREDICTION_CHOICES)

class Case5ParametersForm(forms.Form):
    def __init__(self, parameter_choices, countries, *args, **kwargs):
        super(Case5ParametersForm, self).__init__(*args, **kwargs)
        self.fields['deaths'].label = "Muertes"
        self.fields['deaths'] = forms.ChoiceField(choices=tuple([(param, param) for param in parameter_choices]))
        self.fields['date'].label = "Fechas"
        self.fields['date'] = forms.ChoiceField(choices=tuple([(param, param) for param in parameter_choices]))
        self.fields['country'].label = "País"
        self.fields['country'] = forms.ChoiceField(choices=tuple([(param, param) for param in countries]))
    deaths = forms.ChoiceField()
    country = forms.ChoiceField()
    date = forms.ChoiceField()

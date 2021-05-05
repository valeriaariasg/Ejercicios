#Calculos metereológicos para la NASA

volumen_resevorio = 4.445e8
lluvia = 5e6

lluvia= lluvia - ((0.1*lluvia)/100.0)
volumen_resevorio = volumen_resevorio + lluvia
volumen_resevorio = volumen_resevorio + ((0.05*volumen_resevorio)/100.0)
volumen_resevorio = volumen_resevorio - ((0.02*volumen_resevorio)/100.0)
volumen_resevorio = volumen_resevorio - 2.5e5

print(f'El volumen del reservorio es {volumen_resevorio}m³')

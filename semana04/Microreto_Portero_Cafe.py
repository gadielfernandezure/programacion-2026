"""Microreto: el portero del café."""

energia = int(input("¿cuanta energia tienes de 0-100?: "))
trae_cafe = input("¿Traes café? (si/no): ").lower().strip()=="si"

mensaje = "Completa las reglas del portero."

# < 30 energia y no traigo cafe (vaya dormir)
# si traigo 30 o mas energia o tengo cafe (dejeme pasar)
# portero confundido , revise las respuestas
# TODO: usa and para detectar energía baja sin café.


if energia < 30 and not(trae_cafe):
    mensaje = "acceso denegado: necesitas dormir."
elif energia >= 30 or trae_cafe:
    mensaje = "acceso permitido: pasa , pero comparte café."
else:
    mensaje = "el guarda está confundido, revisa las respuestas"
print("mensaje")


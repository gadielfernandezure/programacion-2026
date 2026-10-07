

Nombre = input("Nombre: ").strip().upper()
Kit = input ("tipo de kit: ").strip().lower()
autorizacion = input("¿tiene autorizacion (si/no)?: ").lower().strip()=="si"

try:
    cantidad = int(input("ingrese la cantidad: "))
except ValueError:
    print("Error cantidad invalida, asignada -1")
    cantidad = -1
    
dias = input("dias de prestamo: ")
try:
    dias = int(input("ingrese la cantidad de dias: "))
except ValueError:
    print("error cantidad dias invalida -1")
    dias = -1
resultado = ""
if not nombre or kit == "" or cantidad < 1 or dias < 1:
    resultado = "registro rechazado: datos inválidos"
elif autorizacion and cantidad <= 3 and not dias > 7:
    resultado = f"solicitud aprobada para {nombre}: {cantidad}kit(s) de {kit}."
elif cantidad > 3 or dias > 7:
    resultado = "solicitud enviada a revisión"
else:
        resultado = "solicitud rechazada: se requiere autorización"
    
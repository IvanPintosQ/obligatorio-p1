from entities.Sistema import Sistema
from exceptions.ErrorLaboratorio import ErrorLaboratorio


def codigos_de(sistema, codigo_caso):
    lista = []
    for ev in sistema.evaluaciones:
        if ev.caso.codigo == codigo_caso:
            lista.append(ev.codigo)
    return lista


def intentar(descripcion, accion):
    try:
        accion()
        print("ERROR: esto no debería haber andado:", descripcion)
    except ErrorLaboratorio as e:
        print("Atajado bien (" + descripcion + "):", e)


s = Sistema()
s.registrar_criterio("Precisión", 2)
s.registrar_criterio("Velocidad", 3)
s.registrar_servicio_api("Claude API", {1: 8, 2: 6}, 40, 5000)    # costo 200, puntaje 6.80
s.registrar_plan_mensual("Plan Equipo", {1: 7, 2: 9}, 10, 20)      # costo 200, puntaje 8.20
s.registrar_plan_mensual("Plan Barato", {1: 3, 2: 3}, 2, 5)        # costo 10,  puntaje 3.00
s.registrar_caso("Atención al cliente", 300, 7)

print("--- Evaluación individual ---")
print(s.registrar_evaluacion(1, 1))
intentar("duplicado", lambda: s.registrar_evaluacion(1, 1))
intentar("opción inexistente", lambda: s.registrar_evaluacion(99, 1))
intentar("caso inexistente", lambda: s.registrar_evaluacion(1, 99))

print("--- Comparar caso 1 ---")
for ev in s.comparar_caso(1):
    print(ev)
print("Códigos del caso 1:", codigos_de(s, 1))
print("Total de evaluaciones:", len(s.evaluaciones))

print("--- Otro caso, sin tocar el primero ---")
s.registrar_caso("Ventas", 100, 5)
s.comparar_caso(2)
print("Códigos del caso 2:", codigos_de(s, 2))
print("Códigos del caso 1:", codigos_de(s, 1))
print("Total de evaluaciones:", len(s.evaluaciones))

print("--- Comparar de nuevo el caso 1 ---")
s.comparar_caso(1)
print("Códigos del caso 1:", codigos_de(s, 1))
print("Códigos del caso 2:", codigos_de(s, 2))
print("Total de evaluaciones:", len(s.evaluaciones))

print("--- Sin opciones ---")
vacio = Sistema()
vacio.registrar_criterio("Precisión", 1)
vacio.registrar_caso("Caso", 100, 5)
intentar("sin opciones", lambda: vacio.comparar_caso(1))
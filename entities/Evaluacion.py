from datetime import datetime
from exceptions.ErrorLaboratorio import ErrorLaboratorio

class Evaluacion():
    def __init__(self, codigo, opcion, caso, criterios):
        self.__codigo = codigo
        self.__opcion = opcion
        self.__caso = caso
        self.__criterios = criterios 
        self.__fecha = datetime.now()
        self.__estado = ""
        self.actualizar_estado()

    @property
    def codigo(self):
        return self.__codigo

    @property
    def opcion(self):
        return self.__opcion

    @property
    def caso(self):
        return self.__caso

    @property
    def fecha(self):
        return self.__fecha

    @property
    def estado(self):
        return self.__estado

    def costo_total(self):
        return self.__opcion.costo_estimado()

    def puntaje_total(self):
        suma_ponderada = 0
        suma_pesos = 0
        for criterio in self.__criterios:
            puntaje = self.__opcion.puntajes[criterio.codigo]
            suma_ponderada = suma_ponderada + puntaje * criterio.peso
            suma_pesos = suma_pesos + criterio.peso
        return suma_ponderada / suma_pesos

    def actualizar_estado(self):
        costo = self.costo_total()
        puntaje = self.puntaje_total()
        presupuesto = self.__caso.presupuesto
        minimo = self.__caso.puntaje_minimo

        if costo > presupuesto:
            self.__estado = "Fuera de presupuesto"
        elif puntaje < minimo:
            self.__estado = "Puntaje insuficiente"
        else:
            self.__estado = "Recomendada"

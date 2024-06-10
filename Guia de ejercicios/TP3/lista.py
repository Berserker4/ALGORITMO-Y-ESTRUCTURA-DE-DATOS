def criterio(dato, campo=None):
    dic = {}
    if(hasattr(dato, '__dict__')):
        dic = dato.__dict__
    if(campo is None or campo not in dic):
        return dato
    else:
        return dic[campo]



class nodoLista():
    info, sig, sublista = None, None, None


class Lista():
    
    def __init__(self):
        self.__inicio = None
        self.__tamanio = 0


    def insertar(self, dato, campo=None):
        nodo = nodoLista()
        nodo.info = dato
        nodo.sublista = Lista()

        if(self.__inicio is None or criterio(nodo.info, campo) < criterio(self.__inicio.info, campo)):
            nodo.sig = self.__inicio
            self.__inicio = nodo
        else:
            anterior = self.__inicio
            actual = self.__inicio.sig
            while(actual is not None and criterio(nodo.info, campo) > criterio(actual.info, campo)):
                anterior = anterior.sig
                actual = actual.sig

            nodo.sig = actual
            anterior.sig = nodo

        self.__tamanio += 1

    def lista_vacia(self):
        return self.__inicio is None

    def tamanio(self):
        return self.__tamanio

    def barrido(self):
        aux = self.__inicio
        while(aux is not None):
            print(aux.info)
            aux = aux.sig

    def barrido_inverso(self):
        p = Pila()
        aux = self.__inicio
        while(aux is not None):
            p.apilar(aux.info)
            aux = aux.sig
        while(not p.pila_vacia()):
            print(p.desapilar())

    def barrido_porc_victorias(self):
        aux = self.__inicio
        while(aux is not None):
            total = aux.info.batallas_ganadas + aux.info.batallas_perdidas
            if(aux.info.batallas_ganadas/total >= 0.79):
                print(aux.info)
            aux = aux.sig

    def barrido_entrenador_mas_tres(self):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.torneos_ganados > 3):
                print(aux.info)
            aux = aux.sig
    
    def barrido_tipo_subtipo(self):
        auxlista = self.__inicio
        while(auxlista is not None):
            auxsublista = auxlista.sublista.__inicio
            while(auxsublista is not None):
                if(auxsublista.info.tipo == 'fuego' and auxsublista.info.subtipo == 'planta') or (auxsublista.info.tipo == 'agua' and auxsublista.info.subtipo == 'volador'):
                    print(auxlista.info)
                    break
                auxsublista = auxsublista.sig
            auxlista = auxlista.sig
    
    def barrido_promedio(self):
        aux = self.__inicio
        suma = 0
        while(aux is not None):
            suma = suma+aux.info.nivel
            aux = aux.sig
        return suma/self.__tamanio

    def barrido_cuantos_tienen_pokemon(self,pokemon):
        auxlista = self.__inicio
        cont = 0
        while(auxlista is not None):
            auxsublista = auxlista.sublista.__inicio
            while(auxsublista is not None):
                if(auxsublista.info.nombre == pokemon):
                    cont += 1
                    break
                auxsublista = auxsublista.sig
            auxlista = auxlista.sig
        return cont

    def barrido_tiene_pokemon(self,pokemons):
        auxlista = self.__inicio
        while(auxlista is not None):
            auxsublista = auxlista.sublista.__inicio
            while(auxsublista is not None):
                if(auxsublista.info.nombre in pokemons):
                    print(auxlista.info)
                    break
                auxsublista = auxsublista.sig
            auxlista = auxlista.sig

    def barrido_repetidos(self):
        auxlista = self.__inicio
        cont = 0
        while(auxlista is not None):
            pokemons = []
            auxsublista = auxlista.sublista.__inicio
            while(auxsublista is not None):
                if(auxsublista.info.nombre in pokemons):
                    cont += 1
                    break
                pokemons.append(auxsublista.info.nombre)
                auxsublista = auxsublista.sig
            auxlista = auxlista.sig
        return cont

    def barrido_lista_lista(self):
        aux = self.__inicio
        while(aux is not None):
            print(aux.info)
            print('sublista:')
            aux.sublista.barrido()
            # aux1 = aux.sublista.__inicio
            # while(aux1 is not None):
            #     print('  ', aux1.info)
            #     aux1 = aux1.sig

            aux = aux.sig

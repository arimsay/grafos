#https://www.repl.it/Eeay
#Arimsay Diaz
# Grafo - nodos enlazados -
# Autor: Javier Rivera
class Nodo:
    def __init__ (self, valor):
        self.info = valor
        self.arcos = []
        
    def enlace (self, ndestino, peso = 1, bdir = False):
        if (type(ndestino) == type(self)):
            arco = Arco(ndestino, peso)
            self.arcos.append(arco)
            if (bdir == True):
                arco = Arco(self, peso)
                ndestino.arcos.append(arco)
            return True
        return False
        
    def muestra_enlaces (self):
        for arco in self.arcos: 
            print arco.nodo.info,
            print arco.peso
            
    def existe_enlace(self, ndestino):
        for arco in self.arcos:
            if (arco.nodo == ndestino):
                return arco
        return False
        
    def eli_enlace (self, ndestino):
        arco = self.existe_enlace(ndestino)
        if (arco != False):
            self.arcos.remove(arco)
            return True
        return False
            
    def __del__(self):
        del self.arcos

        
class Arco:
    def __init__ (self, ndestino, peso=0):
        self.nodo = ndestino
        self.peso = peso

class Grafo:
    def __init__(self, dirigido = True):
        self.__nodos = []
        self.__dirigido = dirigido
        
    def buscaNodo (self, valor):
        for nodo in self.__nodos:
            if (nodo.info == valor):
                return nodo
        return False
    
    def enlace(self, valOrigen, valDestino, peso = 1, bdir = False):
        
        norigen = self.buscaNodo(valOrigen)
        if (not(norigen)):
            return False
            
        ndestino = self.buscaNodo(valDestino)
        if (not(ndestino)):
            return False
        
        if (self.__dirigido == False):
            bdir = True
            
        norigen.enlace(ndestino, peso, bdir)
        return True
        
    def ins_nodo (self, valor):
        if (self.buscaNodo(valor) == False):
            nodo = Nodo(valor)
            self.__nodos.append(nodo)
            return nodo
        return False
        
    def eli_nodo(self, valor):
        nodoE = self.buscaNodo(valor)
        if (nodoE == False):
            return False
            
        for nodo in self.__nodos:
            nodo.eli_enlace(nodoE)
        
        self.__nodos.remove(nodoE)
        return True
    
    def existen_islas(self):
        for nodo in self.__nodos:
            if (len(nodo.arcos) == 0):
                esIsla = True
                for norigen in self.__nodos:
                    if (norigen.existe_enlace(nodo) != False):
                        esIsla = False
                        break
                        
                if (esIsla == True):
                    return True
        return False
    
    def elimina_bucles(self):
        for nodo in self.__nodos:
            if nodo.existe_enlace(nodo):
                nodo.eli_enlace(nodo)
                
    def existe_camino (self, valOrigen, valDestino, camino = []):
        nOrigen = self.buscaNodo(valOrigen)
        nDestino = self.buscaNodo(valDestino)
        if (nOrigen == False or nDestino == False):
            return False
        
        camino.append(valOrigen)
        if (nOrigen.existe_enlace(nDestino) != False):
            camino.append(valDestino)
            return True

        for arco in nOrigen.arcos:
            if (arco.nodo.info in camino):
                continue
            if (self.existe_camino (arco.nodo.info, valDestino, camino)):
                return True

            camino.pop()

        return False


    def mayor_peso(self,valOrigen, valDestino, visitados =[], elem = '', peso = 0):
        nOrigen = self.buscaNodo(valOrigen)
        nDestino = self.buscaNodo(valDestino)
        if (nOrigen == False or nDestino == False):
            return False

        visitados.append(valOrigen)
	for arco in nOrigen.arcos:
		if arco.peso > peso:
			peso = arco.peso
			elem = arco.nodo.info
		if arco.nodo.info == valDestino:
			print (valOrigen,elem),peso
		if(self.existe_camino(arco.nodo.info, valDestino) and arco.nodo.info not in visitados):
			self.mayor_peso(arco.nodo.info,valDestino,visitados,elem,peso)

    def camino(self,origen,destino,valor = []):
        nOrigen = self.buscaNodo(origen)
	nDestino = self.buscaNodo(destino)
	if (nOrigen.existe_enlace(nDestino) != False):
	    valor.append(True)
	    return True

	
	for arco in nOrigen.arcos:
		self.camino(arco.nodo.info,destino)
	if True not in valor:
		return False
	else:
		return True
        
        
    def __str__(self):
        grafo  = ""
        for nodo in self.__nodos:
            grafo = grafo + nodo.info
            arcos = ""
            for arco in nodo.arcos:
                if (arcos != ""):
                    arcos = arcos + ", "
                arcos = arcos + arco.nodo.info + ":" + str(arco.peso)
            grafo = grafo + "(" + arcos + ") "
        return grafo    

		
# PRINCIPAL

g = Grafo()
nodo_a = g.ins_nodo("A")
nodo_b = g.ins_nodo("B")
nodo_c = g.ins_nodo("C")
nodo_d = g.ins_nodo("D")
nodo_e = g.ins_nodo("E")
nodo_f = g.ins_nodo("F")

print g

nodo_a.enlace(nodo_b,5)
nodo_a.enlace(nodo_e,3)
nodo_b.enlace(nodo_c,6)
nodo_c.enlace(nodo_d,7)
nodo_e.enlace(nodo_b,1)
nodo_e.enlace(nodo_f,4)
nodo_f.enlace(nodo_b,1)


print "Nodos"
print g

#g.mayor_peso("A","D")

print g.a_asterisco("A","D")


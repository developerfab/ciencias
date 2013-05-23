
class Djikstra:
    
    def dijkstra(self,G, a, z):
        """
        Algoritmo de Dijkstra
        Determina el camino mas corto entre los vertices 'a' y 'z' de un
        grafo ponderado y conexo 'G'.
        """
        assert a in G
        assert z in G
    
        # Definicion de infinito como un valor mayor 
        # al doble de suma de todos los pesos
        Inf = 0
        for u in G:
            for v, w in G[u]:
                Inf += w
    
        # Inicializacion de estructuras auxiliares:
        #  L: diccionario vertice -> etiqueta
        #  S: conjunto de vertices con etiquetas temporales
        #  A: vertice -> vertice previo (en camino longitud minima)
        L = dict([(u, Inf) for u in G]) #py3: L = {u:Inf for u in G}
        L[a] = 0
        S = set([u for u in G]) #py3: S = {u for u in G}
        A = { }
    
        # Funcion auxiliar, dado un vertice retorna su etiqueta
        # se utiliza para encontrar el vertice the etiqueta minima
        def W(v):
            return L[v]
        # Iteracion principal del algoritmo de Dijkstra
        while z in S:
            u = min(S, key=W)
            S.discard(u)
            for v, w in G[u]:
                if v in S:
                    if L[u] + w < L[v]:
                        L[v] = L[u] + w
                        A[v] = u
    
        # Reconstruccion del camino de longitud minima
        P = []
        u = z
        while u != a:
            P.append(u)
            u = A[u]
        P.append('a')
        P.reverse()
    
        # retorna longitud minima y camino de longitud minima
        return L[z], P
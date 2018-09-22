__author__ =  ' APOLINAR MARIN CAMPOS '

from  Memoria_Dinamica import  *


otralista = []
TiendaDeDeportes = [ ' Balon de Futbol ' , ' Balon de Voleibol ' , ' Valon de Basquetboll ' , ' Balon de tenis ' , ' balon de futbol Americano ' ]
estructuradedatos = [ ' Mario zierra ' , ' Irvin Jesus ' , ' Morro Marin' ]
precios = [ 150 , 110 , 90 , 160 ]
porcentajes = [ .10 , .5 , .2 , .4 ]

listas = memDinamica (TiendaDeDeportes)
listas.imprimirLista ()
listas.ordenarLista ()
listas.imprimirLista ()
listas.agregarelementoarray ( ' Balon de voleibol ' )
listas.imprimirLista ()

lista2 = memDinamica (precios)
lista2.imprimirLista ()
lista2.agregarelementoarray ( 110 )
lista2.imprimirLista ()

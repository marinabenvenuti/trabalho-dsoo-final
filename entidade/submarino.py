#favor nao usar esse submarino para tentar ir ver o titanic pois 
#ele nao é tao bem construido(tal qual o dos milionarios)
from entidade.barco_super import BarcoSuper

class Submarino(BarcoSuper):
    def __init__(self):
        super().__init__("Submarino", 2)
##
# @class Calc
# Representa una operacion matemática sin resultado
# @deprecated Utilise la clase SuperCalc en reemplaso

class Calc():

    ##s
    # @brief Constructor de Calc
    # @detailss Python es maravilloso
    # @param calc_method Symbolo del método de calc
    # @param n1 primer miembro entero
    # @param n2 segundo miembro entero
    # @warning Attention, cuidado con tirar café al teclado
    #
    def __init__(self, calc_method, n1,n2) -> None:
        self.calc_method = calc_method
        self.n1= n1
        self.n2= n2

    ##
    # @brief Describe la información de la clase Calc en forma de cadena
    # @return  Retorna una cadena compuesta por los métodos de Calc
    # @todo Falra correjir
    # @bug Formato incompleto
    #
    def __str__(self):
        return f"{self.n1} {self.calc_method}{self.n2} = ?"
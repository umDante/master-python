"""
Clase de servicio UsuarioServicio
====================================

Esta clase pertenece a la capa de servicio en el modelo de capas, conecta las
instancias de objetos tipo UsuarioServicio con la capa de persistencia de datos
para resolver las distintas consultas 

"""
class UsuarioServicio():


    """ Clase UsuarioServicio resuelve las reglas del negocio, consultando y 
        actualizando a la base de datos sobre la información de usuario

                >>> from userService import UsuarioServicio
                >>> import json
                >>> user = UsuarioServicio(1,"willyUser","WillyPass",23,False)
                >>> print(user.__repr__())
                UsuarioServicio(id = 1, nombre = willyUser, clave =  WillyPass, edad = 23, sasado = False
                >>> print(user.__str__())
                UsuarioServicio(id = 1 nombre = willyUser clave =  WillyPass edad = 23 sasado = False
                >>> user = json.dumps(user.__dict__)
                >>> print(user)
                {"id": 1, "nombre": "willyUser", "clave": "WillyPass", "edad": 23, "casado": false} 
    """


    def __init__(self, id, nombre, clave, edad, casado):

        """
        Método constructor que inicializa los atributos de objetos tipo UsuarioServicio

        :param UsuarioServicio self: 
                        Varaiable usada para instanciar los atrutos de la clase UsuarioServicio
        :param int id: 
                        Varaiable usada para identificar al usuario
        :param str nombre:
                        Varaiable usada para almacenar el nombre de usuario
        :param str clave:
                        Varaiable usada para almacenar la clave de autenticación de usuario en el sistema
        :param int edad:
                        Varaiable usada para almacenar la edad de usuario 
        :param boolean casado:
                        Varaiable usada para almacenar el lestado civil del usuario (soltero/casado) 
            
        """
        self.id=id
        self.nombre=nombre
        self.clave=clave
        self.edad=edad
        self.casado=casado
    

    def postCreateUser(self,usForm): #Crear Update  
        """

                        >>> print(postCreateUser())
                        {
                            "id": 1, 
                            "nombre": "willyUser", 
                            "clave": "WillyPass", 
                            "edad": 23, 
                            "casado": false
                        } 

        Este método recibe y almacena los datos de usuario que son enviados desde una GUI, para esto se instancia un 
        objeto para asignarles todo estos valores y se finaliza guardando este objeto creado en la base de datos
        
        :param UsuarioServicio self: 
                        Varaiable usada para instanciar los atrutos de la clase UsuarioServicio
        :param diccionario usForm: 
                        Varaiable que contiene los datos de usaurios en forma de diccionario de datos 
        :return UsuarioServicio user: 
                        Objeto que contiene los datos del usaurio que ha sido almacenado en la base de datos 
        """
        self.id=usForm["id"]
        self.nombre = usForm["nombre"]
        self.clave=usForm["clave"]
        self.edad = usForm["edad"]
        self.casado=usForm["casado"]   
        user = UsuarioServicio(self.id, self.nombre,self.clave,self.edad, self.casado)
        
        """
        El método saveUserDataBase, se encarga de almacenar el usuario creado en la base de datos,
        luego retornará un objeto tipo usuario para controlar los datos que se almacenaron 
        """        
        user = saveUserDataBase(user)

        return user    

    def getUsuarioById(self,id):

        """                             
                        >>> print(getUsuarioById(1))
                        {
                            "id": 1, 
                            "nombre": "willyUser", 
                            "clave": "WillyPass", 
                            "edad": 23, 
                            "casado": false
                        } 

        Este método recibe un identificador de usuario, con el cual busca en la base de datos que objeto que 
        tenga ese atributo para luego asignarselo al objeto que invocó este método, en el caso que no estuviera, 
        retorna un mensaje de advertencia como cadena de texto.
        
        :param UsuarioServicio self: 
                        Varaiable usada para instanciar los atrutos de la clase UsuarioServicio
        :param int int: 
                        Varaiable que contiene un número entero como clave primaria con el identica un usuario
        :return UsuarioServicio user: 
                        Objeto que contiene los datos del usaurio que ha sido localzado en la Base de Datos 
        :return str mensaje: 
                        Objeto que contiene un mensaje de advertencia por no encontrar el id sooicitado  
                
        getuserByDataBase es el método que se encarga de comunicarse con la capa que busca el objeto por id,
        en la base de datos, retorna un objeto tipo UsuarioServicio.
    
        """

        if type(id)==int and id!="":
            return getuserOfDataBase(id)
        else:
            return "Mensaje: Usuario no existe"

    def getListUsers(self):

        """
                    >>> print(getListUsers())
                        [    
                            {
                                "id": 1, 
                                "nombre": "willyUser1", 
                                "clave": "WillyPass1", 
                                "edad": 23, 
                                "casado": false
                            },
                                                        {
                                "id": 2, 
                                "nombre": "willyUser2", 
                                "clave": "WillyPass2", 
                                "edad": 19, 
                                "casado": true
                            },
                                                        {
                                "id": 3, 
                                "nombre": "willyUser3", 
                                "clave": "WillyPass3", 
                                "edad": 34, 
                                "casado": false
                            }
                        ] 

        Este método se encarga de entregar al objeto que la invoca, todos los usuarios almacenados en la base de datos 
               
        :param UsuarioServicio self: 
                        Varaiable usada para instanciar los atrutos de la clase UsuarioServicio
        :return lista usuario: 
                        Objeto que contiene un mensaje de advertencia por no encontrar el id sooicitado  
        """

        """
        listUsers es el método que se comunica que con la capa que hace las consultas a la base de datos para extraer los 
        toda la lista de usuarios
        """
        return self.listUsers()


    def __str__(self) -> str:

        """
        Método que permite entregar información hacerca de la estructura de la clase a los desarrolladores a fin de poder 
        manipularla 
        """
        return f"UsuarioServicio(\
                        id = {str(self.id)} \
                        nombre = {str(self.nombre)}\
                        clave =  {str(self.clave)} \
                        edad = {self.edad} \
                        casado = {self.casado}"
        
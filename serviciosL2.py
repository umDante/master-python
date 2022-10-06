
class UsuarioServicio():
    def __init__(self, id, nombre, clave, edad, casado):
        self.id=id
        self.nombre=nombre
        self.clave=clave
        self.edad=edad
        self.casado=casado
    

    def postCreateUser(self,usForm): #Crear Update  
        if len(usForm) == 0:
            self.id=usForm["id"]
            self.nombre = usForm["nombre"]
            self.clave=usForm["clave"]
            self.edad = usForm["edad"]
            self.casado=usForm["casado"]   

            # user = UsuarioServicio(usForm["id"], usForm["nombre"],usForm["clave"],usForm["edad"], usForm["casado"])
            # user = UsuarioServicio(self.id, self.nombre,self.clave,self.edad, self.casado)
            # return user    
        return self    

    def getUsuarioById(self,id):#Read
            if type(id)==int and id!="":
                return self.modeloUser()
            else:
                return "Mensaje: Usuario no existe"

    def postListUsers(self):
        return self.listUsers()

    def modeloUser(self):
        return UsuarioServicio(1,"nombreUser","claveUser","edadUSer",True)

    def listUsers(self):
        return [{1,"nombreUser1","claveUser1","edadUSer1",False},
                {2,"nombreUser2","claveUser2","edadUSer2",True},
                {3,"nombreUser3","claveUser3","edadUSer3",False}]

    
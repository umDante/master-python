import unittest
from servicios import UsuarioServicio
'''

Autor: Dante Espinoza

Actividad relacionada con la lección 2:
Implementa un Script con un conjunto de funciones y crea un mínimo de 5
test para cada una de las librerías de test vistasen la clase (unittest y pytest)

'''

class TestUsuarioServicio(unittest.TestCase):


    def setUp(self): # se EXE Antes que cualquier método dentro
        print("Entrando a método testeado")

    def tearDown(self):# se EXE Despues  que cualquier método dentro
        print("Saliendo de método testeado")

        
    def test_constructorUsuarioServicio_instancia(self):    
        user=UsuarioServicio(1,"nombreTest","claveTest",23,True) 
        # self.assertIsInstance(user,UsuarioServicio)
        self.assertEqual(type(user),type(user.modeloUser()))


    def test_constructorUsuarioServicio_Id(self):
        user=UsuarioServicio(1,"nombreTest","claveTest",23,True)
        self.assertAlmostEqual(1,user.id)
        
    def test_constructorUsuarioServicio_Casado(self):
        user=UsuarioServicio(1,"nombreTest","claveTest",23,True)
        self.assertTrue(user.casado)

    def test_constructorUsuarioServicio_clave(self):    
        user=UsuarioServicio(1,"nombreTest","claveTest",23,True)
        self.assertTrue(len(user.clave)>8)
    
    def test_listUsersUsuarioServicio_array(self):
        user=UsuarioServicio(1,"nombreTest","claveTest",23,True)
        self.assertTrue(type(user),type(user.listUsers()))
    
    def test_getUsuarioByIdUsuarioServicio_id(self):
        user=UsuarioServicio(1,"nombreTest","claveTest",23,True)
        self.assertEqual(type(user),type(user.getUsuarioById(1)))

   
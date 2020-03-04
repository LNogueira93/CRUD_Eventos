import requests
import unittest

class EventosUnitTests(unittest.TestCase):

    # Verificando se há apenas 3 alunos.
    def test_01_eventos_retorna_lista_inical(self):
        r1 = requests.delete('http://localhost:5002/resetar')
        self.assertEqual(r1.status_code,202)
        r2 = requests.post('http://localhost:5002/',json={'nome':'Thomas Alexandre','id':1})
        self.assertEqual(r2.status_code,200)
        r3 = requests.post('http://localhost:5002/',json={'nome':'Lucio Mendes','id':2})
        self.assertEqual(r3.status_code,200)
        r4 = requests.post('http://localhost:5002/',json={'nome':'Vinicius Williams','id':3})
        self.assertEqual(r4.status_code,200)
        r = requests.get('http://localhost:5002/')
        self.assertEqual(type(r.json()),type([]))
        self.assertEqual(len(r.json()),3)
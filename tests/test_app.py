import unittest
from unittest.mock import patch
from src.app import soma, eh_par, fatorial, cadastrar, cadastro, envia_email, welcome, envia_sms


class TestApp(unittest.TestCase):

    def test_soma_numeros_positivos(self):
        resultado = soma(2,5)
        self.assertEqual(resultado, 7)
    
    def test_soma_numeros_negativos(self):
        self.assertEqual(soma(-3,-9), -12)



    def test_eh_par_positivo(self):
        self.assertTrue(eh_par(8))
    
    def test_eh_par_negativo(self):
        self.assertTrue(eh_par(-36))
    
    def test_eh_par_falso(self):
        self.assertFalse(eh_par(25))



    def test_fatorial(self):
        self.assertEqual(fatorial(5), 120)



    def test_cadastro(self):
        self.assertEqual(cadastrar("Joe", "j@gmail.com"), "sucesso")

    def test_cadastro_email_existente(self):
        cadastrar("Joe", "j@gmail.com")
        self.assertEqual(cadastrar("Joe", "j@gmail.com"), "email já cadastrado")



    @patch("src.app.save", return_value = True)
    def test_cadastrar_usuario_valido(self, mock_salvar):
        nome = "Carlos"
        cpf = "213471283"
        resultado = cadastro(nome, cpf)
        self.assertTrue(resultado)
        mock_salvar.assert_called_once_with({"nome":nome, "cpf":cpf})



    @patch("src.app.servico_email", return_value = True)
    def test_enviar_email(self, mock_enviar):
        remetente = "carlos@mail.com"
        destinatario = "megan@mail.com"
        resultado = envia_email(remetente, destinatario)
        self.assertTrue(resultado)
        mock_enviar.assert_called_with({"remetente":remetente, "destinatario":destinatario})



    @patch("src.app.send_mail", return_value = True)
    def test_send_email(self, mock_send_mail):
        
        resultado = welcome('carlos@email.com')
        self.assertEqual(resultado, 'email de boas vindas enviado')
        mock_send_mail.assert_called_once_with('carlos@email.com')



    @patch("src.app.servico_sms", return_value = True)
    def test_enviar_sms(self, mock_enviar_sms):
        telefone = '945681212'
        resultado = envia_sms(telefone)
        self.assertTrue(resultado)
        mock_enviar_sms.assert_called_with({"telefone":telefone})



if __name__ == '__main__':
    unittest.main()

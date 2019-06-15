from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User


class BaseApiTest(APITestCase):

    def setUp(self):
        # cria usuário para teste
        admin_password = 'corr3ct_p4ssw0rd'
        self.user = User.objects.create_user(
            username='admin_test', email='admin_test@test.com', password=admin_password)
        # Inicializa Client
        self.client = APIClient()

        # Força autenticação
        self.client.force_authenticate(user=self.user)

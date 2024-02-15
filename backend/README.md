# VeloxNet - Backend

Api da VeloxNet baseada em Django Rest Framework.

## Como Rodar a Aplicação

Siga estas instruções para configurar e executar a aplicação localmente.

### Pré-requisitos

- Python 3.9+ instalado
- Ambiente virtual Python (opcional, mas recomendado)

### Instalação do Python

Siga um dos guias abaixo de acordo ao seu sistema operacional:
- [**Linux**](https://docs.python.org/3/using/unix.html)
- [**Windows**](https://docs.python.org/3/using/windows.html)
- [**MacOS**](https://docs.python.org/3/using/mac.html)

### Configuração do Ambiente Virtual Python (Opcional)

```bash
# Instalação do virtualenv (caso ainda não tenha)
pip install virtualenv

# Criação de um ambiente virtual
virtualenv venv

# Ativação do ambiente virtual
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate
```

### Instalação das Dependências

```bash
cd backend
pip install -r requirements.txt
```

### Executando a Aplicação

```bash
python manage.py migrate  # Aplica as migrações do banco de dados
python manage.py runserver  # Inicia o servidor de desenvolvimento
```

Agora você pode acessar os endpoints em [http://localhost:8000/](http://localhost:8000/).

## Referências

- Python: [Documentação oficial do Python](https://docs.python.org/3/)
- Django: [Documentação oficial do Django](https://docs.djangoproject.com/)
- Django Rest Framework (DRF): [Documentação oficial do Django Rest Framework](https://www.django-rest-framework.org/)

## Endpoints da API

No arquivo [api.rest](../api.rest), que pode ser usado no VSCode com o auxílio da extensão [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client), são listados os endpoints e seus respectivos cabeçalhos e corpo da requisição. Nos endpoints privados com controle de acesso que requerem autenticação e/ou privilégios de administrador, é possível notar o cabeçalho `Authorization: Token <SEU-TOKEN-AQUI>`, onde `<SEU-TOKEN-AQUI>` deve ser substituído pelo token recebido na resposta da chamada ao endpoint de login. Mais detalhes sobre os endpoints podem ser conferidos diretamente no arquivo em questão.

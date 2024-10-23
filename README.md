## Clone o repositório

```
git clone https://github.com/Luc5z/ondeficar.com.git
cd nome-do-seu-projeto
```

## Crie um ambiente virtual (recomendado)

```
python -m venv venv
Ative o ambiente virtual:
```

No Windows:

```
.\venv\Scripts\activate
```

No Unix ou MacOS:

```
source venv/bin/activate
```

## Configuração do Projeto Django

Navegue até a pasta do projeto Django:

```
cd nome_da_pasta_do_projeto_django
```

Execute as migrações para criar a estrutura do banco de dados:

```
python manage.py migrate
```

Crie um superusuário para acessar o painel de administração:

```
python manage.py createsuperuser
```

Inicie o servidor de desenvolvimento:

```
python manage.py runserver
```

Você pode acessar o aplicativo em <http://127.0.0.1:8000/> e o painel de administração em <http://127.0.0.1:8000/admin>.

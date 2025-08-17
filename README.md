# Entrega Final – Blog en Django

## Requisitos del sistema
- Python 3.11+ (probado con 3.13)
- pip y virtualenv

## Instalación
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

## Funcionalidades
- Home (/home/) y About (/about/)
- CRUD de Pages con: título, subtítulo, contenido (ckeditor), imagen, fecha
- Listado con búsqueda y mensaje "No hay páginas aún"
- Autenticación: signup (username, email, password), login, logout
- Perfil: ver, editar (avatar, bio, fecha de nacimiento), cambiar contraseña
- Mensajería interna: inbox y enviar
- Herencia de templates y navbar con enlaces

## Rutas principales
/                 -> listado de páginas  
/pages/           -> alias del listado  
/about/           -> about  
/home/            -> home  
/accounts/signup/ -> registro  
/accounts/login/  -> login  
/accounts/profile/ -> perfil  
/messenger/       -> inbox  
/messenger/nuevo/ -> enviar mensaje

## Video explicativo
https://drive.google.com/drive/folders/1vkvVqwZ-ZxyfJio6QacQW9l37LcHzxI5?usp=sharing
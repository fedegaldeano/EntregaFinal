# TuPrimeraPaginaGaldeano

Sistema web de gestión de licitaciones mineras, desarrollado en **Django 5.2** como entrega final del curso de **Python en Coderhouse**.

---

## 📌 Descripción general

Esta plataforma permite registrar y gestionar empresas licitantes, licitadores y sus ofertas a licitaciones mineras. Además, incorpora funcionalidades de blog (noticias/páginas) y mensajería privada entre usuarios autenticados.

El sistema cubre todas las fases del ciclo de vida de un proyecto minero: **proyecto, construcción, operación y cierre**.

---

## 🧱 Estructura del proyecto

- `EmpresaLicitante`: empresas proveedoras que ofrecen servicios o productos.
- `Licitador`: usuarios o empresas que se postulan a las licitaciones.
- `Licitacion`: convocatorias abiertas publicadas por empresas licitantes.
- `Oferta`: solicitudes enviadas por los licitadores para participar.
- `pages`: app tipo blog para publicar contenido informativo o institucional.
- `messenger`: sistema de mensajería privada entre usuarios registrados.
- `accounts`: gestión de usuarios, login, logout, perfil y registro.

---

## 💡 Funcionalidades implementadas

### 🧾 Gestión de datos
- CRUD completo para empresas licitantes, licitadores, licitaciones y ofertas.
- Herencia de plantillas HTML (`base.html`) y navegación con navbar.
- Buscador de licitaciones disponibles por nombre, descripción o estado.
- Vinculación automática entre ofertas, licitaciones y usuarios.

### 📝 Blog institucional
- Creación, edición, detalle y eliminación de páginas.
- Interfaz amigable para publicaciones informativas.

### 💬 Mensajería entre usuarios
- Envío de mensajes entre usuarios autenticados.
- Listado de conversaciones y mensajes.
- Acceso directo desde el menú de navegación.

### 👤 Usuarios y autenticación
- Registro, login y logout.
- Edición del perfil del usuario.
- Cambio de contraseña.
- Vista condicional del menú según autenticación.

---

## 🚀 ¿Cómo probar el proyecto?

1. **Clonar el repositorio**

```bash
git clone https://github.com/fedegaldeano/TuPrimeraPaginaGaldeano.git
cd TuPrimeraPaginaGaldeano

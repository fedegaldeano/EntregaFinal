<<<<<<< HEAD
# TuPrimeraPaginaGaldeano

Sistema de registro de licitaciones mineras desarrollado en Django como **entrega final del curso de Python en Coderhouse**.

---

## 📌 Descripción general

Este sistema permite registrar empresas licitantes y licitadores interesados en participar de licitaciones mineras, cubriendo todas las fases del ciclo de vida de un proyecto: **proyecto, construcción, operación y cierre**.

Cada licitación puede tener múltiples ofertas asociadas. El sistema está orientado tanto a la gestión administrativa como a la visualización de oportunidades para los licitadores.

---

## 🧱 Estructura del proyecto

- `EmpresaLicitante`: modelo para gestionar empresas proveedoras de bienes o servicios.
- `Licitador`: modelo para registrar empresas que desean postularse a licitaciones.
- `Licitacion`: modelo central donde se definen las convocatorias abiertas.
- `Oferta`: modelo para registrar la postulación de un licitador a una licitación específica.

---

## 💡 Funcionalidades implementadas

### 🧾 Gestión de datos
- Alta, edición y eliminación de empresas licitantes, licitadores, licitaciones y ofertas mediante formularios.
- Listado y búsqueda de licitaciones disponibles.
- Postulación a licitaciones con vinculación automática entre oferta, licitación y licitador.
- Herencia de plantillas HTML.
- CRUD completo para todas las entidades.

### 👤 Funcionalidades de usuarios
- Registro de nuevos usuarios.
- Login y logout.
- Vista de perfil con edición de datos.
- Cambio de contraseña.

---

## 🧪 ¿Cómo probar el proyecto?

1. **Clonar el repositorio:**

```bash
git clone https://github.com/fedegaldeano/TuPrimeraPaginaGaldeano.git
cd TuPrimeraPaginaGaldeano
=======
# EntregaFinal
>>>>>>> 5a073aa6be489d0b5e2ef900f39cc95a4c9519e4

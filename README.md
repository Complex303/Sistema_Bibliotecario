# 📚 Sistema Bibliotecario

Un sistema de gestión de biblioteca desarrollado en Python con interfaz gráfica usando Tkinter y base de datos SQL Server.

## 🖼️ Vista Previa

![Sistema Bibliotecario](biblioprincipal.png)

## 📋 Descripción

Este sistema bibliotecario permite gestionar de manera eficiente los recursos de una biblioteca, incluyendo:

- Gestión de libros (agregar, editar, eliminar, consultar)
- Sistema de préstamos y devoluciones
- Control de usuarios y autenticación
- Generación de reportes
- Interfaz gráfica intuitiva y fácil de usar

## ✨ Características

- 🔐 **Sistema de Login**: Autenticación segura de usuarios
- 📚 **Gestión de Libros**: CRUD completo para el catálogo de libros
- 👥 **Gestión de Usuarios**: Control de usuarios del sistema
- 📋 **Préstamos**: Sistema completo de préstamos y devoluciones
- 🔍 **Consultas**: Búsqueda y consulta de información
- 📊 **Reportes**: Generación de reportes en formato texto
- 🖥️ **Interfaz Amigable**: GUI desarrollada con Tkinter

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**
- **Tkinter** - Interfaz gráfica de usuario
- **pyodbc** - Conexión con base de datos SQL Server
- **SQL Server** - Sistema de gestión de base de datos

## 📁 Estructura del Proyecto

```
Sistema Bibliotecario/
├── Login.py                    # Ventana de autenticación
├── Principal.py                # Ventana principal del sistema
├── Conexion.py                 # Configuración de conexión a BD
├── GestionLibro.py             # Gestión de libros
├── GestionLibroInsertar.py     # Inserción de nuevos libros
├── VentanaConsulta.py          # Ventana de consultas
├── ventanaPedido.py            # Gestión de préstamos
├── ventanaDevolucion.py        # Gestión de devoluciones
├── Licencia.py                 # Información de licencia
├── reporte_prestamo.txt        # Archivo de reportes
├── icono.ico                   # Icono del sistema
├── library.png                 # Imagen del logo
├── *.png                       # Imágenes adicionales
└── README.md                   # Este archivo
```

## 🚀 Instalación y Configuración

### Prerrequisitos

1. **Python 3.x** instalado en el sistema
2. **SQL Server** instalado y configurado
3. Las siguientes librerías de Python:

```bash
pip install pyodbc
pip install tkinter
```

### Configuración de Base de Datos

1. Asegúrate de tener SQL Server instalado y ejecutándose
2. Crea una base de datos llamada `Sistema_Bibliotecario`
3. Configura la cadena de conexión en el archivo `Conexion.py`:

```python
self.cadena_conexion = '''DRIVER={SQL SERVER};
                          Server=TU_SERVIDOR;
                          Database=Sistema_Bibliotecario;
                          Trusted_Connection=yes;'''
```

### Instalación

1. **Clona o descarga** el repositorio:
```bash
git clone [URL_del_repositorio]
cd Sistema_Bibliotecario
```

2. **Configura la base de datos** según las instrucciones anteriores

3. **Ejecuta la aplicación**:
```bash
python Login.py
```

## 💻 Uso del Sistema

### 1. Inicio de Sesión
- Ejecuta `Login.py`
- Ingresa tus credenciales de usuario
- Accede al sistema principal

### 2. Ventana Principal
- **Mantenimiento**: Agregar, editar o eliminar libros
- **Consultas**: Buscar y consultar información
- **Préstamos**: Gestionar préstamos de libros
- **Devoluciones**: Procesar devoluciones

### 3. Funcionalidades Principales

#### Gestión de Libros
- Agregar nuevos libros al catálogo
- Editar información existente
- Eliminar libros del sistema
- Consultar disponibilidad

#### Sistema de Préstamos
- Registrar nuevos préstamos
- Consultar préstamos activos
- Procesar devoluciones
- Generar reportes

## 📊 Reportes

El sistema genera reportes automatizados en el archivo `reporte_prestamo.txt` que incluye:
- Información de préstamos
- Estados de devolución
- Fechas importantes
- Datos de usuarios



## 📝 Notas Importantes

- Asegúrate de que SQL Server esté ejecutándose antes de iniciar la aplicación
- Verifica que la cadena de conexión esté configurada correctamente
- Los archivos de imagen deben estar en el mismo directorio que los scripts
- Se recomienda crear un backup de la base de datos regularmente

## 🔧 Solución de Problemas

### Error de Conexión a Base de Datos
- Verifica que SQL Server esté ejecutándose
- Confirma que el nombre del servidor sea correcto
- Asegúrate de tener permisos de conexión

### Error de Archivos de Imagen
- Verifica que todas las imágenes (.png, .ico) estén en el directorio correcto
- Revisa las rutas de las imágenes en el código

## 📄 Licencia

Este proyecto está bajo la Licencia [TIPO_DE_LICENCIA] - ver el archivo `Licencia.py` para más detalles.

## 👨‍💻 Autor

**Eddy** - Desarrollador Principal



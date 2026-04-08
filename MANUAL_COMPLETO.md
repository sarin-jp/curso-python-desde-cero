# 📖 MANUAL COMPLETO — Curso de Python Desde Cero

> **Este es el documento más importante del curso. Léelo antes de hacer cualquier cosa.**
> Está escrito para alguien que NUNCA ha programado ni instalado nada especial en su computadora.

---

## 📌 Tabla de Contenidos

1. [Antes de empezar — ¿Qué es programar?](#antes-de-empezar)
2. [Paso 1 — Cómo descargar este curso](#paso-1-descargar)
3. [Paso 2 — Instalar Python](#paso-2-python)
4. [Paso 3 — Instalar VS Code](#paso-3-vscode)
5. [Paso 4 — Cómo ejecutar un archivo .py](#paso-4-ejecutar)
6. [Paso 5 — Cómo seguir el curso día a día](#paso-5-rutina)
7. [Estructura del curso explicada](#estructura)
8. [Preguntas frecuentes](#faq)

---

## 🌱 Antes de empezar — ¿Qué es programar? {#antes-de-empezar}

### ¿Qué es programar?

Imagina que tienes un robot que hace exactamente lo que le dices. Si le dices:
- "Suma 2 + 2" → el robot responde "4"
- "Pregúntale al usuario su nombre" → el robot pregunta y espera respuesta
- "Si el número es mayor de 18, di que es mayor de edad" → el robot evalúa y responde

**Programar es exactamente eso**: escribir instrucciones para que la computadora las siga.

### ¿Qué es Python?

Python es un **lenguaje de programación**. Es como un idioma, pero en lugar de comunicarte con personas, te comunicas con la computadora.

Python es especial porque:
- 🟢 Es **muy fácil de leer** (parece inglés normal)
- 🟢 Es **muy popular** (lo usan empresas como Google, Netflix, Instagram)
- 🟢 Sirve para **todo**: web, inteligencia artificial, ciencia de datos, automatización
- 🟢 Es **gratuito** para siempre

### ¿Qué vas a lograr al terminar?

Al completar los 30 días podrás:
- ✅ Crear programas que resuelven problemas reales
- ✅ Automatizar tareas repetitivas de tu computadora
- ✅ Entender código de otros programadores
- ✅ Seguir aprendiendo cosas más avanzadas (web, IA, etc.)
- ✅ Poner "conocimientos de Python" en tu currículum

---

## 📥 Paso 1 — Cómo descargar este curso {#paso-1-descargar}

Tienes dos formas de obtener el curso. Elige la que te resulte más fácil:

### Opción A: Descargar como ZIP (la más fácil, recomendada para principiantes)

1. Ve a la página del repositorio en GitHub
2. Busca el botón verde que dice **"Code"** (está en la parte superior derecha de la lista de archivos)
3. Se abre un menú pequeño. Haz clic en **"Download ZIP"**
4. Se descarga un archivo con extensión `.zip` (por ejemplo `curso-python-desde-cero-main.zip`)
5. Busca ese archivo en tu carpeta de **Descargas**
6. **Extrae el ZIP**:
   - En Windows: Clic derecho sobre el archivo → "Extraer todo" → "Extraer"
   - En Mac: Doble clic sobre el archivo (se extrae automáticamente)
   - En Linux: Clic derecho → "Extraer aquí"
7. Ahora tienes una carpeta llamada `curso-python-desde-cero-main` (o similar)
8. ¡Listo! Esa carpeta contiene todo el curso

### Opción B: Usar Git (para cuando ya sepas un poco más)

Si ya tienes Git instalado, abre la terminal y escribe:

```bash
git clone https://github.com/sarin-jp/curso-python-desde-cero.git
```

Esto descarga automáticamente todos los archivos del curso.

> 💡 **¿No sabes qué es Git?** No te preocupes. Usa la Opción A por ahora. Git es una herramienta que aprenderás después.

---

## 🐍 Paso 2 — Instalar Python {#paso-2-python}

Python es el programa que "entiende" e interpreta tu código. Sin él, los archivos `.py` son solo texto sin vida.

### En Windows

1. Abre tu navegador (Chrome, Firefox, Edge, el que uses)
2. Ve a: **https://www.python.org/downloads/**
3. Verás un botón amarillo grande que dice **"Download Python 3.X.X"** (el número puede variar). Haz clic en él.
4. Se descarga un archivo llamado `python-3.X.X-amd64.exe`
5. Abre (doble clic) ese archivo
6. **🚨 MUY IMPORTANTE 🚨**: Antes de hacer clic en "Install Now", **marca la casilla** que dice:
   ```
   ☑ Add Python 3.X to PATH
   ```
   Esta casilla suele estar abajo del todo en la ventana del instalador. Si no la marcas, Python no funcionará desde la terminal.
7. Haz clic en **"Install Now"**
8. Espera a que instale (puede tardar 1-2 minutos)
9. Cuando diga "Setup was successful", haz clic en **"Close"**

### En Mac

1. Ve a: **https://www.python.org/downloads/**
2. Haz clic en el botón de descarga para Mac
3. Se descarga un archivo `.pkg`
4. Abre ese archivo y sigue el asistente de instalación (siguiente, siguiente, instalar)
5. Ingresa tu contraseña si te la pide
6. ¡Listo!

### En Linux (Ubuntu/Debian)

Abre la terminal y escribe estos comandos (uno por uno, presionando Enter después de cada uno):

```bash
sudo apt update
sudo apt install python3
sudo apt install python3-pip
```

### Cómo verificar que Python se instaló bien

1. Abre la terminal:
   - **Windows**: Presiona `Windows + R`, escribe `cmd`, presiona Enter
   - **Mac**: Presiona `Cmd + Espacio`, escribe `Terminal`, presiona Enter
   - **Linux**: Presiona `Ctrl + Alt + T`

2. Escribe el siguiente comando y presiona Enter:
   ```
   python --version
   ```
   o si eso no funciona:
   ```
   python3 --version
   ```

3. Deberías ver algo como:
   ```
   Python 3.11.4
   ```
   Si ves eso, ¡Python está instalado correctamente! 🎉

> ❌ **¿Ves un error?** En Windows, si marcaste "Add Python to PATH" durante la instalación, cierra y vuelve a abrir la terminal. Si sigue sin funcionar, vuelve a instalar Python y asegúrate de marcar la casilla.

---

## 💻 Paso 3 — Instalar VS Code {#paso-3-vscode}

VS Code (Visual Studio Code) es un **editor de código**. Piensa en él como Microsoft Word, pero en lugar de escribir documentos, escribes programas.

> 💡 **¿Por qué VS Code?** Es gratuito, muy fácil de usar, tiene colores para el código (lo hace más legible) y tiene un botón para ejecutar programas con un solo clic.

### Instalar VS Code

1. Ve a: **https://code.visualstudio.com/**
2. La página detecta tu sistema operativo automáticamente. Haz clic en el botón azul de descarga.
3. Se descarga el instalador
4. Abre el instalador y sigue los pasos (siguiente, aceptar licencia, instalar)
5. Al final, marca la opción **"Abrir con Code"** si aparece
6. Haz clic en "Finalizar"

### Instalar la extensión de Python en VS Code

La extensión de Python hace que VS Code entienda mejor el código Python y te ayude con errores.

1. Abre VS Code
2. En el panel izquierdo hay 5 iconos. Haz clic en el que parece cuatro cuadritos (el último de los cinco) — ese es el de **Extensiones**
3. En el buscador que aparece, escribe: `Python`
4. El primer resultado dice "Python" con autor "Microsoft". Haz clic en **"Install"**
5. Espera unos segundos
6. ¡Listo! Ahora VS Code soporta Python perfectamente

### Alternativa: IDLE (ya viene con Python)

Si no quieres instalar VS Code, Python ya incluye un editor básico llamado **IDLE**:
- En Windows: Menú Inicio → busca "IDLE" → ábrelo
- En Mac: Busca "IDLE" en Spotlight (`Cmd + Espacio`)

IDLE es más básico pero funciona para el curso.

---

## ▶️ Paso 4 — Cómo abrir y ejecutar un archivo .py {#paso-4-ejecutar}

Los archivos del curso tienen extensión `.py`. Aquí tienes tres formas de ejecutarlos:

### Método 1: VS Code (el más fácil) ⭐ Recomendado

1. Abre VS Code
2. Ve a **Archivo → Abrir carpeta** (o `Ctrl + K, Ctrl + O` en Windows/Linux, `Cmd + K, Cmd + O` en Mac)
3. Navega hasta la carpeta del curso que descargaste y selecciónala
4. En el panel izquierdo verás todos los archivos y carpetas del curso
5. Haz clic en `Fase1_Fundamentos` → luego en `dia01_hola_mundo.py`
6. El archivo se abre en el editor
7. Busca el botón **▶️** en la esquina superior derecha (puede decir "Run Python File")
8. Haz clic en ▶️
9. Se abre una terminal en la parte de abajo con el resultado del programa

**¿Cómo se ve la terminal cuando ejecutas el primer programa?**
```
PS C:\Users\TuNombre\curso-python-desde-cero> python dia01_hola_mundo.py
¡Hola, Mundo!
Me llamo Python y soy tu nuevo amigo 🐍
```

### Método 2: Terminal/Símbolo del sistema

1. Abre la terminal (cmd en Windows, Terminal en Mac/Linux)
2. Navega a la carpeta del curso con el comando `cd`:
   ```bash
   # En Windows:
   cd C:\Users\TuNombre\Descargas\curso-python-desde-cero-main\Fase1_Fundamentos

   # En Mac/Linux:
   cd ~/Descargas/curso-python-desde-cero-main/Fase1_Fundamentos
   ```
3. Ejecuta el archivo:
   ```bash
   python dia01_hola_mundo.py
   ```
   O si eso no funciona:
   ```bash
   python3 dia01_hola_mundo.py
   ```

> 💡 **¿Cómo navegar carpetas con `cd`?**
> - `cd NombreCarpeta` → entra a esa carpeta
> - `cd ..` → vuelve a la carpeta anterior
> - `dir` (Windows) o `ls` (Mac/Linux) → muestra qué hay en la carpeta actual

### Método 3: IDLE

1. Abre IDLE
2. Ve a **File → Open** (Archivo → Abrir)
3. Navega a la carpeta del curso y selecciona el archivo `.py`
4. Se abre en una ventana nueva
5. Presiona **F5** o ve a **Run → Run Module**
6. El resultado aparece en la ventana principal de IDLE

---

## 📅 Paso 5 — Cómo seguir el curso día a día {#paso-5-rutina}

### Rutina diaria de 2 horas

Cada día del curso tiene un archivo Python que debes seguir. Esta es la rutina recomendada:

| Tiempo | Actividad | Qué hacer |
|--------|-----------|-----------|
| **10 min** | 📖 **Leer** | Lee todos los comentarios del archivo sin ejecutarlo todavía. Entiende qué va a hacer. |
| **20 min** | ▶️ **Ejecutar** | Ejecuta el programa y observa el resultado. ¿Es lo que esperabas? |
| **30 min** | 🔬 **Experimentar** | Modifica números, textos, y vuelve a ejecutar. ¿Qué cambia? ¡Rompe cosas a propósito! |
| **45 min** | ✏️ **Ejercicios** | Cada archivo tiene ejercicios al final. Hazlos uno por uno. |
| **15 min** | ☕ **Repasar** | Descansa y piensa en lo que aprendiste hoy. |

### Qué hacer cuando algo no funciona

No te asustes. Los errores son **normales** y forman parte del aprendizaje. Sigue estos pasos:

1. **Lee el mensaje de error** — Python te dice exactamente qué salió mal. Por ejemplo:
   ```
   SyntaxError: invalid syntax
   ```
   Eso significa que escribiste algo mal (quizás te faltó cerrar un paréntesis o una comilla).

2. **Busca la línea del error** — El error indica el número de línea. Ve a esa línea y revísala.

3. **Compara con el código original** — Abre el archivo del curso y compara tu código con el ejemplo.

4. **Busca en Google** — Copia el mensaje de error y pégalo en Google. Millones de programadores han tenido el mismo problema.

5. **Pide ayuda** — Si nada funciona, no estás solo. Busca comunidades de Python en español.

### Errores comunes y cómo solucionarlos

| Error | Causa | Solución |
|-------|-------|----------|
| `SyntaxError: invalid syntax` | Algo está mal escrito | Revisa paréntesis, comillas, dos puntos |
| `NameError: name 'x' is not defined` | Usas una variable sin definirla | Asegúrate de haber escrito bien el nombre |
| `IndentationError` | Espacios mal puestos | Python requiere indentar con 4 espacios |
| `TypeError` | Tipo de dato incorrecto | No mezcles texto con números sin convertir |
| `ModuleNotFoundError` | Librería no instalada | Ejecuta `pip install nombre_libreria` |

---

## 🏗️ Estructura del curso explicada {#estructura}

### 🟢 Fase 1: Fundamentos (Días 1–5)
**¿Qué aprenderás?** Las bases absolutas de Python.
- **Día 1**: Tu primer programa. Aprenderás `print()` para mostrar texto.
- **Día 2**: Variables. Aprenderás a guardar información (nombres, números, etc.).
- **Día 3**: Entrada del usuario. Tu programa podrá preguntar cosas.
- **Día 4**: Strings (texto). Aprenderás a manipular palabras y frases.
- **Día 5**: 🎯 Proyecto — Tarjeta de presentación digital.

### 🔵 Fase 2: Control de Flujo (Días 6–10)
**¿Qué aprenderás?** Hacer que tu programa tome decisiones y repita acciones.
- **Día 6**: Condicionales (if/elif/else). "Si pasa esto, haz aquello".
- **Día 7**: Bucle while. "Repite mientras se cumpla esta condición".
- **Día 8**: Bucle for. "Repite exactamente X veces".
- **Día 9**: Listas. Guardar muchas cosas en una sola variable.
- **Día 10**: Diccionarios. Datos con nombre (como una agenda).

### 🟣 Fase 3: Funciones (Días 11–15)
**¿Qué aprenderás?** Organizar tu código en bloques reutilizables.
- **Día 11**: Funciones básicas. Crear tus propias instrucciones.
- **Día 12**: Funciones avanzadas (lambda, comprensiones de lista).
- **Día 13**: Módulos. Usar librerías de Python.
- **Día 14**: Manejo de errores. Que tu programa no "explote".
- **Día 15**: 🎯 Proyecto — Quiz interactivo con puntuación.

### 🟠 Fase 4: Programación Orientada a Objetos (Días 16–20)
**¿Qué aprenderás?** Modelar el mundo real con código.
- **Día 16**: Clases. Crear tus propios "moldes" de objetos.
- **Día 17**: Herencia. Una clase puede "heredar" de otra.
- **Día 18**: 🎯 Proyecto — Sistema de inventario.
- **Día 19**: POO avanzado. Encapsulamiento y propiedades.
- **Día 20**: 🎯 Proyecto — Sistema bancario completo.

### 🔴 Fase 5: Archivos y Librerías (Días 21–25)
**¿Qué aprenderás?** Guardar datos y usar el mundo real.
- **Día 21**: Archivos de texto. Leer y escribir archivos.
- **Día 22**: CSV y JSON. Formatos de datos comunes.
- **Día 23**: pip y librerías externas. Instalar superpoderes.
- **Día 24**: APIs. Obtener datos de internet.
- **Día 25**: SQLite. Tu propia base de datos.

### 🏆 Fase 6: Proyectos Finales (Días 26–30)
**¿Qué aprenderás?** Construir programas completos y profesionales.
- **Día 26**: Gestor de tareas con persistencia en JSON.
- **Día 27**: Web scraping y consumo de APIs.
- **Día 28**: Automatización de archivos.
- **Día 29**: Dashboard con datos estadísticos.
- **Día 30**: 🏆 PROYECTO FINAL — Sistema de gestión de biblioteca.

---

## ❓ Preguntas Frecuentes {#faq}

**¿Necesito internet para hacer el curso?**
Solo necesitas internet para descargar Python y VS Code (una sola vez). Después, todo el curso funciona sin internet. Los días 24 y 27 usan APIs de internet, pero son opcionales.

**¿Puedo ir más rápido que 1 día por archivo?**
¡Sí! Si un día te resulta muy fácil, puedes hacer dos archivos en el mismo día. Pero asegúrate de hacer los ejercicios antes de continuar.

**¿Puedo ir más lento?**
Por supuesto. No hay prisa. Si necesitas dos días para un archivo, tómalos. Lo importante es entender antes de avanzar.

**¿Qué pasa si me salto un día?**
Nada grave. Cada archivo es independiente, aunque se recomienda hacerlos en orden porque los conceptos se van acumulando.

**¿Puedo usar este curso en el teléfono?**
Puedes leer los archivos, pero para ejecutar código Python necesitas una computadora. Existen apps de Python para teléfono pero son más limitadas.

**¿Este curso me conseguirá trabajo?**
Este curso es el primer paso. Después de los 30 días tendrás una base sólida. Para trabajar como programador necesitarás seguir aprendiendo y hacer proyectos propios.

**¿Python es mejor que otros lenguajes?**
Cada lenguaje tiene sus ventajas. Python es excelente para aprender porque es simple y versátil. Después de aprenderlo, otros lenguajes te serán más fáciles.

**¿Dónde puedo hacer preguntas si algo no entiendo?**
- Stack Overflow (en español: es.stackoverflow.com)
- Reddit r/learnpython
- Grupos de Python en Telegram o Discord
- YouTube: busca el error que tienes

**¿Necesito comprar algo?**
No. Python es gratuito. VS Code es gratuito. Este curso es gratuito.

---

> 🎉 **¡Felicitaciones por llegar hasta aquí!** Ya tienes todo lo que necesitas para empezar. Abre el archivo `Fase1_Fundamentos/dia01_hola_mundo.py` y ¡escribe tu primer programa!

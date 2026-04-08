# ⚡ GUÍA DE INSTALACIÓN RÁPIDA

Referencia rápida. Para instrucciones detalladas, ve al [MANUAL_COMPLETO.md](MANUAL_COMPLETO.md).

---

## 1. Descargar el curso

**Opción ZIP** (recomendada):
- Botón verde "Code" en GitHub → "Download ZIP" → Extraer

**Opción Git**:
```bash
git clone https://github.com/sarin-jp/curso-python-desde-cero.git
```

---

## 2. Instalar Python

### Windows
1. Ve a **https://www.python.org/downloads/**
2. Descarga el instalador
3. ⚠️ **MARCA "Add Python to PATH"** antes de instalar
4. Haz clic en "Install Now"

### Mac
1. Ve a **https://www.python.org/downloads/**
2. Descarga el `.pkg` para Mac
3. Ejecuta el instalador (siguiente, siguiente, instalar)

### Linux
```bash
sudo apt update && sudo apt install python3 python3-pip
```

### Verificar instalación
```bash
python --version
# Debe mostrar algo como: Python 3.11.4
```

---

## 3. Instalar VS Code

1. Ve a **https://code.visualstudio.com/**
2. Descarga e instala para tu sistema operativo
3. Abre VS Code → Extensiones (ícono cuadritos) → Busca "Python" → Install

---

## 4. Ejecutar un archivo

### VS Code (recomendado)
1. Archivo → Abrir carpeta → Selecciona la carpeta del curso
2. Abre el archivo `.py` que quieras
3. Haz clic en ▶️ (arriba a la derecha)

### Terminal
```bash
# Navega a la carpeta del archivo
cd Fase1_Fundamentos

# Ejecuta el archivo
python dia01_hola_mundo.py
```

### IDLE
File → Open → selecciona el archivo → F5 (Run Module)

---

## 5. Empezar el curso

Abre en orden:
1. `Fase1_Fundamentos/dia01_hola_mundo.py`
2. Sigue el orden de los días del 1 al 30
3. Marca tu progreso en [PROGRESO.md](PROGRESO.md)

---

## 🔧 Solución rápida de problemas

| Problema | Solución |
|----------|----------|
| `python` no reconocido | Reinstala Python con "Add to PATH" marcado |
| Error de sintaxis | Revisa paréntesis, comillas y dos puntos |
| `ModuleNotFoundError` | Ejecuta `pip install nombre_modulo` |
| Archivo no abre | Asegúrate de abrir la carpeta del curso en VS Code |

# 🚀 MirageMask  
✨ **Descripción breve**: Biblioteca de herramientas para pruebas de Red Team en sistemas Windows, especializada en camuflaje de troyanos.  
[![Release](https://img.shields.io/github/v/release/yourname/project)](https://github.com/yourname/project)  
[![CI/CD](https://img.shields.io/github/actions/workflow/status/yourname/project/build.yml)](https://github.com/yourname/project/actions)  
![Vista previa](back.png)  

## 🌐 Idiomas  
- [English](README.en.md)  
- [简体中文](README.md)  
- [Español](README.es.md)  
- [日本語](README.ja.md)  

## ⚠️ **Exención de responsabilidad legal**  
```text  
• Esta herramienta está estrictamente limitada a **pruebas de seguridad legalmente autorizadas**. Usos prohibidos:  
  ⛔ Penetración no autorizada | ⛔ Ataques DDoS | ⛔ Robo de datos  
• El usuario es responsable de cumplir con el Artículo 285 del Código Penal Chino y el Artículo 27 de la Ley de Ciberseguridad.  
• Los desarrolladores **no asumen responsabilidad** por consecuencias civiles/penales derivadas del uso indebido.  
```

  
Términos completos: [Aviso Legal](../legal/DISCLAIMER.md)  

## 🌟 Funciones  
- ✅ Camuflaje de archivos arbitrarios en Windows  
- 🚄 Secuestro de punto de entrada para archivos grandes  
**Funciones planificadas**  
- 🔒 Extracción de iconos de archivos  
- 🔒 Modificación de iconos EXE  

## 🔰 Vista previa de la UI  
![Vista previa](seeUI.png)  

## 🛠️ Inicio rápido  
### Requisitos previos  
```bash  
python 3.8+  
pyinstaller  
```

  

### Instalación  
```bash  
git clone https://github.com/yourname/project.git  
pip install -r requirements.txt  
pip install pyinstaller  
```

  

## 🤝 Contribución  
1. Bifurca (Fork) el repositorio  
2. Crea una rama de función  
3. Realiza y confirma (commit) los cambios  
4. Sube (push) a la rama  
5. Abre una Pull Request  

## 📜 Licencia  
Bajo licencia [Apache 2.0](LICENSE).  

---  
## ⭐ Bilibili del autor  
【Espacio de Bilibili de Momo el Gato Programador】[https://b23.tv/nKcZ1pB ](https://b23.tv/nKcZ1pB ) 

---  
## ⚜️ Reconocimientos  
Plantilla UI: [PyDracula](https://github.com/Wanderson-Magalhaes/PyDracula)  

## ⚠️ Notas de personalización  
- El código de agrupación está en `/Trojans`  
- La implementación actual prioriza minimalismo para reducir detección  
- En escenarios reales (ejercicios de defensa de red), aplicar medidas adicionales:  
  🔒 Cifrado | 🔒 Ofuscación | 🔒 Anti-ingeniería inversa  
- Las cargas útiles con funciones anti-VM/debug mejoran autenticidad, imitando aplicaciones benignas  

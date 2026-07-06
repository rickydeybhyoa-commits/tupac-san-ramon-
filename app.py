import tkinter as tk
from tkinter import ttk, messagebox
import json

# ==============================================================================
# BASE DE DATOS INTEGRADA (MUNICIPALIDAD DISTRITAL DE SAN RAMÓN)
# Extraído, limpiado y mapeado directamente de tu archivo TUPA
# ==============================================================================
DATOS_TUPA = [
    {
        "id": "1",
        "numero": "1.0",
        "procedimiento": "INSCRIPCIÓN ORDINARIA DE NACIMIENTO DENTRO DE LOS 60 DÍAS",
        "sustento": "SUB GERENCIA DE REGISTRO CIVIL - PROCEDIMIENTOS ADMINISTRATIVOS",
        "requisitos": [
            "1.0 Certificado de Nacido Vivo expedido por Profesional Competente o constancia otorgada por persona autorizada por el Ministerio de Salud.",
            "2.0 Declaración Jurada de la Autoridad Política, Judicial o Administrativa en caso de no haber centro de salud.",
            "3.0 Presencia de los padres o de uno de ellos con DNI vigente."
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "Inmediato (Automático)",
        "inicio": "Sub Gerencia de Registro Civil",
        "autoridad": "Sub Gerente de Registro Civil",
        "reconsideracion": "Sub Gerente de Registro Civil",
        "apelacion": "Gerencia Municipal"
    },
    
{
        "id": "187",
        "numero": "169",
        "procedimiento": "ADMISIÓN DE OSB AL PROGRAMA DE COMPLEMENTACIÓN ALIMENTARIA MUNICIPAL PCAM",
        "sustento": "BASE LEGAL\n- Ley Nº 27767, Ley del Programa Nacional Complementario de Asistencia Alimentaria, pub 27.06.2002\n- D.S 002-2004-MINDES, Reglamento de la Ley Nº 27767, pub. 25.05.2004\n- Ley Nº 27972, Ley Orgánica de Municipalidades",
        "requisitos": [
            "1 Solicitud dirigido al Alcalde cumpliendo con los requisitos generales de presentación, peticionando la Admisión al PCAM",
            "2 Copia simple de la Resolución de Reconocimiento de la OSB emitido por la Municipalidad de San Ramón",
            "3 Copia simple del Padrón de Socias Activas (como mínimo de 15 socias)",
            "4 Copia simple del DNI vigente de las socias activas",
            "5 Copia simple del DNI vigente de los miembros del Consejo Directivo o Junta Directiva",
            "6 Croquis de ubicación del OSB",
            "7 Determinar el lugar donde la OSB recepcionará y atenderá el reparto de los productos pertenecientes al PCAM",
            "8 Libro de Actas",
            "9 Cuaderno de Almacén",
            "10 Cuaderno de gastos diarios y raciones",
            "--------------------------------------------------",
            "📌 NOTAS PARA EL CIUDADANO:",
            "- La Organización deberá contar con un local adecuado para la recepción, almacenamiento y distribución de los alimentos"
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Social y Humano",
        "reconsideracion": "Gerente de Desarrollo Social y Humano\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
]

class BuscadorTupaInstitucional:
    def __init__(self, root):
        self.root = root
        self.root.title("SISTEMA DE CONSULTA TUPA - MUNICIPALIDAD DISTRITAL DE SAN RAMÓN")
        self.root.geometry("950x720") 
        self.root.configure(bg="#F4F6F4")

        # Configuración estética Institucional de San Ramón
        self.COLOR_VERDE_OSCURO = "#1E5631" 
        self.COLOR_VERDE_ACENTO = "#4C9A2A"
        self.COLOR_BLANCO = "#FFFFFF"
        self.COLOR_GRIS_TEXTO = "#333333"

        # Variables de memoria de búsqueda
        self.coincidencias_actuales = []
        self.indice_actual = 0
        self.termino_actual = ""

        self.crear_componentes()
        self.mostrar_resumen_inicial()

    def crear_componentes(self):
        # --- ENCABEZADO INSTITUCIONAL ---
        header = tk.Frame(self.root, bg=self.COLOR_VERDE_OSCURO, height=85)
        header.pack(fill="x", side="top")
        header.pack_propagate(False)

        lbl_logo_texto = tk.Label(header, text="🏛️", font=("Arial", 28), fg=self.COLOR_BLANCO, bg=self.COLOR_VERDE_OSCURO)
        lbl_logo_texto.pack(side="left", padx=20, pady=10)

        lbl_titulo = tk.Label(header, text="MUNICIPALIDAD DISTRITAL DE SAN RAMÓN", font=("Arial", 14, "bold"), fg=self.COLOR_BLANCO, bg=self.COLOR_VERDE_OSCURO)
        lbl_titulo.pack(anchor="w", pady=(15, 0), padx=5)
        
        lbl_sub = tk.Label(header, text="SISTEMA INTERNO DE CONSULTA TUPA", font=("Arial", 10, "italic"), fg="#C5E1A5", bg=self.COLOR_VERDE_OSCURO)
        lbl_sub.pack(anchor="w", padx=5)

        # --- CUERPO PRINCIPAL ---
        contenedor = tk.Frame(self.root, bg="#F4F6F4")
        contenedor.pack(fill="both", expand=True, padx=20, pady=15)

        # Panel de Filtros y Entrada
        frame_busqueda = tk.LabelFrame(contenedor, text=" CRITERIOS DE BÚSQUEDA ", font=("Arial", 10, "bold"), bg=self.COLOR_BLANCO, fg=self.COLOR_VERDE_OSCURO, bd=2, relief="groove")
        frame_busqueda.pack(fill="x", pady=5)

        # Fila de Input
        lbl_buscar = tk.Label(frame_busqueda, text="Buscar término:", font=("Arial", 11, "bold"), bg=self.COLOR_BLANCO, fg=self.COLOR_GRIS_TEXTO)
        lbl_buscar.grid(row=0, column=0, padx=15, pady=15, sticky="w")

        self.txt_entrada = tk.Entry(frame_busqueda, font=("Arial", 12), width=50, bd=1, relief="solid")
        self.txt_entrada.grid(row=0, column=1, padx=5, pady=15, sticky="w")
        self.txt_entrada.bind("<Return>", lambda event: self.buscar())

        btn_buscar = tk.Button(frame_busqueda, text=" 🔍 Buscar ", font=("Arial", 10, "bold"), bg=self.COLOR_VERDE_ACENTO, fg=self.COLOR_BLANCO, bd=0, cursor="hand2", padx=20, pady=4, command=self.buscar)
        btn_buscar.grid(row=0, column=2, padx=10, pady=15)

        # selectores de tipo de filtro
        frame_radios = tk.Frame(frame_busqueda, bg=self.COLOR_BLANCO)
        frame_radios.grid(row=1, column=0, columnspan=3, padx=15, pady=5, sticky="w")

        self.filtro_tipo = tk.StringVar(value="todo")
        
        opciones = [("Número de Item", "numero"), ("Nombre del Trámite", "nombre"), ("Palabra Clave / Sustento", "clave"), ("Todo", "todo")]
        for texto, valor in opciones:
            rb = tk.Radiobutton(frame_radios, text=texto, value=valor, variable=self.filtro_tipo, bg=self.COLOR_BLANCO, activebackground=self.COLOR_BLANCO, fg=self.COLOR_GRIS_TEXTO, font=("Arial", 10))
            rb.pack(side="left", padx=10, pady=5)

        # --- PANEL DE VISUALIZACIÓN (FICHA TÉCNICA) ---
        frame_resultados = tk.LabelFrame(contenedor, text=" FICHA DEL PROCEDIMIENTO ADMINISTRATIVO ", font=("Arial", 10, "bold"), bg=self.COLOR_BLANCO, fg=self.COLOR_VERDE_OSCURO, bd=2, relief="groove")
        frame_resultados.pack(fill="both", expand=True, pady=10)

        # Área de Texto con Scroll integrado
        self.txt_ficha = tk.Text(frame_resultados, font=("Arial", 11), bg="#FAFAFA", fg="#111111", wrap="word", bd=0)
        scroll = tk.Scrollbar(frame_resultados, command=self.txt_ficha.yview)
        self.txt_ficha.configure(yscrollcommand=scroll.set)
        
        scroll.pack(side="right", fill="y")
        self.txt_ficha.pack(side="left", fill="both", expand=True, padx=15, pady=15)

        # --- PIE DE PÁGINA Y BOTONES DE ACCIÓN ---
        frame_acciones = tk.Frame(contenedor, bg="#F4F6F4")
        frame_acciones.pack(fill="x", pady=5)

        self.btn_imprimir = tk.Button(frame_acciones, text="📄 Imprimir Ficha", font=("Arial", 10, "bold"), bg="#E0E0E0", state="disabled", padx=15, pady=6, bd=0, command=self.imprimir_ficha)
        self.btn_imprimir.pack(side="left", padx=5)

        self.btn_pdf = tk.Button(frame_acciones, text="💾 Exportar Ficha", font=("Arial", 10, "bold"), bg="#E0E0E0", state="disabled", padx=15, pady=6, bd=0, command=self.exportar_ficha)
        self.btn_pdf.pack(side="left", padx=5)

        # --- BOTONES DE NAVEGACIÓN ---
        self.btn_anterior = tk.Button(frame_acciones, text="⏮️ Anterior", font=("Arial", 10, "bold"), bg="#E0E0E0", state="disabled", padx=15, pady=6, bd=0, command=self.anterior_resultado)
        self.btn_anterior.pack(side="left", padx=25)

        self.lbl_paginacion = tk.Label(frame_acciones, text="Coincidencia: 0 de 0", font=("Arial", 10, "bold"), bg="#F4F6F4", fg=self.COLOR_GRIS_TEXTO)
        self.lbl_paginacion.pack(side="left", padx=5)

        self.btn_siguiente = tk.Button(frame_acciones, text="Siguiente ⏭️", font=("Arial", 10, "bold"), bg="#E0E0E0", state="disabled", padx=15, pady=6, bd=0, command=self.siguiente_resultado)
        self.btn_siguiente.pack(side="left", padx=25)

        btn_limpiar = tk.Button(frame_acciones, text="🔄 Nueva búsqueda", font=("Arial", 10, "bold"), bg="#666666", fg=self.COLOR_BLANCO, bd=0, cursor="hand2", padx=15, pady=6, command=self.limpiar)
        btn_limpiar.pack(side="right", padx=5)

    def mostrar_resumen_inicial(self):
        self.txt_ficha.configure(state="normal")
        self.txt_ficha.delete("1.0", tk.END)
        self.txt_ficha.insert(tk.END, "SISTEMA TUPA ACTIVO\n", "titulo_inicial")
        self.txt_ficha.insert(tk.END, f"Se han cargado los procedimientos optimizados del TUPA San Ramón de forma interna.\n\nEscriba el número de ítem (ej. '149' o '1.0') o palabras descriptivas como 'vehículos' o 'nacimiento' para desplegar la ficha estructurada institucional.", "cuerpo_inicial")
        
        self.txt_ficha.tag_configure("titulo_inicial", font=("Arial", 14, "bold"), foreground=self.COLOR_VERDE_OSCURO)
        self.txt_ficha.tag_configure("cuerpo_inicial", font=("Arial", 11), foreground="#555555")
        self.txt_ficha.configure(state="disabled")

    def buscar(self):
        termino = self.txt_entrada.get().strip()
        if not termino:
            messagebox.showwarning("Campo vacío", "Por favor, digite un número o palabra para iniciar la consulta.")
            return

        tipo = self.filtro_tipo.get()
        coincidencias = []

        for item in DATOS_TUPA:
            if tipo == "numero" and termino.lower() in item["numero"].lower():
                coincidencias.append(item)
            elif tipo == "nombre" and termino.lower() in item["procedimiento"].lower():
                coincidencias.append(item)
            elif tipo == "clave" and (termino.lower() in item["sustento"].lower() or any(termino.lower() in req.lower() for req in item["requisitos"])):
                coincidencias.append(item)
            elif tipo == "todo":
                if (termino.lower() in item["numero"].lower() or 
                    termino.lower() in item["procedimiento"].lower() or 
                    termino.lower() in item["sustento"].lower() or
                    any(termino.lower() in req.lower() for req in item["requisitos"])):
                    coincidencias.append(item)

        self.coincidencias_actuales = coincidencias
        self.indice_actual = 0
        self.termino_actual = termino
        
        self.desplegar_resultados()

    def desplegar_resultados(self):
        self.txt_ficha.configure(state="normal")
        self.txt_ficha.delete("1.0", tk.END)

        total_resultados = len(self.coincidencias_actuales)

        if total_resultados == 0:
            self.txt_ficha.insert(tk.END, f"❌ No se encontraron procedimientos vinculados al término: '{self.termino_actual}'\n\nVerifique la escritura o cambie el criterio de selección.", "error")
            self.txt_ficha.tag_configure("error", font=("Arial", 11, "bold"), foreground="red")
            
            self.btn_pdf.configure(state="disabled", bg="#E0E0E0")
            self.btn_imprimir.configure(state="disabled", bg="#E0E0E0")
            self.btn_anterior.configure(state="disabled", bg="#E0E0E0")
            self.btn_siguiente.configure(state="disabled", bg="#E0E0E0")
            self.lbl_paginacion.configure(text="Coincidencia: 0 de 0")
        else:
            self.btn_pdf.configure(state="normal", bg=self.COLOR_VERDE_OSCURO, fg=self.COLOR_BLANCO, cursor="hand2")
            self.btn_imprimir.configure(state="normal", bg=self.COLOR_VERDE_OSCURO, fg=self.COLOR_BLANCO, cursor="hand2")

            if self.indice_actual > 0:
                self.btn_anterior.configure(state="normal", bg=self.COLOR_VERDE_OSCURO, fg=self.COLOR_BLANCO, cursor="hand2")
            else:
                self.btn_anterior.configure(state="disabled", bg="#E0E0E0", fg="black")

            if self.indice_actual < total_resultados - 1:
                self.btn_siguiente.configure(state="normal", bg=self.COLOR_VERDE_OSCURO, fg=self.COLOR_BLANCO, cursor="hand2")
            else:
                self.btn_siguiente.configure(state="disabled", bg="#E0E0E0", fg="black")

            self.lbl_paginacion.configure(text=f"Coincidencia: {self.indice_actual + 1} de {total_resultados}")

            self.txt_ficha.insert(tk.END, f"TOTAL COINCIDENCIAS: {total_resultados} | VIENDO EL REGISTRO ACTUAL NÚMERO: {self.indice_actual + 1}\n", "info_conteo")
            self.txt_ficha.insert(tk.END, "═"*75 + "\n\n")
            self.txt_ficha.tag_configure("info_conteo", font=("Arial", 10, "bold"), foreground=self.COLOR_VERDE_ACENTO)

            proc = self.coincidencias_actuales[self.indice_actual]

            secciones = [
                ("N.º ITEM:", proc["numero"]),
                ("PROCEDIMIENTO:", proc["procedimiento"]),
                ("BASE LEGAL / SUSTENTO:", proc["sustento"]),
                ("DERECHO DE TRÁMITE:", proc["derecho_tramite"]),
                ("PLAZO PARA RESOLVER:", proc["plazo"]),
                ("INICIO DEL PROCEDIMIENTO:", proc["inicio"]),
                ("AUTORIDAD COMPETENTE:", proc["autoridad"]),
                ("RECURSO DE RECONSIDERACIÓN:", proc["reconsideracion"]),
                ("RECURSO DE APELACIÓN:", proc["apelacion"])
            ]

            for titulo, contenido in secciones:
                self.txt_ficha.insert(tk.END, f"{titulo}\n", "subtítulo")
                self.txt_ficha.insert(tk.END, f"{contenido}\n\n", "contenido")

            self.txt_ficha.insert(tk.END, "REQUISITOS ESTRUCTURADOS:\n", "subtítulo")
            for req in proc["requisitos"]:
                self.txt_ficha.insert(tk.END, f"  🔹 {req}\n", "contenido")
            
            self.txt_ficha.tag_configure("subtítulo", font=("Arial", 11, "bold"), foreground=self.COLOR_VERDE_OSCURO)
            self.txt_ficha.tag_configure("contenido", font=("Arial", 11), foreground="#222222")

            self.resaltar_coincidencia(self.termino_actual)

        self.txt_ficha.configure(state="disabled")

    def siguiente_resultado(self):
        if self.indice_actual < len(self.coincidencias_actuales) - 1:
            self.indice_actual += 1
            self.desplegar_resultados()

    def anterior_resultado(self):
        if self.indice_actual > 0:
            self.indice_actual -= 1
            self.desplegar_resultados()

    def imprimir_ficha(self):
        try:
            texto_impresion = self.txt_ficha.get("1.0", tk.END)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode="w", encoding="utf-8") as f:
                f.write(texto_impresion)
                nombre_archivo = f.name
            
            os.startfile(nombre_archivo, "print")
        except Exception as e:
            messagebox.showerror("Error de Impresión", f"No se pudo mandar a imprimir:\n{str(e)}")

    # --- FUNCIÓN DE EXPORTAR CORREGIDA PARA EVITAR RESTRICCIONES DE WINDOWS ---
    def exportar_ficha(self):
        try:
            texto_exportar = self.txt_ficha.get("1.0", tk.END)
            proc_actual = self.coincidencias_actuales[self.indice_actual]
            
            # Limpiamos el nombre de caracteres que puedan romper rutas
            nombre_base = f"Ficha_TUPA_Item_{proc_actual['numero']}".replace("/", "_").replace(".", "_")
            
            # Forzamos la creación del archivo en la carpeta temporal de Windows
            ruta_archivo = os.path.join(tempfile.gettempdir(), f"{nombre_base}.txt")
            
            # Bucle inteligente: si el archivo ya está abierto, genera una copia numerada consecutiva
            contador = 1
            while True:
                try:
                    with open(ruta_archivo, "w", encoding="utf-8") as f:
                        f.write(texto_exportar)
                    break 
                except PermissionError:
                    ruta_archivo = os.path.join(tempfile.gettempdir(), f"{nombre_base}_{contador}.txt")
                    contador += 1
            
            # Levanta la ficha directamente en el Bloc de Notas de Windows
            os.startfile(ruta_archivo)
            
        except Exception as e:
            messagebox.showerror("Error al Exportar", f"No se pudo guardar el documento:\n{str(e)}")

    def resaltar_coincidencia(self, palabra):
        self.txt_ficha.tag_configure("amarillo", background="#FFF176", foreground="#000000")
        posicion = "1.0"
        while True:
            posicion = self.txt_ficha.search(palabra, posicion, nocase=True, stopindex=tk.END)
            if not posicion: break
            fin_posicion = f"{posicion}+{len(palabra)}c"
            self.txt_ficha.tag_add("amarillo", posicion, fin_posicion)
            posicion = fin_posicion

    def limpiar(self):
        self.txt_entrada.delete(0, tk.END)
        self.mostrar_resumen_inicial()
        self.btn_pdf.configure(state="disabled", bg="#E0E0E0")
        self.btn_imprimir.configure(state="disabled", bg="#E0E0E0")
        self.btn_anterior.configure(state="disabled", bg="#E0E0E0")
        self.btn_siguiente.configure(state="disabled", bg="#E0E0E0")
        self.lbl_paginacion.configure(text="Coincidencia: 0 de 0")
        self.coincidencias_actuales = []
        self.indice_actual = 0
        self.filtro_tipo.set("todo")

if __name__ == "__main__":
    root = tk.Tk()
    app = BuscadorTupaInstitucional(root)
    root.mainloop()
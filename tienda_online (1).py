"""
╔══════════════════════════════════════╗
║   TECHSTORE — Tienda Online Python   ║
║   Requiere: Python 3.x + tkinter     ║
║   Ejecutar: python tienda_online.py  ║
╚══════════════════════════════════════╝
"""

import tkinter as tk
from tkinter import ttk, messagebox
import random

# ─── DATOS ───────────────────────────────────────────────────────────────────
PRODUCTOS = [
    {"id": 1,  "nombre": "Laptop Pro X",       "precio": 1299.99, "categoria": "Electrónica",    "stock": 15, "emoji": "💻", "rating": 4.8},
    {"id": 2,  "nombre": "Smartphone Ultra",   "precio":  899.00, "categoria": "Electrónica",    "stock": 30, "emoji": "📱", "rating": 4.6},
    {"id": 3,  "nombre": "Audífonos Wireless", "precio":  149.99, "categoria": "Audio",          "stock": 50, "emoji": "🎧", "rating": 4.9},
    {"id": 4,  "nombre": "Teclado Mecánico",   "precio":   89.99, "categoria": "Accesorios",     "stock": 25, "emoji": "⌨️", "rating": 4.5},
    {"id": 5,  "nombre": "Monitor 4K 27\"",    "precio":  399.99, "categoria": "Electrónica",    "stock": 10, "emoji": "🖥️", "rating": 4.7},
    {"id": 6,  "nombre": "Mouse Gamer",        "precio":   59.99, "categoria": "Accesorios",     "stock": 40, "emoji": "🖱️", "rating": 4.4},
    {"id": 7,  "nombre": "Webcam HD 1080p",    "precio":   79.99, "categoria": "Accesorios",     "stock": 20, "emoji": "📷", "rating": 4.3},
    {"id": 8,  "nombre": "SSD 1TB NVMe",       "precio":  129.99, "categoria": "Almacenamiento", "stock": 35, "emoji": "💾", "rating": 4.8},
    {"id": 9,  "nombre": "Bocina Bluetooth",   "precio":   69.99, "categoria": "Audio",          "stock": 45, "emoji": "🔊", "rating": 4.6},
    {"id": 10, "nombre": "Tablet 10\"",        "precio":  349.99, "categoria": "Electrónica",    "stock": 18, "emoji": "📟", "rating": 4.5},
    {"id": 11, "nombre": "Cable USB-C 2m",     "precio":   12.99, "categoria": "Accesorios",     "stock": 100,"emoji": "🔌", "rating": 4.2},
    {"id": 12, "nombre": "Hub USB 7 puertos",  "precio":   39.99, "categoria": "Accesorios",     "stock": 22, "emoji": "🔗", "rating": 4.4},
]

OFERTAS = [
    {"prod_id": 1, "descuento": 15, "etiqueta": "🔥 HOT"},
    {"prod_id": 3, "descuento": 20, "etiqueta": "⚡ FLASH"},
    {"prod_id": 5, "descuento": 10, "etiqueta": "🌟 DEAL"},
    {"prod_id": 9, "descuento": 25, "etiqueta": "💥 OFERTA"},
]

RESEÑAS = [
    {"usuario": "Carlos M.",  "producto": "Laptop Pro X",      "estrellas": 5, "comentario": "Increíble rendimiento, la batería dura todo el día."},
    {"usuario": "Sofia R.",   "producto": "Audífonos Wireless","estrellas": 5, "comentario": "El sonido es espectacular y la cancelación de ruido es excelente."},
    {"usuario": "Miguel Á.",  "producto": "Monitor 4K 27\"",   "estrellas": 4, "comentario": "Imagen muy nítida y colores precisos. Le falta un hub USB."},
    {"usuario": "Ana L.",     "producto": "Mouse Gamer",       "estrellas": 4, "comentario": "Muy cómodo para sesiones largas, el scroll se siente sólido."},
    {"usuario": "Roberto P.", "producto": "SSD 1TB NVMe",      "estrellas": 5, "comentario": "Velocidades impresionantes, instalación del SO en minutos."},
]

C = {
    "bg":         "#0d1117",
    "panel":      "#161b22",
    "sidebar":    "#0d1117",
    "card":       "#1c2128",
    "border":     "#30363d",
    "accent":     "#58a6ff",
    "accent2":    "#3fb950",
    "warning":    "#d29922",
    "danger":     "#f85149",
    "purple":     "#bc8cff",
    "orange":     "#e3884a",
    "text":       "#e6edf3",
    "text_dim":   "#8b949e",
    "btn_bg":     "#21262d",
    "btn_hover":  "#30363d",
    "highlight":  "#1f6feb",
    "sidebar_sel":"#1c2128",
}

NAV_ITEMS = [
    ("🏠", "Inicio",      "ventana_inicio"),
    ("🛍️",  "Productos",  "mostrar_productos"),
    ("🔥", "Ofertas",     "ventana_ofertas"),
    ("📦", "Categorías",  "ventana_categorias"),
    ("⭐", "Reseñas",     "ventana_reseñas"),
    ("🎫", "Cupones",     "ventana_cupones"),
    ("🚚", "Envíos",      "ventana_envios"),
    ("🔔", "Newsletter",  "ventana_newsletter"),
    ("🛠️", "Soporte",     "ventana_soporte"),
    ("⚙️", "Ajustes",     "ventana_ajustes"),
]


class TiendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🛒  TechStore — Tienda Online")
        self.root.geometry("1180x720")
        self.root.minsize(1000, 640)
        self.root.configure(bg=C["bg"])
        self.root.resizable(True, True)

        self.carrito    = {}
        self.filtro_cat = tk.StringVar(value="Todas")
        self.busqueda   = tk.StringVar()
        self.nav_activo = tk.StringVar(value="Inicio")
        self.busqueda.trace("w", lambda *a: self.refrescar_productos())

        self.f_h2    = ("Segoe UI", 13, "bold")
        self.f_h3    = ("Segoe UI", 11, "bold")
        self.f_body  = ("Segoe UI", 10)
        self.f_small = ("Segoe UI",  9)
        self.f_mono  = ("Consolas",  10)

        self._build_ui()
        self.refrescar_productos()

    # ════════════════════════ UI PRINCIPAL ════════════════════════════════════
    def _build_ui(self):
        # HEADER
        header = tk.Frame(self.root, bg=C["panel"], height=58)
        header.pack(fill="x")
        header.pack_propagate(False)

        logo_wrap = tk.Frame(header, bg=C["panel"])
        logo_wrap.pack(side="left")
        tk.Frame(logo_wrap, bg=C["panel"], width=200).pack(side="left")
        tk.Label(logo_wrap, text="⚡ TechStore", font=("Segoe UI", 15, "bold"),
                 bg=C["panel"], fg=C["accent"]).pack(side="left")
        tk.Label(logo_wrap, text=" — Tecnología al mejor precio",
                 font=self.f_small, bg=C["panel"], fg=C["text_dim"]).pack(side="left", padx=6)

        for txt, cmd in [("📋 Pedidos", self.ventana_pedidos), ("👤 Cuenta", self.ventana_cuenta)]:
            self._btn(header, txt, cmd, C["btn_bg"], C["text"]).pack(side="right", padx=6, pady=12)

        self.lbl_carrito = tk.Label(header, text="🛒 (0)  $0.00",
                                    font=self.f_body, bg=C["highlight"],
                                    fg="white", padx=12, pady=5, cursor="hand2")
        self.lbl_carrito.pack(side="right", padx=8, pady=12)
        self.lbl_carrito.bind("<Button-1>", lambda e: self.ventana_carrito())

        # BODY: sidebar + contenido
        main = tk.Frame(self.root, bg=C["bg"])
        main.pack(fill="both", expand=True)

        # ── SIDEBAR ──
        self.sidebar = tk.Frame(main, bg=C["sidebar"], width=200)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        tk.Label(self.sidebar, text="MENÚ", font=("Segoe UI", 8, "bold"),
                 bg=C["sidebar"], fg=C["text_dim"], padx=18, pady=10).pack(anchor="w")

        self.nav_btns = {}
        for emoji, label, metodo in NAV_ITEMS:
            btn = tk.Button(
                self.sidebar, text=f"  {emoji}  {label}",
                font=("Segoe UI", 10), bg=C["sidebar"], fg=C["text"],
                relief="flat", bd=0, anchor="w", padx=10, pady=9, cursor="hand2",
                activebackground=C["sidebar_sel"], activeforeground=C["accent"],
                command=lambda m=metodo, l=label: self._nav(m, l)
            )
            btn.pack(fill="x")
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg=C["sidebar_sel"], fg=C["accent"]))
            btn.bind("<Leave>", lambda e, b=btn, l=label: b.config(
                bg=C["highlight"] if self.nav_activo.get() == l else C["sidebar"],
                fg="white" if self.nav_activo.get() == l else C["text"]))
            self.nav_btns[label] = btn

        tk.Frame(self.sidebar, bg=C["border"], height=1).pack(fill="x", padx=14, pady=6)
        self._btn(self.sidebar, "  🚪  Cerrar Sesión",
                  lambda: messagebox.showinfo("Sesión", "¡Hasta pronto! 👋"),
                  C["sidebar"], C["danger"]).pack(fill="x", anchor="w")

        # ── PANEL DERECHO ──
        right = tk.Frame(main, bg=C["bg"])
        right.pack(side="left", fill="both", expand=True)

        # Barra filtro/búsqueda
        bar = tk.Frame(right, bg=C["panel"], pady=8)
        bar.pack(fill="x")

        tk.Label(bar, text="🔍", font=("Segoe UI", 11),
                 bg=C["panel"], fg=C["text_dim"]).pack(side="left", padx=(14, 2))
        self.entry_bus = tk.Entry(bar, textvariable=self.busqueda, font=self.f_body,
                                  bg=C["card"], fg=C["text"],
                                  insertbackground=C["accent"], relief="flat", bd=0, width=28)
        self.entry_bus.pack(side="left", ipady=6, ipadx=8, padx=(2, 16))
        self.entry_bus.insert(0, "Buscar producto...")
        self.entry_bus.bind("<FocusIn>",  lambda e: self.entry_bus.delete(0, "end")
                            if self.entry_bus.get() == "Buscar producto..." else None)
        self.entry_bus.bind("<FocusOut>", lambda e: self.entry_bus.insert(0, "Buscar producto...")
                            if self.entry_bus.get() == "" else None)

        tk.Label(bar, text="Cat:", font=self.f_small,
                 bg=C["panel"], fg=C["text_dim"]).pack(side="left")
        cats = ["Todas"] + sorted({p["categoria"] for p in PRODUCTOS})
        self.combo_cat = ttk.Combobox(bar, textvariable=self.filtro_cat,
                                      values=cats, state="readonly",
                                      width=16, font=self.f_body)
        self.combo_cat.pack(side="left", padx=6, ipady=4)
        self.combo_cat.bind("<<ComboboxSelected>>", lambda e: self.refrescar_productos())
        self._btn(bar, "↺", self.limpiar_filtros, C["btn_bg"], C["text_dim"]).pack(side="left", padx=4)

        # Canvas con scroll para los productos
        cont = tk.Frame(right, bg=C["bg"])
        cont.pack(fill="both", expand=True, padx=14, pady=8)

        self.canvas = tk.Canvas(cont, bg=C["bg"], highlightthickness=0)
        sb = ttk.Scrollbar(cont, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.frame_productos = tk.Frame(self.canvas, bg=C["bg"])
        self.canvas_win = self.canvas.create_window((0, 0), window=self.frame_productos, anchor="nw")
        self.frame_productos.bind("<Configure>", lambda e: self.canvas.configure(
            scrollregion=self.canvas.bbox("all")))
        self.canvas.bind("<Configure>", lambda e: self.canvas.itemconfig(
            self.canvas_win, width=e.width))
        self.canvas.bind_all("<MouseWheel>", lambda e: self.canvas.yview_scroll(
            int(-1 * (e.delta / 120)), "units"))

        # Status bar
        self.status_var = tk.StringVar(value="✅ Bienvenido a TechStore")
        tk.Label(self.root, textvariable=self.status_var, font=self.f_small,
                 bg=C["panel"], fg=C["text_dim"], anchor="w",
                 padx=14, pady=4).pack(fill="x", side="bottom")

        self._nav_highlight("Inicio")

    def _nav(self, metodo, label):
        self._nav_highlight(label)
        getattr(self, metodo)()

    def _nav_highlight(self, label):
        self.nav_activo.set(label)
        for lbl, btn in self.nav_btns.items():
            btn.config(bg=C["highlight"] if lbl == label else C["sidebar"],
                       fg="white" if lbl == label else C["text"])

    # ════════════════════════ PRODUCTOS ════════════════════════════════════════
    def mostrar_productos(self):
        self.status_var.set("🛍️ Catálogo de productos")

    def refrescar_productos(self):
        for w in self.frame_productos.winfo_children():
            w.destroy()

        q = self.busqueda.get().lower().strip()
        if q == "buscar producto...": q = ""
        cat = self.filtro_cat.get()

        filtrados = [p for p in PRODUCTOS
                     if (cat == "Todas" or p["categoria"] == cat)
                     and (not q or q in p["nombre"].lower())]

        if not filtrados:
            tk.Label(self.frame_productos, text="😕  Sin resultados",
                     font=self.f_h2, bg=C["bg"], fg=C["text_dim"]).pack(pady=60)
            return

        self.status_var.set(f"🛍️ {len(filtrados)} producto(s) encontrados")
        cols = 4
        for i, prod in enumerate(filtrados):
            r, c = divmod(i, cols)
            self._tarjeta_producto(self.frame_productos, prod, r, c)
            self.frame_productos.columnconfigure(c, weight=1)

    def _tarjeta_producto(self, parent, prod, row, col):
        card = tk.Frame(parent, bg=C["card"], cursor="hand2")
        card.grid(row=row, column=col, padx=7, pady=7, sticky="nsew")

        tk.Label(card, text=prod["emoji"], font=("Segoe UI", 28), bg=C["card"]).pack(pady=(12, 2))
        tk.Label(card, text=prod["nombre"], font=self.f_h3,
                 bg=C["card"], fg=C["text"], wraplength=155).pack()
        tk.Label(card, text=prod["categoria"], font=self.f_small,
                 bg=C["card"], fg=C["text_dim"]).pack()
        stars = "★" * int(prod["rating"]) + "☆" * (5 - int(prod["rating"]))
        tk.Label(card, text=f"{stars} {prod['rating']}", font=("Segoe UI", 9),
                 bg=C["card"], fg=C["warning"]).pack(pady=2)
        tk.Label(card, text=f"${prod['precio']:,.2f}", font=("Segoe UI", 13, "bold"),
                 bg=C["card"], fg=C["accent2"]).pack()
        stk_c = C["accent2"] if prod["stock"] > 10 else C["warning"]
        tk.Label(card, text=f"Stock: {prod['stock']}", font=self.f_small,
                 bg=C["card"], fg=stk_c).pack(pady=(0, 4))

        btns = tk.Frame(card, bg=C["card"])
        btns.pack(pady=(2, 10))
        self._btn(btns, "🛒 Agregar", lambda p=prod: self.agregar_carrito(p),
                  C["highlight"], "white").pack(side="left", padx=4)
        self._btn(btns, "ℹ️", lambda p=prod: self.ventana_detalle(p),
                  C["btn_bg"], C["text_dim"]).pack(side="left")

    # ════════════════════════ SECCIONES SIDEBAR ════════════════════════════════

    # ── INICIO ────────────────────────────────────────────────────────────────
    def ventana_inicio(self):
        win = self._nueva_ventana("🏠 Inicio — TechStore", 700, 530)

        banner = tk.Frame(win, bg=C["highlight"], pady=20)
        banner.pack(fill="x")
        tk.Label(banner, text="⚡ TechStore", font=("Segoe UI", 22, "bold"),
                 bg=C["highlight"], fg="white").pack()
        tk.Label(banner, text="La mejor tecnología al alcance de tu mano",
                 font=self.f_body, bg=C["highlight"], fg="#cce3ff").pack(pady=4)
        self._btn(banner, "🛍️  Ver todos los productos",
                  lambda: [win.destroy(), self._nav_highlight("Productos")],
                  "white", C["highlight"]).pack(pady=8)

        stats_f = tk.Frame(win, bg=C["panel"])
        stats_f.pack(fill="x", pady=12, padx=20)
        for i, (val, lbl, col) in enumerate([
            ("12", "Productos",   C["accent"]),
            ("4",  "Categorías",  C["purple"]),
            ("4",  "Ofertas",     C["danger"]),
            ("5",  "Reseñas ⭐", C["warning"]),
        ]):
            f = tk.Frame(stats_f, bg=C["card"], padx=20, pady=14)
            f.grid(row=0, column=i, padx=6, sticky="ew")
            stats_f.columnconfigure(i, weight=1)
            tk.Label(f, text=val, font=("Segoe UI", 22, "bold"), bg=C["card"], fg=col).pack()
            tk.Label(f, text=lbl, font=self.f_small, bg=C["card"], fg=C["text_dim"]).pack()

        tk.Label(win, text="🌟  Productos Destacados", font=self.f_h2,
                 bg=C["panel"], fg=C["text"]).pack(anchor="w", padx=20, pady=(10, 4))
        dest_f = tk.Frame(win, bg=C["panel"])
        dest_f.pack(fill="x", padx=20)
        top3 = sorted(PRODUCTOS, key=lambda p: p["rating"], reverse=True)[:3]
        for i, p in enumerate(top3):
            f = tk.Frame(dest_f, bg=C["card"], padx=14, pady=10)
            f.grid(row=0, column=i, padx=6, sticky="ew")
            dest_f.columnconfigure(i, weight=1)
            tk.Label(f, text=p["emoji"], font=("Segoe UI", 24), bg=C["card"]).pack()
            tk.Label(f, text=p["nombre"], font=self.f_h3,
                     bg=C["card"], fg=C["text"], wraplength=160).pack()
            tk.Label(f, text=f"${p['precio']:,.2f}", font=self.f_body,
                     bg=C["card"], fg=C["accent2"]).pack()
            self._btn(f, "Ver", lambda p=p: [win.destroy(), self.ventana_detalle(p)],
                      C["highlight"], "white").pack(pady=(6, 0))

        self._btn(win, "Cerrar", win.destroy, C["btn_bg"], C["text"]).pack(pady=14)

    # ── OFERTAS ───────────────────────────────────────────────────────────────
    def ventana_ofertas(self):
        win = self._nueva_ventana("🔥 Ofertas Especiales", 640, 500)

        banner = tk.Frame(win, bg="#3d0a0a", pady=12)
        banner.pack(fill="x")
        tk.Label(banner, text="🔥  OFERTAS POR TIEMPO LIMITADO",
                 font=("Segoe UI", 14, "bold"), bg="#3d0a0a", fg=C["danger"]).pack()
        tk.Label(banner, text="¡Descuentos exclusivos — solo por hoy!",
                 font=self.f_small, bg="#3d0a0a", fg="#ffaaaa").pack()

        for oferta in OFERTAS:
            prod = next(p for p in PRODUCTOS if p["id"] == oferta["prod_id"])
            precio_orig = prod["precio"]
            precio_desc = precio_orig * (1 - oferta["descuento"] / 100)

            row = tk.Frame(win, bg=C["card"], pady=10)
            row.pack(fill="x", padx=18, pady=5)

            tk.Label(row, text=prod["emoji"], font=("Segoe UI", 28), bg=C["card"]).pack(side="left", padx=12)

            info = tk.Frame(row, bg=C["card"])
            info.pack(side="left", fill="x", expand=True)
            tk.Label(info, text=prod["nombre"], font=self.f_h3,
                     bg=C["card"], fg=C["text"], anchor="w").pack(anchor="w")
            tk.Label(info, text=f"Precio original: ${precio_orig:,.2f}",
                     font=self.f_small, bg=C["card"], fg=C["text_dim"]).pack(anchor="w")
            tk.Label(info, text=f"Precio oferta:   ${precio_desc:,.2f}",
                     font=("Segoe UI", 11, "bold"), bg=C["card"], fg=C["accent2"]).pack(anchor="w")

            right_f = tk.Frame(row, bg=C["card"])
            right_f.pack(side="right", padx=12)
            tk.Label(right_f, text=f"-{oferta['descuento']}%",
                     font=("Segoe UI", 16, "bold"), bg=C["danger"],
                     fg="white", padx=8, pady=4).pack()
            tk.Label(right_f, text=oferta["etiqueta"], font=self.f_small,
                     bg=C["card"], fg=C["warning"]).pack(pady=4)
            self._btn(right_f, "🛒 Agregar",
                      lambda p=prod: [self.agregar_carrito(p), win.destroy()],
                      C["highlight"], "white").pack()

        self._btn(win, "Cerrar", win.destroy, C["btn_bg"], C["text"]).pack(pady=12)

    # ── CATEGORÍAS ────────────────────────────────────────────────────────────
    def ventana_categorias(self):
        win = self._nueva_ventana("📦 Categorías", 580, 440)
        tk.Label(win, text="📦  Explorar por Categoría", font=self.f_h2,
                 bg=C["panel"], fg=C["accent"]).pack(pady=14)

        cats = sorted({p["categoria"] for p in PRODUCTOS})
        icons  = {"Electrónica": "💻", "Audio": "🎵", "Accesorios": "🔧", "Almacenamiento": "💾"}
        colors = [C["accent"], C["accent2"], C["purple"], C["orange"]]

        grid = tk.Frame(win, bg=C["panel"])
        grid.pack(padx=20, fill="both", expand=True)

        for i, cat in enumerate(cats):
            prods_cat = [p for p in PRODUCTOS if p["categoria"] == cat]
            col = colors[i % len(colors)]

            card = tk.Frame(grid, bg=C["card"], cursor="hand2", padx=20, pady=18)
            card.grid(row=i // 2, column=i % 2, padx=10, pady=10, sticky="nsew")
            grid.columnconfigure(i % 2, weight=1)

            tk.Label(card, text=icons.get(cat, "📁"), font=("Segoe UI", 32), bg=C["card"]).pack()
            tk.Label(card, text=cat, font=self.f_h2, bg=C["card"], fg=col).pack()
            tk.Label(card, text=f"{len(prods_cat)} productos disponibles",
                     font=self.f_small, bg=C["card"], fg=C["text_dim"]).pack(pady=2)

            def ver_cat(c=cat, w=win):
                self.filtro_cat.set(c)
                self.refrescar_productos()
                self._nav_highlight("Productos")
                w.destroy()

            self._btn(card, f"Ver {cat}", ver_cat, C["btn_bg"], col).pack(pady=(8, 0))

        self._btn(win, "Cerrar", win.destroy, C["btn_bg"], C["text"]).pack(pady=12)

    # ── RESEÑAS ───────────────────────────────────────────────────────────────
    def ventana_reseñas(self):
        win = self._nueva_ventana("⭐ Reseñas de Clientes", 640, 520)
        tk.Label(win, text="⭐  Reseñas de Clientes", font=self.f_h2,
                 bg=C["panel"], fg=C["accent"]).pack(pady=14)

        canvas_r = tk.Canvas(win, bg=C["panel"], highlightthickness=0)
        sb = ttk.Scrollbar(win, orient="vertical", command=canvas_r.yview)
        canvas_r.configure(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y")
        canvas_r.pack(side="left", fill="both", expand=True)

        frame_r = tk.Frame(canvas_r, bg=C["panel"])
        cw = canvas_r.create_window((0, 0), window=frame_r, anchor="nw")
        frame_r.bind("<Configure>", lambda e: canvas_r.configure(scrollregion=canvas_r.bbox("all")))
        canvas_r.bind("<Configure>", lambda e: canvas_r.itemconfig(cw, width=e.width))

        for r in RESEÑAS:
            card = tk.Frame(frame_r, bg=C["card"], pady=10)
            card.pack(fill="x", padx=18, pady=5)
            top = tk.Frame(card, bg=C["card"])
            top.pack(fill="x", padx=12)
            tk.Label(top, text=f"👤 {r['usuario']}", font=self.f_h3,
                     bg=C["card"], fg=C["accent"]).pack(side="left")
            stars = "★" * r["estrellas"] + "☆" * (5 - r["estrellas"])
            tk.Label(top, text=stars, font=("Segoe UI", 11),
                     bg=C["card"], fg=C["warning"]).pack(side="right")
            tk.Label(card, text=f"Producto: {r['producto']}", font=self.f_small,
                     bg=C["card"], fg=C["text_dim"], anchor="w").pack(fill="x", padx=12)
            tk.Label(card, text=f'"{r["comentario"]}"', font=self.f_body,
                     bg=C["card"], fg=C["text"], wraplength=540,
                     justify="left", anchor="w").pack(fill="x", padx=12, pady=(4, 0))

        tk.Frame(frame_r, bg=C["border"], height=1).pack(fill="x", padx=18, pady=8)
        self._btn(frame_r, "✍️  Escribir una Reseña",
                  lambda: self._form_reseña(win), C["highlight"], "white").pack(pady=4)
        self._btn(frame_r, "Cerrar", win.destroy, C["btn_bg"], C["text"]).pack(pady=6)

    def _form_reseña(self, parent_win):
        win = self._nueva_ventana("✍️ Escribir Reseña", 420, 360)
        tk.Label(win, text="✍️  Nueva Reseña", font=self.f_h2,
                 bg=C["panel"], fg=C["accent"]).pack(pady=12)

        form = tk.Frame(win, bg=C["panel"])
        form.pack(padx=24, fill="x")
        form.columnconfigure(0, weight=1)

        def lf(txt, row):
            tk.Label(form, text=txt, font=self.f_small, bg=C["panel"],
                     fg=C["text_dim"], anchor="w").grid(row=row*2, column=0, sticky="w", pady=(8,0))
            e = tk.Entry(form, font=self.f_body, bg=C["card"], fg=C["text"],
                         insertbackground=C["accent"], relief="flat", bd=0)
            e.grid(row=row*2+1, column=0, sticky="ew", ipady=6, ipadx=8)
            return e

        e_nombre = lf("Tu nombre", 0)
        e_prod   = lf("Producto",  1)

        tk.Label(form, text="Calificación (1-5)", font=self.f_small,
                 bg=C["panel"], fg=C["text_dim"], anchor="w").grid(row=4, column=0, sticky="w", pady=(8,0))
        estrellas_var = tk.IntVar(value=5)
        sf = tk.Frame(form, bg=C["panel"])
        sf.grid(row=5, column=0, sticky="w")
        for n in range(1, 6):
            tk.Radiobutton(sf, text=str(n)+"★", variable=estrellas_var, value=n,
                           font=self.f_small, bg=C["panel"], fg=C["warning"],
                           selectcolor=C["card"], activebackground=C["panel"]).pack(side="left")

        tk.Label(form, text="Comentario", font=self.f_small,
                 bg=C["panel"], fg=C["text_dim"], anchor="w").grid(row=6, column=0, sticky="w", pady=(8,0))
        txt = tk.Text(form, font=self.f_body, bg=C["card"], fg=C["text"],
                      insertbackground=C["accent"], relief="flat", bd=0,
                      height=3, wrap="word")
        txt.grid(row=7, column=0, sticky="ew", ipadx=8)

        def enviar():
            if not e_nombre.get().strip() or not e_prod.get().strip():
                messagebox.showwarning("Incompleto", "Llena todos los campos.", parent=win)
                return
            RESEÑAS.append({"usuario": e_nombre.get().strip(), "producto": e_prod.get().strip(),
                             "estrellas": estrellas_var.get(),
                             "comentario": txt.get("1.0", "end").strip()})
            messagebox.showinfo("¡Gracias!", "Tu reseña fue publicada. ⭐", parent=win)
            win.destroy()
            self.status_var.set("⭐ ¡Reseña publicada!")

        self._btn(win, "📤 Publicar Reseña", enviar, C["accent2"], "white").pack(pady=12)

    # ── CUPONES ───────────────────────────────────────────────────────────────
    def ventana_cupones(self):
        win = self._nueva_ventana("🎫 Mis Cupones", 520, 420)
        tk.Label(win, text="🎫  Cupones y Descuentos", font=self.f_h2,
                 bg=C["panel"], fg=C["accent"]).pack(pady=14)

        cupones = [
            {"codigo": "TECH20",   "desc": "20% en Electrónica",  "expira": "31/03/2025", "activo": True},
            {"codigo": "AUDIO15",  "desc": "15% en Audio",         "expira": "15/04/2025", "activo": True},
            {"codigo": "FLETE0",   "desc": "Envío gratis",         "expira": "28/02/2025", "activo": False},
            {"codigo": "GAMING10", "desc": "10% en Accesorios",    "expira": "01/05/2025", "activo": True},
        ]

        for cu in cupones:
            row = tk.Frame(win, bg=C["card"], pady=10)
            row.pack(fill="x", padx=18, pady=5)
            col = C["accent2"] if cu["activo"] else C["text_dim"]
            left = tk.Frame(row, bg=C["card"])
            left.pack(side="left", padx=12)
            tk.Label(left, text=cu["codigo"], font=("Consolas", 14, "bold"),
                     bg=C["card"], fg=col).pack(anchor="w")
            tk.Label(left, text=cu["desc"], font=self.f_body,
                     bg=C["card"], fg=C["text"]).pack(anchor="w")
            tk.Label(left, text=f"Expira: {cu['expira']}", font=self.f_small,
                     bg=C["card"], fg=C["text_dim"]).pack(anchor="w")
            estado = "✅ Activo" if cu["activo"] else "❌ Expirado"
            tk.Label(row, text=estado, font=self.f_small, bg=C["card"],
                     fg=C["accent2"] if cu["activo"] else C["danger"]).pack(side="right", padx=16)

        tk.Frame(win, bg=C["border"], height=1).pack(fill="x", padx=18, pady=8)
        tk.Label(win, text="Canjear código:", font=self.f_small,
                 bg=C["panel"], fg=C["text_dim"]).pack()

        row_c = tk.Frame(win, bg=C["panel"])
        row_c.pack(pady=6)
        e_cod = tk.Entry(row_c, font=self.f_mono, bg=C["card"], fg=C["accent"],
                         insertbackground=C["accent"], relief="flat", bd=0, width=18)
        e_cod.pack(side="left", ipady=6, ipadx=8, padx=6)

        def canjear():
            cod = e_cod.get().strip().upper()
            valido = next((c for c in cupones if c["codigo"] == cod and c["activo"]), None)
            if valido:
                messagebox.showinfo("¡Cupón válido!", f"✅ {valido['desc']} aplicado.", parent=win)
            else:
                messagebox.showerror("Inválido", "Código no encontrado o expirado.", parent=win)

        self._btn(row_c, "Canjear", canjear, C["highlight"], "white").pack(side="left")
        self._btn(win, "Cerrar", win.destroy, C["btn_bg"], C["text"]).pack(pady=8)

    # ── ENVÍOS ────────────────────────────────────────────────────────────────
    def ventana_envios(self):
        win = self._nueva_ventana("🚚 Envíos", 560, 480)
        tk.Label(win, text="🚚  Información de Envíos", font=self.f_h2,
                 bg=C["panel"], fg=C["accent"]).pack(pady=14)

        for nombre, tiempo, precio, col in [
            ("🚀 Express",   "1-2 días hábiles",  "$149.00", C["danger"]),
            ("📦 Estándar",  "3-5 días hábiles",  "$59.00",  C["accent"]),
            ("🐢 Económico", "7-10 días hábiles", "GRATIS",  C["accent2"]),
        ]:
            card = tk.Frame(win, bg=C["card"], pady=12)
            card.pack(fill="x", padx=20, pady=6)
            tk.Label(card, text=nombre, font=self.f_h2, bg=C["card"], fg=col).pack(side="left", padx=16)
            tk.Label(card, text=tiempo, font=self.f_body, bg=C["card"], fg=C["text"]).pack(side="left", padx=8)
            tk.Label(card, text=precio, font=("Segoe UI", 12, "bold"),
                     bg=C["card"], fg=col).pack(side="right", padx=16)

        tk.Frame(win, bg=C["border"], height=1).pack(fill="x", padx=20, pady=10)
        tk.Label(win, text="📍  Rastrear mi Pedido", font=self.f_h3,
                 bg=C["panel"], fg=C["text"]).pack()
        tk.Label(win, text="Ingresa tu número de orden:", font=self.f_small,
                 bg=C["panel"], fg=C["text_dim"]).pack(pady=(6, 2))

        row_r = tk.Frame(win, bg=C["panel"])
        row_r.pack()
        e_orden = tk.Entry(row_r, font=self.f_mono, bg=C["card"], fg=C["accent"],
                           insertbackground=C["accent"], relief="flat", bd=0, width=20)
        e_orden.pack(side="left", ipady=6, ipadx=8, padx=6)

        def rastrear():
            if not e_orden.get().strip():
                messagebox.showwarning("Vacío", "Ingresa un número de orden.", parent=win)
                return
            estado = random.choice(["📦 En bodega", "🚚 En camino", "🏠 Entregado", "⏳ En proceso"])
            messagebox.showinfo("Estado", f"Orden: {e_orden.get().strip()}\n\nEstado: {estado}", parent=win)

        self._btn(row_r, "🔍 Rastrear", rastrear, C["highlight"], "white").pack(side="left")
        tk.Label(win, text="Cobertura: Todo México · Envío internacional disponible",
                 font=self.f_small, bg=C["panel"], fg=C["text_dim"]).pack(pady=14)
        self._btn(win, "Cerrar", win.destroy, C["btn_bg"], C["text"]).pack(pady=4)

    # ── NEWSLETTER ────────────────────────────────────────────────────────────
    def ventana_newsletter(self):
        win = self._nueva_ventana("🔔 Newsletter", 460, 380)
        tk.Label(win, text="🔔  Suscríbete al Newsletter", font=self.f_h2,
                 bg=C["panel"], fg=C["accent"]).pack(pady=14)
        tk.Label(win, text="Recibe ofertas exclusivas, novedades y\ncupones directamente en tu correo.",
                 font=self.f_body, bg=C["panel"], fg=C["text"], justify="center").pack(pady=6)

        form = tk.Frame(win, bg=C["panel"])
        form.pack(padx=30, fill="x", pady=8)
        form.columnconfigure(0, weight=1)

        def lf(lbl, row):
            tk.Label(form, text=lbl, font=self.f_small, bg=C["panel"],
                     fg=C["text_dim"], anchor="w").grid(row=row*2, column=0, sticky="w", pady=(8,0))
            e = tk.Entry(form, font=self.f_body, bg=C["card"], fg=C["text"],
                         insertbackground=C["accent"], relief="flat", bd=0)
            e.grid(row=row*2+1, column=0, sticky="ew", ipady=7, ipadx=8)
            return e

        e_nombre = lf("Tu nombre", 0)
        e_email  = lf("Tu correo", 1)

        tk.Label(form, text="Preferencias (opcional):", font=self.f_small,
                 bg=C["panel"], fg=C["text_dim"], anchor="w").grid(row=4, column=0, sticky="w", pady=(8,2))
        prefs = {}
        pf = tk.Frame(form, bg=C["panel"])
        pf.grid(row=5, column=0, sticky="w")
        for p in ["Electrónica", "Audio", "Accesorios", "Ofertas"]:
            v = tk.BooleanVar()
            prefs[p] = v
            tk.Checkbutton(pf, text=p, variable=v, font=self.f_small,
                           bg=C["panel"], fg=C["text"], selectcolor=C["card"],
                           activebackground=C["panel"], cursor="hand2").pack(side="left", padx=4)

        def suscribir():
            if not e_email.get().strip() or "@" not in e_email.get():
                messagebox.showwarning("Email inválido", "Ingresa un correo válido.", parent=win)
                return
            sel = [k for k, v in prefs.items() if v.get()]
            msg = f"✅ Suscripción exitosa!\n\nCorreo: {e_email.get().strip()}"
            if sel: msg += f"\nIntereses: {', '.join(sel)}"
            messagebox.showinfo("¡Listo!", msg, parent=win)
            win.destroy()
            self.status_var.set("🔔 ¡Suscripción al newsletter exitosa!")

        self._btn(win, "📧  Suscribirme", suscribir, C["highlight"], "white").pack(pady=14)
        self._btn(win, "Ahora no", win.destroy, C["btn_bg"], C["text_dim"]).pack()

    # ── SOPORTE ───────────────────────────────────────────────────────────────
    def ventana_soporte(self):
        win = self._nueva_ventana("🛠️ Soporte", 540, 500)
        tk.Label(win, text="🛠️  Centro de Soporte", font=self.f_h2,
                 bg=C["panel"], fg=C["accent"]).pack(pady=14)

        for ico, nombre, detalle in [
            ("💬", "Chat en vivo",       "Tiempo promedio: 2 min"),
            ("📧", "Correo",             "Respuesta en 24 hrs"),
            ("📞", "Teléfono",           "+52 800-TECH-123"),
            ("❓", "Preguntas Frecuentes","Base de conocimientos"),
        ]:
            row = tk.Frame(win, bg=C["card"], pady=10, cursor="hand2")
            row.pack(fill="x", padx=18, pady=4)
            tk.Label(row, text=ico, font=("Segoe UI", 20), bg=C["card"]).pack(side="left", padx=14)
            info = tk.Frame(row, bg=C["card"])
            info.pack(side="left", fill="x", expand=True)
            tk.Label(info, text=nombre, font=self.f_h3, bg=C["card"],
                     fg=C["text"], anchor="w").pack(anchor="w")
            tk.Label(info, text=detalle, font=self.f_small, bg=C["card"],
                     fg=C["text_dim"], anchor="w").pack(anchor="w")
            self._btn(row, "Contactar",
                      lambda n=nombre: messagebox.showinfo("Soporte",
                          f"Conectando con {n}...", parent=win),
                      C["btn_bg"], C["accent"]).pack(side="right", padx=12)

        tk.Frame(win, bg=C["border"], height=1).pack(fill="x", padx=18, pady=10)
        tk.Label(win, text="📝  Enviar Ticket de Soporte", font=self.f_h3,
                 bg=C["panel"], fg=C["text"]).pack()

        form = tk.Frame(win, bg=C["panel"])
        form.pack(padx=20, fill="x", pady=6)
        form.columnconfigure(1, weight=1)

        for i, lbl in enumerate(["Asunto:", "Descripción:"]):
            tk.Label(form, text=lbl, font=self.f_small, bg=C["panel"],
                     fg=C["text_dim"]).grid(row=i, column=0, sticky="w", padx=4, pady=4)

        e_asunto = tk.Entry(form, font=self.f_body, bg=C["card"], fg=C["text"],
                            insertbackground=C["accent"], relief="flat", bd=0)
        e_asunto.grid(row=0, column=1, sticky="ew", ipady=6, ipadx=8)

        e_desc = tk.Text(form, font=self.f_body, bg=C["card"], fg=C["text"],
                         insertbackground=C["accent"], relief="flat", bd=0, height=3, wrap="word")
        e_desc.grid(row=1, column=1, sticky="ew", ipadx=8, pady=4)

        def enviar_ticket():
            if not e_asunto.get().strip():
                messagebox.showwarning("Campo vacío", "Escribe un asunto.", parent=win)
                return
            num = random.randint(10000, 99999)
            messagebox.showinfo("Ticket enviado",
                f"✅ Ticket #{num} creado.\nResponderemos en menos de 24 horas.", parent=win)
            win.destroy()
            self.status_var.set(f"🛠️ Ticket #{num} enviado")

        self._btn(win, "📤 Enviar Ticket", enviar_ticket, C["highlight"], "white").pack(pady=8)

    # ── AJUSTES ───────────────────────────────────────────────────────────────
    def ventana_ajustes(self):
        win = self._nueva_ventana("⚙️ Ajustes", 500, 480)
        tk.Label(win, text="⚙️  Ajustes de la Aplicación", font=self.f_h2,
                 bg=C["panel"], fg=C["accent"]).pack(pady=14)

        form = tk.Frame(win, bg=C["panel"])
        form.pack(padx=24, fill="x")
        form.columnconfigure(1, weight=1)

        opciones = {
            "Notificaciones":    tk.BooleanVar(value=True),
            "Ofertas por email": tk.BooleanVar(value=True),
            "Modo oscuro":       tk.BooleanVar(value=True),
            "Sonidos":           tk.BooleanVar(value=False),
        }
        for i, (lbl, var) in enumerate(opciones.items()):
            tk.Label(form, text=lbl, font=self.f_body, bg=C["panel"],
                     fg=C["text"], anchor="w").grid(row=i, column=0, sticky="w", pady=8, padx=6)
            tk.Checkbutton(form, variable=var, bg=C["panel"],
                           selectcolor=C["card"], activebackground=C["panel"],
                           cursor="hand2").grid(row=i, column=1, sticky="e")

        n = len(opciones)
        tk.Frame(form, bg=C["border"], height=1).grid(row=n, column=0, columnspan=2, sticky="ew", pady=10)

        tk.Label(form, text="Idioma:", font=self.f_body, bg=C["panel"],
                 fg=C["text"], anchor="w").grid(row=n+1, column=0, sticky="w", padx=6, pady=4)
        lang_var = tk.StringVar(value="Español")
        ttk.Combobox(form, textvariable=lang_var, state="readonly",
                     values=["Español", "English", "Français", "Deutsch"],
                     width=18, font=self.f_body).grid(row=n+1, column=1, sticky="e", ipady=4)

        tk.Label(form, text="Moneda:", font=self.f_body, bg=C["panel"],
                 fg=C["text"], anchor="w").grid(row=n+2, column=0, sticky="w", padx=6, pady=4)
        cur_var = tk.StringVar(value="MXN — Peso Mexicano")
        ttk.Combobox(form, textvariable=cur_var, state="readonly",
                     values=["MXN — Peso Mexicano", "USD — Dólar", "EUR — Euro"],
                     width=22, font=self.f_body).grid(row=n+2, column=1, sticky="e", ipady=4)

        tk.Frame(form, bg=C["border"], height=1).grid(row=n+3, column=0, columnspan=2, sticky="ew", pady=10)
        tk.Label(form, text="⚠️ Zona de Peligro", font=self.f_h3,
                 bg=C["panel"], fg=C["warning"]).grid(row=n+4, column=0, columnspan=2, sticky="w", padx=6)

        btns_d = tk.Frame(form, bg=C["panel"])
        btns_d.grid(row=n+5, column=0, columnspan=2, sticky="w", pady=8)
        self._btn(btns_d, "🗑 Borrar datos",
                  lambda: messagebox.askyesno("Confirmar", "¿Borrar todos los datos?", parent=win),
                  C["btn_bg"], C["danger"]).pack(side="left", padx=6)
        self._btn(btns_d, "🔑 Cambiar contraseña",
                  lambda: messagebox.showinfo("Contraseña", "Enlace enviado a tu correo.", parent=win),
                  C["btn_bg"], C["warning"]).pack(side="left")

        btns_f = tk.Frame(win, bg=C["panel"])
        btns_f.pack(pady=12)
        self._btn(btns_f, "💾 Guardar",
                  lambda: [messagebox.showinfo("OK", "✅ Ajustes guardados.", parent=win),
                           self.status_var.set("⚙️ Ajustes actualizados")],
                  C["accent2"], "white").pack(side="left", padx=8)
        self._btn(btns_f, "Cancelar", win.destroy, C["btn_bg"], C["text"]).pack(side="left")

    # ════════════════════════ CARRITO ════════════════════════════════════════
    def agregar_carrito(self, prod):
        self.carrito[prod["id"]] = self.carrito.get(prod["id"], 0) + 1
        self.actualizar_badge()
        self.status_var.set(f"✅ '{prod['nombre']}' agregado al carrito")

    def actualizar_badge(self):
        items = sum(self.carrito.values())
        total = sum(next(p["precio"] for p in PRODUCTOS if p["id"] == pid) * qty
                    for pid, qty in self.carrito.items())
        self.lbl_carrito.config(text=f"🛒 ({items})  ${total:,.2f}")

    def ventana_carrito(self):
        win = self._nueva_ventana("🛒 Mi Carrito", 520, 500)
        tk.Label(win, text="🛒  Tu Carrito", font=self.f_h2,
                 bg=C["panel"], fg=C["accent"]).pack(pady=14)

        if not self.carrito:
            tk.Label(win, text="😕 Carrito vacío", font=self.f_body,
                     bg=C["panel"], fg=C["text_dim"]).pack(pady=30)
            return

        total = 0
        for pid, qty in list(self.carrito.items()):
            prod = next(p for p in PRODUCTOS if p["id"] == pid)
            subtotal = prod["precio"] * qty
            total += subtotal

            row = tk.Frame(win, bg=C["card"], pady=6)
            row.pack(fill="x", padx=16, pady=3)
            tk.Label(row, text=f"{prod['emoji']} {prod['nombre']}",
                     font=self.f_body, bg=C["card"], fg=C["text"],
                     width=22, anchor="w").pack(side="left", padx=8)
            tk.Label(row, text=f"${prod['precio']:,.2f}", font=self.f_small,
                     bg=C["card"], fg=C["text_dim"]).pack(side="left")
            lbl_qty = tk.Label(row, text=str(qty), font=self.f_mono,
                               bg=C["btn_bg"], fg=C["text"], width=3)
            lbl_qty.pack(side="left", padx=6)

            def cambiar(delta, p=prod, lbl=lbl_qty):
                nueva = self.carrito.get(p["id"], 0) + delta
                if nueva <= 0:
                    del self.carrito[p["id"]]
                    self.actualizar_badge()
                    win.destroy(); self.ventana_carrito()
                else:
                    self.carrito[p["id"]] = nueva
                    lbl.config(text=str(nueva))
                    self.actualizar_badge()

            self._btn(row, "−", lambda p=prod: cambiar(-1, p), C["danger"], "white").pack(side="left")
            self._btn(row, "+", lambda p=prod: cambiar( 1, p), C["accent2"],"white").pack(side="left", padx=2)
            tk.Label(row, text=f"=${subtotal:,.2f}", font=("Segoe UI", 10, "bold"),
                     bg=C["card"], fg=C["accent2"]).pack(side="left", padx=6)

        tk.Frame(win, bg=C["border"], height=1).pack(fill="x", padx=16, pady=6)
        tk.Label(win, text=f"TOTAL: ${total:,.2f}", font=("Segoe UI", 14, "bold"),
                 bg=C["panel"], fg=C["accent"]).pack()

        btns = tk.Frame(win, bg=C["panel"])
        btns.pack(pady=12)
        self._btn(btns, "🗑 Vaciar",
                  lambda: [self.carrito.clear(), self.actualizar_badge(), win.destroy()],
                  C["danger"], "white").pack(side="left", padx=8)
        self._btn(btns, "💳 Pagar",
                  lambda: [win.destroy(), self.ventana_checkout(total)],
                  C["highlight"], "white").pack(side="left")

    def ventana_checkout(self, total):
        win = self._nueva_ventana("💳 Pago", 480, 560)
        tk.Label(win, text="💳  Finalizar Compra", font=self.f_h2,
                 bg=C["panel"], fg=C["accent"]).pack(pady=14)

        form = tk.Frame(win, bg=C["panel"])
        form.pack(padx=24, fill="x")
        form.columnconfigure(0, weight=1)
        campos = {}

        def lf(lbl, row, show=""):
            tk.Label(form, text=lbl, font=self.f_small, bg=C["panel"],
                     fg=C["text_dim"], anchor="w").grid(row=row*2, column=0, sticky="w", pady=(8,0))
            e = tk.Entry(form, font=self.f_body, bg=C["card"], fg=C["text"],
                         insertbackground=C["accent"], relief="flat", bd=0, show=show)
            e.grid(row=row*2+1, column=0, sticky="ew", ipady=7, ipadx=8)
            campos[lbl] = e

        lf("📧 Correo",          0)
        lf("👤 Nombre completo", 1)
        lf("🏠 Dirección",       2)
        lf("💳 Número tarjeta",  3)
        lf("📅 Fecha (MM/AA)",   4)
        lf("🔒 CVV",             5, show="•")

        tk.Label(form, text="Método de pago", font=self.f_small, bg=C["panel"],
                 fg=C["text_dim"], anchor="w").grid(row=12, column=0, sticky="w", pady=(8,0))
        metodo = tk.StringVar(value="Tarjeta")
        ttk.Combobox(form, textvariable=metodo, state="readonly",
                     values=["Tarjeta", "PayPal", "Transferencia", "Cripto"],
                     font=self.f_body).grid(row=13, column=0, sticky="ew", ipady=4)

        tk.Frame(win, bg=C["border"], height=1).pack(fill="x", padx=24, pady=8)
        tk.Label(win, text=f"Total: ${total:,.2f}", font=("Segoe UI", 13, "bold"),
                 bg=C["panel"], fg=C["accent2"]).pack()

        def confirmar():
            if any(not v.get().strip() for v in campos.values()):
                messagebox.showwarning("Campos vacíos", "Completa todos los campos.", parent=win)
                return
            win.destroy()
            self.carrito.clear()
            self.actualizar_badge()
            self.ventana_confirmacion(total, metodo.get())

        self._btn(win, f"✅  CONFIRMAR PAGO  ${total:,.2f}", confirmar,
                  C["accent2"], "white", width=30).pack(pady=12)

    def ventana_confirmacion(self, total, metodo):
        win = self._nueva_ventana("✅ Pedido Confirmado", 420, 300)
        num = random.randint(100000, 999999)
        tk.Label(win, text="🎉", font=("Segoe UI", 40), bg=C["panel"]).pack(pady=8)
        tk.Label(win, text="¡Pedido Confirmado!", font=("Segoe UI", 16, "bold"),
                 bg=C["panel"], fg=C["accent2"]).pack()
        tk.Label(win, text=f"Orden #{num}", font=self.f_mono,
                 bg=C["panel"], fg=C["text_dim"]).pack(pady=4)
        tk.Label(win, text=f"${total:,.2f} vía {metodo}", font=self.f_body,
                 bg=C["panel"], fg=C["text"]).pack()
        tk.Label(win, text="📦 Llegará en 3-5 días hábiles", font=self.f_small,
                 bg=C["panel"], fg=C["text_dim"]).pack(pady=6)
        self._btn(win, "Cerrar", win.destroy, C["btn_bg"], C["text"]).pack(pady=12)
        self.status_var.set(f"✅ Orden #{num} confirmada — ${total:,.2f}")

    # ════════════════════════ OTRAS VENTANAS ════════════════════════════════
    def ventana_detalle(self, prod):
        win = self._nueva_ventana(f"ℹ️ {prod['nombre']}", 400, 340)
        tk.Label(win, text=prod["emoji"], font=("Segoe UI", 50), bg=C["panel"]).pack(pady=10)
        tk.Label(win, text=prod["nombre"], font=self.f_h2, bg=C["panel"], fg=C["text"]).pack()
        tk.Label(win, text=prod["categoria"], font=self.f_small, bg=C["panel"], fg=C["text_dim"]).pack()
        stars = "★" * int(prod["rating"]) + "☆" * (5 - int(prod["rating"]))
        tk.Label(win, text=f"{stars} {prod['rating']}", font=("Segoe UI", 11),
                 bg=C["panel"], fg=C["warning"]).pack(pady=2)

        info = tk.Frame(win, bg=C["card"], padx=20, pady=10)
        info.pack(fill="x", padx=20, pady=8)
        for lbl, val, col in [
            ("Precio:", f"${prod['precio']:,.2f}", C["accent2"]),
            ("Stock:",  f"{prod['stock']} uds.",  C["accent"]),
            ("ID:",     f"#{prod['id']}",          C["text_dim"]),
        ]:
            r = tk.Frame(info, bg=C["card"]); r.pack(fill="x", pady=2)
            tk.Label(r, text=lbl, font=self.f_small, bg=C["card"],
                     fg=C["text_dim"], width=10, anchor="w").pack(side="left")
            tk.Label(r, text=val, font=("Segoe UI", 10, "bold"),
                     bg=C["card"], fg=col).pack(side="left")

        btns = tk.Frame(win, bg=C["panel"]); btns.pack()
        self._btn(btns, "🛒 Agregar",
                  lambda: [self.agregar_carrito(prod), win.destroy()],
                  C["highlight"], "white").pack(side="left", padx=6)
        self._btn(btns, "Cerrar", win.destroy, C["btn_bg"], C["text"]).pack(side="left")

    def ventana_pedidos(self):
        win = self._nueva_ventana("📋 Mis Pedidos", 540, 360)
        tk.Label(win, text="📋  Historial de Pedidos", font=self.f_h2,
                 bg=C["panel"], fg=C["accent"]).pack(pady=14)
        for p in [
            {"id": "ORD-884512", "fecha": "2024-11-20", "total": 1449.98, "estado": "Entregado",  "items": 2},
            {"id": "ORD-771034", "fecha": "2024-10-05", "total":  899.00, "estado": "En camino",  "items": 1},
            {"id": "ORD-654289", "fecha": "2024-09-14", "total":  239.98, "estado": "En proceso", "items": 3},
        ]:
            row = tk.Frame(win, bg=C["card"], pady=8)
            row.pack(fill="x", padx=16, pady=4)
            col = {"Entregado": C["accent2"], "En camino": C["accent"],
                   "En proceso": C["warning"]}.get(p["estado"], C["text"])
            tk.Label(row, text=p["id"], font=self.f_mono, bg=C["card"],
                     fg=C["text"], width=14, anchor="w").pack(side="left", padx=10)
            tk.Label(row, text=p["fecha"], font=self.f_small,
                     bg=C["card"], fg=C["text_dim"]).pack(side="left", padx=8)
            tk.Label(row, text=f"${p['total']:,.2f}", font=("Segoe UI", 10, "bold"),
                     bg=C["card"], fg=C["accent2"]).pack(side="left", padx=10)
            tk.Label(row, text=p["estado"], font=self.f_small,
                     bg=C["card"], fg=col).pack(side="right", padx=12)
        self._btn(win, "Cerrar", win.destroy, C["btn_bg"], C["text"]).pack(pady=14)

    def ventana_cuenta(self):
        win = self._nueva_ventana("👤 Mi Cuenta", 420, 400)
        tk.Label(win, text="👤  Mi Cuenta", font=self.f_h2,
                 bg=C["panel"], fg=C["accent"]).pack(pady=14)
        form = tk.Frame(win, bg=C["panel"])
        form.pack(padx=30, fill="x")
        form.columnconfigure(0, weight=1)
        for i, (lbl, val) in enumerate([
            ("Nombre:", "Juan Pérez"), ("Email:", "juan@email.com"),
            ("Teléfono:", "+52 555-123-4567"), ("Ciudad:", "Ciudad de México"),
        ]):
            tk.Label(form, text=lbl, font=self.f_small, bg=C["panel"],
                     fg=C["text_dim"], anchor="w").grid(row=i*2, column=0, sticky="w", pady=(10,0))
            e = tk.Entry(form, font=self.f_body, bg=C["card"], fg=C["text"],
                         insertbackground=C["accent"], relief="flat", bd=0)
            e.insert(0, val)
            e.grid(row=i*2+1, column=0, sticky="ew", ipady=7, ipadx=8)

        btns = tk.Frame(win, bg=C["panel"]); btns.pack(pady=14)
        self._btn(btns, "💾 Guardar",
                  lambda: messagebox.showinfo("OK", "✅ Datos actualizados", parent=win),
                  C["highlight"], "white").pack(side="left", padx=6)
        self._btn(btns, "🚪 Cerrar Sesión",
                  lambda: messagebox.showinfo("Sesión", "¡Hasta pronto! 👋", parent=win),
                  C["danger"], "white").pack(side="left")

    # ════════════════════════ HELPERS ════════════════════════════════════════
    def limpiar_filtros(self):
        self.filtro_cat.set("Todas")
        self.busqueda.set("")
        self.refrescar_productos()

    def _btn(self, parent, text, cmd, bg, fg, width=None):
        kw = dict(text=text, command=cmd, bg=bg, fg=fg,
                  font=("Segoe UI", 9, "bold"), relief="flat", bd=0,
                  padx=10, pady=5, cursor="hand2",
                  activebackground=C["btn_hover"], activeforeground=fg)
        if width: kw["width"] = width
        b = tk.Button(parent, **kw)
        b.bind("<Enter>", lambda e, _bg=bg: b.config(bg=C["btn_hover"]))
        b.bind("<Leave>", lambda e, _bg=bg: b.config(bg=_bg))
        return b

    def _nueva_ventana(self, titulo, w, h):
        win = tk.Toplevel(self.root)
        win.title(titulo)
        win.configure(bg=C["panel"])
        win.resizable(False, False)
        x = self.root.winfo_x() + (self.root.winfo_width()  - w) // 2
        y = self.root.winfo_y() + (self.root.winfo_height() - h) // 2
        win.geometry(f"{w}x{h}+{x}+{y}")
        win.grab_set()
        return win


# ─── MAIN ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure("TCombobox",
        fieldbackground=C["card"], background=C["card"],
        foreground=C["text"], selectbackground=C["highlight"],
        selectforeground="white", borderwidth=0)
    style.configure("Vertical.TScrollbar",
        background=C["btn_bg"], troughcolor=C["bg"],
        arrowcolor=C["text_dim"], borderwidth=0)
    app = TiendaApp(root)
    root.mainloop()

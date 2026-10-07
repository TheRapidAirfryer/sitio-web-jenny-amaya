"""Genera las páginas HTML del sitio de Cupcakes Garden.

Uso: python3 build.py
Edita los textos aquí y vuelve a ejecutar; el encabezado y el pie se comparten entre páginas.
"""
from pathlib import Path

ROOT = Path(__file__).parent / "public"

PRODUCTOS = [
    ("pasteles.html", "Pasteles"),
    ("galletas.html", "Galletas"),
    ("cupcakes.html", "Cupcakes"),
    ("postres.html", "Postres"),
]

# Menú principal: pocas categorías claras (brief, sección 14). Productos agrupa las cuatro líneas.
NAV = [
    ("productos.html", "Productos", PRODUCTOS),
    ("corporativo.html", "Corporativo", None),
    ("eventos.html", "Eventos", None),
    ("nosotros.html", "Nosotros", None),
    ("contacto.html", "Contacto", None),
]

WA_ICON = '<svg aria-hidden="true"><use href="#wa-icon"/></svg>'

FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Alice&family=Great+Vibes&display=swap">\n'
    '<link rel="stylesheet" href="css/estilos.css">'
)


def wa_btn(label, message, cls="btn wa"):
    return f'<a class="{cls}" data-wa="{message}" href="#">{WA_ICON}{label}</a>'


def photo(label, tone="t1"):
    return f'<div class="photo {tone}"><span>{label}</span></div>'


def pic(src, alt, w=800, h=800):
    return f'<img class="photo-img" src="img/{src}" alt="{alt}" width="{w}" height="{h}" loading="lazy">'


# Fotos reales por nombre de producto; lo que no esté aquí queda como marcador
FOTOS = {
    "Cookies estilo New York": ("galleta-new-york.jpg", "Galleta con chispas de chocolate mojada en leche"),
    "Cookies gourmand": ("galleta-gourmand.jpg", "Galleta gourmand cubierta de chocolate"),
    "Cookies americanas": ("galleta-americana.jpg", "Torre de galletas de macadamia"),
    "Alfajores": ("alfajores.jpg", "Alfajores bañados en chocolate y merengue"),
    "Galletas de colección": ("galletas-coleccion.jpg", "Caja de galletas linzer con mermelada"),
    "Tiramisú collection": ("tiramisu.jpg", "Frascos de postre en capas de varios sabores"),
}


def product_photo(name, tone):
    if name in FOTOS:
        return pic(*FOTOS[name])
    return photo(name, tone)


def chips(items):
    return '<ul class="chips">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def header(current):
    current_attr = ' aria-current="page"'
    items = []
    for href, label, children in NAV:
        active = href == current or any(c == current for c, _ in children or [])
        attr = current_attr if active else ""
        if children:
            sub = "".join(
                f'<li><a href="{c}"{current_attr if c == current else ""}>{l}</a></li>' for c, l in children
            )
            items.append(f'<li class="has-sub"><a href="{href}"{attr}>{label}</a><ul class="sub">{sub}</ul></li>')
        else:
            items.append(f'<li><a href="{href}"{attr}>{label}</a></li>')
    links = "".join(items)
    return f"""<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <symbol id="wa-icon" viewBox="0 0 24 24"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5c-.2 0-.4.1-.6.3-.2.2-.8.8-.8 2s.8 2.3 1 2.5c.1.2 1.6 2.5 4 3.5 1.5.6 2 .7 2.8.6.4-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.1-1.2l-.1-.2Z"/></symbol>
</svg>
<div class="notice">Pastelería de diseño en Tegucigalpa · Desde 2013</div>
<header class="top">
  <div class="wrap">
    <a class="brand" href="index.html"><img src="img/logo.png" alt="Cupcakes Garden by Jenny Amaya" width="900" height="431"></a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="menu">Menú</button>
    <nav class="menu" id="menu" aria-label="Principal">
      <ul>{links}</ul>
      <a class="btn solid" href="contacto.html#cotizar">Cotizar</a>
    </nav>
  </div>
</header>"""


FOOTER = """<footer>
  <div class="wrap">
    <div class="foot-brand">
      <img class="sello" src="img/sello.png" alt="Sello de Cupcakes Garden by Jenny Amaya" width="500" height="501">
      <p class="tagline">Pastelería de diseño<span class="tag-sep"> · </span>Diseño. Sabor. Detalle.</p>
    </div>
    <div class="col-prod">
      <h4>Productos</h4>
      <ul>
        <li><a href="productos.html">Todos los productos</a></li>
        <li><a href="pasteles.html">Pasteles</a></li>
        <li><a href="galletas.html">Galletas</a></li>
        <li><a href="cupcakes.html">Cupcakes</a></li>
        <li><a href="postres.html">Postres</a></li>
      </ul>
    </div>
    <div class="col-casa">
      <h4>Cupcakes Garden</h4>
      <ul>
        <li><a href="corporativo.html">Corporativo</a></li>
        <li><a href="eventos.html">Eventos</a></li>
        <li><a href="nosotros.html">Nosotros</a></li>
        <li class="desk-only"><a href="contacto.html">Contacto</a></li>
      </ul>
    </div>
    <div class="col-social">
      <h4>Síguenos</h4>
      <ul>
        <li><a href="https://www.instagram.com/cupcakesgardenhn/">Instagram</a></li>
        <li><a href="https://www.facebook.com/search/top?q=Cupcakes%20Garden">Facebook</a></li>
        <li><a href="https://www.tiktok.com/@cupcakes.garden.h">TikTok</a></li>
        <li><a data-wa="Hola Cupcakes Garden" href="#">WhatsApp</a></li>
      </ul>
    </div>
    <div class="legal">
      <span>© 2026 Cupcakes Garden. Tegucigalpa, Honduras.</span>
      <span><a href="legal.html#terminos">Términos y condiciones</a> · <a href="legal.html#privacidad">Política de privacidad</a></span>
    </div>
  </div>
</footer>
<a class="wa-float" data-wa="Hola Cupcakes Garden, quiero hacer un pedido." href="#" aria-label="Escribir por WhatsApp">""" + WA_ICON + """</a>
<script src="js/sitio.js"></script>"""


def page(filename, title, description, body):
    full_title = "Cupcakes Garden" if filename == "index.html" else f"{title} · Cupcakes Garden"
    html = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{full_title}</title>
<meta name="description" content="{description}">
<link rel="icon" href="img/sello.png">
{FONTS}
</head>
<body>
{header(filename)}
<main>
{body}
</main>
{FOOTER}
</body>
</html>
"""
    (ROOT / filename).write_text(html, encoding="utf-8")


def page_hero(script, title, intro):
    return f"""<section class="page-hero">
  <div class="wrap">
    <p class="script">{script}</p>
    <h1>{title}</h1>
    <p class="lead">{intro}</p>
  </div>
</section>"""


# ---------- Inicio ----------
# Foto de portada de cada línea (vacío = bloque de color mientras llega la foto)
PORTADAS = {
    "Pasteles": ("portada-pasteles.jpg", "Pastel de dos pisos azul con orquídeas blancas y detalles dorados"),
    "Galletas": ("portada-galletas.jpg", "Galleta con chispas de chocolate partida a mano"),
    "Cupcakes": ("portada-cupcakes.jpg", "Cupcake de vainilla con frosting, caramelo, chocolate y nuez"),
    "Postres": ("portada-postres.jpg", "Rebanada de pastel con capas de frutos rojos y frosting rosado"),
}


def line_cover(name, tone):
    if name in PORTADAS:
        src, alt = PORTADAS[name]
        return f'<img class="photo-img" src="img/{src}" alt="{alt}" width="800" height="1000" loading="lazy">'
    return photo(name, tone)


LINEAS = [
    ("pasteles.html", "Pasteles", "De diseño, para cada ocasión, clásicos y personalizados. También nuestra cake tasting box.", "t1"),
    ("galletas.html", "Galletas", "Estilo New York, gourmand, americanas, linzer, alfajores, cottage y gluten free.", "t3"),
    ("cupcakes.html", "Cupcakes", "Clásicos pick your color, gourmet y personalizados.", "t2"),
    ("postres.html", "Postres", "Spooning collection: tiramisú, cheesecakes y tres leches, más postres individuales.", "t4"),
    ("corporativo.html", "Corporativo", "Detalles y regalos para empresas, con cajas y kits listos para comprar.", "t3"),
    ("eventos.html", "Eventos", "Mesas dulces, Coffee &amp; Bakery Experience y propuestas para tu celebración.", "t2"),
]
cards = "".join(
    f'<a class="card" href="{href}">{line_cover(name, tone)}<h3>{name}</h3><p>{text}</p><span class="more">Ver {name.lower()} →</span></a>'
    for href, name, text, tone in LINEAS[:4]
)
page("index.html", "Inicio", "Cupcakes Garden: pastelería de diseño en Tegucigalpa para celebrar, regalar y compartir.", f"""
<section class="hero">
  <div class="wrap">
    <div class="text">
      <img class="logo-hero" src="img/logo.png" alt="Cupcakes Garden by Jenny Amaya" width="900" height="431">
      <h1>Pastelería para celebrar, regalar y compartir.</h1>
      <p class="lead">Desde pasteles diseñados para momentos especiales hasta galletas, cupcakes y postres que combinan diseño, sabor y atención al detalle.</p>
      <div class="actions">
        <a class="btn solid" href="productos.html">Ver productos</a>
        <a class="btn" href="contacto.html#cotizar">Cotizar</a>
      </div>
    </div>
    {pic("inicio-principal.jpg", "Pastel rosado con cerezas sobre base de madera", 800, 1000)}
  </div>
</section>

<section id="lineas" class="alt">
  <div class="wrap">
    <div class="section-head center">
      <p class="script">Nuestras líneas</p>
      <h2>Todo lo que hacemos</h2>
    </div>
    <div class="grid two-on-phone cols-4 occasions">{cards}</div>
  </div>
</section>

<section>
  <div class="wrap feature">
    {pic("tasting-box.jpg", "Cake tasting box con porciones de varios sabores", 1000, 800)}
    <div class="text">
      <p class="eyebrow">Cake tasting box</p>
      <h2>Descubre nuestros sabores antes de elegir tu pastel</h2>
      <p>Una selección de 5 porciones de nuestros pasteles para que pruebes, descubras tus favoritos y elijas con seguridad el sabor perfecto para tu celebración. Eliges 5 entre 12 sabores.</p>
      {wa_btn("Pedir mi tasting box", "Hola Cupcakes Garden, quiero pedir una cake tasting box.")}
    </div>
  </div>
</section>

<section class="tint">
  <div class="wrap feature reverse">
    <div class="text">
      <p class="eyebrow">Cupcakes clásicos</p>
      <h2>Pick your color</h2>
      <p>Elige el color del frosting y crea tu combinación. Packs de 2, 4, 6 o 12, en vainilla o chocolate, con relleno de dulce de leche, chocolate o fresa.</p>
      <a class="btn solid" href="cupcakes.html#clasicos">Arma tus cupcakes</a>
    </div>
    {photo("Cupcakes pick your color", "t2")}
  </div>
</section>

<section class="band">
  <div class="wrap grid cols-2">
    <div>
      <p class="eyebrow">Corporativo</p>
      <h2>Detalles que representan a tu marca</h2>
      <p>Regalos para clientes y colaboradores con empaque, colores y mensajes personalizados.</p>
      <a class="btn solid" href="corporativo.html#cotizar">Solicitar cotización corporativa</a>
    </div>
    <div>
      <p class="eyebrow">Eventos</p>
      <h2>Propuestas dulces para momentos que merecen ser recordados</h2>
      <p>Bodas, cumpleaños, bautizos, graduaciones, lanzamientos y mesas de postres.</p>
      <a class="btn solid" href="eventos.html#cotizar">Cuéntanos sobre tu evento</a>
    </div>
  </div>
</section>

<section>
  <div class="wrap feature">
    {pic("nuestra-historia.jpg", "Cuatro pasteles pequeños en tonos pastel", 1000, 800)}
    <div class="text">
      <p class="script">Desde 2013</p>
      <h2>Creando momentos a través de la pastelería</h2>
      <p>Cupcakes Garden nació con una pasión por la pastelería y por crear productos que acompañaran momentos importantes. Hoy seguimos creciendo sin perder lo que nos caracteriza: el buen gusto, la creatividad y la intención detrás de cada creación.</p>
      <a class="btn" href="nosotros.html">Conoce nuestra historia</a>
    </div>
  </div>
</section>
""")


# ---------- Productos ----------
pcards = "".join(
    f'<a class="card" href="{href}">{line_cover(name, tone)}<h3>{name}</h3><p>{text}</p><span class="more">Ver {name.lower()} →</span></a>'
    for href, name, text, tone in LINEAS[:4]
)
page("productos.html", "Productos", "Pasteles, galletas, cupcakes y postres de Cupcakes Garden.", f"""
{page_hero("Productos", "Pastelería de diseño", "Elige una línea para ver sus opciones y hacer tu pedido por WhatsApp.")}
<section>
  <div class="wrap grid two-on-phone cols-4 occasions">{pcards}</div>
</section>
""")


# ---------- Pasteles ----------
page("pasteles.html", "Pasteles", "Pasteles de diseño, para ocasiones especiales, clásicos, tradicionales de merengue y cake tasting box.", f"""
{page_hero("Pasteles", "Pasteles hechos para celebrar y compartir", "Desde diseños personalizados hasta opciones clásicas, creamos pasteles que combinan sabor, estética y atención al detalle.")}

<section>
  <div class="wrap feature">
    <img class="photo-img portrait" src="img/pastel-diseno-acuarela.jpg" alt="Pastel de diseño de cuatro pisos en tonos lila y blanco con flores de azúcar" width="800" height="1000">
    <div class="text">
      <p class="eyebrow">Pasteles de diseño</p>
      <h2>Un pastel único para tu celebración</h2>
      <p>Pasteles personalizados y conceptuales, con especial atención al diseño y al acabado. Cuéntanos tu idea y preparamos una propuesta.</p>
      {wa_btn("Cotizar pastel de diseño", "Hola Cupcakes Garden, quiero cotizar un pastel de diseño.")}
    </div>
  </div>
</section>

<section class="alt" id="ocasiones">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Pasteles para ocasiones especiales</p>
      <h2>Para cada momento importante</h2>
    </div>
    <div class="grid two-on-phone cols-4 occasions">
      <div class="card"><img class="photo-img" src="img/pastel-beisbol.jpg" alt="Pastel de cumpleaños con tema de béisbol" width="800" height="1000" loading="lazy"><h3>Cumpleaños</h3></div>
      <div class="card"><img class="photo-img" src="img/pastel-flores.jpg" alt="Pastel blanco de dos pisos con flores rosadas" width="800" height="1000" loading="lazy"><h3>Aniversarios</h3></div>
      <div class="card"><img class="photo-img" src="img/pastel-galaxia.jpg" alt="Pastel temático de galaxia con personajes y esferas" width="800" height="1000" loading="lazy"><h3>Graduaciones</h3></div>
      <div class="card"><img class="photo-img" src="img/pastel-pato.jpg" alt="Pastel infantil con personaje de pato" width="800" height="1000" loading="lazy"><h3>Bautizos</h3></div>
      <div class="card"><img class="photo-img" src="img/pastel-oh-baby.jpg" alt="Pastel de baby shower con tema de viajes" width="800" height="1000" loading="lazy"><h3>Baby showers y revelaciones</h3></div>
      <div class="card"><img class="photo-img" src="img/pastel-dinosaurios.jpg" alt="Pastel de dinosaurios en dos pisos" width="800" height="1000" loading="lazy"><h3>Niños</h3></div>
      <div class="card"><img class="photo-img" src="img/pastel-casita-bosque.jpg" alt="Pastel de casita en el bosque con musgo y hongos" width="800" height="1000" loading="lazy"><h3>Celebraciones especiales</h3></div>
      <a class="card" href="eventos.html#cotizar"><img class="photo-img" src="img/pastel-boda-clasico.jpg" alt="Pastel de boda clásico de cinco pisos" width="800" height="1000" loading="lazy"><h3>Bodas</h3><span class="more">Cotizar boda →</span></a>
    </div>
    <div class="actions" style="margin-top:2rem">{wa_btn("Pedir pastel para mi ocasión", "Hola Cupcakes Garden, quiero un pastel para una ocasión especial.")}</div>
  </div>
</section>

<section>
  <div class="wrap grid cols-2">
    <div class="card boxed">
      {pic("pastel-clasico.jpg", "Pastel rosado con pétalos blancos y macarons")}
      <p class="eyebrow">Pasteles clásicos</p>
      <h3>Bonitos y fáciles de elegir</h3>
      <p>Diseños sencillos y elegantes para quienes buscan una opción bonita sin requerir un concepto completamente personalizado.</p>
      {wa_btn("Pedir pastel clásico", "Hola Cupcakes Garden, quiero pedir un pastel clásico.", "btn wa small")}
    </div>
    <div class="card boxed">
      {photo("Pasteles de merengue", "t4")}
      <p class="eyebrow">Tradicionales de merengue</p>
      <h3>Recetas de toda la vida</h3>
      <p>Una colección inspirada en recetas tradicionales, de esas que nos han acompañado durante generaciones. Con cobertura de merengue.</p>
      <dl class="facts"><div><dt>Sabores</dt><dd>Vainilla, chocolate</dd></div><div><dt>Rellenos</dt><dd>Piña, dulce de leche, fresas</dd></div></dl>
      {wa_btn("Pedir pastel de merengue", "Hola Cupcakes Garden, quiero pedir un pastel tradicional de merengue.", "btn wa small")}
    </div>
  </div>
</section>

<section class="tint" id="tasting-box">
  <div class="wrap feature reverse">
    <div class="text">
      <p class="eyebrow">Cake tasting box</p>
      <h2>Descubre nuestros sabores antes de elegir tu pastel</h2>
      <p>Una selección de 5 porciones de nuestros pasteles, creada para que puedas probar, descubrir tus favoritos y elegir con seguridad el sabor perfecto para tu celebración.</p>
      <dl class="facts"><div><dt>Porciones</dt><dd>5</dd></div><div><dt>Sabores para elegir</dt><dd>12</dd></div></dl>
      {wa_btn("Pedir mi tasting box", "Hola Cupcakes Garden, quiero pedir una cake tasting box.")}
    </div>
    {pic("tasting-box-sabores.jpg", "Caja de degustación de pastel con sabores etiquetados", 1000, 800)}
  </div>
</section>

<section id="sabores">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Sabores y rellenos</p>
      <h2>Nuestra carta de sabores</h2>
      <p class="muted">Muy pronto publicaremos la carta completa, organizada en sabores convencionales, gourmet y de vanguardia. Mientras tanto, pregúntanos por WhatsApp.</p>
    </div>
    {wa_btn("Preguntar por sabores", "Hola Cupcakes Garden, ¿qué sabores de pastel tienen?", "btn")}
  </div>
</section>
""")


# ---------- Galletas ----------
GALLETAS = [
    ("Cookies estilo New York", "Grandes, gruesas y suaves por dentro.", "t3"),
    ("Cookies gourmand", "Combinaciones intensas para los más golosos.", "t1"),
    ("Cookies americanas", "La galleta clásica, crujiente por fuera.", "t4"),
    ("Alfajores", "Rellenos de dulce de leche.", "t3"),
    ("Galletas de colección", "Spritz, cottage y linzer.", "t2"),
    ("Gluten free", "Opciones sin gluten.", "t4"),
]
gcards = "".join(
    f'<div class="card">{product_photo(n, t)}<h3>{n}</h3><p>{d}</p>{wa_btn("Pedir", "Hola Cupcakes Garden, quiero pedir: " + n + ".", "btn wa small")}</div>'
    for n, d, t in GALLETAS
)
page("galletas.html", "Galletas", "Galletas estilo New York, gourmand, americanas, alfajores, galletas de colección y decoradas.", f"""
{page_hero("Galletas", "Galletas hechas para disfrutar, regalar y compartir", "Galletas de autor para cualquier antojo, para regalar o para tu próximo evento.")}
<section>
  <div class="wrap grid">{gcards}</div>
</section>
<section class="tint">
  <div class="wrap grid cols-2">
    <div class="card boxed">
      <p class="eyebrow">Galletas corporativas</p>
      <h3>Con los colores y el logo de tu empresa</h3>
      <p>Cajas de galletas personalizadas para clientes y colaboradores.</p>
      <a class="btn small" href="corporativo.html#cotizar">Cotizar corporativo</a>
    </div>
    <div class="card boxed">
      <p class="eyebrow">Galletas decoradas</p>
      <h3>Personalizadas para tu evento</h3>
      <p>Diseñadas a juego con la temática de tu celebración.</p>
      <a class="btn small" href="eventos.html#cotizar">Cotizar para evento</a>
    </div>
  </div>
</section>
""")


# ---------- Cupcakes ----------
def options(name, values, checked=0, kind="radio"):
    return '<div class="options">' + "".join(
        f'<label><input type="{kind}" name="{name}" value="{v}"{" checked" if i == checked else ""}><span>{v}</span></label>'
        for i, v in enumerate(values)
    ) + "</div>"


page("cupcakes.html", "Cupcakes", "Cupcakes clásicos pick your color, gourmet y personalizados.", f"""
{page_hero("Cupcakes", "Pequeños detalles que hacen especial cualquier celebración", "Arma tu pedido de cupcakes clásicos o gourmet y envíalo por WhatsApp.")}

<section id="clasicos">
  <div class="wrap feature">
    {photo("Cupcakes clásicos", "t2")}
    <form class="builder boxed" data-product="Cupcakes clásicos pick your color">
      <div>
        <p class="eyebrow">Cupcakes clásicos</p>
        <h2>Pick your color</h2>
        <p class="muted">Elige el color del frosting y crea tu combinación.</p>
      </div>
      <fieldset><legend>Pack</legend>{options("Pack", ["2", "4", "6", "12"], 2)}</fieldset>
      <fieldset><legend>Sabor</legend>{options("Sabor", ["Vainilla", "Chocolate"])}</fieldset>
      <fieldset><legend>Relleno</legend>{options("Relleno", ["Dulce de leche", "Chocolate", "Fresa"])}</fieldset>
      <fieldset><legend>Color del frosting</legend>{options("Color", ["Rosa", "Blanco", "Verde", "Dorado", "Lila", "Otro (lo indico en el chat)"])}</fieldset>
      <p class="summary" aria-live="polite"></p>
      <button class="btn wa" type="submit">{WA_ICON}Pedir por WhatsApp</button>
    </form>
  </div>
</section>

<section class="alt" id="gourmet">
  <div class="wrap feature reverse">
    <form class="builder boxed" data-product="Cupcakes gourmet">
      <div>
        <p class="eyebrow">Cupcakes gourmet</p>
        <h2>Sabores especiales</h2>
      </div>
      <fieldset><legend>Pack</legend>{options("Pack", ["6", "12"])}</fieldset>
      <fieldset><legend>Sabor</legend>{options("Sabor", ["Red velvet", "Salted caramel", "Carrot", "Fudge chocolate"])}</fieldset>
      <p class="summary" aria-live="polite"></p>
      <button class="btn wa" type="submit">{WA_ICON}Pedir por WhatsApp</button>
    </form>
    {photo("Cupcakes gourmet", "t1")}
  </div>
</section>

<section>
  <div class="wrap grid cols-2">
    <div class="card boxed">
      {photo("Cupcakes personalizados", "t3")}
      <p class="eyebrow">Cupcakes de diseño personalizados</p>
      <h3>Para tu temática</h3>
      <p>Para cumpleaños, celebraciones, baby showers, revelaciones y temáticas especiales. Requieren cotización.</p>
      <a class="btn small" href="eventos.html#cotizar">Cotizar</a>
    </div>
    <div class="card boxed">
      {photo("Cupcakes corporativos", "t4")}
      <p class="eyebrow">Cupcakes corporativos</p>
      <h3>Con la imagen de tu empresa</h3>
      <p>Ideales para lanzamientos, reuniones y regalos a clientes.</p>
      <a class="btn small" href="corporativo.html#cotizar">Cotizar corporativo</a>
    </div>
  </div>
</section>
""")


# ---------- Postres ----------
SPOONING = [("Tiramisú collection", "t4"), ("Cheesecake collection", "t1"), ("Tres leches collection", "t3")]
INDIVIDUALES = ["Cheesecakes clásicos", "Cheesecakes vascos", "Tres leches", "Tiramisú", "Pavlovas", "Tartas", "Loaf cakes"]
scards = "".join(
    f'<div class="card">{product_photo(n, t)}<h3>{n}</h3>{wa_btn("Pedir", "Hola Cupcakes Garden, quiero pedir: " + n + ".", "btn wa small")}</div>'
    for n, t in SPOONING
)
page("postres.html", "Postres", "Spooning collection y postres individuales: tiramisú, cheesecakes, tres leches, pavlovas, tartas y loaf cakes.", f"""
{page_hero("Postres", "Pequeños momentos, grandes antojos", "Postres para disfrutar con cuchara, compartir en la mesa o regalar.")}
<section>
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Spooning collection</p>
      <h2>Para disfrutar con cuchara</h2>
    </div>
    <div class="grid">{scards}</div>
  </div>
</section>
<section class="alt">
  <div class="wrap feature">
    {pic("postres-individuales.jpg", "Mini bundt cakes de chocolate y vainilla", 1000, 800)}
    <div class="text">
      <p class="eyebrow">Postres individuales</p>
      <h2>Tu antojo, en su porción</h2>
      {chips(INDIVIDUALES)}
      {wa_btn("Pedir postres", "Hola Cupcakes Garden, quiero pedir postres individuales.")}
    </div>
  </div>
</section>
""")


# ---------- Formularios ----------
def field(label, name, kind="text", required=False, full=False, options_list=None, hint=None):
    req = " required" if required else ""
    cls = ' class="full"' if full else ""
    if kind == "select":
        opts = '<option value="">Selecciona</option>' + "".join(f"<option>{o}</option>" for o in options_list)
        control = f'<select id="{name}" name="{name}"{req}>{opts}</select>'
    elif kind == "textarea":
        control = f'<textarea id="{name}" name="{name}"{req}></textarea>'
    else:
        control = f'<input id="{name}" name="{name}" type="{kind}"{req}>'
    extra = f'<span class="hint">{hint}</span>' if hint else ""
    return f"<label{cls} for=\"{name}\">{label}{control}{extra}</label>"


TIPOS_EVENTO = ["Boda", "Cumpleaños", "Bautizo", "Baby shower", "Graduación", "Evento empresarial", "Lanzamiento", "Celebración privada", "Otro"]
FORM_EVENTO = f"""<form class="form" data-title="Solicitud de cotización de evento" novalidate>
  {field("Nombre", "ev-nombre", required=True)}
  {field("WhatsApp", "ev-whatsapp", "tel", required=True)}
  {field("Correo", "ev-correo", "email")}
  {field("Fecha", "ev-fecha", "date", required=True)}
  {field("Tipo de evento", "ev-tipo", "select", True, options_list=TIPOS_EVENTO)}
  {field("Lugar", "ev-lugar")}
  {field("Número de invitados", "ev-invitados", "number")}
  {field("Presupuesto aproximado", "ev-presupuesto")}
  {field("Productos que necesita", "ev-productos", full=True, hint="Pasteles, cupcakes, galletas decoradas, macarons, postres, mesa de postres…")}
  {field("Comentarios", "ev-comentarios", "textarea", full=True, hint="Si tienes fotos de inspiración, envíalas en el chat de WhatsApp.")}
  <button class="btn solid full" type="submit">Enviar solicitud</button>
  <p class="form-note" role="status" hidden></p>
</form>"""

FORM_CORP = f"""<form class="form" data-title="Solicitud de propuesta corporativa" novalidate>
  {field("Empresa", "co-empresa", required=True)}
  {field("Nombre del contacto", "co-nombre", required=True)}
  {field("Cargo", "co-cargo")}
  {field("WhatsApp", "co-whatsapp", "tel", required=True)}
  {field("Correo", "co-correo", "email")}
  {field("Fecha de entrega", "co-fecha", "date")}
  {field("Tipo de ocasión", "co-ocasion", "select", options_list=["Regalos para clientes", "Bienvenida de colaboradores", "Aniversario de empresa", "Lanzamiento", "Evento empresarial", "Navidad", "Día de la Madre", "Día del Padre", "Otra fecha especial"])}
  {field("Cantidad aproximada", "co-cantidad", "number")}
  {field("Producto de interés", "co-producto", "select", options_list=["Cajas de galletas", "Cookies collection", "Alfajores", "Cupcakes", "Macarons", "Brownies", "Kit personalizado", "Otro"])}
  {field("¿Necesita personalización?", "co-personalizacion", "select", options_list=["Sí", "No", "No estoy seguro"])}
  {field("Presupuesto aproximado", "co-presupuesto", full=True)}
  {field("Comentarios", "co-comentarios", "textarea", full=True, hint="Si tienes tu logo o una referencia, envíala en el chat de WhatsApp.")}
  <button class="btn solid full" type="submit">Solicitar propuesta</button>
  <p class="form-note" role="status" hidden></p>
</form>"""


# ---------- Corporativo ----------
page("corporativo.html", "Corporativo", "Regalos y repostería personalizada para empresas, clientes y colaboradores.", f"""
{page_hero("Corporativo", "Detalles que representan a tu marca", "Repostería y regalos personalizados para empresas, clientes, colaboradores y ocasiones especiales.")}

<section>
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Compra inmediata</p>
      <h2>Listos para regalar</h2>
      <p class="muted">Dos opciones que puedes pedir hoy, sin cotización.</p>
    </div>
    <div class="grid cols-2">
      <div class="card boxed">{pic("corp-caja-galletas.jpg", "Caja de alfajores para regalo")}<h3>Caja de galletas</h3><p>Una selección de nuestras galletas en caja de regalo.</p>{wa_btn("Pedir cajas", "Hola Cupcakes Garden, quiero pedir cajas corporativas de galletas.", "btn wa small")}</div>
      <div class="card boxed">{pic("corp-kit.jpg", "Caja de rebanadas de loaf cake con tarjeta de agradecimiento")}<h3>Kit corporativo</h3><p>Un kit de postres variados listo para entregar.</p>{wa_btn("Pedir kits", "Hola Cupcakes Garden, quiero pedir kits corporativos.", "btn wa small")}</div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap grid">
    <div class="card"><p class="eyebrow">Regalos corporativos</p>{chips(["Cajas de galletas", "Cookies collection", "Alfajores", "Cupcakes", "Macarons", "Brownies", "Kits personalizados", "Regalos para clientes y colaboradores"])}</div>
    <div class="card"><p class="eyebrow">Personalización</p>{chips(["Empaque", "Branding", "Tarjetas", "Colores corporativos", "Mensajes personalizados"])}</div>
    <div class="card"><p class="eyebrow">Ocasiones</p>{chips(["Regalos para clientes", "Bienvenida de colaboradores", "Aniversarios de empresa", "Lanzamientos", "Eventos empresariales", "Navidad", "Día de la Madre", "Día del Padre", "Fechas especiales"])}</div>
  </div>
</section>

<section class="tint" id="cotizar">
  <div class="wrap quote">
    <div class="intro">
      <p class="script">Cotiza</p>
      <h2>Solicitar cotización corporativa</h2>
      <p class="muted">Cuéntanos qué necesita tu empresa y te enviamos una propuesta.</p>
    </div>
    {FORM_CORP}
  </div>
</section>
""")


# ---------- Eventos ----------
page("eventos.html", "Eventos", "Propuestas dulces para bodas, cumpleaños, bautizos, graduaciones y eventos empresariales.", f"""
{page_hero("Eventos", "Creamos propuestas dulces para momentos que merecen ser recordados", "Pasteles, cupcakes, cookies, galletas decoradas, macarons, postres, mesas de postres y propuestas personalizadas.")}

<section>
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Celebramos contigo</p>
      <h2>Tipos de evento</h2>
    </div>
    {chips(["Bodas", "Cumpleaños", "Bautizos", "Baby showers", "Graduaciones", "Eventos empresariales", "Lanzamientos", "Celebraciones privadas", "Mesas de postres"])}
  </div>
</section>

<section class="alt">
  <div class="wrap grid cols-2">
    <div class="card boxed">{photo("Mesa dulce", "t1")}<p class="eyebrow">Mesas dulces</p><h3>Una mesa a la medida de tu evento</h3><p>Combinamos pasteles, cupcakes, galletas y postres con la temática de tu celebración.</p></div>
    <div class="card boxed">{pic("eventos-coffee.jpg", "Rebanada de carrot cake con café latte")}<p class="eyebrow">Coffee &amp; Bakery Experience</p><h3>Nuestro carrito de café y repostería</h3><p>Una experiencia de café y bakery para que tus invitados disfruten en el momento.</p></div>
  </div>
</section>

<section class="tint" id="cotizar">
  <div class="wrap quote">
    <div class="intro">
      <p class="script">Cotiza</p>
      <h2>Cuéntanos sobre tu evento</h2>
      <p class="muted">Completa el formulario y preparamos una propuesta para ti.</p>
    </div>
    {FORM_EVENTO}
  </div>
</section>
""")


# ---------- Nosotros ----------
page("nosotros.html", "Nosotros", "Cupcakes Garden: pastelería hondureña fundada en 2013.", f"""
{page_hero("Nuestra historia", "Desde 2013 creando momentos a través de la pastelería", "Cupcakes Garden es una pastelería hondureña especializada en pastelería de diseño para celebrar, regalar y crear momentos especiales.")}

<section>
  <div class="wrap feature">
    <img class="photo-img portrait" src="img/jenny-amaya.jpg" alt="Jenny Amaya, fundadora de Cupcakes Garden" width="1200" height="1490">
    <div class="text">
      <p class="eyebrow">Nuestra historia</p>
      <p>Cupcakes Garden nació con una pasión por la pastelería y por crear productos que acompañaran momentos importantes. Con los años hemos evolucionado, ampliado nuestra propuesta y desarrollado nuevas líneas de productos, manteniendo nuestro compromiso con el sabor, el diseño y la atención al detalle.</p>
      <p>Hoy seguimos creciendo sin perder aquello que nos caracteriza: el buen gusto, la creatividad y la intención detrás de cada creación.</p>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap grid pillars">
    <div class="card"><p class="eyebrow">Lo que hacemos</p><p>Desarrollamos desde un pastel para una celebración íntima hasta propuestas completas para eventos, empresas y ocasiones especiales. Nuestro trabajo combina creatividad, técnica y atención al detalle para que cada producto tenga identidad propia y forme parte de una experiencia memorable.</p></div>
    <div class="card"><p class="eyebrow">Nuestra esencia</p><p>Creemos que cada producto comunica y forma parte de la celebración. El diseño y el sabor deben ir de la mano; por eso cuidamos desde la selección y elaboración del producto hasta la presentación final.</p></div>
    <div class="card"><p class="eyebrow">Nuestra evolución</p><p>Cupcakes Garden continúa desarrollando nuevas propuestas y conceptos alrededor de la pastelería, el café y la experiencia gastronómica.</p></div>
  </div>
</section>

<section>
  <div class="wrap grid cols-2">
    <div class="card boxed"><p class="eyebrow">Misión</p><p>Crear productos de pastelería y repostería que combinen sabor, diseño y calidad, convirtiendo cada celebración y cada detalle en una experiencia memorable.</p></div>
    <div class="card boxed"><p class="eyebrow">Visión</p><p>Ser una marca referente en Honduras en pastelería y repostería de diseño, reconocida por la calidad de sus productos, su estética, innovación y capacidad de crear experiencias alrededor de la gastronomía.</p></div>
  </div>
  <div class="wrap section-head center" style="margin-top:3rem;margin-bottom:0">
    <p class="script">Gracias por dejarnos ser parte de tus momentos.</p>
  </div>
</section>
""")


# ---------- Contacto ----------
page("contacto.html", "Contacto", "Contacto de Cupcakes Garden en Tegucigalpa: WhatsApp, correo, horario y redes sociales.", f"""
{page_hero("Contacto", "Hablemos", "Escríbenos para pedidos, dudas o cotizaciones.")}

<section>
  <div class="wrap contact">
    <dl>
      <div><dt>Ubicación</dt><dd>Res. Altos del Trapiche, 5.ª etapa<br>Tegucigalpa, Honduras</dd></div>
      <div><dt>Horario</dt><dd>Lunes a sábado, 8:00 a. m. a 5:00 p. m.</dd></div>
      <div><dt>Correo</dt><dd>cupcakesgardenhn@gmail.com</dd></div>
      <div><dt>WhatsApp</dt><dd>Próximamente</dd></div>
    </dl>
    <div class="card">
      <p class="eyebrow">Redes sociales</p>
      <div class="social">
        {wa_btn("WhatsApp", "Hola Cupcakes Garden", "btn wa small")}
        <a class="btn small" href="https://www.instagram.com/cupcakesgardenhn/">Instagram @cupcakesgardenhn</a>
        <a class="btn small" href="https://www.facebook.com/search/top?q=Cupcakes%20Garden">Facebook</a>
        <a class="btn small" href="https://www.tiktok.com/@cupcakes.garden.h">TikTok @cupcakes.garden.h</a>
      </div>
    </div>
  </div>
</section>

<section class="tint" id="cotizar">
  <div class="wrap">
    <div class="section-head center">
      <p class="script">Cotizar</p>
      <h2>¿Qué quieres cotizar?</h2>
    </div>
    <div class="grid cols-2">
      <a class="card boxed" href="eventos.html#cotizar">{pic("contacto-eventos.jpg", "Pastel de boda blanco con flores de azúcar")}<h3>Eventos</h3><p>Bodas, cumpleaños, bautizos, graduaciones, mesas de postres y más.</p><span class="more">Cotizar evento →</span></a>
      <a class="card boxed" href="corporativo.html#cotizar">{pic("contacto-corporativo.jpg", "Caja de regalo con mini bundt cake y lazo rojo")}<h3>Corporativo</h3><p>Regalos y detalles personalizados para tu empresa.</p><span class="more">Cotizar corporativo →</span></a>
    </div>
  </div>
</section>
""")


# ---------- Legal ----------
page("legal.html", "Términos y privacidad", "Términos y condiciones y política de privacidad de Cupcakes Garden.", f"""
{page_hero("Información legal", "Términos y privacidad", "Texto pendiente de entregar por Cupcakes Garden.")}
<section id="terminos">
  <div class="wrap section-head">
    <h2>Términos y condiciones</h2>
    <p class="muted">Aquí irán las condiciones de pedidos, anticipos, cambios, cancelaciones y entregas.</p>
  </div>
</section>
<section id="privacidad" class="alt">
  <div class="wrap section-head">
    <h2>Política de privacidad</h2>
    <p class="muted">Aquí irá cómo se usan los datos que los clientes envían en los formularios y por WhatsApp.</p>
  </div>
</section>
""")

print("Páginas generadas.")

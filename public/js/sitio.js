// Cupcakes Garden: comportamiento del sitio (fase 1, pedidos por WhatsApp)

// Número de WhatsApp: código de país + número, sin espacios ni "+". Ejemplo: "50400000000".
// Mientras esté vacío, los botones muestran un aviso en lugar de abrir WhatsApp.
const WHATSAPP = "";

const waLink = (text) => "https://wa.me/" + WHATSAPP + "?text=" + encodeURIComponent(text);

function toast(message) {
  let el = document.querySelector(".toast");
  if (!el) {
    el = document.createElement("div");
    el.className = "toast";
    el.setAttribute("role", "status");
    document.body.appendChild(el);
  }
  el.textContent = message;
  el.hidden = false;
  clearTimeout(toast.timer);
  toast.timer = setTimeout(() => { el.hidden = true; }, 3500);
}

const SIN_NUMERO = "Muy pronto podrás escribirnos por WhatsApp desde aquí.";

function openWhatsApp(text) {
  if (!WHATSAPP) { toast(SIN_NUMERO); return; }
  window.open(waLink(text), "_blank", "noopener");
}

// Enlaces con data-wa="mensaje" abren WhatsApp con ese mensaje ya escrito
document.querySelectorAll("[data-wa]").forEach((a) => {
  if (WHATSAPP) {
    a.href = waLink(a.dataset.wa);
    a.target = "_blank";
    a.rel = "noopener";
  } else {
    a.addEventListener("click", (e) => { e.preventDefault(); toast(SIN_NUMERO); });
  }
});

// Menú en celular
const toggle = document.querySelector(".menu-toggle");
const menu = document.getElementById("menu");
if (toggle && menu) {
  toggle.addEventListener("click", () => {
    const open = menu.classList.toggle("open");
    toggle.setAttribute("aria-expanded", String(open));
  });
}

// Armadores de cupcakes: arman el pedido y lo envían por WhatsApp
document.querySelectorAll("form.builder").forEach((form) => {
  const out = form.querySelector(".summary");
  const describe = () => {
    const data = new FormData(form);
    const parts = [];
    for (const [key, value] of data.entries()) {
      if (value) parts.push(key + ": " + value);
    }
    return form.dataset.product + " (" + parts.join(", ") + ")";
  };
  const update = () => { if (out) out.textContent = "Tu pedido: " + describe(); };
  form.addEventListener("change", update);
  update();
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    openWhatsApp("Hola Cupcakes Garden, quiero pedir: " + describe() + ".");
  });
});

// Formularios de cotización: arman un mensaje con todas las respuestas
document.querySelectorAll("form.form").forEach((form) => {
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const note = form.querySelector(".form-note");
    if (!form.checkValidity()) {
      form.reportValidity();
      return;
    }
    const lines = [form.dataset.title];
    form.querySelectorAll("input, select, textarea").forEach((field) => {
      const label = field.closest("label");
      if (!label || !field.value) return;
      const name = label.firstChild.textContent.trim();
      lines.push(name + ": " + field.value);
    });
    const text = lines.join("\n");
    if (!WHATSAPP) {
      if (note) {
        note.hidden = false;
        note.textContent = "Gracias. El envío por WhatsApp se activará muy pronto; por ahora escríbenos a cupcakesgardenhn@gmail.com.";
      }
      return;
    }
    openWhatsApp(text);
    if (note) {
      note.hidden = false;
      note.textContent = "Abrimos WhatsApp con tu solicitud. Si tienes fotos de inspiración, envíalas en el mismo chat.";
    }
  });
});

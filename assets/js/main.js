/* ==========================================================================
   Omni Digital — Scripts du site
   ========================================================================== */

/* ---------------------------------------------------------------------------
   CONFIGURATION — à personnaliser
   - FORM_ENDPOINT : URL d'un service de formulaires (ex. https://formspree.io/f/xxxxxx).
     Laissez vide pour que les formulaires ouvrent le logiciel de messagerie
     du visiteur avec un e-mail pré-rempli adressé à CONTACT_EMAIL.
   - BOOKING : jours/horaires proposés dans l'agenda de prise de rendez-vous.
--------------------------------------------------------------------------- */
const OMNI_CONFIG = {
  FORM_ENDPOINT: "",
  CONTACT_EMAIL: "contact@omnidigital.fr",
  BOOKING: {
    workingDays: [1, 2, 3, 4, 5],            // 0 = dimanche … 6 = samedi
    slots: ["09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00"],
    durationMin: 30,
    minNoticeHours: 12,                       // délai minimum avant un rendez-vous
    maxDaysAhead: 45
  }
};

(function () {
  "use strict";
  document.documentElement.classList.remove("no-js");

  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => Array.from(c.querySelectorAll(s));

  /* ---------- Header au défilement ---------- */
  const header = $(".site-header");
  const stickyCta = $(".sticky-cta");
  const onScroll = () => {
    const y = window.scrollY;
    header && header.classList.toggle("is-scrolled", y > 10);
    stickyCta && stickyCta.classList.toggle("is-visible", y > 700);
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ---------- Menu mobile ---------- */
  const toggle = $(".nav-toggle");
  if (toggle) {
    toggle.addEventListener("click", () => {
      const open = document.body.classList.toggle("nav-open");
      const menu = $(".nav-menu");
      if (menu && header) menu.style.top = open ? header.getBoundingClientRect().bottom + "px" : "";
      toggle.setAttribute("aria-expanded", String(open));
    });
    $$(".nav-menu a").forEach(a => a.addEventListener("click", () => {
      document.body.classList.remove("nav-open");
      toggle.setAttribute("aria-expanded", "false");
    }));
    document.addEventListener("keydown", e => {
      if (e.key === "Escape" && document.body.classList.contains("nav-open")) {
        document.body.classList.remove("nav-open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.focus();
      }
    });
  }

  /* ---------- Images : repli élégant si une image ne charge pas ---------- */
  $$("img").forEach(img => {
    if (img.complete && img.naturalWidth === 0) img.style.opacity = "0";
    else img.addEventListener("error", () => { img.style.opacity = "0"; }, { once: true });
  });

  /* ---------- Apparition au défilement ---------- */
  const revealEls = $$(".reveal");
  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver(entries => {
      entries.forEach(en => {
        if (en.isIntersecting) { en.target.classList.add("is-visible"); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
    revealEls.forEach(el => io.observe(el));
  } else {
    revealEls.forEach(el => el.classList.add("is-visible"));
  }

  /* ---------- Compteurs animés ---------- */
  const counters = $$("[data-count]");
  if (counters.length && "IntersectionObserver" in window) {
    const co = new IntersectionObserver(entries => {
      entries.forEach(en => {
        if (!en.isIntersecting) return;
        const el = en.target;
        const target = parseFloat(el.dataset.count);
        const decimals = (el.dataset.count.split(".")[1] || "").length;
        const dur = 1600;
        const t0 = performance.now();
        const tick = now => {
          const p = Math.min((now - t0) / dur, 1);
          const eased = 1 - Math.pow(1 - p, 3);
          el.textContent = (target * eased).toLocaleString("fr-FR", { minimumFractionDigits: decimals, maximumFractionDigits: decimals });
          if (p < 1) requestAnimationFrame(tick);
        };
        requestAnimationFrame(tick);
        co.unobserve(el);
      });
    }, { threshold: 0.5 });
    counters.forEach(c => co.observe(c));
  }

  /* ---------- Filtres (portfolio & blog) ---------- */
  $$("[data-filter-group]").forEach(group => {
    const targetSel = group.dataset.filterGroup;
    const items = $$(targetSel);
    const search = $("[data-search='" + targetSel + "']");
    const empty = $("[data-empty='" + targetSel + "']");
    let current = "all";
    const apply = () => {
      const q = search ? search.value.trim().toLowerCase() : "";
      let visible = 0;
      items.forEach(it => {
        const cats = (it.dataset.cat || "").split(" ");
        const okCat = current === "all" || cats.includes(current);
        const okQ = !q || it.textContent.toLowerCase().includes(q);
        const show = okCat && okQ;
        it.classList.toggle("is-hidden", !show);
        it.style.display = show ? "" : "none";
        if (show) visible++;
      });
      if (empty) empty.style.display = visible ? "none" : "block";
    };
    $$(".filter-btn", group).forEach(btn => {
      btn.addEventListener("click", () => {
        $$(".filter-btn", group).forEach(b => { b.classList.remove("is-active"); b.setAttribute("aria-pressed", "false"); });
        btn.classList.add("is-active");
        btn.setAttribute("aria-pressed", "true");
        current = btn.dataset.filter;
        apply();
      });
    });
    search && search.addEventListener("input", apply);
  });

  /* ---------- Envoi des formulaires ---------- */
  const validate = form => {
    let ok = true;
    $$("[required]", form).forEach(input => {
      const field = input.closest(".field") || input.parentElement;
      let valid = input.type === "checkbox" ? input.checked : input.value.trim() !== "";
      if (valid && input.type === "email") valid = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(input.value.trim());
      if (valid && input.type === "tel" && input.value.trim()) valid = /^[+()\d\s.-]{8,}$/.test(input.value.trim());
      field && field.classList.toggle("has-error", !valid);
      if (!valid) ok = false;
    });
    if (!ok) {
      const first = $(".has-error input, .has-error select, .has-error textarea", form);
      first && first.focus();
    }
    return ok;
  };

  const formToObject = form => {
    const data = {};
    new FormData(form).forEach((v, k) => {
      if (k === "_gotcha") return;
      data[k] = data[k] ? data[k] + ", " + v : v;
    });
    return data;
  };

  const sendForm = async (form, data) => {
    if (form.querySelector("[name='_gotcha']") && form.querySelector("[name='_gotcha']").value) return true; // anti-spam
    if (OMNI_CONFIG.FORM_ENDPOINT) {
      const res = await fetch(OMNI_CONFIG.FORM_ENDPOINT, {
        method: "POST",
        headers: { "Content-Type": "application/json", Accept: "application/json" },
        body: JSON.stringify(data)
      });
      if (!res.ok) throw new Error("Envoi impossible");
      return true;
    }
    // Repli : ouverture de la messagerie avec un e-mail pré-rempli
    const subject = data._subject || "Demande depuis le site Omni Digital";
    const body = Object.entries(data).filter(([k]) => !k.startsWith("_")).map(([k, v]) => k + " : " + v).join("\n");
    window.location.href = "mailto:" + OMNI_CONFIG.CONTACT_EMAIL + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
    return true;
  };

  $$("form[data-omni-form]").forEach(form => {
    $$("input, select, textarea", form).forEach(el => {
      el.addEventListener("input", () => {
        const f = el.closest(".field");
        f && f.classList.remove("has-error");
      });
    });
    form.addEventListener("submit", async e => {
      e.preventDefault();
      if (!validate(form)) return;
      const btn = $("button[type='submit']", form);
      const label = btn ? btn.innerHTML : "";
      if (btn) { btn.disabled = true; btn.textContent = "Envoi en cours…"; }
      try {
        await sendForm(form, formToObject(form));
        const wrap = form.closest("[data-form-wrap]") || form;
        wrap.classList.add("is-sent");
        wrap.scrollIntoView({ behavior: "smooth", block: "center" });
      } catch (err) {
        alert("Oups, l'envoi a échoué. Écrivez-nous directement à " + OMNI_CONFIG.CONTACT_EMAIL);
      } finally {
        if (btn) { btn.disabled = false; btn.innerHTML = label; }
      }
    });
  });

  /* Pré-sélection d'un service depuis l'URL (?service=seo) */
  const params = new URLSearchParams(location.search);
  const svc = params.get("service");
  if (svc) {
    const chip = $("input[name='services'][value='" + CSS.escape(svc) + "']");
    if (chip) chip.checked = true;
  }

  /* ---------- Prise de rendez-vous ---------- */
  const booking = $("[data-booking]");
  if (booking) initBooking(booking);

  function initBooking(root) {
    const cfg = OMNI_CONFIG.BOOKING;
    const state = { view: startOfMonth(new Date()), date: null, time: null, type: "Visioconférence" };
    const grid = $(".cal-grid", root);
    const title = $(".cal-title", root);
    const prev = $(".cal-prev", root);
    const next = $(".cal-next", root);
    const slotsBox = $(".slots", root);
    const slotsTitle = $(".slots-title", root);
    const toStep2 = $("[data-to-step='2']", root);
    const summary = $(".booking-summary", root);
    const steps = $$(".booking-steps span", root);
    const panels = $$(".booking-panel", root);
    const form = $("form", root);
    const now = new Date();
    const minDate = new Date(now.getTime() + cfg.minNoticeHours * 3600 * 1000);
    const maxDate = new Date(now.getFullYear(), now.getMonth(), now.getDate() + cfg.maxDaysAhead);
    const fmtMonth = new Intl.DateTimeFormat("fr-FR", { month: "long", year: "numeric" });
    const fmtLong = new Intl.DateTimeFormat("fr-FR", { weekday: "long", day: "numeric", month: "long" });

    function startOfMonth(d) { return new Date(d.getFullYear(), d.getMonth(), 1); }
    function sameDay(a, b) { return a && b && a.toDateString() === b.toDateString(); }
    function slotDate(day, hhmm) { const [h, m] = hhmm.split(":").map(Number); return new Date(day.getFullYear(), day.getMonth(), day.getDate(), h, m); }
    function availableSlots(day) { return cfg.slots.filter(s => slotDate(day, s) >= minDate); }
    function isAvailable(day) {
      if (!cfg.workingDays.includes(day.getDay())) return false;
      if (day > maxDate) return false;
      return availableSlots(day).length > 0;
    }

    function renderCalendar() {
      title.textContent = fmtMonth.format(state.view);
      grid.innerHTML = "";
      ["Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim"].forEach(d => {
        const el = document.createElement("div"); el.className = "dow"; el.textContent = d; grid.appendChild(el);
      });
      const first = state.view;
      const offset = (first.getDay() + 6) % 7;
      for (let i = 0; i < offset; i++) grid.appendChild(document.createElement("div"));
      const days = new Date(first.getFullYear(), first.getMonth() + 1, 0).getDate();
      for (let d = 1; d <= days; d++) {
        const date = new Date(first.getFullYear(), first.getMonth(), d);
        const b = document.createElement("button");
        b.type = "button";
        b.className = "cal-day";
        b.textContent = d;
        b.setAttribute("aria-label", fmtLong.format(date));
        if (sameDay(date, now)) b.classList.add("today");
        if (isAvailable(date)) {
          b.classList.add("available");
          b.addEventListener("click", () => { state.date = date; state.time = null; renderCalendar(); renderSlots(); });
        } else {
          b.disabled = true;
        }
        if (sameDay(date, state.date)) { b.classList.add("is-selected"); b.setAttribute("aria-pressed", "true"); }
        grid.appendChild(b);
      }
      prev.disabled = state.view <= startOfMonth(now);
      next.disabled = startOfMonth(maxDate) <= state.view;
      updateSummary();
    }

    function renderSlots() {
      slotsBox.innerHTML = "";
      if (!state.date) {
        slotsTitle.textContent = "Choisissez une date";
        slotsBox.innerHTML = '<p class="slots-empty">Sélectionnez un jour disponible (en bleu) dans le calendrier.</p>';
        updateSummary();
        return;
      }
      slotsTitle.textContent = "Créneaux du " + fmtLong.format(state.date);
      availableSlots(state.date).forEach(s => {
        const b = document.createElement("button");
        b.type = "button"; b.className = "slot"; b.textContent = s.replace(":", "h");
        if (state.time === s) b.classList.add("is-selected");
        b.addEventListener("click", () => { state.time = s; renderSlots(); });
        slotsBox.appendChild(b);
      });
      updateSummary();
    }

    function updateSummary() {
      toStep2.disabled = !(state.date && state.time);
      if (state.date && state.time) {
        summary.innerHTML = "<strong>" + capitalize(fmtLong.format(state.date)) + "</strong><br>à " + state.time.replace(":", "h") + " · " + cfg.durationMin + " min<br>" + state.type;
      } else {
        summary.innerHTML = "Aucun créneau sélectionné pour l'instant.";
      }
    }
    function capitalize(s) { return s.charAt(0).toUpperCase() + s.slice(1); }

    function goStep(n) {
      panels.forEach((p, i) => p.classList.toggle("is-active", i === n - 1));
      steps.forEach((s, i) => { s.classList.toggle("is-active", i === n - 1); s.classList.toggle("is-done", i < n - 1); });
      root.scrollIntoView({ behavior: "smooth", block: "start" });
    }

    $$("input[name='type_rdv']", root).forEach(r => r.addEventListener("change", () => { state.type = r.value; updateSummary(); }));
    prev.addEventListener("click", () => { state.view = new Date(state.view.getFullYear(), state.view.getMonth() - 1, 1); renderCalendar(); });
    next.addEventListener("click", () => { state.view = new Date(state.view.getFullYear(), state.view.getMonth() + 1, 1); renderCalendar(); });
    toStep2.addEventListener("click", () => goStep(2));
    $$("[data-to-step='1']", root).forEach(b => b.addEventListener("click", () => goStep(1)));

    form.addEventListener("submit", async e => {
      e.preventDefault();
      if (!validate(form)) return;
      const data = formToObject(form);
      data._subject = "Demande de rendez-vous — " + capitalize(fmtLong.format(state.date)) + " à " + state.time;
      data.rendez_vous = capitalize(fmtLong.format(state.date)) + " à " + state.time.replace(":", "h") + " (" + cfg.durationMin + " min)";
      data.format = state.type;
      const btn = $("button[type='submit']", form);
      const label = btn.innerHTML;
      btn.disabled = true; btn.textContent = "Réservation…";
      try {
        await sendForm(form, data);
        $(".confirm-when", root).textContent = data.rendez_vous;
        $(".confirm-type", root).textContent = state.type;
        $(".ics-link", root).addEventListener("click", downloadIcs);
        goStep(3);
      } catch (err) {
        alert("Oups, la réservation a échoué. Écrivez-nous à " + OMNI_CONFIG.CONTACT_EMAIL);
      } finally {
        btn.disabled = false; btn.innerHTML = label;
      }
    });

    function downloadIcs(e) {
      e.preventDefault();
      const start = slotDate(state.date, state.time);
      const end = new Date(start.getTime() + cfg.durationMin * 60000);
      const f = d => d.toISOString().replace(/[-:]/g, "").split(".")[0] + "Z";
      const ics = [
        "BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Omni Digital//RDV//FR", "BEGIN:VEVENT",
        "UID:" + Date.now() + "@omnidigital.fr", "DTSTAMP:" + f(new Date()), "DTSTART:" + f(start), "DTEND:" + f(end),
        "SUMMARY:Rendez-vous découverte — Omni Digital", "DESCRIPTION:" + state.type + " avec l'équipe Omni Digital",
        "END:VEVENT", "END:VCALENDAR"
      ].join("\r\n");
      const a = document.createElement("a");
      a.href = URL.createObjectURL(new Blob([ics], { type: "text/calendar" }));
      a.download = "rdv-omni-digital.ics";
      a.click();
    }

    // Démarre sur le mois du premier jour disponible
    for (let i = 0; i <= cfg.maxDaysAhead; i++) {
      const d = new Date(now.getFullYear(), now.getMonth(), now.getDate() + i);
      if (isAvailable(d)) { state.view = startOfMonth(d); break; }
    }
    renderCalendar();
    renderSlots();
  }

  /* ---------- Newsletter ---------- */
  $$("form[data-newsletter]").forEach(f => {
    f.addEventListener("submit", async e => {
      e.preventDefault();
      const input = $("input[type='email']", f);
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(input.value.trim())) { input.focus(); return; }
      try { await sendForm(f, { email: input.value.trim(), _subject: "Inscription newsletter" }); } catch (_) {}
      f.innerHTML = '<p style="color:#fff;margin:0">Merci ! Vous êtes bien inscrit(e). ✔</p>';
    });
  });

  /* ---------- Copier le lien (articles) ---------- */
  $$("[data-copy-link]").forEach(b => b.addEventListener("click", () => {
    navigator.clipboard && navigator.clipboard.writeText(location.href).then(() => {
      b.setAttribute("title", "Lien copié !");
      b.style.background = "var(--orange-500)"; b.style.color = "#fff";
    });
  }));
  $$("[data-share]").forEach(a => {
    const u = encodeURIComponent(location.href), t = encodeURIComponent(document.title);
    const map = {
      linkedin: "https://www.linkedin.com/sharing/share-offsite/?url=" + u,
      facebook: "https://www.facebook.com/sharer/sharer.php?u=" + u,
      x: "https://twitter.com/intent/tweet?url=" + u + "&text=" + t
    };
    a.href = map[a.dataset.share] || "#";
  });

  /* ---------- Bandeau cookies ---------- */
  const cookie = $(".cookie");
  if (cookie) {
    let consent = null;
    try { consent = localStorage.getItem("omni-cookies"); } catch (_) {}
    if (!consent) setTimeout(() => cookie.classList.add("is-visible"), 1200);
    $$("[data-cookie]", cookie).forEach(b => b.addEventListener("click", () => {
      try { localStorage.setItem("omni-cookies", b.dataset.cookie); } catch (_) {}
      cookie.classList.remove("is-visible");
    }));
  }

  /* ---------- Année du footer ---------- */
  $$("[data-year]").forEach(el => { el.textContent = new Date().getFullYear(); });
})();

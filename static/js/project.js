document.querySelectorAll(".copy-btn").forEach((btn) => {
    btn.addEventListener("click", async () => {
        try {
            await navigator.clipboard.writeText(btn.dataset.copy);
            btn.classList.add("copied");
            setTimeout(() => btn.classList.remove("copied"), 1800);
        } catch (e) {
            console.warn("Не удалось скопировать", e);
        }
    });
});

const lightbox = document.getElementById("lightbox");
if (lightbox) {
    const lbImg = lightbox.querySelector("img");

    document.querySelectorAll(".js-lightbox").forEach((img) => {
        img.addEventListener("click", () => {
            lbImg.src = img.src;
            lbImg.alt = img.alt;
            lightbox.hidden = false;
        });
    });

    const close = () => { lightbox.hidden = true; lbImg.src = ""; };
    lightbox.addEventListener("click", close);
    document.addEventListener("keydown", (e) => { if (e.key === "Escape") close(); });
}

if (window.hljs) hljs.highlightAll();

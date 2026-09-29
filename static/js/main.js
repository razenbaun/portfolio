document.querySelectorAll(".h-scroll-wrapper").forEach((wrapper) => {
    const scroller = wrapper.querySelector(".h-scroll");
    const btnPrev = wrapper.querySelector(".scroll-btn.prev");
    const btnNext = wrapper.querySelector(".scroll-btn.next");

    const updateButtons = () => {
        const maxScroll = scroller.scrollWidth - scroller.clientWidth;
        wrapper.classList.toggle("has-left", scroller.scrollLeft > 4);
        wrapper.classList.toggle("has-right", scroller.scrollLeft < maxScroll - 4);
        if (btnPrev) btnPrev.disabled = scroller.scrollLeft <= 4;
        if (btnNext) btnNext.disabled = scroller.scrollLeft >= maxScroll - 4;
    };

    if (btnPrev) btnPrev.addEventListener("click", () =>
        scroller.scrollBy({ left: -340, behavior: "smooth" }));
    if (btnNext) btnNext.addEventListener("click", () =>
        scroller.scrollBy({ left: 340, behavior: "smooth" }));

    // Drag-to-scroll (v2 — с порогом)
    let isDown = false, isDragging = false, startX = 0, startScroll = 0;

    scroller.addEventListener("mousedown", (e) => {
        isDown = true;
        isDragging = false;
        startX = e.pageX;
        startScroll = scroller.scrollLeft;
    });

    scroller.addEventListener("mousemove", (e) => {
        if (!isDown) return;
        const dx = e.pageX - startX;
        if (!isDragging && Math.abs(dx) > 5) {
            isDragging = true;
            scroller.classList.add("dragging");
        }
        if (isDragging) {
            e.preventDefault();
            scroller.scrollLeft = startScroll - dx;
        }
    });

    const stopDrag = () => {
        isDown = false;
        isDragging = false;
        scroller.classList.remove("dragging");
    };
    scroller.addEventListener("mouseleave", stopDrag);
    scroller.addEventListener("mouseup", stopDrag);
    scroller.addEventListener("mousemove", (e) => {
        if (!isDown) return;
        e.preventDefault();
        scroller.scrollLeft = startScroll - (e.pageX - startX);
    });

    scroller.addEventListener("scroll", updateButtons);
    window.addEventListener("resize", updateButtons);
    updateButtons();
});

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

    // Drag-to-scroll
    let isDown = false, startX = 0, startScroll = 0;
    scroller.addEventListener("mousedown", (e) => {
        isDown = true;
        scroller.classList.add("dragging");
        startX = e.pageX;
        startScroll = scroller.scrollLeft;
    });
    const stopDrag = () => {
        isDown = false;
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

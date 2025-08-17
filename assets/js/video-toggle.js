document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".more-button").forEach(btn => {
    btn.addEventListener("click", () => {
      const target = document.querySelector(btn.dataset.target);
      if (!target) return;

      target.querySelectorAll(".hidden").forEach(fig => {
        fig.classList.remove("hidden");
        const ifr = fig.querySelector("iframe[data-src]");
        if (ifr) ifr.src = ifr.dataset.src;
      });

      btn.remove();
    });
  });
});

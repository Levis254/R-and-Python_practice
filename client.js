document.addEventListener("DOMContentLoaded", function() {
    const galleryContainer = document.querySelector(".gallery-container");
    let currentIndex = 0;
  
    setInterval(() => {
      currentIndex = (currentIndex + 1) % galleryContainer.children.length;
      galleryContainer.style.transform = `translateX(-${currentIndex * 100}%)`;
    }, 15000);
  });
  
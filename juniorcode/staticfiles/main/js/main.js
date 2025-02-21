const menuIMG = document.getElementById('menu-img');
document.addEventListener('mousemove', (event) => {
    const x = -((event.clientX * .3) / 8);
    const y = -((event.clientY * .3) / 8);

    menuIMG.style.transform = `translate(${x}px, ${y}px)`;
    menuIMG.style.transition = 'transform 0.1s ease';
});
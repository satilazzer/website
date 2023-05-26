let zapis = document.querySelectorAll('.zapis');
let header = document.querySelector('#header');
let bottom_header = document.querySelector('.bottom_header');
let choose_city = document.querySelector('.choose_city');
let wrapper = document.querySelector('.wrap');
let cover = document.querySelector('.cover')
let close = document.querySelector('.close');
let whatsapp = document.querySelector('.whatsapp_icon');
let burger = document.querySelector('.header_burger');
let header_navbar = document.querySelector('.bottom_header .nav_list');
/*
window.addEventListener('scroll', function(){
    let scrollY = window.scrollY;
    if (scrollY>200){
        header.classList.add('header_scroll');
        bottom_header.classList.add('bottom_header_scroll');
    }
    else{
        header.classList.remove('header_scroll');
        bottom_header.classList.remove('bottom_header_scroll');
    }
});
*/

burger.addEventListener('click', function(){
    bottom_header.classList.toggle('bottom_header_burger');
    header_navbar.classList.toggle('nav_list_burger');
});

for (let zap of zapis){
    zap.addEventListener('click', function(){
        choose_city.classList.add('choose_city_active');
        cover.classList.add('negligible');
        wrapper.classList.add('hide');
    });
}


close.addEventListener('click', function(){
    choose_city.classList.remove('choose_city_active');
    cover.classList.remove('negligible');
    wrapper.classList.remove('hide');
});






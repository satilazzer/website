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
let see_more = document.querySelector('.see_more a');
let all_gallery = document.querySelector('.all_gallery');
let choose_city_see_more = document.querySelector('.choose_city_see_more');
let confirm_city = document.querySelector('.confirm_city');
let address = document.querySelector('.address');
let shipping_form = document.querySelector('.shipping_info');
let shipping_img = document.querySelector('.shipping_img');
let payment_type_cash = document.querySelector('.payment__type--paypal');
let payment_type_card = document.querySelector('.payment__type--cc');
let card_input_details = document.querySelector('.form__cc');
let btn_cash = document.querySelector('.btn_cash');
let btn_card = document.querySelector('.btn_card');
const customSelect = document.querySelector(".custom-select");
const selectBtn = document.querySelector(".select-button");

const selectedValue = document.querySelector(".selected-value");
const optionsList = document.querySelectorAll(".select-dropdown li");

// add click event to select button

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
close.addEventListener('click', function(){
    choose_city.classList.remove('choose_city_active');
    cover.classList.remove('negligible');
    wrapper.classList.remove('hide');
});

burger.addEventListener('click', function(){
    bottom_header.classList.toggle('bottom_header_burger');
    header_navbar.classList.toggle('nav_list_burger');
});

window.addEventListener('scroll', function(){
    if (!(sessionStorage.getItem("is_city_choosed") == "True")){
        choose_city.classList.add('choose_city_active');
        cover.classList.add('negligible');
        wrapper.classList.add('hide');
    }
});

confirm_city.addEventListener('click', function(){
    choose_city.classList.remove('choose_city_active');
    sessionStorage.setItem("is_city_choosed", "True");
    cover.classList.remove('negligible');
    wrapper.classList.remove('hide');
});

address.addEventListener('click', function(){
    shipping_form.classList.add('active');
    cover.classList.add('negligible');
    wrapper.classList.add('hide');
});

shipping_img.addEventListener('click', function(){
    shipping_form.classList.remove('active');
    cover.classList.remove('negligible');
    wrapper.classList.remove('hide');
});

payment_type_cash.addEventListener('click', function(){
    payment_type_cash.classList.add('active_one');
    payment_type_card.classList.remove('active_one');
    card_input_details.classList.add('hide_card_details');
    btn_cash.classList.add('active_btn');
    btn_card.classList.add('hide_card_details');
});

payment_type_card.addEventListener('click', function(){
    payment_type_card.classList.add('active_one');
    payment_type_cash.classList.remove('active_one');
    card_input_details.classList.remove('hide_card_details');
    btn_cash.classList.remove('active_btn');
    btn_card.classList.remove('hide_card_details');
});

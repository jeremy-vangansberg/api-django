'use strict';


const info_p = document.querySelector('.api_info');
const btn = document.querySelector('.btn-primary');
const csrf = document.getElementsByName('csrfmiddlewaretoken')
const form = document.getElementById('p-form')

form.addEventListener('submit', e => {
    e.preventDefault()
    const fd = new FormData();
    fd.append('csrfmiddlewaretoken', csrf[0].value)

    $.ajax({
        type: "POST",
        data: fd
    })
})



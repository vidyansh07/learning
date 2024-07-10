// alert("Hello Er Govind Thakur");
const icon = document.querySelector('#icon')
const ul = document.querySelector('#ul')

const li =document.querySelectorAll('li')

// ul.style.display = "none"

li.forEach((data) => {
   console.log(data)
   return data.classList.add("color")
})


icon.addEventListener('click', () => {
ul.style.display = "flex"
ul.style.transition ="5s"
icon.style.display = "none"
})
let close = document.querySelector('#close')

close.onclick = () => {
   icon.style.display = "flex"
   ul.style.transition = "0.9s"
   ul.style.display = "none"
}
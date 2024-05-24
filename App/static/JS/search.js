const wrapper = document.querySelector(".wrapper");
const select_btn = document.querySelector(".select_btn");
const options = document.querySelector(".options");
const search = document.querySelector(".Aone");

select_btn.addEventListener("click", () => {
    wrapper.classList.toggle('active');
    addCities();
})

const wrapper2 = document.querySelector(".wrapper2");
const select_btn2 = document.querySelector(".select_btn2");
const options2 = document.querySelector(".options2");
const search2 = document.querySelector(".search2");

select_btn2.addEventListener("click", () => {
    wrapper2.classList.toggle('active');
    addCities2();
})

// const cities = ["Adalaj", "Adipur", "Ahmedabad", "Alang", "Amreli", "Anand", "Anjar", "Ankleshwar", "Bardoli", "Bharuch", "Bhavnagar", "Bhuj", "Botad", "Chala", "Chandkheda", "Chorwad", "Dabhoi", "Dahod", "Dahej", "Dakor", "Daman", "Dascroi", "Deesa", "Dehgam", "Devgadbaria", "Dhandhuka", "Dhangadhra", "Dharampur", "Dholka", "Dhoraji", "Dwarka", "Gadhada", "Gandhidham", "Gandhinagar", "Godhra", "Gondal", "Halol", "Halvad", "Jamnagar", "Jambusar", "Jetpur", "Junagadh", "Kadi", "Kalol", "Kapadwanj", "Kapadvanj", "Karamsad", "Keshod", "Khambhalia", "Khedbrahma", "Kosamba", "Kutch", "Lathi", "Limdi", "Limbdi", "Mahuva", "Malpur", "Mandvi", "Mangrol", "Manavadar", "Modasa", "Morbi", "Nadiad", "Navsari", "Padra", "Palanpur", "Pardi", "Patan", "Patdi", "Petlad", "Porbandar", "Rajkot", "Rajpipla", "Rajpur", "Rajula", "Ranavav", "Rapar", "Salaya", "Sanand", "Savarkundla", "Sayad", "Sayan", "Sidhpur", "Somnath", "Songadh", "Surat", "Surendranagar", "Sutrapada", "Surat", "Talaja", "Thangadh", "Umargam", "Umreth", "Unjha", "Upleta", "Valsad", "Vallabh Vidhyanagar", "Vapi", "Vav", "Vadnagar", "Vadodara", "Vallabh Vidhyanagar", "Valsad", "Vapi", "Vav", "Veraval", "Vijalpor", "Vijapur", "Viramgam", "Visavadar", "Visnagar", "Vyara", "Wadhwan", "Wankaner"];

const cities = [ "Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"];

//1
function addCities(selectedCities) {
    options.innerHTML = "";
    cities.forEach(city => {
        let isSelected = cities == selectedCities?"selected":""
        let li = `<li onclick="updateName(this)" class="${isSelected}">${city}</li>`;
        options.insertAdjacentHTML('beforeend', li);
    })
}
function addCities2(selectedCities) {

    options2.innerHTML = "";
    cities.forEach(city => {
        let isSelected2 = cities == selectedCities?"selected":""
        let li = `<li onclick="updateName2(this)" class="${isSelected2}">${city}</li>`;
        options2.insertAdjacentHTML('beforeend', li);
    })
}

//2
function updateName(selectedList) {
    search.value = "";
    addCities(selectedList.innerText);
    wrapper.classList.remove('active');
    // arrow.classList.toggle('fa-angle-up');
    select_btn.firstElementChild.innerText = selectedList.innerText;
    document.querySelector('#source').value = selectedList.innerText;
}

function updateName2(selectedList) {
    search2.value = "";
    addCities2(selectedList.innerText);
    wrapper2.classList.remove('active');
    // arrow2.classList.toggle('fa-angle-up');
    select_btn2.firstElementChild.innerText = selectedList.innerText;
    document.querySelector('#destination').value = selectedList.innerText;
}

//3
search.addEventListener("keyup", () => {
    let arr = [];
    let searchVal = search.value.toLowerCase();
    arr = cities.filter(data => {
        return data.toLowerCase().startsWith(searchVal);
    }).map(data => `<li onclick="updateName(this)">${data}</li>`).join("");
    console.log(arr);
    console.log(searchVal);
    options.innerHTML = arr ? arr : `<p>Oops ! state not found </p>`;
})

search2.addEventListener("keyup", () => {
    let arr2 = [];
    let searchVal2 = search2.value.toLowerCase();
    arr2 = cities.filter(data => {
        return data.toLowerCase().startsWith(searchVal2);
    }).map(data => `<li onclick="updateName2(this)">${data}</li>`).join("");
    console.log(arr2);
    console.log(searchVal2);
    options2.innerHTML = arr2 ? arr2 : `<p>Oops ! state not found </p>`;
})





// slider js 
let nextDom = document.getElementById('next');
let prevDom = document.getElementById('prev');

let slider = document.querySelector('.slider');
let list = document.querySelector('.slider .list');
let thumb = document.querySelector('.slider .thumbnail');


nextDom.onclick = function () {
    showSlider('next');
}
prevDom.onclick = function () {
    showSlider('prev');
}

let timeRunning = 2000;
let timeAutoNext = 4000; 
let runTimeOut;
let runAutoRun = setTimeout(()=>{
    nextDom.click();
},timeAutoNext);

function showSlider(type) {
    let itemSlider = document.querySelectorAll('.slider .list .item ');
    let itemThumb = document.querySelectorAll('.slider .thumbnail .item');

    if (type === "next") {
        list.appendChild(itemSlider[0]);
        thumb.appendChild(itemThumb[0]);
        slider.classList.add('next');
    } else {
        let positionLastItem = itemSlider.length - 1;
        list.prepend(itemSlider[positionLastItem]);
        thumb.prepend(itemThumb[positionLastItem]);
        slider.classList.add('prev');
    }

    clearTimeout(runTimeOut);
    runTimeOut = setTimeout(() => {
        slider.classList.remove('next');
        slider.classList.remove('prev');
    }, timeRunning)
    clearTimeout(runAutoRun);
    runAutoRun = setTimeout(()=>{
        nextDom.click();
    },timeAutoNext);
}

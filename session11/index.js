const title = document.getElementById('title');
title.style.color = 'red';
// cont titlelength = title.length;
title.innerHTML = '쟈스 빠르네요';

const divs = document.querySelectorAll('div');
for (let i = 0; i < divs.length; i++) {
    // console.log(divs[i]);
    const currentDiv = divs[i];
    currentDiv.style.height = '100px';
    currentDiv.style.width = '100%';
    currentDiv.innerText = `${i+1}번째 Div`;
}
console.log(divs[i]);
console.log(divs);
console.log(title);

const subtitle = document.querySelector('#title1');
console.log(subTitle);

//     if (titlelength > 20) {
//         title.style.color = "red";
//     } else {
//         title.style.color = 'blue';
//     }
// // (조건문) ? (참일 경우) : (거짓일 경우)
//     titlelength > 20
//     ? (title.style.color = 'red')
//     : (title.style.color = 'blue');

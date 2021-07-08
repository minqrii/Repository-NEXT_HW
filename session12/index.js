const parent = document.querySelector(".parent");
const son1 = document.querySelector("#son1");
const son2 = document.querySelector("#son2");
const children = parent.querySelectorAll(".child");


for (let i=0; i<2; i++) {
    console.log(children[i]);
    children[i].classList.add("red");
}

son1.textContent = "오늘 정말 힘들군요...";

const sj = document.createElement("div");
const yena = document.createElement("p");

sj.appendChild(yena);
document.body.appendChild(sj);

sj.setAttribute("id", "sj");
sj.setAttribute("class", "parent");
yena.setAttribute("id", "yena");
yena.setAttribute("class", "child");

yena.texthtml("저는 예나입니다.");
    // children.classlist.add("red");

// console.log(parent, son1, son2);

// son1.classList.add("red");
// son2.classList.add("red");
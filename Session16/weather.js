const input = document.querySelector("#city");
const button = document.querySelector("#submit");
const weatherBox = document.querySelector("#weatherBox");

const API_KEY = "5dcf284d069dcb6e679d12aba2c18dc1";

button.addEventListener("click", async () => {
  //input의 값을 가져와서 도시이름으로 url에 넣는다.
  const city = input.value;

  try {
    // current weather
    // const res = await axios.get(
    //   `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${API_KEY}`
    // );
    // console.log(res);

    // //res에서 원하는 값 가져오기
    // const { main, description, icon } = res.data.weather[0];
    // const temp = Math.round(res.data.main.temp - 273.15);
    // const name = res.data.name;
    
    // //사용자에게 보여주기
    // weatherBox.innerHTML = `
    //   <div class="name">${name}</div>
    //   <img class="icon" src="http://openweathermap.org/img/w/${icon}.png">
    //   <div class="main">${main}</div>
    //   <div class="description">${description}</div>
    //   <div class="temp">${temp}°C</div>
    // `;

    // forecast 4days
  const forecast = await axios.get(
    `https://api.openweathermap.org/data/2.5/forecast/?q=${city}&appid=${API_KEY}`
  );

  for (let i = 0; i < 6; i++) {
    const {main, description, icon} = forecast.data.list[i].weather[0];
    const temp = Math.round(forecast.data.list[i].main.temp - 273.15);
    const time = forecast.data.list[i].dt_txt;
    const newtime = []
    for (let j = 11; j < 16; j++) {
      newtime.push(time[j])
    }
    const newtimestring = newtime.join('')
      const $weatherElement = `
      <div class="content">
          <div class="time">${newtimestring}</div>
          <img class="icon" src="http://openweathermap.org/img/w/${icon}.png">
          <div class="main">날씨 : ${main}</div>
          <div class="description">설명 : ${description}</div>
          <div class="temp">온도 : ${temp}°C</div>
      </div>
        `
      weatherBox.insertAdjacentHTML('beforeend', $weatherElement);
  }
  const cityname = forecast.data.city.name
  const citybox = document.getElementById('citybox')
  citybox.innerHTML = `In ${cityname}`
  console.log(forecast)
  } catch (error) {
    console.log(error);
  }
});

// 로고 바꾸기
    const randomnumber = Math.floor(Math.random());
    document.getElementsByClassName('logo').style=`content="\f0${randomnumber}"`;

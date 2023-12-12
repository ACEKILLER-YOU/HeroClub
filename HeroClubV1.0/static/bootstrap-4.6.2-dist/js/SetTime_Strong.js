const strong_startButton = document.querySelector('#strong-start');
const strong_stopButton = document.querySelector('#strong-stop');
const strong_time = document.querySelector('#strong-time');
const strong_commitButton = document.querySelector('#strong-submit');

let strong_startTime, strong_endTime, strong_elapsedTime, strong_timerInterval;

function formatTime(time) {
    const hours = Math.floor(time / 3600).toString().padStart(2, '0');
    const minutes = Math.floor((time % 3600) / 60).toString().padStart(2, '0');
    const seconds = (time % 60).toString().padStart(2, '0');
    return `${hours}:${minutes}:${seconds}`;
}

    strong_startButton.addEventListener('click', () => {
      strong_startTime = Date.now();
      strong_timerInterval = setInterval(() => {
        strong_elapsedTime = Math.floor((Date.now() - strong_startTime) / 1000);
        strong_time.textContent = formatTime(strong_elapsedTime);
      }, 1000);
    });

    strong_stopButton.addEventListener('click', () => {
      strong_endTime = Date.now();
      clearInterval(strong_timerInterval);
      strong_elapsedTime = Math.floor((strong_endTime - strong_startTime) / 1000);
      strong_time.textContent = formatTime(strong_elapsedTime);


    strong_commitButton.addEventListener('click', () => {
        // 将耗时提交到后端
        fetch('/HeroClub/Strong_Use', {
        method: 'POST',
        body: JSON.stringify({ time: strong_elapsedTime, type: "strong" }),
        headers: {
          'Content-Type': 'application/json'
        }
      })
      .then(response => {
        if (response.ok) {
          console.log('提交成功！');
        } else {
          console.error('提交失败！');
        }
      })
      .catch(error => {
        console.error('提交失败：', error);
      });
    });
    });
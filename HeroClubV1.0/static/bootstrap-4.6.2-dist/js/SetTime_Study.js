const study_startButton = document.querySelector('#study-start');
const study_stopButton = document.querySelector('#study-stop');
const study_time = document.querySelector('#study-time');
const study_commitButton = document.querySelector('#study-submit');

let study_startTime, study_endTime, study_elapsedTime, study_timerInterval;

function formatTime(time) {
    const hours = Math.floor(time / 3600).toString().padStart(2, '0');
    const minutes = Math.floor((time % 3600) / 60).toString().padStart(2, '0');
    const seconds = (time % 60).toString().padStart(2, '0');
    return `${hours}:${minutes}:${seconds}`;
}

    study_startButton.addEventListener('click', () => {
      study_startTime = Date.now();
      study_timerInterval = setInterval(() => {
        study_elapsedTime = Math.floor((Date.now() - study_startTime) / 1000);
        study_time.textContent = formatTime(study_elapsedTime);
      }, 1000);
    });

    study_stopButton.addEventListener('click', () => {
      study_endTime = Date.now();
      clearInterval(study_timerInterval);
      study_elapsedTime = Math.floor((study_endTime - study_startTime) / 1000);
      study_time.textContent = formatTime(study_elapsedTime);


    study_commitButton.addEventListener('click', () => {
        // 将耗时提交到后端
        fetch('/HeroClub/Study_Use', {
        method: 'POST',
        body: JSON.stringify({ time: study_elapsedTime, type: "study" }),
        headers: {
          'Content-Type': 'application/json'
        }
      })
      .then(response => {
        if (response.ok) {
          console.log('提交成功！');
        } else {
          alert("提交失败")
          console.error('提交失败！');
        }
      })
      .catch(error => {
        alert("提交失败")
        console.error('提交失败：', error);
      });
    });
    });
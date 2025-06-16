<!DOCTYPE html>
<html lang="ar">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>ابدأ النقر ⭐</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      font-family: 'Arial', sans-serif;
      background: linear-gradient(to bottom, #1a1a2e, #16213e);
      color: white;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
    }
    h1 {
      font-size: 2.5em;
      margin-bottom: 10px;
    }
    #stats {
      font-size: 1.5em;
      margin-bottom: 20px;
    }
    #star-image {
      width: 150px;
      height: 150px;
      margin-bottom: 20px;
    }
    button {
      padding: 15px 30px;
      font-size: 1.5em;
      border: none;
      border-radius: 12px;
      background-color: #ffca28;
      color: #000;
      cursor: pointer;
      box-shadow: 0 0 15px #ffca28a1;
      transition: all 0.2s ease;
    }
    button:active {
      transform: scale(0.97);
    }
  </style>
</head>
<body>
  <h1>ابدأ النقر ❤️</h1>
  <div id="stats">⭐ <span id="stars">0</span> | ⚡ <span id="energy">10</span></div>
  <img id="star-image" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/HD_star_icon.svg/2048px-HD_star_icon.svg.png" alt="نجمة">
  <button onclick="collectStar()">🔘 اجمع نجمة</button>

  <script>
    let stars = 0;
    let energy = 10;
    const starsEl = document.getElementById("stars");
    const energyEl = document.getElementById("energy");

    function collectStar() {
      if (energy <= 0) {
        alert("⚠️ لا توجد طاقة كافية!");
        return;
      }
      stars++;
      energy--;
      updateDisplay();
    }

    function updateDisplay() {
      starsEl.textContent = stars;
      energyEl.textContent = energy;
    }

    // تجديد الطاقة كل 30 ثانية بحد أقصى 10
    setInterval(() => {
      if (energy < 10) {
        energy++;
        updateDisplay();
      }
    }, 30000);
  </script>
</body>
</html>

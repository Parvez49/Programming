function displayLocalTime() {
    const now = new Date();
    const timeString = now.toLocaleTimeString();
    document.getElementById('local-time').textContent = timeString;
  }
  
  document.addEventListener('DOMContentLoaded', () => {
    setInterval(displayLocalTime, 1000);
  });
  
const video = document.getElementById("raceVideo");
const telemetryDisplay = document.getElementById("telemetryDisplay");
const apiStart = "2025-04-13T18:00:00.000Z";
const videoOffset = 3;
const driverNumber = 1;

video.addEventListener("timeupdate", async () => {
  const currentTime = video.currentTime;
  try {
    const res = await fetch(
      `http://127.0.0.1:5000/sync_data?video_time=${currentTime}&api_start=${apiStart}&video_offset=${videoOffset}&driver_number=${driverNumber}`
    );
    const data = await res.json();
    telemetryDisplay.innerHTML = `
      <p>Speed: ${data.speed || 0} km/h</p>
      <p>Throttle: ${data.throttle || 0}%</p>
      <p>Brake: ${data.brake || 0}%</p>
      <p>Time: ${data.date}</p>
    `;
  } catch (err) {
    console.error("Error fetching telemetry:", err);
  }
});

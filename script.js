const form = document.getElementById("download-form");
const urlInput = document.getElementById("url");
const statusEl = document.getElementById("status");
const btn = document.getElementById("download-btn");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const url = urlInput.value.trim();
  const mode = document.querySelector('input[name="mode"]:checked').value;

  if (!url) {
    statusEl.textContent = "Please paste a YouTube link first.";
    statusEl.className = "status error";
    return;
  }

  btn.disabled = true;
  btn.textContent = "Downloading...";
  statusEl.textContent = "Fetching your file, please wait...";
  statusEl.className = "status loading";

  try {
    const res = await fetch("/download", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url, mode }),
    });

    if (!res.ok) {
      const errData = await res.json().catch(() => ({}));
      throw new Error(errData.error || "Download failed.");
    }

    const blob = await res.blob();
    const disposition = res.headers.get("Content-Disposition") || "";
    let filename = mode === "audio" ? "audio.mp3" : "video.mp4";
    const match = disposition.match(/filename\*?=(?:UTF-8'')?"?([^";]+)"?/i);
    if (match && match[1]) filename = decodeURIComponent(match[1]);

    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    link.remove();
    URL.revokeObjectURL(link.href);

    statusEl.textContent = "Done! Saved to your downloads folder.";
    statusEl.className = "status success";
  } catch (err) {
    statusEl.textContent = err.message;
    statusEl.className = "status error";
  } finally {
    btn.disabled = false;
    btn.textContent = "Download";
  }
});

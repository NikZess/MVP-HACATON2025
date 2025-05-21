const API_URL = "http://127.0.0.1:8000/api/v1"

document.querySelector("form").addEventListener("submit", async (e) => {
  e.preventDefault();

  const username = document.getElementById("username").value.trim();
  const password = document.getElementById("password").value;

  try {
      const response = await fetch(`${API_URL}/auth/login`, {
          method: "POST",
          headers: {
              "Content-Type": "application/json"
          },
          body: JSON.stringify({ username, password }),
          credentials: "include"
      });

      if (response.ok) {
          window.location.href = "/dashboard";
      } else {
          const errorData = await response.json();
          alert(`Ошибка: ${errorData.detail}`);
      }
  } catch (err) {
      alert("Ошибка соединения с сервером.");
      console.error(err);
  }
});

// Simple fetch helpers for demo. Adjust API endpoints as needed.

function show(el, data) {
  el.textContent = JSON.stringify(data, null, 2);
}

document.addEventListener('DOMContentLoaded', () => {
  const farmForm = document.getElementById('farm-form');
  const farmResult = document.getElementById('farm-result');
  const listBtn = document.getElementById('list-farms');
  const listResult = document.getElementById('list-result');
  const loginForm = document.getElementById('login-form');
  const loginResult = document.getElementById('login-result');

  if (farmForm) {
    farmForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const form = new FormData(farmForm);
      const body = Object.fromEntries(form.entries());
      try {
        const res = await fetch('/api/farms/', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(body)
        });
        const data = await res.json();
        show(farmResult, data);
      } catch (err) {
        show(farmResult, { error: err.message });
      }
    });
  }

  if (listBtn) {
    listBtn.addEventListener('click', async () => {
      try {
        const res = await fetch('/api/farms/');
        const data = await res.json();
        show(listResult, data);
      } catch (err) {
        show(listResult, { error: err.message });
      }
    });
  }

  if (loginForm) {
    loginForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const form = new FormData(loginForm);
      const body = Object.fromEntries(form.entries());
      try {
        // example: token endpoint for simplejwt
        const res = await fetch('/api/token/', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify(body)
        });
        const data = await res.json();
        show(loginResult, data);
        // store token in localStorage for manual testing
        if (data.access) localStorage.setItem('access', data.access);
      } catch (err) {
        show(loginResult, { error: err.message });
      }
    });
  }
});
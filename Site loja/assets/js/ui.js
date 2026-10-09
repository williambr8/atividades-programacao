function showToast(message) {
  const toast = document.createElement('div');
  toast.className = `fixed bottom-20 right-6 bg-black text-white px-6 py-4 rounded-2xl shadow-2xl z-[100]`;
  toast.innerHTML = message;
  document.body.appendChild(toast);

  setTimeout(() => toast.remove(), 3000);
}

function toggleCart() {
  alert("Carrinho em desenvolvimento (próxima etapa)");
  // Aqui você pode criar um drawer depois
}

// Voltar ao topo
window.onscroll = function() {
  const btn = document.getElementById('backToTop');
  if (btn) btn.style.display = window.scrollY > 400 ? "block" : "none";
};
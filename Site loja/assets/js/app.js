// assets/js/app.js - VERSÃO LIMPA

function renderProducts(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  container.innerHTML = '';

  products.forEach(product => {
    const html = `
      <div class="product-card bg-white rounded-3xl overflow-hidden cursor-pointer group" onclick="window.location.href='product.html'">
        <img src="${product.image}" alt="${product.name}" class="w-full h-96 object-cover transition-transform group-hover:scale-105">
        <div class="p-6">
          <h3 class="font-medium text-lg">${product.name}</h3>
          <p class="text-gold font-bold mt-2">R$ ${product.price.toFixed(2)}</p>
          
          <button onclick="event.stopImmediatePropagation(); addToCart(${product.id});" 
                  class="mt-4 w-full bg-black text-white py-3.5 rounded-2xl hover:bg-gold hover:text-black transition text-sm font-medium">
            Adicionar ao Carrinho
          </button>
        </div>
      </div>`;
    container.innerHTML += html;
  });
}

// Inicialização
document.addEventListener('DOMContentLoaded', () => {
  renderProducts('products-grid');
  renderProducts('shop-grid');
  updateCartCount();
});

// Funções mínimas (sem alert desnecessário)
function toggleSearch() {
  // Busca futura
}
window.verPromocao = function() {
  const nome  = document.querySelector('#produto').value.trim();
  const preco = Number(document.querySelector('#preco').value);
  if (!nome || !preco) {
    document.querySelector('#saida').textContent = 'Preencha produto e preço.';
    return;
  }
  const total = preco * 2 + (preco / 2);
  document.querySelector('#saida').innerHTML =
    `${nome} - Promoção: Leve 3 por R$: ${total.toFixed(2)}<br>` +
    `O 3º produto custa apenas R$: ${(preco / 2).toFixed(2)}`;
}
window.calcular = function() {
  const valor = Number(document.querySelector('#valor').value);
  const tempo = Number(document.querySelector('#tempo').value);
  if (!valor || !tempo) {
    document.querySelector('#saida').textContent = 'Preencha valor e tempo.';
    return;
  }
  const blocos = Math.ceil(tempo / 15);
  const total = blocos * valor;
  document.querySelector('#saida').innerHTML =
    `Valor a Pagar R$: ${total.toFixed(2)}`;
}
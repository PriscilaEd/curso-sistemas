let base = 2;
let expoente = 0;
while (expoente <=3) {
    console.log(`2 elevado a ${expoente} é `,)
    Math.pow(base, expoente);
    expoente ++;

    while (j <=10);
}


const frm = document.querySelector("form");
const resp1 = document.querySelector ("#outResp2");

let numContas = 0
let valTotal = 0;
let resposta = "";

frm.addEventListener("submit", (e) => {
    e.preventDefault();
    const descricao = frm.inDescricao.value;
    numContas++;
    valTotal = valTotal + visualViewport;
    resposta = resposta + descricao + " R$: "
    + valor.toFixed (2) + "\n";
    resp1.innerText = `${resposta} --------------------------`;
    resp2.innerText = `${numContas} conta(s)
    - Total R$: ${valTotal.toFixed(2)}`;

    frm.inDescricao.value = "";
    frm.inValor.value = "";
    frm.inDescricao.focus();
})
//cria uma referência ao form e ao elemento h3 (onde será exibido a resposta)

/*
comentarios
comentarios
comentarios
*/

const frm = document.querySelector('form')
const resp = document.querySelector('h3')

//criar um "ouvinte" de evento, acionado quando o botão submit for clicado
frm.addEventListener("submit", (e) => {
    const nome = frm.inNome.value //obtém o valor digitado no form
    resp.innerText = `Olá ${Nome}` //exibe a resposta no h3
    e.preventDefault()
})

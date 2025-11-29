const perguntasPre = [
    {
        texto: "O que é orçamento pessoal?",
        opcoes: [
            "Lista de tudo que eu quero comprar.",
            "Planejamento de quanto dinheiro entra e sai em um período.",
            "Registro apenas das dívidas.",
            "O valor que sobra no fim do mês."
        ],
        correta: 1
    },
    {
        texto:
            "Se você recebe R$ 1.000 e gasta R$ 1.200 todo mês, o que está acontecendo?",
        opcoes: [
            "Você está economizando R$ 200.",
            "Está tudo equilibrado, porque alguns gastos são supérfluos.",
            "Você está entrando em déficit/dívida de R$ 200 por mês.",
            "Isso não afeta nada no longo prazo."
        ],
        correta: 2
    },
    {
        texto:
            "Qual sequência representa bem o 'controle de gastos em 3 passos'?",
        opcoes: [
            "Anotar gastos, pagar dívidas, fazer mais dívidas.",
            "Anotar tudo, classificar gastos, ajustar/cortar e planejar.",
            "Guardar tudo na poupança sem olhar os gastos.",
            "Esperar sobrar dinheiro e depois anotar."
        ],
        correta: 1
    }
];

const perguntasPos = [
    {
        texto:
            "Você ganha R$ 1.500. Seguindo a ideia 50/30/20, quanto seria APROXIMADAMENTE para necessidades (moradia, contas, comida)?",
        opcoes: [
            "R$ 300",
            "R$ 750",
            "R$ 1.500",
            "R$ 1.200"
        ],
        correta: 1 
    },
    {
        texto:
            "Você quer comprar um fone de R$ 200, mas isso faria você estourar o orçamento deste mês. Qual a atitude mais saudável financeiramente?",
        opcoes: [
            "Comprar assim mesmo, porque você merece.",
            "Parcelar em 10x no cartão para não sentir.",
            "Rever o orçamento, ver se pode cortar algum gasto ou adiar a compra.",
            "Pedir emprestado para vários amigos."
        ],
        correta: 2
    },
    {
        texto:
            "Ao analisar seus gastos, você percebe que tem muito delivery e streaming. Eles se encaixam principalmente em qual tipo de gasto?",
        opcoes: [
            "Essenciais fixos.",
            "Variáveis e muitas vezes supérfluos.",
            "Impostos obrigatórios.",
            "Investimentos de longo prazo."
        ],
        correta: 1
    }
];


const telaInicial = document.getElementById("tela-inicial");
const telaPerguntas = document.getElementById("tela-perguntas");
const telaAula = document.getElementById("tela-aula");
const telaResultado = document.getElementById("tela-resultado");
const btnComecar = document.getElementById("btn-comecar");
const btnProxima = document.getElementById("btn-proxima");
const btnIrDesafios = document.getElementById("btn-ir-desafios");
const btnJogarNovamente = document.getElementById("btn-jogar-novamente");
const tituloEtapa = document.getElementById("titulo-etapa");
const textoEtapa = document.getElementById("texto-etapa");
const textoPergunta = document.getElementById("texto-pergunta");
const opcoesContainer = document.getElementById("opcoes");
const textoProgresso = document.getElementById("progresso");
const spanResPre = document.getElementById("res-pre");
const spanResPos = document.getElementById("res-pos");
const spanResDif = document.getElementById("res-dif");
const spanResSessoes = document.getElementById("res-sessoes");
const spanResMediaPre = document.getElementById("res-media-pre");
const spanResMediaPos = document.getElementById("res-media-pos");

let etapa = "pre";
let indicePergunta = 0;
let respostaSelecionada = null;
let acertosPre = 0;
let acertosPos = 0;

function trocarTela(telaAtivar) {
    [telaInicial, telaPerguntas, telaAula, telaResultado].forEach((tela) => {
        tela.classList.remove("ativa");
    });
    telaAtivar.classList.add("ativa");
}
function carregarPergunta() {
    const lista =
        etapa === "pre" ? perguntasPre : perguntasPos;
    const perguntaAtual = lista[indicePergunta];
    textoPergunta.textContent = perguntaAtual.texto;
    opcoesContainer.innerHTML = "";
    respostaSelecionada = null;
    btnProxima.disabled = true;
    perguntaAtual.opcoes.forEach((op, index) => {
        const btn = document.createElement("button");
        btn.classList.add("btn-opcao");
        btn.textContent = op;
        btn.addEventListener("click", () =>
            selecionarOpcao(index, btn)
        );
        opcoesContainer.appendChild(btn);
    });
    textoProgresso.textContent = `Pergunta ${
        indicePergunta + 1
    } de ${lista.length}`;
}
function selecionarOpcao(indice, botao) {
    respostaSelecionada = indice;
    const botoes = document.querySelectorAll(".btn-opcao");
    botoes.forEach((b) => b.classList.remove("selecionada"));
    botao.classList.add("selecionada");
    btnProxima.disabled = false;
}
function corrigirResposta() {
    const lista =
        etapa === "pre" ? perguntasPre : perguntasPos;
    const perguntaAtual = lista[indicePergunta];
    if (respostaSelecionada === perguntaAtual.correta) {
        if (etapa === "pre") {
            acertosPre++;
        } else {
            acertosPos++;
        }
    }
}
function atualizarTextoEtapa() {
    if (etapa === "pre") {
        tituloEtapa.textContent = "Pré-teste";
        textoEtapa.textContent =
            "Responda sem pesquisar nem pedir ajuda. É só para ver como está seu conhecimento antes da mini-aula.";
    } else {
        tituloEtapa.textContent = "Desafios (pós-teste)";
        textoEtapa.textContent =
            "Agora responda com base no que aprendeu. Vamos ver a diferença!";
    }
}

function salvarEstatisticas(acertosPreRodada, acertosPosRodada) {
    const dadosBrutos = localStorage.getItem("financasNaPraticaStats");
    let stats;

    if (dadosBrutos) {
        stats = JSON.parse(dadosBrutos);
    } else {
        stats = {
            sessoes: 0,
            somaPre: 0,
            somaPos: 0
        };
    }
    stats.sessoes += 1;
    stats.somaPre += acertosPreRodada;
    stats.somaPos += acertosPosRodada;
    localStorage.setItem(
        "financasNaPraticaStats",
        JSON.stringify(stats)
    );
    return stats;
}

function mostrarResultado() {
    spanResPre.textContent = `${acertosPre} / ${perguntasPre.length}`;
    spanResPos.textContent = `${acertosPos} / ${perguntasPos.length}`;
    const dif = acertosPos - acertosPre;
    const prefixo = dif >= 0 ? "+" : "";
    spanResDif.textContent = `${prefixo}${dif}`;
    const stats = salvarEstatisticas(acertosPre, acertosPos);
    const mediaPre =
        stats.somaPre / stats.sessoes;
    const mediaPos =
        stats.somaPos / stats.sessoes;
    spanResSessoes.textContent = stats.sessoes;
    spanResMediaPre.textContent =
        mediaPre.toFixed(2) +
        ` / ${perguntasPre.length}`;
    spanResMediaPos.textContent =
        mediaPos.toFixed(2) +
        ` / ${perguntasPos.length}`;
}

btnComecar.addEventListener("click", () => {
    etapa = "pre";
    indicePergunta = 0;
    acertosPre = 0;
    acertosPos = 0;
    atualizarTextoEtapa();
    carregarPergunta();
    trocarTela(telaPerguntas);
});
btnProxima.addEventListener("click", () => {
    corrigirResposta();
    const lista =
        etapa === "pre" ? perguntasPre : perguntasPos;
    const ultimaPergunta =
        indicePergunta === lista.length - 1;
    if (!ultimaPergunta) {
        indicePergunta++;
        carregarPergunta();
    } else {
        if (etapa === "pre") {
            trocarTela(telaAula);
        } else {
            mostrarResultado();
            trocarTela(telaResultado);
        }
    }
});
btnIrDesafios.addEventListener("click", () => {
    etapa = "pos";
    indicePergunta = 0;
    atualizarTextoEtapa();
    carregarPergunta();
    trocarTela(telaPerguntas);
});
btnJogarNovamente.addEventListener("click", () => {
    etapa = "pre";
    indicePergunta = 0;
    acertosPre = 0;
    acertosPos = 0;
    atualizarTextoEtapa();
    carregarPergunta();
    trocarTela(telaPerguntas);
});
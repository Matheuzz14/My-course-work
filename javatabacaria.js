// A página que está sendo exibida, depois de carregar todos os arquivos vai executar a função anônima que recebeu.
window.onload = function(){ // Window se refere ao objeto global que representa a janela do navegador onde a página está sendo exibida. // Onload é acionado dps de toda a página carregar.
    const aviso = document.getElementById("aviso");
    // Seleciona o elemento que possui o id "aviso" e armazena dentro de uma variável constante.
    const confirmacao = sessionStorage.getItem("confirmou");
    // Local Storage = área de armazenamento do navegador, retem informações mesmo após ser fechado, e o SessionStorage retem informação enquanto a página estiver aberta, mas quando fechada, as informações são esquecidas. E o getItem usado para acessar um valor dentro de um dos dois Storage.
    // A informação dentro da váriavel "confirmou" é armazenada na variável constante "confimação"
    if (confirmacao === "true"){
        // É uma condicional normal, se a pessoa já tiver entrado no site ele não mostra o popup, caso contrário, o aviso aparece.
        aviso.style.display = "none";
        body.classList.remove("blur-background")
    }else{
        aviso.style.display = "block";
    };
//addEventListener = adiciona um evento (ou função) quando a pessoa executar determinada ação, nesse caso, quando apertar o botão.
    document.getElementById("confirmacao").addEventListener("click", function(){
    const aviso = document.getElementById("aviso");
    //Muda a configuração do popup para não aparecer depois que a pessoa aperta o botão de prosseguir.
    aviso.style.display = "none";
    //Adiciona true a variavel que será testada caso a página recarregue. setItem = adiciona um valor a uma variavel do sessionStorage ou localStorage.
    sessionStorage.setItem("confirmou", "true");
});
};

const botoesCarrossel = document.querySelectorAll(".botao");
const imagens = document.querySelectorAll(".banner");
function passar(){
    const botaoSelecionado = document.querySelector(".selecionado");
    let indiceAtual = Array.from(botoesCarrossel).indexOf(botaoSelecionado);
    let novIndice = (indiceAtual + 1) % botoesCarrossel.length;
    botaoSelecionado.classList.remove("selecionado");
    botoesCarrossel[novIndice].classList.add("selecionado");
    const imagemOn = document.querySelector(".On");
    imagemOn.classList.remove("On");
    imagens[novIndice].classList.add("On");
};
let intervalo = setInterval(passar, 7000);
botoesCarrossel.forEach((botao, indice) => {
    botao.addEventListener("click", () => {
        clearInterval(intervalo)
        //Desmarcar botão anteriormente selecionado
        const botaoSelecionado = document.querySelector(".selecionado");
        botaoSelecionado.classList.remove("selecionado");
        //Marcar o botão que foi selecionado
        botao.classList.add("selecionado");
        //Esconder o banner ativo
        const imagemOn = document.querySelector(".On");
        imagemOn.classList.remove("On")
        //Banner correspondente ao botão
        imagens[indice].classList.add("On")
        setTimeout(() => {
            intervalo = setInterval(passar, 7000)
        },3000);
    });
});

let atualIndice = 0;

function passarProduto() {
    const secoes = document.querySelectorAll('.produtosCarrossel');
    if (secoes.length === 0) return;

    // Remover a classe Ativo da seção atual
    secoes[atualIndice].classList.remove('ativo');

    // Atualizar o índice (loop infinito)
    atualIndice = (atualIndice + 1) % secoes.length;

    // Adicionar a classe Ativo na nova seção
    secoes[atualIndice].classList.add('ativo');
}

function voltarProduto() {
    const secoes = document.querySelectorAll('.produtosCarrossel');
    if (secoes.length === 0) return;

    // Remover a classe Ativo da seção atual
    secoes[atualIndice].classList.remove('ativo');

    // Atualizar o índice (loop infinito para voltar)
    atualIndice = (atualIndice - 1 + secoes.length) % secoes.length;

    // Adicionar a classe Ativo na nova seção
    secoes[atualIndice].classList.add('ativo');
}

// Inicializa o carrossel
document.addEventListener('DOMContentLoaded', () => {
    const secoes = document.querySelectorAll('.produtosCarrossel');
    if (secoes.length > 0) {
        secoes[0].classList.add('ativo'); // Mostra a primeira seção
    }

    // Adiciona eventos aos botões
    document.querySelector('.botaoAvanc').addEventListener('click', passarProduto);
    document.querySelector('.botaoVoltar').addEventListener('click', voltarProduto);
});
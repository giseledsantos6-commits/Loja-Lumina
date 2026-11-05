# Loja Lumina

Site de loja virtual simples feito com **Python** e **Flask**. Possui página inicial, catálogo de produtos carregado de um arquivo JSON e formulário de contato.

## Estrutura do projeto

```
Loja-Lumina/
├── app.py                  # Servidor Flask (arquivo principal)
├── requirements.txt        # Dependências do projeto
├── README.md               # Este arquivo
├── data/
│   └── produtos.json       # Lista de produtos (nome, preço, imagem)
├── templates/
│   ├── base.html           # Layout comum (cabeçalho e rodapé)
│   ├── index.html          # Página inicial
│   ├── produtos.html       # Catálogo de produtos
│   └── contato.html        # Página de contato
└── static/
    ├── css/style.css       # Estilos do site
    ├── js/main.js          # Interações (menu, botão "adicionar")
    └── img/
        ├── logo.png        # Logo da Lumina
        └── produtos/       # Fotos dos produtos
```

## Requisitos

- Python 3.9 ou superior
- pip

## Como rodar

1. Abra um terminal na pasta do projeto:

   ```bash
   cd Loja-Lumina
   ```

2. (Opcional, recomendado) Crie e ative um ambiente virtual:

   ```bash
   # Linux / macOS
   python3 -m venv venv
   source venv/bin/activate

   # Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Inicie o servidor:

   ```bash
   python app.py
   ```

5. Abra no navegador: <http://127.0.0.1:5000>

Para parar o servidor, pressione `Ctrl + C` no terminal.

## Rotas

| Rota             | Método     | Descrição                                  |
|------------------|------------|--------------------------------------------|
| `/`              | GET        | Página inicial com produtos em destaque    |
| `/produtos`      | GET        | Catálogo completo                          |
| `/contato`       | GET, POST  | Formulário de contato                      |
| `/api/produtos`  | GET        | Lista de produtos em JSON                  |

## Cadastrando produtos

Os produtos ficam em `data/produtos.json`, como uma lista de objetos:

```json
[
  {
    "nome": "Luminária Aurora",
    "preco": 129.90,
    "imagem": "img/produtos/aurora.jpg"
  }
]
```

- `nome`: nome exibido no catálogo.
- `preco`: número (use ponto como separador decimal). O site formata como `R$ 129,90`.
- `imagem`: caminho da foto dentro da pasta `static/`.

Basta salvar o arquivo e recarregar a página para ver as mudanças.

## Antes de publicar

- Troque a `secret_key` em `app.py` por uma chave segura (de preferência lida de uma variável de ambiente).
- Desative o modo `debug` (`app.run(debug=True)`).
- Use um servidor de produção, como Gunicorn, em vez do servidor de desenvolvimento do Flask.

## Tecnologias

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- HTML, CSS e JavaScript

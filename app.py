"""Loja Lumina - servidor Flask.

Como rodar:
    pip install -r requirements.txt
    python app.py
Depois abra http://127.0.0.1:5000 no navegador.
"""

import json
from pathlib import Path

from flask import Flask, flash, jsonify, redirect, render_template, request, url_for

BASE_DIR = Path(__file__).resolve().parent
PRODUTOS_JSON = BASE_DIR / "data" / "produtos.json"

app = Flask(__name__)
# Necessário para usar flash(). Em produção, defina via variável de ambiente.
app.secret_key = "lumina-dev-key-troque-em-producao"


def carregar_produtos():
    """Lê a lista de produtos do arquivo JSON.

    Retorna uma lista vazia se o arquivo não existir ou estiver inválido,
    para o site não quebrar.
    """
    try:
        with open(PRODUTOS_JSON, encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


@app.template_filter("brl")
def formatar_brl(valor):
    """Formata um número como moeda brasileira: 1234.5 -> R$ 1.234,50"""
    try:
        texto = f"{float(valor):,.2f}"
    except (TypeError, ValueError):
        return valor
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}"


@app.route("/")
def index():
    produtos = carregar_produtos()
    destaques = produtos[:3]  # os 3 primeiros aparecem na página inicial
    return render_template("index.html", destaques=destaques)


@app.route("/produtos")
def produtos():
    return render_template("produtos.html", produtos=carregar_produtos())


@app.route("/contato", methods=["GET", "POST"])
def contato():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip()
        mensagem = request.form.get("mensagem", "").strip()

        if not (nome and email and mensagem):
            flash("Por favor, preencha todos os campos.", "erro")
            return redirect(url_for("contato"))

        # Aqui você poderia enviar um e-mail ou salvar em um banco de dados.
        print(f"[Contato] {nome} <{email}>: {mensagem}")
        flash(f"Obrigado, {nome}! Recebemos sua mensagem.", "sucesso")
        return redirect(url_for("contato"))

    return render_template("contato.html")


@app.route("/api/produtos")
def api_produtos():
    """Retorna os produtos em JSON (útil para o main.js)."""
    return jsonify(carregar_produtos())


@app.errorhandler(404)
def pagina_nao_encontrada(erro):
    return render_template("index.html", destaques=carregar_produtos()[:3]), 404


if __name__ == "__main__":
    app.run(debug=True)

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from Controller.item_controller import ItemController


controller = ItemController()

st.title("Cadastro de itens")

st.subheader("Adicionar novo item")
descricao = st.text_input("Descrição do item")
quantidade = st.number_input("Quantidade", min_value=1, step=1)

if st.button("Salvar"):
    if descricao != "":
        controller.criarItem(descricao, quantidade)
        st.success("Item cadastrado com sucesso")
    else:
        st.warning("Digite uma descrição antes de salvar")

st.subheader("Itens cadastrados")
itens = controller.obterTodosOsItens()

if len(itens) > 0:
    for item in itens:
        st.write(f"ID: {item.id} | {item.descricao} | Quantidade: {item.quantidade}")
else:
    st.info("Nenhum item cadastrado ainda")
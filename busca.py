import streamlit as st
import requests

# URL do logo
logo_url = "https://i.imgur.com/WNB3KPh.jpeg"

# para centralizar
st.markdown(
    f"""
    <style>
        .centered-logo {{
            display: flex;
            justify-content: center;
        }}
    </style>
    <div class="centered-logo">
        <img src="{logo_url}" width="300">
    </div>
    """,
    unsafe_allow_html=True
)

# Função para consultar o CEP na API dos Correios
def buscar_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        if 'erro' not in dados:
            return dados
        else:
            return None
    else:
        return None

# Interface com o usuário
st.title("Web App: Busca CEP!")
st.write("Digite o CEP p/ consultar o endereço e pressione Enter.")

cep_input = st.text_input("Obs.: apenas números", "")

if cep_input:
    st.write("Buscando informações...")
    # Remover caracteres não numéricos do CEP...
    cep = ''.join(filter(str.isdigit, cep_input))
    
    if len(cep) == 8:  # Verifica se o CEP tem 8 dígitos
        resultado = buscar_cep(cep)
        if resultado:
            st.subheader(f"Endereço encontrado para o CEP {cep}:")
            st.write(f"**Logradouro:** {resultado['logradouro']}")
            st.write(f"**Bairro:** {resultado['bairro']}")
            st.write(f"**Cidade:** {resultado['localidade']}")
            st.write(f"**UF:** {resultado['uf']}")
        else:
            st.error("CEP não encontrado ou inválido.")
    else:
        st.error("Digite um CEP válido com 8 dígitos.")

# Rodapé c/ informações de contato
st.markdown("""
---
#### Busca CEP, via API pública dos Correios
💬 Por Ary Ribeiro. Contato, através do email: aryribeiro@gmail.com
""")
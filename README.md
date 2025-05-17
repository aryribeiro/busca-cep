Obs.: caso o app esteja no modo "sleeping" (dormindo) ao entrar, basta clicar no botão que estará disponível e aguardar, para ativar o mesmo.
![print busca cep](https://github.com/user-attachments/assets/8c91ed05-77cf-4b65-8516-4b2689a217c2)

## Web App: Busca CEP

Este é um aplicativo web simples desenvolvido com **Streamlit** que permite a consulta de informações de um endereço a partir do CEP utilizando a API pública dos Correios.

## Funcionalidade

O usuário insere um CEP e o app retorna as seguintes informações:

- **Logradouro**
- **Bairro**
- **Cidade**
- **UF** (Unidade Federativa)

O aplicativo valida se o CEP possui 8 dígitos e realiza uma consulta à API pública `https://viacep.com.br` para retornar os dados do endereço.

## Como rodar o aplicativo

Para rodar este aplicativo, siga os passos abaixo:

1. **Instale o Streamlit e requests:**

    Se você ainda não tem o `Streamlit` e `requests` instalados, instale-os utilizando pip:

    ```bash
    pip install streamlit requests
    ```

2. **Execute o código no Streamlit:**

    Salve o código fornecido em um arquivo Python, por exemplo `app.py`, e execute o seguinte comando no terminal:

    ```bash
    streamlit run app.py
    ```

3. **Acesse o aplicativo no navegador:**

    O Streamlit irá iniciar o servidor local e você poderá acessar o app no seu navegador no endereço [http://localhost:8501](http://localhost:8501).

## Contribuições

Este projeto foi desenvolvido por **Ary Ribeiro**.

## Contato

💬 Ary Ribeiro - aryribeiro@gmail.com
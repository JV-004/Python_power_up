# Projeto: Automatização de Preenchimento com PyAutoGUI 🚀

Este projeto realiza a automação do preenchimento de um sistema web utilizando a biblioteca `PyAutoGUI`. O código também utiliza `pandas` para manipular os dados de uma tabela de produtos armazenada em um arquivo CSV. A principal funcionalidade é a inserção automática de informações como códigos, marcas e preços em um formulário de uma plataforma web.

## Funcionalidades ✨

- 🌐 Abrir automaticamente o navegador web e acessar um sistema online.
- 🔐 Realizar login na plataforma preenchendo e-mail e senha.
- 📄 Ler dados de um arquivo CSV com informações sobre produtos.
- 🔧 Preencher os campos do formulário com os dados lidos.
- 🚫 Tratar campos vazios para evitar erros durante o preenchimento.

## Tecnologias Utilizadas 💻

- **Python**: Linguagem de programação principal do projeto.
- **PyAutoGUI**: Biblioteca para automação de mouse e teclado.
- **Pandas**: Biblioteca para leitura e manipulação de dados.
- **Time**: Utilizada para controlar pausas entre as operações.

## Como Utilizar 🔄

1. **Clonar o Repositório**

   ```bash
   git clone https://github.com/seu-usuario/Python_power_up.git
   cd nome-do-repositorio
   ```

2. **Instalar as Dependências**
   Certifique-se de ter o Python instalado. Em seguida, instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar o Arquivo CSV**
   Certifique-se de que o arquivo `produtos.csv` está na mesma pasta do script. O arquivo deve conter as colunas:

   - `codigo`
   - `marca`
   - `tipo`
   - `categoria`
   - `preco_unitario`
   - `custo`
   - `obs`

4. **Executar o Script**
   Execute o script para iniciar a automação:

   ```bash
   python codigo.py
   ```

## Observações ⚠️

- O projeto utiliza coordenadas fixas para clicar em elementos na tela. Certifique-se de ajustar as posições (x, y) no código de acordo com a resolução do seu monitor.
- Evite movimentar o mouse ou interagir com o teclado durante a execução do script.

## Melhorias Futuras 🚀

- Tornar as coordenadas dinâmicas utilizando a biblioteca `pyautogui.locateOnScreen` para localizar elementos na tela.
- Adicionar suporte a diferentes formatos de arquivo (como Excel).
- Implementar tratamento de erros mais robusto para casos de falha no preenchimento.

## Contribuição 🙌

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou submeter pull requests.

---

**Autor:** João Vittor Fontes\
**Licença:** MIT


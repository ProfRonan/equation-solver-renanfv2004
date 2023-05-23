# Equation Solver

O script principal de vocês deve estar no arquivo `main.py`.

## 📝 Instruções 📝

Faça um programa que receba um número indicando qual o grau da equação, se esse número for menor do que `1` ou maior do que `2`, o programa deve imprimir `Grau inválido`.

1. Se o grau for `1`, o programa deve imprimir `A equação é do primeiro grau`.
   Em seguida ele deve pedir para o usuário digitar o valor de `a`.
   Caso o usuário digite `0` para `a`, o programa deve imprimir `Valor de a inválido` e terminar o programa.
   Se o usuário digitar um valor diferente de `0` para `a`, o programa deve pedir para o usuário digitar o valor de `b` e imprimir o valor da raiz da da equação `ax + b = 0` com exatamente duas casas decimais, independentemente se o número for inteiro ou não.
2. Se o grau for `2`, o programa deve imprimir `A equação é do segundo grau`.
   Em seguida ele deve pedir para o usuário digitar o valor de `a`.
   Caso o usuário digite `0` para `a`, o programa deve imprimir `Valor de a inválido` e terminar.
   1. Se o usuário digitar um valor diferente de `0` para `a` o programa deve pedir os valores `b` e `c` correspondente à equação `ax² + bx + c = 0`.
   2. Caso o usuário digite um valor de `b² - 4ac` menor do que `0`, o programa deve imprimir `A equação não possui raízes reais` e terminar.
   3. Caso o usuário digite um valor de `b² - 4ac` igual a `0`, o programa deve imprimir `A equação possui uma raiz real` e terminar.
      Em seguida ele deve imprimir o valor da raiz com exatamente duas casas decimais, independentemente se o número for inteiro ou não.
   4. Caso o usuário digite um valor de `b² - 4ac` maior do que `0`, o programa deve imprimir `A equação possui duas raízes reais` e terminar.
      Em seguida ele deve imprimir o valor das raízes com exatamente duas casas decimais, independentemente se o número for inteiro ou não e terminar.

## 🧪 Testes Automáticos 🧪

Para testar automaticamente o programa **antes** de fazer um commit e enviar o seu trabalho existem algumas formas de fazer isso.

1. executar o módulo `unittest` direto no terminal.
   Para isso, basta executar o seguinte comando:

```bash
python -m unittest discover -s test
```

2. executar o arquivo `test_main.py` no terminal.
   Para isso, basta executar o seguinte comando:

```bash
python test/test_main.py
```

3. caso você esteja usando o [VSCode](https://code.visualstudio.com/), você pode abrir a paleta de comandos `CTRL+SHIFT+P` e digitar `Run All Tests`.

4. no seu editor de código, você pode executar o arquivo `test_main.py` e verificar o resultado dos testes no terminal.

## 🤖 Observações Importantes 🤖

- **Não altere o nome dos arquivos**. Os arquivos `test_main.py` e `main.py` precisam ter esses nomes para que os testes funcionem.
- **Não altere o nome das funções**. Os testes dependem que as funções tenham os nomes especificados no enunciado ou já escritos nos arquivos.
- **Não altere o nome dos parâmetros**. Os testes dependem que as funções tenham os parâmetros especificados no enunciado ou já escritos nos arquivos.
- **Antes de fazer um commit**, execute os testes usando um dos métodos acima para verificar se o seu programa está funcionando corretamente.
- **Caso não consiga corrigir os erros**, entre em contato com o professor ou monitores para que eles possam te ajudar.
  Para isso você deve fazer um commit com o seu trabalho incompleto e abrir uma **issue** no repositório do exercício explicando o seu problema.

## 👀 Curiosidades 👀

O arquivo `requirements.txt` contém uma lista de dependências que o seu programa precisa para funcionar.

No caso desse exercício, a única dependência é o módulo `unittest` que é usado para fazer os testes automáticos.
E como o módulo `unittest` já vem instalado com o python, não é necessário instalar nada.

> Quando precisarmos instalar dependências, o comando `pip` é usado para instalar pacotes do python.
> Caso você precise instalar as dependências do seu programa, basta executar o seguinte comando:
>
> ```bash
> pip install -r requirements.txt
> ```

Os arquivos `Dockerfile` contém as instruções para criar uma imagem do docker com o seu programa.
Isso é útil para que eu possa executar o seu programa em um ambiente controlado e não ter problemas com dependências nem com possível códigos maliciosos na hora de rodar o programa.
São usados dois arquivos `Dockerfile`, um para rodar o seu programa e outro para rodar os testes.

Os arquivos dentro `.vscode` servem para configurar o ambiente de desenvolvimento no [VSCode](https://code.visualstudio.com/).
E facilitar a execução dos testes e do programa.

Os arquivos dentro da pasta `test` são usados para testar o seu programa.

O arquivo `.gitignore` serve para dizer ao git quais arquivos ele deve ignorar.

### :whale: Rodando o programa dentro do docker :whale:

Para aqueles que gostariam de aprender mais sobre o [docker](https://www.docker.com/), aqui vai uma breve explicação de como usar o docker para rodar o seu programa e os testes.

Primeiro, você precisa instalar o docker na sua máquina.
Para isso, basta seguir as instruções do site do [docker](https://docs.docker.com/get-docker/).

Depois de instalar o docker, você precisa criar uma imagem do docker com o seu programa.
Para isso, você precisa criar um arquivo `Dockerfile` com as instruções para criar a imagem do docker.
No caso desse exercício, o arquivo `Dockerfile` já está pronto.

Para criar a imagem do docker com o seu programa, basta executar o seguinte comando:

```bash
docker build -t python-app .
```

Para rodar o seu programa dentro do docker, basta executar o seguinte comando:

```bash
docker run -it --rm python-app
```

Para criar a imagem do docker com os testes, basta executar o seguinte comando:

```bash
docker build -t python-app-test -f test/Dockerfile .
```

Para rodar os testes dentro do docker, basta executar o seguinte comando:

```bash
docker run -it --rm python-app-test
```

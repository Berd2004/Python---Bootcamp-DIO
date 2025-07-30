<<<<<<< HEAD
Repositório com o códigos feitos durante o bootcamp da DIO em parceria com o Santander!
=======

># **versionamento** 

- Git: plataforma de controle de versão distribuído
- Github: plataforma de hospedagem de código para controle de versão com o git 

*repositório: é onde o código fica armazenado (remotamente)* 

--> Permite que as alterações em um código sejam armazenadas ao longo do tempo, facilitando a organização e colaboração de diferentes pessoas em um mesmo projeto.

--> Gerencia quais as alterações foram feitas, de acordo com data, autor etc...




-------------------------------------------------------------------------------

>Comandos do git

-mkdir nome do respositorio: cria a pasta local do respositorio

-git branch -m "main": muda o nome da branch atual para outro nome

-git init + "nome do arquivo" : serve para iniciar um repositório dentro da pasta do projeto. Com isso é criado na pasta, uma outra pasta com a extensão ***.git***

-git add nome do arquivo: serve para adicionar os arquivos do projeto que serão comitados posteriormente (é uma sala de espera digamos assim)

-git add .   :  o  "."  indica que todos os arquivos da branch vão ser comitados para o repositório local (máquina).

-git status: mostra o status dos arquivos que estão prontos para serem comitados

$ git remote add origin https://github.com/Berd2004/Python---Bootcamp-DIO.git: *é o comando que só se usa uma vez, serve para fazer a conexão do repositório do máquina com o remoto (do github)*

-git commit -m "nome da mensagem": É o comando que vai enviar o projeto para o repositório com uma mensagem de envio.

-git push -u origin main: envia os arquivos do repositório local para o repositório remoto no github

**-Git pull**: "Puxa" as alterações do repositório remoto (servidor) para a máquina local

**-Git Push:** "Empurra" as alterações para o repositório remoto

-git clone: clona na máquina local um repositório remoto

## Para subir alterações

- Usa os seguintes comandos, nessa ordem:

**-git add .**
**-git commit -m "mensagem"**
**-git push origin main**



## Atalhos git
- CTRL + L: Limpa o prompt
- Shift + Insert: Cola o que foi copiado
- Seta pra cima ou pra baixo: retorna os comandos escritos anteriormente
>>>>>>> 39875da (enviando os arquivos de resumo do git)

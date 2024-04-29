app.py
é responsável por definir as seguintes rotas HTTP GET, POST, PUT, DELETE que irá expor, mapeando-as para as funções correspondentes que irão processar as requisições. Importar e utiliza funções definidas em outros arquivos, como o randon_data.py, para realizar operações de acesso e manipulação dos dados no banco de dados

funcoes.py
É onde são armazenadas as funcionalidades essenciais e a lógica de negócios específicas da API, contribuindo para a organização e eficiência do desenvolvimento do aplicativo web.

randon_data.py, 
Desempenha um papel central na configuração e interação com o banco de dados em uma API, fornecendo as bases necessárias para a manipulação dos dados armazenados no banco de dados utilizado pela aplicação.





Tutorial de como fazer o passo a passo para o usuário explicando como configurar o git remote para sincronizar com o github ou outro repositório remoto.
-Abra o Terminal ou Git Bash e liste o repositório remoto configurado atualmente para o seu fork com o comando: $ git remote -v.
-Especifique um novo repositório remoto chamado "upstream" que será sincronizado com o fork usando o comando: git remote add upstream https://github.com/ORIGINAL-OWNER/ORIGINAL-REPOSITORY.git.
-Confirme o novo repositório "upstream" especificado para o seu fork com o comando: $ git remote -v.
-Antes de começar a trabalhar no repositório, atualize o seu repositório local com o repositório central usando: git pull upstream master.
-Faça suas edições, salve, adicione com git add, e faça commit com git commit no seu repositório local.
-Atualize o repositório central com as alterações do seu fork através de um Pull Request.
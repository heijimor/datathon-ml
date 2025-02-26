### Objetivo

Seu desafio é desenvolver esse modelo de sistema de recomendação e realizar o deploy dele utilizando as
técnicas aprendidas no curso. Nesse cenário, surge o desafio de fornecer recomendações personalizadas para
cada usuário com base nos dados de notícias do G1, predizendo qual será a próxima notícia que ele vai ler.

#### Alguns pontos importantes devem ser considerados:

1. Como lidar com o cold-start? Usuários ou itens com poucas informações devem ser tratados de forma diferenciada em relação a perfis mais completos?
2. O conceito de recência é essencial para garantir que as recomendações de notícias sejam relevantes e oportunas.

---

### O projeto deve conter:

1. Treinamento do modelo.

2. Salvamento do modelo.

3. Criação de uma API para previsões.

4. Empacotamento com Docker.

5. Testes e validação da API.

6. Deploy em ambiente produtivo: API local ou nuvem (a nuvem é opcional).

---

### Dados

O seu objetivo é gerar um ranking para a coluna history. Ou seja: quando um usuário loga, é necessário prever
quais serão os próximos acessos dele. Observe que o mesmo userId está tanto na validação quanto no treino.

Dados de treino
/files/treino: dados capturados de usuários
/itens/itens: matérias

validacao.csv: dados para validacao, para comparar com o modelo treinado

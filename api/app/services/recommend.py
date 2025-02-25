import pandas as pd
import pickle

def model_recommend(user_id: str) -> list[dict]:
  with open("./documentation/top_n_article_similarity.pkl", "rb") as f:
    loaded_similar_articles = pickle.load(f)
    
  user_article_history = pd.read_csv('./data/files/treino/treino_parte1.csv')
  df_article = pd.read_csv('./data/itens/itens/itens-parte3.csv')
  user_article = get_user_article(user_id, user_article_history)
  intercalated_articles = get_intercalated_articles(user_article_history, loaded_similar_articles)
  filtered_df = df_article.loc[df_article['page'].isin(intercalated_articles), ['title', 'url']]
  predictions = filtered_df.to_dict(orient='records')
  return predictions

def get_user_article(user_id: str, user_article_history: pd.DataFrame):
  user_data = user_article_history[user_article_history['userId'] == user_id]
  if user_data.empty:
      return None
  return user_data

def get_intercalated_articles(user_article_history, loaded_similar_articles):
    # Lista de artigos recomendados intercalados
    intercalated_recommendations = []

    # Iterar sobre a lista de artigos no histórico do usuário
    for article_id in user_article_history['history']:
        # Obter os artigos recomendados para o artigo de interesse
        recommended_articles = loaded_similar_articles.get(article_id, [])
        
        # Intercalar os artigos recomendados na lista final
        if recommended_articles:
            if not intercalated_recommendations:
                intercalated_recommendations = recommended_articles  # Primeira vez, só adiciona os primeiros artigos
            else:
                # Se já houver artigos, intercale com os existentes
                intercalated_recommendations = [
                    item for pair in zip(intercalated_recommendations, recommended_articles) for item in pair
                ]

    return intercalated_recommendations
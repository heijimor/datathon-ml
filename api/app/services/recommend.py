import pandas as pd
import pickle

# def model_recommend(user_id: str) -> list[dict]:
#   with open("./documentation/top_n_article_similarity.pkl", "rb") as f:
#     loaded_similar_articles = pickle.load(f)
    
#   user_article_history = pd.read_csv('./data/files/treino/treino_parte1.csv')
#   df_article = pd.read_csv('./data/itens/itens/itens-parte3.csv')
#   user_article = get_user_article(user_id, user_article_history)
#   intercalated_articles = get_intercalated_articles(user_article_history, loaded_similar_articles)
#   filtered_df = df_article.loc[df_article['page'].isin(intercalated_articles), ['title', 'url']]
#   predictions = filtered_df.to_dict(orient='records')
#   return predictions

# def get_user_article(user_id: str, user_article_history: pd.DataFrame):
#   user_data = user_article_history[user_article_history['userId'] == user_id]
#   if user_data.empty:
#       return None
#   return user_data

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
  
def model_recommend(user_id, user_type=None, top_n=5):
  with open("./app/services/cos_sim_matrix.pkl", "rb") as f:
    cos_sim_df = pickle.load(f)

  df_interactions = pd.read_parquet("./app/services/interactions.parquet")

  print(f"user_id type: {type(user_id)}")
  print(f"cos_sim_df.index type: {type(cos_sim_df.index)}")
  print(f"cos_sim_df.index: {cos_sim_df.index[:10]}")  # First 10 user IDs
  user_id = int(user_id)  # or str(user_id) depending on the format

  # Ensure user_id exists in the similarity matrix
  if user_id not in cos_sim_df.index:
      raise ValueError(f"User ID {user_id} not found in similarity matrix")
  
  # Get the similarity scores for the specified user
  user_similarity = cos_sim_df.loc[user_id]
  
  # If user_type is relevant, we can filter or adjust the similarity calculation accordingly
  # Example: Add logic here to adjust based on user_type, if necessary
  # For simplicity, assuming user_type isn't directly used for filtering the similarity matrix

  # Sort the similarities (excluding the user itself) and get the most similar users
  similar_users = user_similarity.sort_values(ascending=False).index[1:top_n+1]
  
  recommended_articles = []
  for similar_user in similar_users:
      # Get articles interacted with by similar users
      similar_user_articles = df_interactions[df_interactions['userId'] == similar_user]['page']
      recommended_articles.extend(similar_user_articles)
  
  # Remove duplicates by converting to a set
  recommended_articles = list(set(recommended_articles))
  input_article_ids = recommended_articles[:top_n]

  df_articles = pd.read_csv('./data/itens/itens/itens-parte1.csv')
  input_article_ids = [article_id.strip() for article_id in input_article_ids]

  matched_articles = df_articles[df_articles['page'].isin(input_article_ids)]
  # print(df_articles)
  print(matched_articles)
  # Create the response with url and title
  response = [{"url": row["url"], "title": row["title"]} for _, row in matched_articles.iterrows()]

  
  # Return the top N recommended articles
  return response
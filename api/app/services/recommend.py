import pandas as pd
import pickle
import joblib
from pymongo import MongoClient

def model_recommend(user_id, user_type=None, top_n=6):
    with open("./app/services/cos_sim_matrix.pkl", "rb") as f:
        cos_sim_df = pickle.load(f)
    df_interactions = pd.read_parquet("./app/services/interactions.parquet")
    user_id = int(user_id)

    if user_id in cos_sim_df.index:
        return recommend_for_logged_user(user_id, cos_sim_df, df_interactions, top_n)
    return recommend_for_new_user(df_interactions)
    # O K-Means pode ajudar a classificar novos usuários em clusters baseados em atributos demográficos ou comportamento inicial (ex: tempo na página, número de cliques, categoria de interesse).

def recommend_for_logged_user(user_id, cos_sim_df, df_interactions, top_n):
    user_similarity = cos_sim_df.loc[user_id]
    similar_users = user_similarity.sort_values(ascending=False).index[1:top_n+1]
    recommended_articles = []

    for similar_user in similar_users:
        similar_user_articles = df_interactions[df_interactions['userId'] == similar_user]['page']
        recommended_articles.extend(similar_user_articles)
    
    input_article_ids = list(set(recommended_articles))[:top_n]
    input_article_ids = [article_id.strip() for article_id in input_article_ids]
    mongo_client = MongoClient("mongodb://admin:adminpassword@mongodb:27017")
    db = mongo_client["mydatabase"]
    articles_collection = db["articles"]
    return list(articles_collection.find({"page": {"$in": input_article_ids}}, {"_id": 0, "url": 1, "title": 1}))

def recommend_for_new_user(df_interactions):
    kmeans = joblib.load("./app/services/kmeans_model.pkl")
    df_users = pd.read_csv("./app/services/treino_parte1.csv")
    # Identifica o cluster médio
    default_features = get_default_user_features(kmeans)
    default_cluster = kmeans.predict([default_features])[0]
    default_cluster = int(default_cluster)
    print(f"Usuário novo pertence ao cluster {default_cluster}")
    # Filtra usuários desse cluster
    print(df_users.columns)

    similar_users = df_users[df_users["cluster"] == default_cluster]["userId"]
    
    # Pega os artigos mais vistos por usuários desse cluster
    popular_articles = df_interactions[df_interactions["userId"].isin(similar_users)]
    recommended_articles = popular_articles.groupby("page").size().reset_index(name="popularity")
    recommended_articles = recommended_articles.sort_values("popularity", ascending=False)
    return recommended_articles["page"].head(5).tolist()

def get_default_user_features(kmeans):
    # Retorna o centroide de um cluster médio (usuário típico)
    default_cluster_center = kmeans.cluster_centers_.mean(axis=0)
    return default_cluster_center

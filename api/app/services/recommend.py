import pandas as pd
import pickle
import joblib
from app.services.mongo_client import MongoDBClient

mongo_client = MongoDBClient()

from fastapi import FastAPI, HTTPException
import pandas as pd
import numpy as np
import pickle
import os
from app.services.mongo_client import MongoDBClient

root_path = os.getenv('HOST_PATH')
models_path = f"{root_path}/artifacts/models"

with open(f"{models_path}/collaborative_model.pkl", "rb") as f:
    svd = pickle.load(f)

with open(f"{models_path}/user_item_matrix.pkl", "rb") as f:
    user_item_matrix = pickle.load(f)

def recommend(user_id: str, user_type: str, top_n: int = 5):
    """Combina recomendações colaborativas e baseadas em conteúdo."""
    if user_id in user_item_matrix.index:
        collab = recommend_for_logged(user_id, top_n)
        return list(collab)
    content = recommend_for_non_logged(top_n)
    return list(content)

def recommend_for_logged(user_id: str, top_n: int = 5):
    """Recomenda itens baseados em interações de usuários semelhantes."""
    user_vector = user_item_matrix.loc[user_id].values.reshape(1, -1)
    user_factors = svd.transform(user_vector)  # Fatores do usuário
    item_scores = svd.inverse_transform(user_factors)  # Prever interações futuras
    top_items = np.argsort(item_scores[0])[::-1][:top_n]
    recommendations = user_item_matrix.columns[top_items].tolist()
    return get_articles_by_recommendations(recommendations)

def recommend_for_non_logged(top_n: int = 5):
    """Recomenda itens com base na similaridade de conteúdo."""
    recommendations = user_item_matrix.columns[:top_n].tolist()
    return get_articles_by_recommendations(recommendations)

def get_articles_by_recommendations(recommendations):
    articles_collection = mongo_client.get_collection("articles")
    query = {"$in": recommendations}
    return articles_collection.find({"page": query }, {"_id": 0, "url": 1, "title": 1})
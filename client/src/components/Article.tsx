// src/components/ArticleCard.tsx
import React from "react";

interface ArticleCardProps {
  title: string;
  url: string;
}

const Article: React.FC<ArticleCardProps> = ({ title, url }) => {
  return (
    <div
      style={{
        border: "1px solid #ddd",
        margin: "10px",
        padding: "10px",
        maxWidth: "250px",
      }}
    >
      <a href={url}>
        <h2>{title}</h2>
      </a>
    </div>
  );
};

export default Article;

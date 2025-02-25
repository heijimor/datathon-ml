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
        margin: "10px",
        padding: "10px",
        maxWidth: "350px",
      }}
    >
      <a href={url}>
        <div
          style={{
            border: "1px solid #ddd",
            maxWidth: "350px",
            height: "150px",
            borderRadius: "10px",
            textAlign: "center",
            overflow: "hidden", // Evita que a imagem ultrapasse os cantos arredondados
          }}
        >
          <img
            src="../../public/no-image.png"
            alt="Imagem"
            style={{
              width: "150px",
              height: "150px",

              objectFit: "cover", // Garante que a imagem cubra o espaço sem distorcer
            }}
          />
        </div>
        <div>
          <h3 style={{ color: "#c4170c" }}>{title}</h3>
        </div>
      </a>
    </div>
  );
};

export default Article;

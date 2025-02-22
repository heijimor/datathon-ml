import "./App.css";
import Header from "./components/Header";
import Article from "./components/Article";
import Footer from "./components/Footer";
import Navbar from "./components/Navbar";
import { useEffect, useState } from "react";

type Article = {
  title: string;
  url: string;
};

function App() {
  const [articles, setArticles] = useState<Article[]>([]);

  const retrieveArticles = async () => {
    const response = await fetch("http://localhost:8000/api/predict", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        user: "",
        userType: "Non-Logged",
      }),
    });
    const articles = (await response.json()) as Array<Article>;
    setArticles(articles);
  };

  useEffect(() => {
    retrieveArticles();
  }, []);

  return (
    <>
      <div>
        <Header />
        <Navbar />
        <div
          style={{
            display: "flex",
            flexWrap: "wrap",
            justifyContent: "center",
            flexDirection: "row",
          }}
        >
          {articles.map((article, index) => (
            <Article key={index} title={article.title} url={article.url} />
          ))}
        </div>
        <Footer />
      </div>
    </>
  );
}

export default App;

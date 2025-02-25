import "./App.css";
import Header from "./components/Header";
import Article from "./components/Article";
import Footer from "./components/Footer";
import Navbar from "./components/Navbar";
import { useEffect, useState } from "react";
import UserMenu from "./components/UserMenu";

type Article = {
  title: string;
  url: string;
};

function App() {
  const [articles, setArticles] = useState<Article[]>([]);

  const [selectedOption, setSelectedOption] = useState<string | null>(null);

  const handleSelectedOptionChange = (newSelectedOption: string) => {
    setSelectedOption(newSelectedOption);
    retrieveArticles();
  };

  const retrieveArticles = async () => {
    const userId = selectedOption ?? "69817";

    const response = await fetch(
      `http://localhost:8000/api/recommend/${userId}`,
      {
        method: "GET",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
      }
    );
    const articles = (await response.json()) as Array<Article>;
    setArticles(articles);
  };

  useEffect(() => {
    retrieveArticles();
  }, [selectedOption]);

  return (
    <>
      <div>
        <UserMenu
          selectedOption={selectedOption}
          onSelectedOptionChange={handleSelectedOptionChange}
        />
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

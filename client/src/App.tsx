import { useEffect, useState } from "react";
import Logo from "./components/Logo";
import Article from "./components/Article";
import Footer from "./components/Footer";
import Navbar from "./components/Navbar";
import UserMenu from "./components/UserMenu";

type Article = {
  title: string;
  url: string;
};

function App() {
  const [articles, setArticles] = useState<Article[]>([]);
  const [selectedOption, setSelectedOption] = useState("103"); // Default value set

  const handleSelectedOptionChange = (newSelectedOption: string) => {
    setSelectedOption(newSelectedOption);
  };

  const retrieveArticles = async (userId: string) => {
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
    retrieveArticles(selectedOption);
  }, [selectedOption]);

  return (
    <div>
      <header
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
          backgroundColor: "#ffffff",
          color: "#2f3134",
          padding: "10px 200px",
          maxWidth: "1320px",
        }}
      >
        <Logo />
        <UserMenu
          selectedOption={selectedOption}
          onSelectedOptionChange={handleSelectedOptionChange}
        />
      </header>

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
  );
}

export default App;

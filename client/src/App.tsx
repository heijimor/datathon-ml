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
  const [selectedOption, setSelectedOption] = useState({
    id: "c196609069bdb5a080bdc889d71028674e580318f0bd6c1bcc869ee0e632a735",
    type: "Logged",
  });

  const handleSelectedOptionChange = (newSelectedOption) => {
    console.log(newSelectedOption);
    setSelectedOption(newSelectedOption);
  };

  const retrieveArticles = async (user) => {
    const response = await fetch(
      `http://localhost:8000/api/recommend/${user.id}/type/${user.type}`,
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

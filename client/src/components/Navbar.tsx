import React from "react";

const Navbar: React.FC = () => {
  return (
    <nav
      style={{
        backgroundColor: "white",
        padding: "10px 0",
        borderTop: "2px solid #f5f6f7",
      }}
    >
      <ul
        style={{
          display: "flex",
          justifyContent: "center",
          gap: "20px", // Spacing between items
          listStyle: "none", // Remove bullet points
          padding: 0,
          margin: 0,
          fontFamily: "Arial, sans-serif", // Adjust font
        }}
      >
        <li style={{ color: "red", fontWeight: "bold" }}>g1</li>
        <li style={{ color: "blue", fontWeight: "bold" }}>o globo</li>
        <li style={{ color: "teal", fontWeight: "bold" }}>valor</li>
        <li style={{ color: "green", fontWeight: "bold" }}>ge</li>
        <li style={{ color: "orange", fontWeight: "bold" }}>cartola</li>
        <li style={{ color: "red", fontWeight: "bold" }}>globoplay</li>
        <li style={{ color: "orange", fontWeight: "bold" }}>gshow</li>
        <li style={{ color: "purple", fontWeight: "bold" }}>receitas</li>
        <li style={{ color: "black", fontWeight: "bold" }}>quem</li>
        <li style={{ color: "gray", fontWeight: "bold" }}>podcast</li>
      </ul>
    </nav>
  );
};

export default Navbar;

// src/components/Navbar.tsx
import React from "react";

const Navbar: React.FC = () => {
  return (
    <nav style={{ backgroundColor: "#333", padding: "10px", color: "white" }}>
      <ul style={{ display: "flex", justifyContent: "space-around" }}>
        <li>Home</li>
        <li>News</li>
        <li>Entertainment</li>
        <li>Sports</li>
      </ul>
    </nav>
  );
};

export default Navbar;

// src/components/Header.tsx
import React from "react";
import UserMenu from "./UserMenu";

const Header: React.FC = () => {
  return (
    <header>
      <div>
        <UserMenu />
      </div>
      <div
        style={{ backgroundColor: "#d50032", padding: "10px", color: "white" }}
      >
        <h1>Globus.com</h1>
      </div>
    </header>
  );
};

export default Header;

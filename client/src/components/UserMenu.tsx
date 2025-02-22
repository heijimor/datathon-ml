// src/components/UserMenu.tsx
import React, { useState } from "react";

const UserMenu: React.FC = () => {
  const [selectedOption, setSelectedOption] = useState<string>("");

  const [users, setUsers] = useState([
    "0adffd7450d3b9840d8c6215f0569ad942e782fb19b805367b02b709b73f42a1",
    "a64a6e34e27d6f312c0d15c7deba04d3c3466741e329365ce9b33db90d7b1cd9",
  ]);

  const handleChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setSelectedOption(event.target.value);
  };

  return (
    <div
      style={{
        display: "flex",
        justifyContent: "flex-end",
        backgroundColor: "white",
      }}
    >
      <select
        value={selectedOption}
        onChange={handleChange}
        style={{
          backgroundColor: "#333",
          color: "white",
          border: "none",
          borderRadius: "4px",
          padding: "5px",
          cursor: "pointer",
          width: "200px",
        }}
      >
        {users.map((user, index) => (
          <option key={index} value={user}>
            {user}
          </option>
        ))}
      </select>
    </div>
  );
};

export default UserMenu;

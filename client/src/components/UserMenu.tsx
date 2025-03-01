import React, { useState } from "react";

interface UserMenuProps {
  selectedOption: string;
  onSelectedOptionChange: (newSelectedOption: string) => void;
}

const UserMenu: React.FC<UserMenuProps> = ({
  selectedOption,
  onSelectedOptionChange,
}) => {
  const [users] = useState([
    {
      label: "103 (Logado)",
      value: "c196609069bdb5a080bdc889d71028674e580318f0bd6c1bcc869ee0e632a735",
    },
    {
      label: "54594 (Logado)",
      value: "ac28b85fb23da7b4c32ffb8adef475078382ee265f783e9001ac00f0c513ee3a",
    },
    { label: "69817 (Não Logado)", value: "69817" },
    { label: "698100 (Não Logado)", value: "698100" },
  ]);

  const handleChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    onSelectedOptionChange(event.target.value);
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
          <option key={index} value={user.value}>
            {user.label}
          </option>
        ))}
      </select>
    </div>
  );
};

export default UserMenu;

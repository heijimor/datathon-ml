import React, { useState } from "react";

interface UserMenuProps {
  selectedOption: string;
  onSelectedOptionChange: (newSelectedOption: string) => void;
}

const UserMenu: React.FC<UserMenuProps> = ({
  selectedOption,
  onSelectedOptionChange,
}) => {
  const [users, setUsers] = useState([
    "103", // 0adffd7450d3b9840d8c6215f0569ad942e782fb19b805367b02b709b73f42a1
    "69817", // a64a6e34e27d6f312c0d15c7deba04d3c3466741e329365ce9b33db90d7b1cd9
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
          <option key={index} value={user}>
            {user}
          </option>
        ))}
      </select>
    </div>
  );
};

export default UserMenu;

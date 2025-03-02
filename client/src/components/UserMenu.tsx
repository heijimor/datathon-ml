import React, { useState } from "react";

interface UserMenuProps {
  selectedOption: string; // Specify the type of selectedOption
  onSelectedOptionChange: (newSelectedOption: object) => void; // Specify the type of newSelectedOption
}

const UserMenu: React.FC<UserMenuProps> = ({
  selectedOption,
  onSelectedOptionChange,
}) => {
  const [users] = useState([
    {
      label:
        "ac28b85fb23da7b4c32ffb8adef475078382ee265f783e9001ac00f0c513ee3a (Logado)",
      value: {
        id: "ac28b85fb23da7b4c32ffb8adef475078382ee265f783e9001ac00f0c513ee3a",
        type: "Logged",
      },
    },
    {
      label: "69817 (Não Logado)",
      value: { id: "69817", type: "Non-Logged" },
    },
    {
      label:
        "a50f16d51820754a3db8281180950c3619c2b5a154926cb383de0fd023404756 (Logado)",
      value: {
        id: "a50f16d51820754a3db8281180950c3619c2b5a154926cb383de0fd023404756",
        type: "Logged",
      },
    },
  ]);

  const handleChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    const selectedUser = JSON.parse(event.target.value);
    onSelectedOptionChange(selectedUser); // Pass the entire object
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
        value={JSON.stringify(selectedOption)} // Store as JSON string
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
          <option key={index} value={JSON.stringify(user.value)}>
            {user.label}
          </option>
        ))}
      </select>
    </div>
  );
};

export default UserMenu;

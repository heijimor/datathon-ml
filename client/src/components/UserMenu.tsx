import React, { useState } from "react";

interface UserMenuProps {
  selectedOption: string;
  onSelectedOptionChange: (newSelectedOption: string) => void;
}

const UserMenu: React.FC<UserMenuProps> = ({
  selectedOption,
  onSelectedOptionChange,
}) => {
  const [users] = useState(["103", "69817"]);

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

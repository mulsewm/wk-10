import React from "react";

export const Card = ({ children }) => {
  return (
    <div className="border p-4 rounded shadow bg-white p-4">
      {children}
    </div>
  );
};

export const CardContent = ({ children }) => {
  return <div className="p-2">{children}</div>;
};

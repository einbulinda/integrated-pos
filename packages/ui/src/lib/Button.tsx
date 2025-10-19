import * as React from "react";

type ButtonProps = React.ButtonHTMLAttributes<HTMLButtonElement> & {
  variant?: "primary" | "secondary";
};

export const Button: React.FC<ButtonProps> = ({
  variant = "primary",
  ...props
}) => {
  const base = "px-4 py-2 rounded-md";
  const theme =
    variant === "primary" ? "bg-black text-white" : "bg-gray-200 text-black";
  return <button className={`${base} ${theme}`} {...props} />;
};

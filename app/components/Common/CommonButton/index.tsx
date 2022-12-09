import React, { FC, ReactNode } from "react"

interface IProps {
  onClick: (e: React.MouseEvent) => void,
  children: ReactNode
}

export const CommonButton :FC<IProps> = ({ onClick, children }) => {
  return <button onClick={onClick}>{children}</button>
}

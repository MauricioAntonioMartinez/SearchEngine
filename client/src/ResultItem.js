import React from "react";

export const ResultItem = (props) => {
  return (
    <div className="result-item">
      <h3>{props.item.title}</h3>
      <span>
        <a href={props.item?.url}>{props.item?.url}</a>
      </span>
    </div>
  );
};

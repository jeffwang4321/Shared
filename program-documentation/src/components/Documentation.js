import React from "react";
import { useParams } from "react-router-dom";
import MarkdownRenderer from "./MarkdownRenderer";

const Documentation = () => {
  const { page } = useParams();

  return (
    <div>
      <h2>Documentation</h2>
      <MarkdownRenderer page={page} />
    </div>
  );
};

export default Documentation;

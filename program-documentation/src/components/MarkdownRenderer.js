import React, { useState, useEffect } from "react";
import ReactMarkdown from "react-markdown";

const MarkdownRenderer = ({ page }) => {
  const [markdown, setMarkdown] = useState("");

  useEffect(() => {
    const fetchMarkdown = async () => {
      try {
        const response = await fetch(`/documentation/${page}.md`);
        const text = await response.text();
        console.log(text);
        setMarkdown(text);
      } catch (error) {
        console.error("Error fetching markdown:", error);
      }
    };

    fetchMarkdown();
  }, [page]);

  return <ReactMarkdown>{markdown}</ReactMarkdown>;
};

export default MarkdownRenderer;

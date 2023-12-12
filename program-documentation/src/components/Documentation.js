import React from "react";
import { useParams } from "react-router-dom";
import ReactMarkdown from "react-markdown";

const Documentation = () => {
  const { page } = useParams();

  // Assume your Markdown files are stored in the /docs folder
  const markdownPath = require(`../documentation/${page}.md`);

  const markdownContent = `
# Page 1

This is the first page of your documentation.

## Section 1

This is the first section of your first page.

Here's some example code:

\`\`\`javascript
console.log('Hello, world!');
\`\`\`

## Section 2

This is the second section of your first page.

You can add more content here.
`;

  return (
    <div>
      <h2>{page}</h2>
      <ReactMarkdown>{markdownPath.default}</ReactMarkdown>
    </div>
  );
};

export default Documentation;

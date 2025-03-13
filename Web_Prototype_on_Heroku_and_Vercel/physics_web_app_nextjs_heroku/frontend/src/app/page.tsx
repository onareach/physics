// page.tsx

'use client';

import { useEffect, useState } from 'react';
import { MathJax, MathJaxContext } from 'better-react-mathjax';

interface Formula {
  id: number;
  formula_name: string;
  latex: string;
}

export default function Home() {
  const [formulas, setFormulas] = useState<Formula[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    console.log("API URL:", process.env.NEXT_PUBLIC_API_URL); // Add this for debugging
    fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/formulas`)
      .then((res) => {
        if (!res.ok) {
          throw new Error(`HTTP error! Status: ${res.status}`);
        }
        return res.json();
      })
      .then((data) => setFormulas(data))
      .catch((err) => setError(err.message));
  }, []);

  return (
    <MathJaxContext>
      <div style={{ marginLeft: '20px', marginTop: '20px' }}>  {/* Added margin */}
        <h1>Physics Formula Viewer</h1>
        {error ? (
          <p style={{ color: 'red' }}>Error: {error}</p>
        ) : (
          <ul>
            {formulas.map((formula) => (
              <li key={formula.id}>
                <strong>{formula.formula_name}:</strong>
                <MathJax>{`\\(${formula.latex}\\)`}</MathJax>
              </li>
            ))}
          </ul>
        )}
      </div>
    </MathJaxContext>
  );
}

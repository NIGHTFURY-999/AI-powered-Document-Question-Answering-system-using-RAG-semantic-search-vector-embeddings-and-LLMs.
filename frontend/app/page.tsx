"use client";

import { useState } from "react";

export default function Home() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  async function askQuestion() {
    if (!question.trim()) {
      return;
    }

    setLoading(true);
    setAnswer("");

    try {
      const response = await fetch("http://127.0.0.1:8000/ask", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          question: question,
        }),
      });

      const data = await response.json();

      setAnswer(data.answer);
    } catch (error) {
      setAnswer("Could not connect to the backend.");
    }

    setLoading(false);
  }

  return (
    <main className="min-h-screen bg-gray-950 text-white px-6 py-12">

      <div className="mx-auto max-w-3xl">

        <h1 className="text-4xl font-bold">
          Document QA Assistant
        </h1>

        <p className="mt-3 text-gray-400">
          Ask questions about your uploaded documents using RAG.
        </p>

        <div className="mt-10">

          <textarea
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="Ask a question about your document..."
            className="w-full rounded-xl border border-gray-700 bg-gray-900 p-4 text-white outline-none focus:border-gray-400"
            rows={5}
          />

          <button
            onClick={askQuestion}
            disabled={loading}
            className="mt-4 rounded-xl bg-white px-6 py-3 font-semibold text-black disabled:opacity-50"
          >
            {loading ? "Thinking..." : "Ask Question"}
          </button>

        </div>

        {answer && (
          <div className="mt-10 rounded-xl border border-gray-800 bg-gray-900 p-6">

            <h2 className="text-xl font-semibold">
              Answer
            </h2>

            <p className="mt-4 whitespace-pre-wrap text-gray-300">
              {answer}
            </p>

          </div>
        )}

      </div>

    </main>
  );
}
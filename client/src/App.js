import axios from "axios";
import React, { useEffect, useState } from "react";
import { ResultItem } from "./ResultItem";

function App() {
  const [search, setSearch] = useState();
  const [indexPage, setIndexPage] = useState(false);
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState([]);

  useEffect(() => {
    (async () => {
      try {
        const res = await axios.get("http://localhost:5000");
        console.log(res.data);
      } catch (e) {
        console.log(e.message);
      }
    })();
  }, []);

  const searchHandler = async () => {
    if (!search.trim().length) return;

    let url = `search?q=${search}`;
    if (indexPage) {
      url = `page_index?url=${search}`;
    }

    try {
      setLoading(true);
      const res = await axios.post(`http://localhost:5000/${url}`);

      if (!indexPage) {
        setResults(res.data.results);
      }
      console.log(res.data);
    } catch (e) {
      console.log(e.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <main className="content">
        <h1>{indexPage ? "Index an Url" : "Searcher"}</h1>
        <input
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          placeholder={indexPage ? "Url .." : "Search.."}
          disabled={loading}
        />
        <button onClick={searchHandler} disabled={loading}>
          {indexPage ? "Index" : "Search"}
        </button>

        <button disabled={loading} onClick={() => setIndexPage((e) => !e)}>
          {!indexPage ? "Change to index" : "Change to search"}
        </button>

        {results.map((item, index) => (
          <ResultItem item={item} key={index} />
        ))}
      </main>
    </div>
  );
}

export default App;

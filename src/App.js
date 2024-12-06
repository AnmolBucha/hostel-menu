import React, { useState } from "react";
import axios from "axios";

function App() {
  const [budget, setBudget] = useState("");
  const [nutritionalGoals, setNutritionalGoals] = useState("");
  const [menu, setMenu] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://localhost:5000/generate-menu", {
        budget,
        nutritionalGoals,
      });
      setMenu(response.data.menu);
    } catch (error) {
      console.error("Error generating menu:", error);
    }
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>Hostel Weekly Menu Generator</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Budget per week (₹):
          <input
            type="number"
            value={budget}
            onChange={(e) => setBudget(e.target.value)}
            required
          />
        </label>
        <br />
        <label>
          Nutritional Goals (e.g., calories, proteins, etc.):
          <textarea
            value={nutritionalGoals}
            onChange={(e) => setNutritionalGoals(e.target.value)}
            required
          />
        </label>
        <br />
        <button type="submit">Generate Menu</button>
      </form>
      {menu && (
        <div>
          <h2>Generated Weekly Menu</h2>
          <pre>{JSON.stringify(menu, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;

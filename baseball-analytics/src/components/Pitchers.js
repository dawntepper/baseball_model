import React, { useState, useEffect } from 'react';

function Pitchers() {
  const [pitchers, setPitchers] = useState([]); // State to store the pitchers data

  // Fetch data from Flask API on component mount
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost:5000/api/pitchers'); // Adjust if your Flask API is running on a different port
        const data = await response.json();
        setPitchers(data); // Set the fetched data to state
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <h1>Probable Pitchers</h1>
      <ul>
        {pitchers.map((pitcher, index) => (
          <li key={index}>
            {pitcher.pitcher} - {pitcher.team} - Throws: {pitcher.handedness} - vs {pitcher.opponent_team}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Pitchers;

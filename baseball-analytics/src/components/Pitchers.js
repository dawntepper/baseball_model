import React, { useState, useEffect } from 'react';

function Pitchers() {
  const [pitchers, setPitchers] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost:5000/api/pitchers'); 
        const data = await response.json();
        setPitchers(data);
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

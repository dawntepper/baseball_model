import React, { useState, useEffect } from 'react';

function Pitchers() {
  const [pitchers, setPitchers] = useState([]);  // State to store the pitchers data

  // Function to fetch data from the API
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost:5000/scrape/pitchers'); // Adjust the URL if needed
        const data = await response.json();
        setPitchers(data); // Set the fetched data to the state
      } catch (error) {
        console.error('Error fetching pitchers:', error);
      }
    };

    fetchData();
  }, []);

  // Rendering the pitchers data
  return (
    <div>
      <h1>Probable Pitchers</h1>
      <ul>
        {pitchers.map((pitcher, index) => (
          <li key={index}>
            Name: {pitcher.Name}, Team: {pitcher.Team}, Handedness: {pitcher.Handedness}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Pitchers;

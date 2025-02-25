import React, { useEffect, useState } from "react";
import { Line } from "react-chartjs-2";
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from "chart.js";
import { Card, CardContent } from "./components/Card";  
import axios from "axios";

// **Register required Chart.js components**
ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

const Dashboard = () => {
  const [prices, setPrices] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:5000/api/prices")
      .then((response) => {
        setPrices(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div className="text-center p-4">Loading data...</div>;
  }

  const chartData = {
    labels: prices.map((item) => item.Date),
    datasets: [
      {
        label: "Brent Oil Price (USD per Barrel)",
        data: prices.map((item) => item.Price),
        fill: false,
        borderColor: "#007bff",
        tension: 0.1,
      },
    ],
  };

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Brent Oil Price Dashboard</h1>
      <Card>
        <CardContent>
          <Line data={chartData} />
        </CardContent>
      </Card>
    </div>
  );
};

export default Dashboard;

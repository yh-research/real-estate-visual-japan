import { Line } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

export default function chart({
  title,
  labels,
  data,
  color = "rgb(75, 192, 192, 1)",
}) {
  const chartData = {
    labels,
    datasets: [
      {
        label: title,
        data,
        borderColor: color,
        backgroundColor: color,
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: { legend: { position: "top" } },
  };

  return <line data={chartData} options={options} />;
}

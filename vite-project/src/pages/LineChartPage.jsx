import { useState } from "react";

import LineChart from "../components/LineChart";
import Legend from "../components/Legend";
import data0DecNov from "../files/data_0_dec-nov.json";
import data12DecNov from "../files/data_12_dec-nov.json";

const data_0 = {
  name: "v2 ds: 0",
  color: "red",
  items: data0DecNov,
};

const data_12 = {
  name: "v2 ds: 12",
  color: "green",
  items: data12DecNov,
};

const dimensions = {
  width: 1300,
  height: 700,
  margin: {
    top: 100,
    right: 200,
    bottom: 10,
    left: 100,
  },
};

export function LineChartPage() {
  const [selectedItems, setSelectedItems] = useState([]);
  const legendData = [data_0, data_12];
  const chartData = [
    ...[data_0, data_12].filter((d) => selectedItems.includes(d.name)),
  ];
  const onChangeSelection = (name) => {
    const newSelectedItems = selectedItems.includes(name)
      ? selectedItems.filter((item) => item !== name)
      : [...selectedItems, name];
    setSelectedItems(newSelectedItems);
  };
  return (
    <div className="line-chart-container">
      <Legend
        data={legendData}
        selectedItems={selectedItems}
        onChange={onChangeSelection}
      />
      <LineChart data={chartData} dimensions={dimensions} />
    </div>
  );
}

export default LineChartPage;

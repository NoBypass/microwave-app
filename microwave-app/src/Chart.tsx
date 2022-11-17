import React from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Line } from 'react-chartjs-2';
import dataJSON from './db.json'

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

export const options = {
  responsive: true,
  plugins: {
    title: {
      display: true,
      text: 'Mikrowellen',
  },
  elements: {
    line: {
      borderJoinStyle: 'round'
    }
  }
  },
};

function getFreeMics(data) {
  var count = 0
  for (let i = 0; i < data.length; i++) {
    if (JSON.parse(data[i].on)) count += 1
  }
  return count
}

var dataArr = []
var timeArr = []

const len = 6
for (let i = 0; i < len; i++) {
  dataArr.push(getFreeMics(dataJSON[dataJSON.length - (i+1)]))
  timeArr.push(dataJSON[dataJSON.length - (i+1)][0].date.toString().slice(11, 19))
}

const labels = timeArr;

export const data = {
  labels,
  datasets: [
    {
      label: 'Besetzte Mikrowellen',
      data: dataArr.reverse(),
      borderColor: 'rgb(45, 140, 230)',
      backgroundColor: 'rgba(45, 140, 230, 0.5)',
    }
  ],
};

export default function App() {
  return <Line options={options} data={data} width={6} height={3} />;
}

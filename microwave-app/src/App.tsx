import React, {useState, useEffect} from 'react';
import './App.css';
import Chart from './Chart'
import dataJSON from './db.json'

function getFreeMics(data) {
  var count = 0
  for (let i = 0; i < data.length; i++) {
    if (JSON.parse(data[i].on)) count += 1
  }
  return String(count)
}

function App() {
  var unusedMicrowaves = getFreeMics(dataJSON[dataJSON.length - 1])
  console.log(unusedMicrowaves)
  var noonState = 'Du kannst in den Mittag gehen.'
  if (unusedMicrowaves === '0') {
    unusedMicrowaves = 'keine'
    noonState = 'Warte noch ein bisschen mit deiner Pause.'
  }
  var n = 'n'
  var sind = 'sind'
  if (unusedMicrowaves === '1') {
    n = '' 
    sind = 'ist'
  }

  return (
    <div className="App">
      <div className='top'>
        <a href="https://discord.com/api/oauth2/authorize?client_id=1037640620623278130&permissions=&&scope=bot" className="dc">Invite Discord Bot</a>
        <p className='title'>Es {sind} aktuell {unusedMicrowaves} Mikrowelle{n} frei!</p>
        <p className="subtitle">{noonState}</p>
      </div>
      <div className='rounder'></div>
      <div className="chart">
        <Chart />
      </div>
    </div>
  );
}

export default App;

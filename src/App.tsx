import React from 'react';
import './App.css';
const mqtt = require('mqtt')
const client  = mqtt.connect('mqtt://10.0.103.157:1883')

function App() {
  client.on('message', (topic: any, msg: any) => {
    console.log('received message')
    console.log(msg.toString())
    client.end()
  })

  return (
    <div className="App">

    </div>
  );
}

export default App;

// We provided some simple React template code. Your goal is to modify the component so that you can properly toggle the button to switch between an ON state and an OFF state. When the button is on and it is clicked, it turns off and the text within it changes from ON to OFF and vice versa. Make use of component state for this challenge.

// You are free to add classes and styles, but make sure you leave the component ID's and clases provided as they are. Submit your code once it is complete and our system will validate your output.

import React, { useState } from "react";
import { createRoot } from "react-dom/client";

function Toggle() {
  const[On,SetOn] = useState(true)
  function handleClick() {
    SetOn(!On)
  }

  return <button onClick={handleClick}>{isOn? 'ON' : 'OFF' }</button>;
}

const container = document.getElementById("root");
const root = createRoot(container);
root.render(<Toggle />);

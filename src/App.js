import logo from "./logo.svg";
import "./App.css";
import React, { createRef } from "react";
import flag from "./flag.png";

const colours = {
  1: "blue",
  2: "green",
  3: "red",
  4: "purple",
  5: "#800000", // maroon
  6: "#30D5C8", // turquoise
  7: "black",
  8: "gray",
};

function App() {
  let refsArray = [];
  let gridComponentsArray = [];
  let bombs = [];
  let totalBombs = 40;

  const handleBlankCell = (row, col) => {
    // 13 10
    try {
      for (let i = -1; i < 2; i++) {
        if (refsArray[row - 1][col + i].current.className === "clickedCell") {
          continue;
        } else {
          handleClick(row - 1, col + i);
          console.log("did something");
        }
      }
    } catch (err) {}
    try {
      for (let i = -1; i < 2; i++) {
        if (refsArray[row][col + i].current.className === "clickedCell") {
          continue;
        } else {
          handleClick(row, col + i);
          console.log("did something");
        }
      }
    } catch (err) {}
    try {
      for (let i = -1; i < 2; i++) {
        if (refsArray[row + 1][col + i].current.className === "clickedCell") {
          continue;
        } else {
          handleClick(row + 1, col + i);
          console.log("did something");
        }
      }
    } catch (err) {}
  };

  const handleClick = (row, col, e) => {
    let eventForBlankCell;
    if (e === undefined) {
      eventForBlankCell = "click";
    }
    if (eventForBlankCell === "click" || e.type === "click") {
      refsArray[row][col].current.innerHTML = "";
      let bombCount = 0;

      if (bombs[row].includes(col)) {
        // if cell is a bomb
        refsArray[row][col].current.style.backgroundColor = "red";
      } else {
        // if cell is not a bomb
        refsArray[row][col].current.className = "clickedCell";
        refsArray[row][col].current.style.backgroundColor = "#c6c6c6";
        // check for row above
        try {
          for (let i = -1; i < 2; i++) {
            if (bombs[row - 1].includes(col + i)) {
              bombCount += 1;
            }
          }
        } catch (err) {}
        // check for current row
        try {
          for (let i = -1; i < 2; i++) {
            if (bombs[row].includes(col + i)) {
              bombCount += 1;
            }
          }
        } catch (err) {}
        // check for row below
        try {
          for (let i = -1; i < 2; i++) {
            if (bombs[row + 1].includes(col + i)) {
              bombCount += 1;
            }
          }
        } catch (err) {}

        // populate cell info based on the number of bombs around
        const numberElement = document.createElement("p");

        if (eventForBlankCell === "click") {
          if (bombCount > 0) {
            numberElement.innerHTML = bombCount;
            numberElement.style.color = colours[bombCount];
          } else {
            console.log(row, col);
            handleBlankCell(row, col);
            numberElement.innerHTML = "";
          }
        } else {
          if (bombCount > 0) {
            numberElement.innerHTML = bombCount;
            numberElement.style.color = colours[bombCount];
          } else {
            console.log(row, col);
            handleBlankCell(row, col);
            numberElement.innerHTML = "";
          }
        }

        refsArray[row][col].current.appendChild(numberElement);
      }
    } else if (e.type === "contextmenu") {
      // flagging the cell
      if (refsArray[row][col].current.children.length > 0) {
        refsArray[row][col].current.innerHTML = "";
      } else {
        const flagElement = document.createElement("img");
        flagElement.src = flag;
        refsArray[row][col].current.appendChild(flagElement);
      }
    }
  };

  for (let row = 0; row < 20; row++) {
    refsArray.push([]);
    gridComponentsArray.push([]);
    bombs.push([]);

    for (let i = 0; i < totalBombs / 10; i++) {
      bombs[row].push(Math.floor(Math.random() * 20));
    }

    for (let col = 0; col < 20; col++) {
      const newRef = createRef();
      refsArray[row].push(newRef);
      gridComponentsArray[row].push(
        <div
          ref={newRef}
          className="unclickedCell"
          onClick={(e) => {
            handleClick(row, col, e);
          }}
          onContextMenu={(e) => {
            e.preventDefault();
            handleClick(row, col, e);
          }}
        />
      );
    }
  }

  return (
    <div className="App">
      <div className="wrapper">
        <div className="grid">
          {gridComponentsArray.map((innerList) =>
            innerList.map((cell, key) => cell)
          )}
        </div>
      </div>
    </div>
  );
}

export default App;

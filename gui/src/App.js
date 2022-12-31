import "./App.css";
import React, { createRef, useEffect, useState } from "react";
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
  const [cellClassArray, setCellClassArray] = useState([]);
  const [gridComponentsArray, setGridComponentsArray] = useState([]);
  let refsArray = [];
  let bombs = [];
  let cellClassArrayCopy = [];
  let gridComponentsArrayCopy = [];
  let totalBombs = 40;
  class Cell {
    constructor(row, col, state, bombCountAround, isBomb) {
      this.row = row;
      this.col = col;
      this.state = state;
      this.bombCountAround = bombCountAround;
      this.isBomb = isBomb;
      this.isFlagged = false;
    }

    leftClick() {
      // check if bomb
      if (this.isBomb) {
        this.state = "bomb";
      } else {
        this.state = "clickedCell";
        const bombCountElement = document.createElement("p");
        bombCountElement.innerHTML = this.bombCountAround;
        refsArray[this.row][this.col].current.appendChild(bombCountElement);
      }
    }

    rightClick() {
      this.isFlagged = !this.isFlagged;
      this.state = this.isFlagged ? "unclickedCell" : "flagged";
      if (cellClassArray[this.row][this.col].isFlagged) {
        const flagElement = document.createElement("img");
        flagElement.src = flag;
        refsArray[this.row][this.col].current.appendChild(flagElement);
      } else {
        refsArray[this.row][this.kcol].current.innerHTML = "";
      }
    }
  }

  const checkForBombsAround = (row, col) => {
    let bombCount = 0;
    let isBomb = false;
    if (bombs[row].includes(col)) {
      isBomb = true;
    } else {
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
    }

    return { bombCount, isBomb };
  };

  useEffect(() => {
    // populate bombs
    for (let row = 0; row < 20; row++) {
      bombs.push([]);
      for (let i = 0; i < totalBombs / 10; i++) {
        bombs[row].push(Math.floor(Math.random() * 20));
      }
    }

    // adding the components
    for (let row = 0; row < 20; row++) {
      // refsArray.push([]);
      cellClassArrayCopy.push([]);

      for (let col = 0; col < 20; col++) {
        // const newRef = createRef();

        const { bombCount, isBomb } = checkForBombsAround(row, col);

        cellClassArrayCopy[row].push(
          new Cell(row, col, "unclickedCell", bombCount, isBomb)
        );

        // gridComponentsArrayCopy[row].push(
        //   <div
        //     ref={newRef}
        //     className={cellClassArray[row][col].state ?? "unclickedCell"}
        //     onClick={() => {
        //       cellClassArray[row][col].leftClick();
        //     }}
        //     onContextMenu={(e) => {
        //       e.preventDefault();
        //       cellClassArray[row][col].rightClick();
        //     }}
        //   />
        // );

        // refsArray[row].push(newRef);
      }
    }
    setCellClassArray(cellClassArrayCopy);
  }, []);

  console.log(cellClassArray);

  useEffect(() => {
    const newRef = createRef();
    console.log(cellClassArray);

    for (let row = 0; row < 20; row++) {
      gridComponentsArrayCopy.push([]);
      refsArray.push([]);

      for (let col = 0; col < 20; col++) {
        gridComponentsArrayCopy[row].push(
          <div
            ref={newRef}
            // className={cellClassArray[row][col].state ?? "unclickedCell"}
            onClick={() => {
              cellClassArray[row][col].leftClick();
            }}
            onContextMenu={(e) => {
              e.preventDefault();
              cellClassArray[row][col].rightClick();
            }}
          />
        );
        refsArray[row].push(newRef);
      }
    }
    setGridComponentsArray(gridComponentsArrayCopy.slice());
  }, [cellClassArray]);

  return (
    <div className="App">
      <div className="wrapper">
        <div className="grid">
          {gridComponentsArray.map((innerList, row) =>
            innerList.map((cell, col) => {
              return cell;
            })
          )}
        </div>
      </div>
      <div
        style={{
          backgroundColor: "red",
          padding: 5,
          width: "fit-content",
          cursor: "pointer",
        }}
        onClick={() => setGridComponentsArray((current) => current.slice())}
      >
        Force Rerender
      </div>
    </div>
  );
}

export default App;

// const handleBlankCell = (row, col) => {
//   try {
//     for (let i = -1; i < 2; i++) {
//       if (refsArray[row - 1][col + i].current.className === "clickedCell") {
//         continue;
//       } else {
//         handleClick(row - 1, col + i);
//         console.log("did something");
//       }
//     }
//   } catch (err) {}
//   try {
//     for (let i = -1; i < 2; i++) {
//       if (refsArray[row][col + i].current.className === "clickedCell") {
//         continue;
//       } else {
//         handleClick(row, col + i);
//         console.log("did something");
//       }
//     }
//   } catch (err) {}
//   try {
//     for (let i = -1; i < 2; i++) {
//       if (refsArray[row + 1][col + i].current.className === "clickedCell") {
//         continue;
//       } else {
//         handleClick(row + 1, col + i);
//         console.log("did something");
//       }
//     }
//   } catch (err) {}
// };

// const handleClick = (row, col, e) => {
// if (refsArray[row][col].current.className === "clickedCell") {
//   console.log("thing");
//   // check if number of bombs around it equal to the number flagged
//   // get number of bombs around cell
// }
// let eventForBlankCell;
// if (e === undefined) {
//   eventForBlankCell = "click";
// }
// if (eventForBlankCell === "click" || e.type === "click") {
//   refsArray[row][col].current.innerHTML = "";
//   let bombCount = 0;
//   let flagsAroundCount = 0;

//   if (bombs[row].includes(col)) {
//     // if cell is a bomb
//     refsArray[row][col].current.style.backgroundColor = "red";
//   } else {
//     // if cell is not a bomb
//     refsArray[row][col].current.className = "clickedCell";
//     refsArray[row][col].current.style.backgroundColor = "#c6c6c6";
//     // check for row above
//     try {
//       for (let i = -1; i < 2; i++) {
//         if (bombs[row - 1].includes(col + i)) {
//           bombCount += 1;
//         }
//         if (refsArray[row - 1][col + i].current.className === "flagged") {
//           flagsAroundCount += 1;
//         }
//       }
//     } catch (err) {}
//     // check for current row
//     try {
//       for (let i = -1; i < 2; i++) {
//         if (bombs[row].includes(col + i)) {
//           bombCount += 1;
//         }
//         if (refsArray[row][col + i].current.className === "flagged") {
//           flagsAroundCount += 1;
//         }
//       }
//     } catch (err) {}
//     // check for row below
//     try {
//       for (let i = -1; i < 2; i++) {
//         if (bombs[row + 1].includes(col + i)) {
//           bombCount += 1;
//         }
//         if (refsArray[row + 1][col + i].current.className === "flagged") {
//           flagsAroundCount += 1;
//         }
//       }
//     } catch (err) {}

// if (
//   refsArray[row][col].current.className === "clickedCell" ||
//   flagsAroundCount === bombCount
// ) {
//   e = { type: "click" };
//   try {
//     for (let i = -1; i < 2; i++) {
//       if (
//         refsArray[row - 1][col + i].current.className ===
//           "clickedCell" ||
//         refsArray[row - 1][col + i].current.className === "flagged"
//       ) {
//         continue;
//       } else {
//         refsArray[row - 1][col + i].current.className = "clickedCell";
//         // handleClick(row - 1, col + i, e);
//         console.log("did something");
//       }
//     }
//   } catch (err) {}
//   try {
//     for (let i = -1; i < 2; i++) {
//       if (
//         refsArray[row][col + i].current.className === "clickedCell" ||
//         refsArray[row][col + i].current.className === "flagged"
//       ) {
//         continue;
//       } else {
//         refsArray[row][col + i].current.className = "clickedCell";
//         // handleClick(row, col + i, e);
//         console.log("did something");
//       }
//     }
//   } catch (err) {}
//   try {
//     for (let i = -1; i < 2; i++) {
//       if (
//         refsArray[row + 1][col + i].current.className ===
//           "clickedCell" ||
//         refsArray[row + 1][col + i].current.className === "flagged"
//       ) {
//         continue;
//       } else {
//         refsArray[row + 1][col + i].current.className = "clickedCell";
//         // handleClick(row + 1, col + i, e);
//         console.log("did something");
//       }
//     }
//   } catch (err) {}
// }

// populate cell info based on the number of bombs around
//       const numberElement = document.createElement("p");

//       if (eventForBlankCell === "click") {
//         if (bombCount > 0) {
//           numberElement.innerHTML = bombCount;
//           numberElement.style.color = colours[bombCount];
//         } else {
//           console.log(row, col);
//           handleBlankCell(row, col);
//           numberElement.innerHTML = "";
//         }
//       } else {
//         if (bombCount > 0) {
//           numberElement.innerHTML = bombCount;
//           numberElement.style.color = colours[bombCount];
//         } else {
//           console.log(row, col);
//           handleBlankCell(row, col);
//           numberElement.innerHTML = "";
//         }
//       }

//       refsArray[row][col].current.appendChild(numberElement);
//     }
//   } else if (e.type === "contextmenu") {
//     // flagging the cell
//     if (refsArray[row][col].current.children.length > 0) {
//       refsArray[row][col].current.innerHTML = "";
//       refsArray[row][col].current.className = "flagged";
//     } else {
//       const flagElement = document.createElement("img");
//       flagElement.src = flag;
//       refsArray[row][col].current.className = "unclickedCell";
//       refsArray[row][col].current.appendChild(flagElement);
//     }
//   }
// };

const character = "!";
const count = 10;
const rows = [];
const inverted = false;

const padRow = (rowNumber, rowCount) => 
  " ".repeat(rowCount - rowNumber) + character.repeat(2 * rowNumber - 1) + " ".repeat(rowCount - rowNumber);

for (let i = 1; i <= count; i++) {
  inverted ? rows.unshift(padRow(i, count)) : rows.push(padRow(i, count));
}

const result = rows.join("\n");
console.log(result);
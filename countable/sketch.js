function setup(){
  createCanvas(700, 700);
  frameRate(5);
}

function a(i,j){
  return Math.round(1000*(i+1)/(j+1))/1000;
}

// sets:
// A_1 = {1, 2, 3, 4, ...}
// A_2 = {2, 4, 6, 8, ...}
// A_3 = {3, 6, 9, 12, ...}

let A_union = {};
let grid = {};

function grid_hash(i, j){
  return i+":"+j;
}

function next_animation_frame(){
  if(A_union[a(row, col)]){
    grid[grid_hash(row, col)] = "duplicate";
  }
  else{
    grid[grid_hash(row, col)] = "first";
    A_union[a(row, col)] = true;
    document.getElementById("serialnums").innerHTML += `<p>${a(row, col)} \t\t #${serial_number}</p>`;
    serial_number += 1;
  }

  if(row > 0){
    row -= 1;
    col += 1;
  }
  else{
    row = col + 1;
    col = 0;
    if(row > size){
      size = size *2;
    }
  }

  setTimeout(next_animation_frame, speed);
}

let row = 0;
let col = 0;
let size = 4;
let speed = 300;
let serial_number = 1;

function draw(){
  background(0, 255, 255);
  for (var row = 0; row < size; row++) {
    for (var col = 0; col < size; col++) {
      if(grid[grid_hash(row, col)]){
        if(grid[grid_hash(row, col)] == "first"){
          fill(0, 255, 0);
        }
        else if(grid[grid_hash(row, col)] == "duplicate"){
          fill(255, 0, 0);
        }
      }
      else {
        fill(200, 200, 200, 100);
      }
      rect(col*width/size, row*height/size, width/size, height/size);
      fill(0,0,0);
      text(a(row,col), col*width/size, row*height/size, width/size, height/size);
    }
  }
}

setTimeout(next_animation_frame, 500);


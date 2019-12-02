
// THOUGHTS:
//
// shouldn't have to completely recalculate connections every time, they barely update
// a different possible way of doing cnnections: R3 distance
// a different possible way of doing connections: fixed connections from the beginning of the program

let dots = [];
let dotTrajectories = [];
let redirectPr = 0.1;
let wallEjectionSpeedMultiplier = 30;
let n = 15;
let neighborThresh = 3; // the max number of connections
let distThresh = 50;
let repulseDist = 10;
let repulsiveFnets = [];

// let color1 = new p5.Vector(138, 255, 255);
// let color2 = new p5.Vector(255, 74, 74);
// let color1 = new p5.Vector(255, 0, 0);
// let color2 = new p5.Vector(0, 0, 255);
let color1 = new p5.Vector(128,255,255);
let color2 = new p5.Vector(255,255,255);

let colorLerp = 0.5;
let colorChange = 0.001;

let speed = 0.5;

function setup(){
	let cnv = createCanvas(250, 250);
  cnv.parent("canvas-parent");

	for(let i=0; i < n; i++){
		dots.push(createVector(random()*width, random()*height));
    dotTrajectories.push(random()*TWO_PI);
    repulsiveFnets.push(createVector(0,0));
	}
}

function draw() {
  if (colorLerp >= 1) {
    colorChange *= -1;
  }
  if(colorLerp <= 0) {
    colorChange *= -1;
  }
  colorLerp += colorChange;
  let currentColor = p5.Vector.lerp(color1, color2, colorLerp);
  let antiColor = p5.Vector.lerp(color1, color2, 1-colorLerp);
 
	// background(200,200,200);
  background(0);
  stroke(currentColor.x, currentColor.y, currentColor.z);
	perturbDots();
  connectDots();
  strokeWeight(3);
	fill(antiColor.x, antiColor.y, antiColor.z);
	for(let i in dots){
		ellipse(dots[i].x, dots[i].y, 10, 10);
	}
}

function realMod(n, m){
  return ((n%m) + m) % m;
}

function perturbDots(){
	for(let i in dots){

    let dotHeading = p5.Vector.fromAngle(dotTrajectories[i]).mult(speed);
    dots[i].add(dotHeading);

    if (random() < redirectPr) {
      dotTrajectories[i] += randomGaussian(0,TWO_PI/12);
    }

    // pretty good randomness
    dots[i].x += randomGaussian(0, speed/10);
    dots[i].y += randomGaussian(0, speed/10);
   
    // less good randomness
		// dots[i].x += (random()-0.5)*10*speed;
		// dots[i].y += (random()-0.5)*10*speed;

    // bounce off boundaries
    if (dots[i].x > width){
      dots[i].x -= speed*wallEjectionSpeedMultiplier;
      dotTrajectories[i] += PI;
    }
    else if (dots[i].x < 0){
      dots[i].x += speed*wallEjectionSpeedMultiplier;
      dotTrajectories[i] += PI;
    }
    if (dots[i].y > height){
      dots[i].y -= speed*wallEjectionSpeedMultiplier;
      dotTrajectories[i] += PI;
    }
    else if (dots[i].y < 0){
      dots[i].y += speed*wallEjectionSpeedMultiplier;
      dotTrajectories[i] += PI;
    }

    if (repulsiveFnets[i].mag() > 0){
      dotTrajectories[i] += PI;
      repulsiveFnets[i].setMag(speed*3);
      dots[i].add(repulsiveFnets[i]);
      repulsiveFnets[i].mult(0);
    }

	}
}

function connectDots() {
  let connectionsMade = [];
  let closestCandidates = [];
  for(let i = 0; i < n; i++) {
    connectionsMade.push(0);
    let allDists = []; // this is stupid, I should be inserting new distances in to a sorted array, but WHATEVER!! n^2 log n VS n^2 log n AM I RIGHT? technically but the constants are egregious
    for(let j = i+1; j < n; j++) {
      nodeDist = dots[i].dist(dots[j]);
      if (nodeDist < distThresh){
        allDists.push({"dist":nodeDist, "indices":[i,j]});
      }
    }
    allDists.sort(function(x,y){x.dist - y.dist});
    for(let k = 0; k < min(allDists.length, neighborThresh); k++) {
      closestCandidates.push(allDists[k]);
    }
  }
  // OK THIS is kinda trash too, but asymptotically "whatever"
  closestCandidates.sort(function(x,y){x.dist - y.dist});

  for(let k in closestCandidates){
    let i = closestCandidates[k].indices[0];
    let j = closestCandidates[k].indices[1];
    if (connectionsMade[i] < neighborThresh && connectionsMade[j] < neighborThresh) {
      line(dots[i].x, dots[i].y, dots[j].x, dots[j].y);
      if (closestCandidates[k].dist < repulseDist){
        repulsiveFnets[i].add(p5.Vector.sub(dots[i], dots[j]));
        repulsiveFnets[j].add(p5.Vector.sub(dots[j], dots[i]));
      }
    }
  }
}



const W=500, H=500, N=3;
let player=[0,0];
let line_segs = [];

function setup() {
  createCanvas(W, H);
  for (let i = 0; i < N; i++) {
    line_segs.push([[random(W)-W/2,random(H)-H/2],[random(W)-W/2,random(H)-H/2]]);
  }
}

function weirdatan(x,y){
  let res = Math.atan2(x,y);
  if(res >= 0){
    return res;
  } else {
    return Math.PI-res;
  }
}

/*
Let θi , ϕi be the angles from the player to the more clockwise and more counter clockwise endpoints of the
line segment for wall i, i.e. θi < ϕi where angle is measured horizontal ray pointing to the right from the
player. Create a lists A,D of wall indices i sorted by θi , ϕi in increasing (i.e. counter-clockwise) order. We
loop over all the O(n) angles in counter-clockwise order. As we loop, we maintain a minheap of the currently
visible walls, sorted by how close they are to the player: that is, the minimum element in the minheap is
the wall visible with our current line-of-sight angle. We also maintain pointers for each wall to its location
in the min-heap. At angle θi wall i appears and we insert it into the minheap, by repeatedly comparing
its distance from the player along the line of sight to the distance from the player along the line of sight for
other walls in the minheap (updating the pointers as we go). At angle ϕi we must delete wall i from the
min-heap (we find it using the pointers), and re-balance the heap, with comparisons as described above. At
each θ we mark the min element, i.e. closest wall, as being visible by the player.
Consider the running time of this algorithm: we must sort the line segments by θi , and then we must
perform O(n) inserts and delete-mins on the minheap. Overall, this takes O(n log n) time.
*/

function visible(){
  let theta = [], phi = [];
  let A = [], D=[];
  for (let i=0; i<N; i++){
    const e1 = line_segs[i][0], e2 = line_segs[i][1];
    let a1 = weirdatan(e1[0]-player[0], e1[1]-player[1]);
    let a2 = weirdatan(e2[0]-player[0], e2[1]-player[1]);
    theta.push(Math.min(a1,a2));
    phi.push(Math.max(a1,a2));
    A.push(i); D.push(i);
  }

  // sentinels
  theta.push(Infinity);
  phi.push(Infinity);
  A.push(N);D.push(N);

  A.sort((i,j)=> theta[i]-theta[j]);
  D.sort((i,j)=> phi[i]-phi[j]);

  let ai=0,di=0;
  console.log(A);
  console.log(theta)
  console.log(D);
  console.log(phi);
  while(ai < N || di < N){
    if (theta[A[ai]] < phi[D[di]]){
      console.log("arrive! "+ A[ai] + ": " + theta[A[ai]]);
      ai += 1;
    }
    else{
      console.log("depart! "+ D[di] + ": " + phi[D[di]]);
      di += 1;
    }
  }

}

function draw() {
  stroke(0);
  translate(W/2,H/2);
  strokeWeight(2);
  ellipse(player[0],player[1],5,5);
  for (let i = 0; i < N; i++) {
    strokeWeight(2+5*i);
    const e1 = line_segs[i][0], e2 = line_segs[i][1];
    line(e1[0],e1[1],e2[0],e2[1]);
  }

  strokeWeight(1);
  stroke(255,0,0);
  for(let t = 0; t < Math.PI*2; t+=0.5){
    line(0,0,Math.cos(t-Math.PI/2)*50, Math.sin(t-Math.PI/2)*50);
    text(t,Math.cos(t-Math.PI/2)*50, Math.sin(t-Math.PI/2)*50);
  }

}


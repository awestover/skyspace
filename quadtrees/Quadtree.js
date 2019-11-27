// the game tree. checks all collisions

let MAX_OCCUPANTS = 4;
class Quadtree {
  constructor(cross) { // a cross is [center x,center y, width across, height]
    this.cross = cross;
    this.box = this.crossesBox(this.cross);
    this.occupants = [];
    this.split = false;
    this.regions = [];
  }

  clear() {
    this.occupants = [];
    this.split = false;
    this.regions = [];
  }

  insertUser(user)
  {
    for (let an in allAnimals)
    {
      for (let i in user[allAnimals[an]])
      {
        this.insert(user[allAnimals[an]][i]);
      }
    }
  }

  splitNode() {
    this.split = true;
    for (let i = 0; i < 4; i++) {
      this.regions.push(new Quadtree(this.subregionCross(i)));
    }
    let cOccupants = this.occupants;
    this.occupants = [];
    for (var i = 0; i < cOccupants.length; i++) {
      this.insert(cOccupants[i]);
    }
  }

  insert(other) {
    if (!this.split)
    {
      this.occupants.push(other);
      if (this.occupants.length > MAX_OCCUPANTS)
      {
        this.splitNode();
      }
      return true;
    }
    let isIn = -1;
    for (let i = 0; i < 4; i++)
    {
      if (this.rectCollide(other.getBox(), this.regions[i].box))
      {
        if (isIn == -1)
        {
          isIn = i;
        }
        else
        {
          other.idx = 4;
          this.occupants.push(other);
          return true;
        }
      }
    }
    other.idx = isIn;
    this.regions[isIn].insert(other);
  }

  getParent(other) {
    if (!this.split){
      return this;
    }
    let isIn = -1;
    for (let i = 0; i < 4; i++)
    {
      if (this.rectCollide(other.getBox(), this.regions[i].box))
      {
        if (isIn == -1)
        {
          isIn = i;
        }
        else
        {
          return this; // Luke, I am your father...
        }
      }
    }
    return this.regions[isIn].getParent(other);
  }

  getCodedParent(code) {
    if (code.length > 0)
    {
      return this.regions[code[0]].getCodedParent(code.slice(1));
    }
    else {
      return this;
    }
  }

  crossesBox(cross) {
    return [cross[0]-cross[2]/2,cross[1]-cross[3]/2,cross[2],cross[3]];
  }

  // quadrant system
  /* ie
    1 0
    2 3
  */
  subregionCross(i) {
    let cross = [0,0,this.cross[2]/2,this.cross[3]/2];
    if(i == 0) {
      cross[0] = this.cross[0] + this.cross[2]/4;
      cross[1] = this.cross[1] - this.cross[3]/4;
    }
    else if(i == 1)
    {
      cross[0] = this.cross[0] - this.cross[2]/4;
      cross[1] = this.cross[1] - this.cross[3]/4;
    }
    else if(i == 2) {
      cross[0] = this.cross[0] - this.cross[2]/4;
      cross[1] = this.cross[1] + this.cross[3]/4;
    }
    else if(i == 3) {
      cross[0] = this.cross[0] + this.cross[2]/4;
      cross[1] = this.cross[1] + this.cross[3]/4;
    }
    return cross;
  }

  // 1 d collision detection (real number line)
  collideX(a, b)
  {
    return ((b[0] < a[1]) && (b[1] > a[0]));
  }

  // do 2 boxes intersect?
  rectCollide(a, b)
  {
    let xInt = this.collideX([a[0], a[0]+a[2]], [b[0], b[0]+b[2]]);
    let yInt = this.collideX([a[1], a[1]+a[3]], [b[1], b[1]+b[3]]);
    return (xInt && yInt);
  }

  display() {
    if (this.split)
    {
      stroke(0,255,0);
      line(this.cross[0]-this.cross[2]/2, this.cross[1], this.cross[0]+this.cross[2]/2, this.cross[1]);
      line(this.cross[0], this.cross[1]-this.cross[3]/2, this.cross[0], this.cross[1]+this.cross[3]/2);
      for (let i = 0; i < 4; i++)
      {
        if (this.regions[i])
        {
          this.regions[i].display();
        }
      }
    }
  }

}


// from the old thing

  // crumby comparison for now
  // getCollisions()
  // {
  //   let collisions = [];
  //   for (var i = 0; i < this.values.length; i++)
  //   {
  //     for (var j = i+1; j < this.values.length; j++)
  //     {
  //         if (this.checkBoxCollide(this.values[i].getBox(), this.values[j].getBox()))
  //         {
  //           collisions.push([i, j]);
  //         }
  //     }
  //   }
  //   return collisions;
  // }

  // getPredatorTargets()
  // {
  //   let predatorIdxs = [];// idx of predators
  //   let targets = []; // for predator sight animal collisions, lists center coords
  //   for (let i in this.values)
  //   {
  //     let targetPos = [];
  //     let targetDist = false; // really squared distances...
  //     if (this.values[i].type == "predators")
  //     {
  //       for (let j in this.values)
  //       {
  //         if (i!=j && this.values[j].type=="personals")
  //         {
  //           if (rectInCircle(this.values[j].getBox(), [this.values[i].getCenter(), this.values[i].sightR]))
  //           {
  //             let cDist = centerSqaredDist(this.values[i], this.values[j]);
  //             if (targetDist==false || targetDist > cDist)
  //             {
  //               targetDist = cDist;
  //               targetPos = this.values[j].getCenter();
  //             }
  //           }
  //         }
  //       }
  //       if (targetPos.length == 2)
  //       {
  //         targets.push(targetPos);
  //         predatorIdxs.push(i);
  //       }
  //     }
  //   }
  //   return [predatorIdxs, targets];
  // }

  // // crumby comparison FOR NOW
  // getCollisionsWith(box)
  // {
  //   let collisions = [];
  //   for (var i = 0; i < this.values.length; i++)
  //   {
  //     if (this.checkBoxCollide(this.values[i].getBox(), box))
  //     {
  //       collisions.push(i);
  //     }
  //   }
  //   return collisions;
  // }

  // getTerritoryCollisions()
  // {
  //   let collisions = [];
  //   for (let i = 0; i < this.values.length; i++)
  //   {
  //     for (let j = 0; j < numTerritories; j++)
  //     {
  //       if (rectInCircle(this.values[i].getBox(), [territoryLocs[j], territoryR]))
  //       {
  //         collisions.push([i,j]);
  //         break;
  //       }
  //     }
  //   }
  //   return collisions;
  // }

// }

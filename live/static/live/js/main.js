function myFunction() {
    var g = new Graph( [
    {"nm":0,"x":430,"y":250,"go":[1,7,16,4,10,21,25,23],"chk":1},
    {"nm":1,"x":430,"y":110,"go":[14,19,2,0],"chk":0},
    {"nm":2,"x":430,"y":80,"go":[3,1],"chk":0},
    {"nm":3,"x":430,"y":50,"go":[9,12,2],"chk":0},
    {"nm":4,"x":430,"y":390,"go":[17,18,5,0,7],"chk":0},
    {"nm":5,"x":430,"y":420,"go":[4,6],"chk":0},
    {"nm":6,"x":430,"y":440,"go":[9,12,5],"chk":0},
    {"nm":7,"x":560,"y":250,"go":[14,17,8,0,4],"chk":0},
    {"nm":8,"x":590,"y":250,"go":[9,7],"chk":0},
    {"nm":9,"x":620,"y":250,"go":[3,6,8],"chk":0},
    {"nm":10,"x":300,"y":250,"go":[18,19,11,0],"chk":0},
    {"nm":11,"x":270,"y":250,"go":[10,12],"chk":0},
    {"nm":12,"x":240,"y":250,"go":[6,3,11],"chk":0},
    {"nm":13,"x":460,"y":250,"go":[],"chk":0},
    {"nm":14,"x":560,"y":110,"go":[1,7,15],"chk":0},
    {"nm":15,"x":540,"y":130,"go":[14,16],"chk":0},
    {"nm":16,"x":520,"y":150,"go":[15,0],"chk":0},
    {"nm":17,"x":560,"y":390,"go":[7,4,24],"chk":0},
    {"nm":18,"x":300,"y":390,"go":[4,10,22],"chk":0},
    {"nm":19,"x":300,"y":110,"go":[10,1,20],"chk":0},
    {"nm":20,"x":320,"y":130,"go":[19,21],"chk":0},
    {"nm":21,"x":340,"y":150,"go":[20,0],"chk":0},
    {"nm":22,"x":320,"y":370,"go":[23,18],"chk":0},
    {"nm":23,"x":340,"y":350,"go":[22,0],"chk":0},
    {"nm":24,"x":540,"y":370,"go":[17,25],"chk":0},
    {"nm":25,"x":520,"y":350,"go":[24,0],"chk":0},
    {"nm":26,"go":[],"x":490,"y":320,"chk":0},
    {"nm":27,"go":[],"x":520,"y":290,"chk":0},
    {"nm":28,"go":[],"x":460,"y":350,"chk":0}
    ]
                     );
    window.document.getElementById("graph").innerHTML = g;
}

function first() {
    document.write(5 + 155);
}

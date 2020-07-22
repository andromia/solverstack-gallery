function buildVrpMap(data) {
    console.log("data", data);

    d3.select("#vrp-map").append("p").text(JSON.stringify(data));
}

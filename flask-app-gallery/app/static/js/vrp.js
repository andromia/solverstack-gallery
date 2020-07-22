function plotOrigins(markers) {
    console.log("markers", markers);

    // The svg
    var svg = d3.select("svg"),
    width = +svg.attr("width"),
    height = +svg.attr("height");

    // Map and projection
    var projection = d3.geoMercator()
    .center([markers[0].longitude, markers[0].latitude])
    .scale(500)
    .translate([ width/2, height/2 ])

    // Load external data and boot
    d3.json("https://raw.githubusercontent.com/holtzy/D3-graph-gallery/master/DATA/world.geojson")
        .then(function(data) {

        // Filter data
        data.features = data.features.filter( function(d){return d.properties.name=="USA"} );

        // Draw the map
        svg.append("g")
            .selectAll("path")
            .data(data.features)
            .enter()
            .append("path")
            .attr("fill", "#b8b8b8")
            .attr("d", d3.geoPath()
                .projection(projection)
            )
            .style("stroke", "black")
            .style("opacity", .3)

        // Add circles:
        svg
        .selectAll("myCircles")
        .data(markers)
        .enter()
        .append("circle")
            .attr("cx", function(d){ return projection([d.longitude, d.latitude])[0] })
            .attr("cy", function(d){ return projection([d.longitude, d.latitude])[1] })
            .attr("r", 14)
            .style("fill", "69b3a2")
            .attr("stroke", "#69b3a2")
            .attr("stroke-width", 3)
            .attr("fill-opacity", .4)
    }).catch(function(error) {
        console.log("error", error);
      });
}

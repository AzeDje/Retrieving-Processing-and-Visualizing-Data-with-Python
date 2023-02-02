
// set the dimensions and margins of the graph
var margin = {top: 20, right: 20, bottom: 85, left: 80},
    width = 660 - margin.left - margin.right,
    height = 600 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg = d3.select("#svg2")
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

var parseDate = d3.timeParse("%Y");
data2.forEach(function(d) {
    d.date = parseDate(String(d.date));
  });

    // Add X axis --> it is a date format
    var x = d3.scaleTime()
      .domain(d3.extent(data2, function(d) { return d.date; }))
      .range([ 0, width ]);
    svg.append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x))
    .selectAll("text")
      .attr("transform", "translate(-10,0)rotate(-45)")
      .style("text-anchor", "end")
    svg.append('text')
      .style("text-anchor", "end")
     .attr('x',width+20)
     .attr('y',height+margin.top+20)
     .text('Year') ; 
    // Max value observed:
    const max = d3.max(data2, function(d) { return +d.value; })

    // Add Y axis
    var y = d3.scaleLinear()
      .domain([0, max])
      .range([ height, 0 ]);
    svg.append("g")
      .call(d3.axisLeft(y))
    svg.append('text')
  .style("text-anchor", "end")
  .attr("transform", "rotate(-90)")
  .attr('y',-margin.left+40)
  .attr('dy',-margin.top)
  .text('Million metric tonnes carbon dioxide');

    // Set the gradient
    svg.append("linearGradient")
      .attr("id", "line-gradient")
      .attr("gradientUnits", "userSpaceOnUse")
      .attr("x1", 0)
      .attr("y1", y(0))
      .attr("x2", 0)
      .attr("y2", y(max))
      .selectAll("stop")
        .data([
          {offset: "0%", color: "blue"},
          {offset: "100%", color: "red"}
        ])
      .enter().append("stop")
        .attr("offset", function(d) { return d.offset; })
        .attr("stop-color", function(d) { return d.color; });
svg.append('text')
      .attr('class', 'title')
      .attr('x', width / 2)
      .attr('y', 10)
      .attr('text-anchor', 'middle')
      .text('CO2 Emissions in the world over the time')
    // Add the line
    svg.append("path")
      .datum(data2)
      .attr("fill", "none")
      .attr("stroke", "url(#line-gradient)" )
      .attr("stroke-width", 2)
      .attr("d", d3.line()
        .x(function(d) { return x(d.date) })
        .y(function(d) { return y(d.value) })
        );


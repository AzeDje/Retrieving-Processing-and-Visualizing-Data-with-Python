// set the dimensions and margins of the graph
var margin = {top: 20, right: 20, bottom: 85, left: 80},
    width = 660 - margin.left - margin.right,
    height = 600 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg = d3.select("#svg1")
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

// X axis
var x = d3.scaleBand()
  .range([ 0, width ])
  .domain(data1.map(function(d) { return d.Country; }))
  .padding(0.2);
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
  .text('Location')  

// Add Y axis
var y = d3.scaleLinear()
  .domain([0, 100000])
  .range([ height, 0]);
svg.append("g")
  .call(d3.axisLeft(y));
svg.append('text')
  .style("text-anchor", "end")
  .attr("transform", "rotate(-90)")
  .attr('y',-margin.left+40)
  .attr('dy',-margin.top)
  .text('Thousand barrels per day')

// Bars
svg.selectAll("mybar")
  .data(data1)
  .enter()
  .append("rect")
    .attr("x", function(d) { return x(d.Country); })
    .attr("width", x.bandwidth())
    .attr("fill", "#69b3a2")
    // no bar at the beginning thus:
    .attr("height", function(d) { return height - y(0); }) // always equal to 0
    .attr("y", function(d) { return y(0); });
svg.append('text')
      .attr('class', 'title')
      .attr('x', width / 2)
      .attr('y', 10)
      .attr('text-anchor', 'middle')
      .text('Top 10 largest Petroleum consuming in 2021')
// Animation
svg.selectAll("rect")
  .transition()
  .duration(800)
  .attr("y", function(d) { return y(d.Value); })
  .attr("height", function(d) { return height - y(d.Value); })
  .delay(function(d,i){console.log(i) ; return(i*100)});

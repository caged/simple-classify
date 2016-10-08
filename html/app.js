const el = d3.select(".js-vis"),
    ewidth = parseFloat(el.style("width")),
    eheight = parseFloat(el.style("height"))

const margin = { top: 20, right: 20, bottom: 20, left: 50 },
    width = (ewidth / 2) - margin.left - margin.right,
    height = (eheight / 2) - margin.top - margin.bottom

const combos = [
  ['G', 'F'],
  ['F', 'C'],
  ['C', 'G']
]

const vis = el.selectAll('.scatter')
  .data(combos)
.enter().append('svg')
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")")

vis.append('text')
  .text(String)

function format(row) {
    row.G = +row.G
    row.F = +row.F
    row.C = +row.C

    return row
}

function draw(err, data) {
  if(err) return console.log(err)

  data = data.filter((d) => { return d.season == '2014-15' })

  var x = d3.scaleLinear()
    .domain([0, 1])
    .range([0, width])
    .clamp(true)

  var y = d3.scaleLinear()
    .domain([1, 0])
    .range([height, 0])
    .clamp(true)

  var xax = d3.axisTop(x),
      yax = d3.axisLeft(y)

  vis.selectAll('.node')
    .data(data)
  .enter().append('circle')
    .attr('class', 'node')
    .attr('r', '3')
    .attr('cx', function(d) {
      var keys = d3.select(this.parentNode).datum()
      return x(d[keys[0]])
    })
    .attr('cy', function(d) {
      var keys = d3.select(this.parentNode).datum()
      return y(d[keys[1]])
    })
    .on('click', function(d) { console.log(d); })

}

d3.csv('/data/results.csv')
  .row(format)
  .get(draw)

// // Generate fake data
// var random = d3.randomNormal(0, 0.2),
//     data = d3.range(300).map(function() {
//       return [random() + Math.sqrt(3), random() + 1];
//     })
//
// var x = d3.scaleLinear()
//   .domain(d3.extent(data, function(d) { return d[0] }))
//   .range([0, width])
//
// var y = d3.scaleLinear()
//   .domain(d3.extent(data, function(d) { return d[1] }))
//   .range([height, 0])
//
// var xax = d3.axisTop(x),
//     yax = d3.axisLeft(y)
//
// var vis = el.append("svg")
//   .attr("width", width + margin.left + margin.right)
//   .attr("height", height + margin.top + margin.bottom)
// .append("g")
//   .attr("transform", "translate(" + margin.left + "," + margin.top + ")")
//
// vis.append("g")
//   .call(xax)
//
// vis.append("g")
//   .call(yax)
//
// var nodes = vis.append("g")
//   .attr("class", "nodes")
//
// nodes.selectAll(".node")
//   .data(data)
// .enter().append("circle")
//   .attr("r", 3)
//   .attr("cx", function(d) { return x(d[0]) })
//   .attr("cy", function(d) { return y(d[1]) })
//   .style("fill", function() { return "hsl(" + Math.random() * 360 + ", 50%, 50%)"; })

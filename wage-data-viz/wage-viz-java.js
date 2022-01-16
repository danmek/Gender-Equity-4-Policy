function draw_wage_map() {
        //

    var width = 900;
        height = 700;

    var tip = d3.tip()
      .attr('class', 'd3-tip')
      .offset([-5, 0])
      .html(function(d) {
        var dataRow = countryById.get(d.properties.name);
           if (dataRow) {
               console.log(dataRow);
               return "In " + dataRow.states + " women make " + dataRow.mortality + " percent of what men do.";
           } else {
               console.log("no dataRow", d);
               return d.properties.name + ": No data.";
           }
      })


    var svg = d3.select('#vis').append('svg')
        .attr('width', width)
        .attr('height', height);

    svg.call(tip);

    var projection = d3.geo.albersUsa()
        .scale(900) // mess with this if you want
        .translate([width / 2, height / 2]);

    var path = d3.geo.path()
        .projection(projection);

    var colorScale = d3.scale.linear().range(["#D4EEFF", "#073452"]).interpolate(d3.interpolateLab);

    var countryById = d3.map();

    // we use queue because we have 2 data files to load.
    queue()
        .defer(d3.json, "USA.json")
        .defer(d3.csv, "mortality.csv", typeAndSet) // process
        .await(loaded);

    function typeAndSet(d) {
        d.mortality = +d.mortality;
        countryById.set(d.states, d);
        return d;
    }

    function getColor(d) {
        var dataRow = countryById.get(d.properties.name);
        if (dataRow) {
            console.log(dataRow);
            return colorScale(dataRow.mortality);
        } else {
            console.log("no dataRow", d);
            return "#ccc";
        }
    }


    function loaded(error, usa, mortality) {

        console.log(usa);
        console.log(mortality);

        colorScale.domain(d3.extent(mortality, function(d) {return d.mortality;}));

        var states = topojson.feature(usa, usa.objects.units).features;

        svg.selectAll('path.states')
            .data(states)
            .enter()
            .append('path')
            .attr('class', 'states')
            .attr('d', path)
            .on('mouseover', tip.show)
            .on('mouseout', tip.hide)
            .attr('fill', function(d,i) {
                console.log(d.properties.name);
                return getColor(d);
            })
            .append("title");

        var linear = colorScale;

        svg.append("g")
          .attr("class", "legendLinear")
          .attr("transform", "translate(20,20)");

        var legendLinear = d3.legend.color()
          .shapeWidth(30)
          .orient('horizontal')
          .scale(linear);

        svg.select(".legendLinear")
          .call(legendLinear);

    }

}

draw_wage_map();

import * as d3 from "d3";
import { useState, useEffect, useRef } from "react";
import PropTypes from "prop-types";

export function LineChart({ data = [], dimensions = {} }) {
  const svgRef = useRef(null);
  // to detect what line to animate we should store previous data state
  const [prevItems, setPrevItems] = useState([]);
  const { width, height, margin = {} } = dimensions;
  const svgWidth = width + margin.left + margin.right;
  const svgHeight = height + margin.top + margin.bottom;

  useEffect(() => {
    if (data.length > 0) {
      console.log('data', data)
      const xScale = d3
        .scaleTime()
        .domain(d3.extent(data[0].items, (d) => d.year))
        .range([0, width]);
      const yScale = d3
        .scaleLinear()
        .domain([
          d3.min(data[0].items, (d) => d.temperature - 0.5),
          d3.max(data[0].items, (d) => d.temperature + 0.5),
        ])
        .range([height, 0]);
      const svgEl = d3.select(svgRef.current);
      svgEl.selectAll("*").remove(); 
      const svg = svgEl
        .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);
      const xAxis = d3
        .axisBottom(xScale)
        .ticks(10)
        .tickSize(-height + margin.bottom)
        .tickFormat(d3.format("d"));
      const xAxisGroup = svg
        .append("g")
        .attr("transform", `translate(0, ${height - margin.bottom})`)
        .call(xAxis);
      xAxisGroup.select(".domain").remove();
      xAxisGroup.selectAll("line").attr("stroke", "rgba(255, 255, 255, 0.2)");
      xAxisGroup
        .selectAll("text")
        .attr("opacity", 0.5)
        .attr("font-size", "1rem");
      const yAxis = d3
        .axisLeft(yScale)
        .ticks(10)
        .tickSize(-width)
        .tickFormat((v) => `${v}°C`);
      const yAxisGroup = svg.append("g").call(yAxis);
      yAxisGroup.select(".domain").remove();
      yAxisGroup.selectAll("line").attr("stroke", "rgba(255, 255, 255, 0.2)");
      yAxisGroup
        .selectAll("text")
        .attr("opacity", 0.5)
        .attr("font-size", "1rem");
      const line = d3
        .line()
        .x((d) => xScale(d.year))
        .y((d) => yScale(d.temperature));
      const lines = svg
        .selectAll(".line")
        .data(data)
        .enter()
        .append("path")
        .attr("fill", "none")
        .attr("stroke", (d) => d.color)
        .attr("stroke-width", 3)
        .attr("d", (d) => line(d.items));
      // Use stroke-dashoffset for transition
      lines.each((d, i, nodes) => {
        const element = nodes[i];
        const length = element.getTotalLength();
        if (!prevItems.includes(d.name)) {
          d3.select(element)
            .attr("stroke-dasharray", `${length},${length}`)
            .attr("stroke-dashoffset", length)
            .transition()
            .duration(750)
            .ease(d3.easeLinear)
            .attr("stroke-dashoffset", 0);
        }
      });
      setPrevItems(data.map(({ name }) => name));
    }
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [data]);

  return <svg ref={svgRef} width={svgWidth} height={svgHeight} />;
}

LineChart.propTypes = {
  data: PropTypes.array.isRequired,
  dimensions: PropTypes.object.isRequired,
};

export default LineChart;

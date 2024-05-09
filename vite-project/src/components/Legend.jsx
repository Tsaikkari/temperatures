import PropTypes from 'prop-types';

const Legend = ({ data, selectedItems, onChange }) => (
  <div className="legend-container">
    {data.map((d) => (
      <div className="checkbox" style={{ color: d.color }} key={d.name}>
        {d.name !== "data_0" && (
          <input
            type="checkbox"
            value={d.name}
            checked={selectedItems.includes(d.name)}
            onChange={() => onChange(d.name)}
          />
        )}
        <label>{d.name}</label>
      </div>
    ))}
  </div>
);

Legend.propTypes = {
  data: PropTypes.array.isRequired,
  selectedItems: PropTypes.array.isRequired,
  onChange: PropTypes.func.isRequired,
};

export default Legend;

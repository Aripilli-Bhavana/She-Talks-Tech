const SkillMeter = ({ skill, match }) => (
    <div className="skill-meter">
      <div className="meter-bar" style={{ width: `${match}%` }}>
        <span className="glow-text">{skill}</span>
      </div>
      <div className="match-percent">{match}%</div>
    </div>
  );
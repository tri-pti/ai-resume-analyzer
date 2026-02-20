function ScoreCircle({ score }) {
  const radius = 70;
  const stroke = 10;
  const normalizedRadius = radius - stroke * 2;
  const circumference = normalizedRadius * 2 * Math.PI;
  const strokeDashoffset =
    circumference - (score / 100) * circumference;

  let color = "#ef4444";
  if (score >= 70) color = "#22c55e";
  else if (score >= 40) color = "#f59e0b";

  return (
    <div style={{ textAlign: "center" }}>
      <svg height={radius * 2} width={radius * 2}>
        <circle
          stroke="#e5e7eb"
          fill="transparent"
          strokeWidth={stroke}
          r={normalizedRadius}
          cx={radius}
          cy={radius}
        />
        <circle
          stroke={color}
          fill="transparent"
          strokeWidth={stroke}
          strokeDasharray={`${circumference} ${circumference}`}
          style={{
            strokeDashoffset,
            transition: "stroke-dashoffset 1s ease"
          }}
          r={normalizedRadius}
          cx={radius}
          cy={radius}
        />
      </svg>

      <h2>{score}%</h2>
    </div>
  );
}

export default ScoreCircle;
import ScoreCircle from "./components/ScoreCircle";
import { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [jobRole, setJobRole] = useState("AI Engineer");
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!file) {
      alert("Please upload a resume");
      return;
    }

    const formData = new FormData();
    formData.append("resume", file);
    formData.append("job_role", jobRole);

    try {
      const response = await axios.post(
        "http://127.0.0.1:5000/analyze-resume",
        formData
      );

      setResult(response.data);
    } catch (error) {
      console.error(error);
      alert("Error analyzing resume");
    }
  };

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>AI Resume Analyzer</h1>

      <form onSubmit={handleSubmit}>
        <input
          type="file"
          accept=".pdf"
          onChange={(e) => setFile(e.target.files[0])}
        />

        <br /><br />

        <select value={jobRole} onChange={(e) => setJobRole(e.target.value)}>
          <option>AI Engineer</option>
          <option>Web Developer</option>
          <option>Data Analyst</option>
        </select>

        <br /><br />

        <button type="submit">Analyze Resume</button>
      </form>

     {result && (
  <div style={{ marginTop: "30px" }}>
    <h2>Results</h2>

    <p><strong>Job Role:</strong> {result.job_role}</p>

    <h3>ATS Score</h3>
    <ScoreCircle score={result.ats_score || 0} />

    <p><strong>Recommended Role:</strong> {result.recommended_role}</p>
    <p><strong>Role Match Score:</strong> {result.role_match_score}%</p>

    <p><strong>Detected Skills:</strong></p>
    <ul>
      {(result.detected_skills || []).map((skill, index) => (
        <li key={index}>{skill}</li>
      ))}
    </ul>

    <p><strong>Missing Skills:</strong></p>
    <ul>
      {(result.missing_skills || []).map((skill, index) => (
        <li key={index}>{skill}</li>
      ))}
    </ul>

    <h3>Improvement Suggestions</h3>
    <ul>
      {(result.suggestions || []).map((s, i) => (
        <li key={i}>{s}</li>
      ))}
    </ul>

    <h3>Role Comparison</h3>
<ul>
  {Object.entries(result.role_comparison || {}).map(([role, score], i) => (
    <li key={i}>
      {role} : {score}%
    </li>
  ))}
</ul>
  </div>
)}
    </div>
  );
}

export default App;
"use client"

import { useEffect, useState } from "react";

export default function Home() {
  const [campaigns, setCampaigns] = useState([]);
  const [filter, setFilter] = useState("All");

  useEffect(() => {
    fetch("https://campaign-analytics-dashboard-production.up.railway.app/campaigns")
      .then((res) => res.json())
      .then(setCampaigns);
  }, []);

  const filteredCampaigns = campaigns.filter((c) =>
    filter === "All" ? true : c.status === filter
  );

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Campaign Analytics</h1>

      <select
        className="mb-4 p-2 border rounded"
        onChange={(e) => setFilter(e.target.value)}
        value={filter}
      >
        <option value="All">All</option>
        <option value="Active">Active</option>
        <option value="Paused">Paused</option>
      </select>

      <table className="w-full border border-collapse">
        <thead>
          <tr className="bg-gray-100">
            <th className="p-2 border">Campaign Name</th>
            <th className="p-2 border">Status</th>
            <th className="p-2 border">Clicks</th>
            <th className="p-2 border">Cost</th>
            <th className="p-2 border">Impressions</th>
          </tr>
        </thead>
        <tbody>
          {filteredCampaigns.map((c) => (
            <tr key={c.id}>
              <td className="p-2 border">{c.name}</td>
              <td className="p-2 border">{c.status}</td>
              <td className="p-2 border">{c.clicks}</td>
              <td className="p-2 border">${c.cost.toFixed(2)}</td>
              <td className="p-2 border">{c.impressions}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
